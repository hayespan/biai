# -*- coding: utf-8 -*-
from flask import Flask, request, session

from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy(use_native_unicode="utf8")
import sys
reload(sys)
sys.setdefaultencoding('utf8')
logger = None


class App(object):
    def __init__(self, *args, **kwargs):
        self.app = Flask(__name__, instance_relative_config=True)
        self.app.config.from_object('config')
        self.app.config.from_pyfile('config.py')
        logger = self.app.logger
        # config/xxx.py -- scence config
        # app.config.from_envvar('APP_CONFIG_FILE') # APP_CONFIG_FILE defined in start.sh

        self.__init_db()
        self.__init_babel()
        self.__init_script()
        self.__init_migrate()
        self.__init_login_manager()

        self.__init_blueprint()

    def __init_babel(self):
        # i18n
        from flask.ext.babel import Babel
        from language import support_langs
        self.babel = Babel(self.app)
        self.app.config['BABEL_DEFAULT_LOCALE'] = 'zh_CN'
        @self.babel.localeselector
        def get_locale():
            lc = session.get('locale', 'zh_CN')
            if lc:
                return lc
            return request.accept_languages.best_match(support_langs)

    def __init_db(self):
        db.init_app(self.app)

    def __init_login_manager(self):
        # flask-login
        from flask.ext.login import LoginManager
        self.login_manager = LoginManager()
        self.login_manager.session_protection = 'strong'
        self.login_manager.login_view = 'admin.login'

        from .model.admin import Admin
        @self.login_manager.user_loader
        def load_user(admin_id):
            return Admin.query.get(int(admin_id))
        from .model.admin import MyAnonymousUser
        self.login_manager.anonymous_user = MyAnonymousUser
        self.login_manager.init_app(self.app)

    def __init_migrate(self):
        from flask.ext.migrate import Migrate
        self.migrate = Migrate(self.app, db)

    def __init_script(self):
        from flask.ext.script import Manager, Shell
        self.manager = Manager(self.app)
        from flask.ext.migrate import MigrateCommand
        self.manager.add_command('db', MigrateCommand)
        def make_shell_context():
            import controller
            import model
            import service
            import util
            return dict(app=self.app,
                    db=db,
                    controller=controller,
                    model=model,
                    service=service,
                    util=util,
                    )
        self.manager.add_command('shell', Shell(make_context=make_shell_context))

    def __init_blueprint(self):
        from .controller.pc import pcbp
        self.app.register_blueprint(
                pcbp,
                )
        from .controller.mb import mbbp # mobile-end
        self.app.register_blueprint(
                mbbp,
                url_prefix='/m'
                # subdomain='m',
                )
        from .controller.admin import adminbp
        self.app.register_blueprint(
                adminbp,
                url_prefix='/admin',
                )


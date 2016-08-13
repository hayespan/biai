var gulp = require('gulp');
var sass = require('gulp-sass');
var watch = require('gulp-watch');
var gutil = require('gulp-util');

gulp.task('sass', function() {
	return gulp.src('app/static/scss/*.scss')
	.pipe(sass())
    .on('error', function(error) {
        gutil.log(gutil.colors.red(error.message));
        this.emit('end');
    })
	.pipe(gulp.dest('app/static/css'));
});

gulp.task('watch', function() {
	gulp.watch('app/static/scss/*.scss', ['sass']);
});

gulp.task('default', ['watch']);
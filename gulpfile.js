var gulp = require('gulp');
var sass = require('gulp-sass');
var watch = require('gulp-watch');

gulp.task('default', function() {
	return gulp.src('app/static/scss/*.scss')
	.pipe(watch('app/static/scss/*.scss'))
	.pipe(sass())
	.pipe(gulp.dest('app/static/css'));
});
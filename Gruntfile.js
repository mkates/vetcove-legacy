// The Grunt file, which performs all minification and compression locally before uploading

module.exports = function(grunt) {

  // Project configuration.
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    banner: 'VetCove, Copyright 2014',
    uglify: {
      options: {
        banner: '<%= banner %=>'
      },
      build: {
        src: ['vetcove/static/js/**/*.js'],
        dest: 'vetcove/static/compiled/main.min.js'
      }
    },
    less: {
      compiler: {
        options: {
          strictMath: true
        },
        files: {
          'vetcove/static/compiled/main.css': 'vetcove/static/less/main.less'
        }
      }
    },
    autoprefixer: {
      options: {
        browsers: [
          'Android 2.3',
          'Android >= 4',
          'Chrome >= 20',
          'Firefox >= 24', // Firefox 24 is the latest ESR
          'Explorer >= 8',
          'iOS >= 6',
          'Opera >= 12',
          'Safari >= 6'
        ]
      },
      build: {
        src: 'vetcove/static/compiled/main.css'
      },
    },
    usebanner: {
      options: {
        position: 'top',
        banner: '<%= banner %>'
      },
      files: {
        src: 'vetcove/static/compiled/main.css'
      }
    },
    cssmin: {
      combine: {
        files: {
          'vetcove/static/compiled/main.min.css': 'vetcove/static/compiled/main.css'
        }
      }
    },
    'heroku-deploy' : {
        production : {
            deployBranch : 'prod'
        },
        staging : {
            deployBranch : 'staging'
        }
    }
  });

  // Load the plugins
  grunt.loadNpmTasks('grunt-contrib-uglify');

  // These plugins provide necessary tasks.
  require('load-grunt-tasks')(grunt, { scope: 'devDependencies' });
  
  // Time each process in case there are bottlenecks
  require('time-grunt')(grunt);

  // JS distribution task
  grunt.registerTask('_js', ['uglify']);
  // Less Scripts
  grunt.registerTask('_less', ['less:compiler','autoprefixer','usebanner','cssmin']);

  // Combine the tasks to run by default //
  grunt.registerTask('default',['_less','_js']);
};
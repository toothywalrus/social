'use strict';

/**
 * @ngdoc directive
 * @name tryApp.directive:authApplication
 * @description
 * # authApplication
 */
angular.module('tryApp')
  .directive('authApplication', function ($cookieStore, $http, $rootScope) {
    return {
      restrict: 'A',
      link: function (scope, element, attrs) {
        var main = document.getElementById('main');
        var login = document.getElementById('login-holder');

        var loginFailed = document.getElementById('login-failed');

        var applyLogin = function(good) {
            if (good) {
                main.style.display = 'block';
                login.style.display = 'none';
            } else {
                main.style.display = 'none';
                login.style.display = 'block';
            }
        };

        scope.$on('event:auth-loginRequired', function(data) {
            applyLogin(false);
        });

        scope.$on('event:auth-loginConfirmed', function(data) {
            applyLogin(true);
        });

        scope.$on('event:auth-loginCancelled', function(data) {
            loginFailed.style.display = 'block';
        });
      }
    };
  });

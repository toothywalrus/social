'use strict';

/**
 * @ngdoc directive
 * @name tryApp.directive:login
 * @description
 * # loginsam
 */
angular.module('tryApp')
  .directive('login', function ($http, $cookieStore, authService) {
    return {
      template: '<form><label>Username</label>' + 
            '<input type="text" ng-model="username"><label>Password</label>' +
            '<input type="password" ng-model="password"><br>' + 
            '<input type="submit"></form>',
      restrict: 'A',
      link: function (scope, elem, attrs) {
        elem.bind('submit', function() {
            var user_data = {
                'username': scope.username,
                'password': scope.password
            };

            $http.post('/api/api-token-auth/', user_data)
                .success(function(response) {
                    $cookieStore.put('djangotoken', response.token);
                    $http.defaults.headers.common['Authorization'] = 'Token ' + response.token;
                    authService.loginConfirmed();
                })
                .error(function(data, status) {
                    authService.loginCancelled();
                });
        });
      }
    };
  });

'use strict';

/**
 * @ngdoc overview
 * @name tryApp
 * @description
 * # tryApp
 *
 * Main module of the application.
 */
angular
  .module('tryApp', [
    'ngAnimate',
    'ngCookies',
    'ngResource',
    'ngRoute',
    'ngSanitize',
    'ngTouch',
    'restangular'
  ])
  .config(function ($routeProvider, RestangularProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'views/main.html',
        controller: 'MainCtrl'
      })
      .when('/me', {
        templateUrl: 'views/profile.html',
        controller: 'ProfileCtrl'
      })
      .when('/profile/:userID', {
        templateUrl: 'views/profile.html',
        controller: 'ProfileCtrl'
      })
      .when('/message/', {
        templateUrl: 'views/message.html',
        controller: 'SendMessageCtrl'
      })
      .when('/messages', {
        templateUrl: 'views/messages.html',
        controller: 'MessageListCtrl'
      })
      .when('/about', {
        templateUrl: 'views/about.html',
        controller: 'AboutCtrl'
      })
      .when('/friends', {
        templateUrl: 'views/friends.html',
        controller: 'FriendListCtrl'
      })
      .otherwise({
        redirectTo: '/'
      });

      console.log('hello');

      // var interceptor = function($q, $rootScope, Auth) {
      //   return {
      //     'response': function(resp) {
      //       if (resp.config.url == '/api/login') {
      //         Auth.setToken(resp.data.token);
      //       }
      //     },
      //     'responseError': function(rejection) {
      //       switch(rejection.status) {
      //         case 401:
      //           if (rejection.config.url !== 'api/login')
      //             $rootScope.$broadcast('auth:loginRequired');
      //           break;
      //         case 403:
      //           $rootScope.$broadcast('auth:forbidden');
      //           break;
      //         case 404:
      //           $rootScope.$broadcast('page:notFound');
      //           break;
      //         case 500:
      //           $rootScope.$broadcast('server:error');
      //           break;
      //       }

      //       return $q.reject(rejection);
      //     }
      //   };
      // };

      //$httpProvider.interceptors.push(interceptor);

      RestangularProvider.setBaseUrl('/api');
      RestangularProvider.setDefaultHttpFields({cache: true});
  });
  // .run(function($rootScope, $location, Auth) {
  //   $rootScope.$on('$routeChangeStart', function(evt, next, curr) {
  //     if (!Auth.isAuthorized(next.access_level)) {
  //       if (Auth.isLoggedIn()) {
  //         $location.path('/');
  //       } else {
  //         $location.path('/login');
  //       }
  //     }
  //   });
  // });


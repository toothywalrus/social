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
    'restangular',
    'http-auth-interceptor'
  ])
  .config(function ($httpProvider, $routeProvider, RestangularProvider, ACCESS_LEVELS) {
    $routeProvider
      .when('/', {
        templateUrl: 'views/main.html',
        controller: 'MainCtrl',
        access_level: ACCESS_LEVELS.pub,
      })
      .when('/me', {
        templateUrl: 'views/profile.html',
        controller: 'ProfileCtrl',
        access_level: ACCESS_LEVELS.user
      })
      .when('/profile/:userID', {
        templateUrl: 'views/profile.html',
        controller: 'ProfileCtrl',
        access_level: ACCESS_LEVELS.pub
      })
      .when('/message/', {
        templateUrl: 'views/message.html',
        controller: 'SendMessageCtrl',
        access_level: ACCESS_LEVELS.user
      })
      .when('/messages', {
        templateUrl: 'views/messages.html',
        controller: 'MessageListCtrl',
        access_level: ACCESS_LEVELS.user
      })
      .when('/about', {
        templateUrl: 'views/about.html',
        controller: 'AboutCtrl',
        access_level: ACCESS_LEVELS.user
      })
      .when('/friends', {
        templateUrl: 'views/friends.html',
        controller: 'FriendListCtrl',
        access_level: ACCESS_LEVELS.user
      })
      .otherwise({
        redirectTo: '/'
      });

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
  })
  .run(function($cookieStore, $rootScope, $location, $http) {
    if ($cookieStore.get('djangotoken')) {
      $http.defaults.headers.common['Authorization'] = 'Token ' + $cookieStore.get('djangotoken');
      document.getElementById('main').style.display = 'block';
    } else {
      document.getElementById('login-holder').style.display = 'block';
    }

    // $rootScope.$on('$routeChangeStart', function(evt, next, curr) {
    //   if (!Auth.isAuthorized(next.access_level)) {
    //     if (Auth.isLoggedIn()) {
    //       $location.path('/');
    //     } else {
    //       $location.path('/login');
    //     }
    //   }
    // });
  });


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

      RestangularProvider.setBaseUrl('/api');
      RestangularProvider.setDefaultHttpFields({cache: true});
  });

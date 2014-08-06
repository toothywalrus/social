'use strict';

/**
 * @ngdoc function
 * @name tryApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the tryApp
 */
angular.module('tryApp')
  .controller('MainCtrl', function ($scope, $http) {
    $scope.awesomeThings = [
      'HTML5 Boilerplate',
      'AngularJS',
      'Karma'
    ];
    console.log("hello");
  });

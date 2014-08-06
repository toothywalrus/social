'use strict';

/**
 * @ngdoc function
 * @name tryApp.controller:AboutCtrl
 * @description
 * # AboutCtrl
 * Controller of the tryApp
 */
angular.module('tryApp')
  .controller('AboutCtrl', function ($scope) {
    $scope.awesomeThings = [
      'HTML5 Boilerplate',
      'AngularJS',
      'Karma'
    ];
  });

'use strict';

angular.module('tryApp')
  .controller('MessageListCtrl', function ($scope, Restangular) {
    $scope.conversations = Restangular.oneUrl('me').all('conversations').getList().$object;
  });

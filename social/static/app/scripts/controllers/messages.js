'use strict';

angular.module('tryApp')
  .controller('MessageListCtrl', function ($scope, Restangular) {
    Restangular.one('users', 1).getList('messages')
    .then(function(messages) {
        $scope.messages = messages;
    });
  });

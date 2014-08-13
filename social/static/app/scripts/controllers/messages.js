'use strict';

angular.module('tryApp')
  .controller('MessageListCtrl', function ($scope, Restangular) {
    Restangular.all('messages').getList()
    .then(function(messages) {
        $scope.messages = messages;
    });
  });

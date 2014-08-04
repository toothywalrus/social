angular.module('tryApp')
  .controller('FriendListCtrl', function ($scope, Restangular) {
    Restangular.all('users').getList()
    .then(function(users) {
        $scope.users = users;
    });
  });

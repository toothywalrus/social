angular.module('tryApp')
  .controller('ProfileCtrl', function ($scope, $routeParams, Restangular) {
    $scope.user = Restangular.one('users', $routeParams.userID || 1).get().$object;
  });

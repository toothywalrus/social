app = angular.module('social', []);

app.controller('MainCtrl', ['$scope', '$http', function($scope, $http) {
    $scope.users = [];
    $http.get('/api/users').then(function(result) {
        angular.forEach(result.data, function(item) {
            $scope.users.push(item);
        });
    });
}]);
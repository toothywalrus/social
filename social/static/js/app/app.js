app = angular.module('social', ['ui.router']);

app.controller('MainCtrl', ['$scope', '$http', function($scope, $http) {
    $scope.users = [];
    $http.get('/api/users').then(function(result) {
        angular.forEach(result.data, function(item) {
            $scope.users.push(item);
        });
    });
}]);


app.controller('UserListController', ['$scope', '$http', function($scope, $http) {
    $scope.users = [];
    $http.get('/api/users').then(function(result) {
        angular.forEach(result.data, function(item) {
            $scope.users.push(item);
        });
    });
}]);


app.config(['$stateProvider', '$urlRouterProvider', '$httpProvider',
    function($stateProvider, $urlRouterProvider, $httpProvider) {

    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';

    $urlRouterProvider.otherwise('/state1');

    $stateProvider
        .state('users', {
            url: '/users',
            templateUrl: 'templates/user-list.html',
            controller: 'UserListController'
        })
        .state('inbox', {
            views: {
                'filters': {
                    template: '<h4>Filter inbox</h4>',
                    contoller: function($scope) {}
                },
                'mailbox': {
                    template: '<h4>Mailbox</h4>',
                    contoller: function($scope) {}
                },
                'priority': {
                    template: '<h4>Priority</h4>',
                    contoller: function($scope) {}
                }
            }
        });
        // .state('inbox', {
        //     url: '/inbox/:inboxId',
        //     template: '<div><h1>Welcome to your inbox {{ inboxId }}</h1>\
        //                 <a ui-sref="inbox.priority">Show priority</a>\
        //                 <div ui-view></div>\
        //                 </div>',
        //     controller: function($scope, $stateParams) {
        //         $scope.inboxId = $stateParams.inboxId;
        //     }
        // })
        // .state('inbox.priority', {
        //     url: '/priority',
        //     template: '<h2>Your priority inbox</h2>'
        // });
}]);
/* global angular */
var snippets = angular.module('snippets',[]);

snippets.config(function($interpolateProvider) {
    // Allow django templates adn angular to co-exist
    // by changing angulars brace from {{ to {[{
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
});


snippets.controller('ListCtrl', function($scope, $log, $http) {

    // Just a dummy init function
    $scope.initialize = function(data) {
        $log.log('initialize', data);
        $scope.initData = data;
    };

    $scope.loadItems = function() {
        $scope.items = $http.get('http://104.197.200.142/Amol/rest/api/snippets').then(function(response){
            return response.data;
        });
    };

    $scope.loadItems();
    
    $scope.saveItem = function() {

    };

});

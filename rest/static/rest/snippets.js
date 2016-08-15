/* global angular */
var snippets = angular.module('snippets',[]);

snippets.config(function($interpolateProvider) {
    // Allow django templates adn angular to co-exist
    // by changing angulars brace from {{ to {[{
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
});


snippets.controller('ListController', function($scope, $http) {

    $scope.loadItems = function() {
        $http.get('/Amol/rest/api/snippets/').then(function(response){
            //console.log("never been so mad");
            //console.log(response);
            $scope.items = response.data.results; 
                       
        });
    };
    
    $scope.loadItems();    
    
});

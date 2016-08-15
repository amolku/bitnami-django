/* global angular */
var snippets = angular.module('snippets',[]);

snippets.config(function($interpolateProvider) {
    // Allow django templates adn angular to co-exist
    // by changing angulars brace from {{ to {[{
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
});

snippets.controller('ListController', function ListController($scope)
{
    $scope.items = [
        {
            name: 'Python'
        }, {
            name: 'Ruby'
        }
    ];

});

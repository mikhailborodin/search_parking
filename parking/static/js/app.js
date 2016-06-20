angular.module('SearchParking', [])
  .factory('api', function ($http, $q) {
    function get(model, filter) {
      var defer = $q.defer();
      $http.get('/api/v1/' + model + '/?' + jQuery.param(filter)).success(function (data, status) {
        defer.resolve({data: data, status: status});
      }).error(function (msg, status) {
        defer.resolve({msg: msg, status: status});
      });
      return defer.promise
    }
    return {
      get: get
    }
  })
  .controller('Map', function ($scope, api) {
    $scope.crd = {'latitude': 55.7, 'longitude': 37.6};
    $scope.distance = [1, 10, 50];
    $scope.search = function (distance){
      $scope.crd['distance'] = $scope.distance[distance];
      api.get('parking', $scope.crd).then(function(resp){
        if (resp.status==200) {
          if (resp.data.objects[0].is_free) {
            custom_layer.clearLayers().addData(resp.data.objects[0]);
            custom_layer.addTo(map).bindPopup(resp.data.objects[0].title).openPopup();
            map.fitBounds(custom_layer.getBounds());
          } else {
            var rr = confirm(resp.data.objects[0].title + ': ' + resp.data.objects[0].status);
            if (rr == true) {
              distance += 1;
              $scope.search(distance)
            }
          }
        } else {
          var r = confirm(resp.msg.error_message);
          if (r == true) {
              distance += 1;
              $scope.search(distance)
          } else {
              alert(resp.msg.error_message);
          }
        }
      });
    }
  });
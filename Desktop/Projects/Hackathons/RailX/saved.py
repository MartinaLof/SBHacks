    <div id="map"></div>
    <script>
    var map;
      function initMap() {
        map = new google.maps.Map(document.getElementById('map'), {
          zoom: 10,
          center: new google.maps.LatLng(-24.90, 31.65),
          mapTypeId: 'terrain'
        });

        // JSON coordinates
        map.data.loadGeoJson('https://firebasestorage.googleapis.com/v0/b/team-3-project-257012.appspot.com/o/data%2Fele_json.json?alt=media');
        map.data.loadGeoJson('https://firebasestorage.googleapis.com/v0/b/team-3-project-257012.appspot.com/o/data%2Froad_json.json?alt=media');

        map.data.setStyle(function(feature) {
            return {
                icon: feature.getProperty("icon"),
                title: feature.getProperty("name")
            }
        });
      }

      // Loop through the results array and place a marker for each
      // set of coordinates.
      window.eqfeed_callback = function(results) {
        for (var i = 0; i < results.features.length; i++) {
          var coords = results.features[i].geometry.coordinates;
          var latLng = new google.maps.LatLng(coords[1],coords[0]);
          var marker = new google.maps.Marker({
            position: latLng,
            map: map
          });
        }
      }
      
    </script>
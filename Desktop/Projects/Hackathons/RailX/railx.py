import csv
import pandas as pd 

csvfile = 'ElephantMovement.csv'

data = pd.read_csv(csvfile)
print(data)

for i in range(1, len(data)):
    lattitude = data['location-lat'].iloc[i]
    longitude = data['location-long'].iloc[i]
    print(lattitude, longitude)

datahtml = data.to_html
print("HTML", datahtml)

# write-html-2-mac.py
import webbrowser

f = open('railx.html', 'w')

message = """<!DOCTYPE html>
<html>
  <head>
    <title>Simple Map</title>
    <meta name="viewport" content="initial-scale=1.0">
    <meta charset="utf-8">

    <!--Styles-->
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <!-- Custom CSS -->
    <link rel="stylesheet" type="text/css" href="main.css">

  </head>
  <body>

<!-- Navbar -->
<nav class="navbar navbar-expand-lg">

    <!-- Navbar Icon -->
    <span class="navbar-header">
        <a class="navbar-brand" href=""><img src='static/railx_logo_blue.png' alt="logo" style="width:80px"/></a>
    </span>
  
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="nav navbar-nav">
            <li class="nav-item active"><a class="nav-link" href="">ABOUT</a></li>
            <li class="nav-item active"><a class="nav-link" href="">STORY</a></li>
            <li class="nav-item active"><a class="nav-link" href="">CONTACT</a></li>
      </ul>

    </div>

    <span>
        <a class="navbar" href=""><img src='static/elephant_safari.jpeg' alt="logo" style="width:175px"/></a>
    </span>

</div>
</nav>

<div id="floating-panel">
      <button type="button" class="btn btn-warning" onclick="toggleHeatmap()">Toggle Heatmap</button>
      <!--<button type="button" class="btn btn-warning" onclick="toggleMarkers()">Toggle Markers</button>-->
      <button type="button" class="btn btn-warning" onclick="changeGradient()">Change gradient</button>
      <button type="button" class="btn btn-warning" onclick="changeRadius()">Change radius</button>
      <button type="button" class="btn btn-warning" onclick="changeOpacity()">Change opacity</button>
    </div>
    <div id="map"></div>

    <script>

      // This example requires the Visualization library. Include the libraries=visualization
      // parameter when you first load the API. For example:
      // <script src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&libraries=visualization">

      var map, heatmap, markermap;

      function initMap() {
        var markers_data = new google.maps.Data();
        var line_data = new google.maps.Data();

        map = new google.maps.Map(document.getElementById('map'), {
          zoom: 10,
          center: new google.maps.LatLng(-24.85, 31.65),
          mapTypeId: 'satellite'
        });

        // JSON coordinates
        //map.data.loadGeoJson('https://firebasestorage.googleapis.com/v0/b/team-3-project-257012.appspot.com/o/data%2Fele_json.json?alt=media');
        line_data.loadGeoJson('https://firebasestorage.googleapis.com/v0/b/team-3-project-257012.appspot.com/o/data%2Froad_json.json?alt=media');
        line_data.setMap(map);
        
        heatmap = new google.maps.visualization.HeatmapLayer({
          data: getPoints(),
          map: map
        });

        markermap = new google.maps.Map({
          data: getMarkers(),
          map: map
        })

        // Set the fill color to blue when the feature is clicked.
        map.data.addListener('click', function(event) {
          map.data.overrideStyle(event.feature, {fillColor: 'blue'});
        });
        
        // Set the style of the map
        map.data.setStyle(function(feature) {
            return {
                icon: feature.getProperty("icon"),
                title: feature.getProperty("RailX"),
                fillColor: 'green'
            }
        });

      }

      function toggleMarkers() {
        //markermap.setMap(markermap.getMap() ? map : null);
        markers_data.setMap(null);
      }

      function toggleHeatmap() {
        heatmap.setMap(heatmap.getMap() ? null : map);
      }

      function changeGradient() {
        var gradient = [
          'rgba(0, 255, 255, 0)',
          'rgba(0, 255, 255, 1)',
          'rgba(0, 191, 255, 1)',
          'rgba(0, 127, 255, 1)',
          'rgba(0, 63, 255, 1)',
          'rgba(0, 0, 255, 1)',
          'rgba(0, 0, 223, 1)',
          'rgba(0, 0, 191, 1)',
          'rgba(0, 0, 159, 1)',
          'rgba(0, 0, 127, 1)',
          'rgba(63, 0, 91, 1)',
          'rgba(127, 0, 63, 1)',
          'rgba(191, 0, 31, 1)',
          'rgba(255, 0, 0, 1)'
        ]
        heatmap.set('gradient', heatmap.get('gradient') ? null : gradient);
      }

      function changeRadius() {
        heatmap.set('radius', heatmap.get('radius') ? null : 20);
      }

      function changeOpacity() {
        heatmap.set('opacity', heatmap.get('opacity') ? null : 0.2);
      }

      function getMarkers() {
        return map.data.loadGeoJson('https://firebasestorage.googleapis.com/v0/b/team-3-project-257012.appspot.com/o/data%2Fele_json.json?alt=media');
      }

      // Heatmap data: 500 Points
      function getPoints() {
        return [
          new google.maps.LatLng(-24.72041,31.810859999999998), new
google.maps.LatLng(-24.72042,31.812109999999997), new
google.maps.LatLng(-24.72014,31.815179999999998), new
google.maps.LatLng(-24.71988,31.8156199999999), new
google.maps.LatLng(-25.0018999999999,31.30975), new
google.maps.LatLng(-24.71985,31.8157099999999), new
google.maps.LatLng(-25.002589999999998,31.30824), new
google.maps.LatLng(-24.7208299999999,31.8124499999999), new
google.maps.LatLng(-25.00366,31.30527), new
google.maps.LatLng(-24.72372,31.810209999999998), new
google.maps.LatLng(-25.005229999999997,31.301709999999996), new
google.maps.LatLng(-25.009079999999997,31.30228), new
google.maps.LatLng(-24.7250599999999,31.8087), new
google.maps.LatLng(-24.7263799999999,31.8078399999999), new
google.maps.LatLng(-25.0082899999999,31.30214), new
google.maps.LatLng(-24.7279599999999,31.806390000000004), new
google.maps.LatLng(-25.01473,31.3022199999999), new
google.maps.LatLng(-24.734679999999997,31.80289), new
google.maps.LatLng(-25.0158999999999,31.30232), new
google.maps.LatLng(-24.7422,31.7962799999999), new
google.maps.LatLng(-25.01577,31.303459999999998), new
google.maps.LatLng(-24.74247,31.796090000000003), new
google.maps.LatLng(-24.742829999999998,31.7955299999999), new
google.maps.LatLng(-24.743129999999997,31.7943), new
google.maps.LatLng(-25.01921,31.3042599999999), new
google.maps.LatLng(-24.74292,31.79295), new
google.maps.LatLng(-25.0196599999999,31.305), new
google.maps.LatLng(-24.74288,31.79175), new
google.maps.LatLng(-24.7418699999999,31.79128), new
google.maps.LatLng(-24.7414899999999,31.79233), new
google.maps.LatLng(-25.0196499999999,31.3089499999999), new
google.maps.LatLng(-24.74155,31.7936699999999), new
google.maps.LatLng(-25.0198299999999,31.3090599999999), new
google.maps.LatLng(-24.741889999999998,31.79465), new
google.maps.LatLng(-24.7407399999999,31.7938599999999), new
google.maps.LatLng(-24.74151,31.79397), new
google.maps.LatLng(-24.741629999999997,31.79402), new
google.maps.LatLng(-25.02371,31.30767), new
google.maps.LatLng(-25.02465,31.306929999999998), new
google.maps.LatLng(-24.74175,31.79397), new
google.maps.LatLng(-25.0249899999999,31.3066), new
google.maps.LatLng(-24.74155,31.79393), new
google.maps.LatLng(-24.74175,31.79372), new
google.maps.LatLng(-25.02709,31.3041799999999), new
google.maps.LatLng(-24.7415999999999,31.7943399999999), new
google.maps.LatLng(-25.0261199999999,31.30452), new
google.maps.LatLng(-24.74156,31.795009999999998), new
google.maps.LatLng(-25.0243499999999,31.3058799999999), new
google.maps.LatLng(-25.023239999999998,31.305640000000004), new
google.maps.LatLng(-25.02308,31.30527), new
google.maps.LatLng(-25.02352,31.30387), new
google.maps.LatLng(-25.0252799999999,31.300559999999997), new
google.maps.LatLng(-25.0260099999999,31.30047), new
google.maps.LatLng(-24.7389,31.80185), new
google.maps.LatLng(-25.02619,31.30074), new
google.maps.LatLng(-24.7387,31.80227), new
google.maps.LatLng(-25.0265799999999,31.30048), new
google.maps.LatLng(-25.0264099999999,31.30077), new
google.maps.LatLng(-25.0263199999999,31.30082), new
google.maps.LatLng(-24.73881,31.803), new
google.maps.LatLng(-25.0262899999999,31.3010699999999), new
google.maps.LatLng(-24.7387699999999,31.8032499999999), new
google.maps.LatLng(-25.027279999999998,31.30167), new
google.maps.LatLng(-25.02756,31.3016499999999), new
google.maps.LatLng(-25.02807,31.30204), new
google.maps.LatLng(-24.73741,31.8064199999999), new
google.maps.LatLng(-25.0293199999999,31.3031599999999), new
google.maps.LatLng(-25.02964,31.303379999999997), new
google.maps.LatLng(-25.02982,31.30384), new
google.maps.LatLng(-25.03003,31.30368), new
google.maps.LatLng(-25.03002,31.304159999999996), new
google.maps.LatLng(-25.0299699999999,31.3052899999999), new
google.maps.LatLng(-24.73607,31.81108), new
google.maps.LatLng(-25.0296699999999,31.305999999999997), new
google.maps.LatLng(-24.735879999999998,31.81117), new
google.maps.LatLng(-25.029989999999998,31.3068099999999), new
google.maps.LatLng(-24.7358599999999,31.8114999999999), new
google.maps.LatLng(-25.02944,31.30834), new
google.maps.LatLng(-24.735889999999998,31.81185), new
google.maps.LatLng(-25.0293899999999,31.3091599999999), new
google.maps.LatLng(-24.73565,31.81219), new
google.maps.LatLng(-25.029429999999998,31.310409999999997), new
google.maps.LatLng(-24.73507,31.8131799999999), new
google.maps.LatLng(-25.0285699999999,31.311259999999997), new
google.maps.LatLng(-24.73462,31.81369), new
google.maps.LatLng(-25.0267699999999,31.3121399999999), new
google.maps.LatLng(-24.734379999999998,31.8141), new
google.maps.LatLng(-25.02634,31.31237), new
google.maps.LatLng(-24.7333,31.8154399999999), new
google.maps.LatLng(-25.02522,31.31185), new
google.maps.LatLng(-24.73255,31.81502), new
google.maps.LatLng(-25.02562,31.3109199999999), new
google.maps.LatLng(-24.73081,31.8138499999999), new
google.maps.LatLng(-25.0248099999999,31.310809999999996), new
google.maps.LatLng(-24.7279699999999,31.81369), new
google.maps.LatLng(-25.02286,31.3106), new
google.maps.LatLng(-25.022289999999998,31.3077499999999), new
google.maps.LatLng(-25.02347,31.3073599999999), new
google.maps.LatLng(-24.72265,31.81519), new
google.maps.LatLng(-25.0236899999999,31.307059999999996), new
google.maps.LatLng(-25.02295,31.306590000000003), new
google.maps.LatLng(-24.7204599999999,31.8158199999999), new
google.maps.LatLng(-24.7202799999999,31.8160799999999), new
google.maps.LatLng(-25.022879999999997,31.30677), new
google.maps.LatLng(-25.02298,31.3067099999999), new
google.maps.LatLng(-24.72201,31.80702), new
google.maps.LatLng(-24.72256,31.80547), new
google.maps.LatLng(-25.02305,31.30704), new
google.maps.LatLng(-24.7225499999999,31.8045399999999), new
google.maps.LatLng(-25.02297,31.30827), new
google.maps.LatLng(-25.02289,31.3081), new
google.maps.LatLng(-25.02297,31.3078), new
google.maps.LatLng(-24.72485,31.800259999999998), new
google.maps.LatLng(-25.022579999999998,31.307609999999997), new
google.maps.LatLng(-24.7256299999999,31.79702), new
google.maps.LatLng(-25.023139999999998,31.308359999999997), new
google.maps.LatLng(-24.726129999999998,31.7966799999999), new
google.maps.LatLng(-25.02351,31.309590000000004), new
google.maps.LatLng(-24.72682,31.79598), new
google.maps.LatLng(-25.0257299999999,31.30974), new
google.maps.LatLng(-25.0282899999999,31.3104699999999), new
google.maps.LatLng(-24.7264899999999,31.79557), new
google.maps.LatLng(-24.72588,31.79484), new
google.maps.LatLng(-25.0305199999999,31.312459999999998), new
google.maps.LatLng(-25.03161,31.3141399999999), new
google.maps.LatLng(-25.032529999999998,31.314459999999997), new
google.maps.LatLng(-24.72277,31.793259999999997), new
google.maps.LatLng(-25.03291,31.31482), new
google.maps.LatLng(-24.7215099999999,31.7933999999999), new
google.maps.LatLng(-25.0333399999999,31.315179999999998), new
google.maps.LatLng(-24.7208599999999,31.79389), new
google.maps.LatLng(-25.0333,31.315659999999998), new
google.maps.LatLng(-25.03329,31.3157), new
google.maps.LatLng(-24.71995,31.7940499999999), new
google.maps.LatLng(-24.71929,31.79438), new
google.maps.LatLng(-25.0333299999999,31.315590000000004), new
google.maps.LatLng(-24.71875,31.79588), new
google.maps.LatLng(-24.71752,31.79787), new
google.maps.LatLng(-24.717579999999998,31.797829999999998), new
google.maps.LatLng(-25.0332,31.31734), new
google.maps.LatLng(-24.7175699999999,31.79782), new
google.maps.LatLng(-25.03293,31.318590000000004), new
google.maps.LatLng(-24.7176699999999,31.797759999999997), new
google.maps.LatLng(-25.031979999999997,31.318759999999997), new
google.maps.LatLng(-24.717129999999997,31.79917), new
google.maps.LatLng(-25.03319,31.32002), new
google.maps.LatLng(-25.0322099999999,31.3191099999999), new
google.maps.LatLng(-25.0303399999999,31.318609999999996), new
google.maps.LatLng(-24.7151,31.8016299999999), new
google.maps.LatLng(-25.027479999999997,31.316540000000003), new
google.maps.LatLng(-24.714779999999998,31.8027699999999), new
google.maps.LatLng(-25.02645,31.316329999999997), new
google.maps.LatLng(-24.7140899999999,31.8048199999999), new
google.maps.LatLng(-25.0259299999999,31.315559999999998), new
google.maps.LatLng(-24.71358,31.8055799999999), new
google.maps.LatLng(-25.02365,31.314159999999998), new
google.maps.LatLng(-24.71265,31.8073599999999), new
google.maps.LatLng(-25.0218099999999,31.314), new
google.maps.LatLng(-24.711779999999997,31.80902), new
google.maps.LatLng(-25.02093,31.3136599999999), new
google.maps.LatLng(-25.02075,31.3137), new
google.maps.LatLng(-24.7068499999999,31.8147799999999), new
google.maps.LatLng(-24.70655,31.8157299999999), new
google.maps.LatLng(-25.019579999999998,31.31314), new
google.maps.LatLng(-24.7062999999999,31.8156199999999), new
google.maps.LatLng(-25.0191,31.3132799999999), new
google.maps.LatLng(-24.70628,31.815579999999997), new
google.maps.LatLng(-25.0196,31.3123299999999), new
google.maps.LatLng(-24.70951,31.80965), new
google.maps.LatLng(-25.0193599999999,31.3124), new
google.maps.LatLng(-24.7118,31.803390000000004), new
google.maps.LatLng(-25.01868,31.3127), new
google.maps.LatLng(-25.0185999999999,31.3127299999999), new
google.maps.LatLng(-24.7145499999999,31.7937699999999), new
google.maps.LatLng(-24.7190499999999,31.79298), new
google.maps.LatLng(-24.71959,31.7930099999999), new
google.maps.LatLng(-24.72171,31.792709999999996), new
google.maps.LatLng(-24.7234799999999,31.7919799999999), new
google.maps.LatLng(-24.723489999999998,31.7920799999999), new
google.maps.LatLng(-25.0273399999999,31.2941199999999), new
google.maps.LatLng(-25.02821,31.290340000000004), new
google.maps.LatLng(-24.7261999999999,31.79243), new
google.maps.LatLng(-25.028579999999998,31.286459999999998), new
google.maps.LatLng(-24.72727,31.79267), new
google.maps.LatLng(-25.03085,31.2852299999999), new
google.maps.LatLng(-24.7276999999999,31.7928099999999), new
google.maps.LatLng(-25.03191,31.28557), new
google.maps.LatLng(-24.72776,31.793359999999996), new
google.maps.LatLng(-25.0321,31.285429999999998), new
google.maps.LatLng(-24.7276899999999,31.7938499999999), new
google.maps.LatLng(-25.03265,31.28473), new
google.maps.LatLng(-24.7279599999999,31.7934799999999), new
google.maps.LatLng(-25.0327899999999,31.28453), new
google.maps.LatLng(-25.033079999999998,31.2846499999999), new
google.maps.LatLng(-25.03375,31.2851199999999), new
google.maps.LatLng(-24.7271199999999,31.7946999999999), new
google.maps.LatLng(-25.0340799999999,31.28517), new
google.maps.LatLng(-25.03461,31.2853999999999), new
google.maps.LatLng(-25.03499,31.2860699999999), new
google.maps.LatLng(-25.03497,31.286140000000003), new
google.maps.LatLng(-24.7264799999999,31.798790000000004), new
google.maps.LatLng(-25.035,31.2861599999999), new
google.maps.LatLng(-24.72654,31.79849), new
google.maps.LatLng(-25.03511,31.2862), new
google.maps.LatLng(-25.0350299999999,31.286209999999997), new
google.maps.LatLng(-24.72491,31.80019), new
google.maps.LatLng(-24.7240499999999,31.8017399999999), new
google.maps.LatLng(-25.03818,31.289140000000003), new
google.maps.LatLng(-25.03854,31.289309999999997), new
google.maps.LatLng(-24.7232799999999,31.80319), new
google.maps.LatLng(-25.03949,31.28975), new
google.maps.LatLng(-24.72336,31.8032499999999), new
google.maps.LatLng(-25.0400099999999,31.28978), new
google.maps.LatLng(-25.0403699999999,31.290309999999998), new
google.maps.LatLng(-25.040329999999997,31.29175), new
google.maps.LatLng(-24.72276,31.80322), new
google.maps.LatLng(-25.039839999999998,31.29445), new
google.maps.LatLng(-25.03941,31.2984499999999), new
google.maps.LatLng(-25.04025,31.2992199999999), new
google.maps.LatLng(-25.04063,31.299509999999998), new
google.maps.LatLng(-24.7224,31.804240000000004), new
google.maps.LatLng(-25.04119,31.3000499999999), new
google.maps.LatLng(-24.72214,31.804609999999997), new
google.maps.LatLng(-25.0414999999999,31.30087), new
google.maps.LatLng(-25.0417099999999,31.3013499999999), new
google.maps.LatLng(-25.04126,31.30228), new
google.maps.LatLng(-24.72045,31.8075399999999), new
google.maps.LatLng(-25.0408599999999,31.30347), new
google.maps.LatLng(-24.720229999999997,31.80797), new
google.maps.LatLng(-25.039,31.302709999999998), new
google.maps.LatLng(-24.72007,31.8087799999999), new
google.maps.LatLng(-25.03689,31.30067), new
google.maps.LatLng(-24.71985,31.80917), new
google.maps.LatLng(-25.034589999999998,31.29839), new
google.maps.LatLng(-24.71955,31.8118699999999), new
google.maps.LatLng(-25.0337099999999,31.29699), new
google.maps.LatLng(-25.0332599999999,31.2948099999999), new
google.maps.LatLng(-25.0331499999999,31.2944), new
google.maps.LatLng(-25.0345499999999,31.2917899999999), new
google.maps.LatLng(-24.72176,31.8149699999999), new
google.maps.LatLng(-25.03432,31.29125), new
google.maps.LatLng(-24.7285299999999,31.811740000000004), new
google.maps.LatLng(-25.036089999999998,31.28762), new
google.maps.LatLng(-24.73186,31.80805), new
google.maps.LatLng(-25.03497,31.2860799999999), new
google.maps.LatLng(-24.7352999999999,31.801509999999997), new
google.maps.LatLng(-25.0345599999999,31.2855999999999), new
google.maps.LatLng(-24.7353799999999,31.798990000000003), new
google.maps.LatLng(-25.03452,31.285629999999998), new
google.maps.LatLng(-24.73551,31.79744), new
google.maps.LatLng(-25.03432,31.28479), new
google.maps.LatLng(-24.73607,31.79607), new
google.maps.LatLng(-25.03412,31.28285), new
google.maps.LatLng(-24.735429999999997,31.79577), new
google.maps.LatLng(-25.03415,31.2819), new
google.maps.LatLng(-24.735529999999997,31.7938399999999), new
google.maps.LatLng(-25.034879999999998,31.28143), new
google.maps.LatLng(-25.03506,31.2809899999999), new
google.maps.LatLng(-24.7376399999999,31.7912399999999), new
google.maps.LatLng(-25.0348599999999,31.27778), new
google.maps.LatLng(-24.73509,31.7917899999999), new
google.maps.LatLng(-25.0341799999999,31.27859), new
google.maps.LatLng(-24.7339699999999,31.7932899999999), new
google.maps.LatLng(-25.0331499999999,31.27832), new
google.maps.LatLng(-25.0325899999999,31.278809999999996), new
google.maps.LatLng(-25.03153,31.2775399999999), new
google.maps.LatLng(-25.031779999999998,31.276259999999997), new
google.maps.LatLng(-25.03205,31.27605), new
google.maps.LatLng(-25.03209,31.2755), new
google.maps.LatLng(-25.03192,31.275009999999998), new
google.maps.LatLng(-24.72889,31.79295), new
google.maps.LatLng(-25.031979999999997,31.27354), new
google.maps.LatLng(-25.031779999999998,31.2729299999999), new
google.maps.LatLng(-25.03196,31.273059999999997), new
google.maps.LatLng(-25.03209,31.27307), new
google.maps.LatLng(-24.7284,31.792140000000003), new
google.maps.LatLng(-24.7284399999999,31.79192), new
google.maps.LatLng(-25.031589999999998,31.271859999999997), new
google.maps.LatLng(-24.72813,31.792109999999997), new
google.maps.LatLng(-25.0309199999999,31.269379999999998), new
google.maps.LatLng(-24.7274999999999,31.792759999999998), new
google.maps.LatLng(-25.03098,31.26877), new
google.maps.LatLng(-25.0311799999999,31.2661), new
google.maps.LatLng(-25.031589999999998,31.26455), new
google.maps.LatLng(-24.726779999999998,31.79383), new
google.maps.LatLng(-25.031589999999998,31.2645899999999), new
google.maps.LatLng(-25.0315599999999,31.2646599999999), new
google.maps.LatLng(-25.03151,31.26455), new
google.maps.LatLng(-25.03151,31.2639), new
google.maps.LatLng(-24.7257199999999,31.7935799999999), new
google.maps.LatLng(-25.0313799999999,31.26319), new
google.maps.LatLng(-24.72567,31.79332), new
google.maps.LatLng(-25.0312899999999,31.2625899999999), new
google.maps.LatLng(-25.0303399999999,31.261459999999996), new
google.maps.LatLng(-25.02915,31.2606499999999), new
google.maps.LatLng(-24.7258299999999,31.7926399999999), new
google.maps.LatLng(-25.0283799999999,31.2596099999999), new
google.maps.LatLng(-24.72587,31.792659999999998), new
google.maps.LatLng(-25.027379999999997,31.259559999999997), new
google.maps.LatLng(-25.02712,31.2601), new
google.maps.LatLng(-25.0268,31.260479999999998), new
google.maps.LatLng(-25.0264899999999,31.2608199999999), new
google.maps.LatLng(-24.725839999999998,31.7927299999999), new
google.maps.LatLng(-25.0261999999999,31.261029999999998), new
google.maps.LatLng(-25.02569,31.2609199999999), new
google.maps.LatLng(-25.0280999999999,31.261440000000004), new
google.maps.LatLng(-24.72655,31.7931199999999), new
google.maps.LatLng(-24.72605,31.79334), new
google.maps.LatLng(-24.72546,31.793709999999997), new
google.maps.LatLng(-24.72523,31.7933899999999), new
google.maps.LatLng(-25.02261,31.2608), new
google.maps.LatLng(-25.02582,31.2622299999999), new
google.maps.LatLng(-24.72428,31.793029999999998), new
google.maps.LatLng(-24.7242099999999,31.7928), new
google.maps.LatLng(-25.02661,31.26275), new
google.maps.LatLng(-25.0265999999999,31.26362), new
google.maps.LatLng(-25.02994,31.2652), new
google.maps.LatLng(-25.0316399999999,31.266479999999998), new
google.maps.LatLng(-25.033279999999998,31.2664399999999), new
google.maps.LatLng(-24.72372,31.7924599999999), new
google.maps.LatLng(-25.03491,31.266779999999997), new
google.maps.LatLng(-24.7229099999999,31.79294), new
google.maps.LatLng(-25.0360699999999,31.2673799999999), new
google.maps.LatLng(-24.72152,31.79392), new
google.maps.LatLng(-25.0369899999999,31.26762), new
google.maps.LatLng(-24.7201899999999,31.79547), new
google.maps.LatLng(-25.038529999999998,31.2673899999999), new
google.maps.LatLng(-25.0394499999999,31.2681), new
google.maps.LatLng(-25.0395399999999,31.26913), new
google.maps.LatLng(-24.7171999999999,31.797590000000003), new
google.maps.LatLng(-25.04045,31.270529999999997), new
google.maps.LatLng(-25.0420599999999,31.2698199999999), new
google.maps.LatLng(-25.0435899999999,31.268729999999998), new
google.maps.LatLng(-25.0441499999999,31.2684399999999), new
google.maps.LatLng(-24.714579999999998,31.8012), new
google.maps.LatLng(-25.04364,31.26874), new
google.maps.LatLng(-25.04364,31.26878), new
google.maps.LatLng(-25.04327,31.268909999999998), new
google.maps.LatLng(-25.0435699999999,31.2687999999999), new
google.maps.LatLng(-25.0438499999999,31.2685999999999), new
google.maps.LatLng(-25.04362,31.2683199999999), new
google.maps.LatLng(-25.0451,31.268009999999997), new
google.maps.LatLng(-25.04617,31.266779999999997), new
google.maps.LatLng(-25.0456299999999,31.267329999999998), new
google.maps.LatLng(-25.04532,31.267509999999998), new
google.maps.LatLng(-25.04523,31.26728), new
google.maps.LatLng(-25.0451699999999,31.26697), new
google.maps.LatLng(-25.04465,31.2667299999999), new
google.maps.LatLng(-25.0438499999999,31.266109999999998), new
google.maps.LatLng(-25.04212,31.26499), new
google.maps.LatLng(-25.04221,31.2654999999999), new
google.maps.LatLng(-24.6944,31.840290000000003), new
google.maps.LatLng(-25.03957,31.26142), new
google.maps.LatLng(-24.69441,31.8400399999999), new
google.maps.LatLng(-25.037779999999998,31.259809999999998), new
google.maps.LatLng(-25.03669,31.25824), new
google.maps.LatLng(-25.0365299999999,31.2569599999999), new
google.maps.LatLng(-24.6988699999999,31.83755), new
google.maps.LatLng(-25.037779999999998,31.25625), new
google.maps.LatLng(-24.70054,31.8401999999999), new
google.maps.LatLng(-25.0404899999999,31.25822), new
google.maps.LatLng(-25.04191,31.259359999999997), new
google.maps.LatLng(-25.04326,31.2603599999999), new
google.maps.LatLng(-24.7061899999999,31.8414499999999), new
google.maps.LatLng(-25.04456,31.259459999999997), new
google.maps.LatLng(-24.71554,31.83967), new
google.maps.LatLng(-25.04641,31.260559999999998), new
google.maps.LatLng(-25.0479999999999,31.261229999999998), new
google.maps.LatLng(-25.05009,31.26209), new
google.maps.LatLng(-25.050929999999997,31.2612899999999), new
google.maps.LatLng(-25.04909,31.2546399999999), new
google.maps.LatLng(-25.04974,31.2534199999999), new
google.maps.LatLng(-25.05092,31.2535899999999), new
google.maps.LatLng(-24.7192599999999,31.818690000000004), new
google.maps.LatLng(-25.0520099999999,31.25315), new
google.maps.LatLng(-25.05198,31.253159999999998), new
google.maps.LatLng(-24.71796,31.81775), new
google.maps.LatLng(-25.0522899999999,31.2527), new
google.maps.LatLng(-25.0530499999999,31.2512599999999), new
google.maps.LatLng(-24.7181199999999,31.8160899999999), new
google.maps.LatLng(-25.05396,31.24895), new
google.maps.LatLng(-24.7199099999999,31.8156399999999), new
google.maps.LatLng(-25.0543799999999,31.249059999999997), new
google.maps.LatLng(-24.7192599999999,31.815309999999997), new
google.maps.LatLng(-25.05552,31.2487199999999), new
google.maps.LatLng(-24.72475,31.8080099999999), new
google.maps.LatLng(-25.0563,31.249159999999996), new
google.maps.LatLng(-24.72673,31.809109999999997), new
google.maps.LatLng(-25.0567199999999,31.24912), new
google.maps.LatLng(-25.05751,31.249209999999998), new
google.maps.LatLng(-25.05732,31.24914), new
google.maps.LatLng(-25.05685,31.2488899999999), new
google.maps.LatLng(-24.73317,31.8030499999999), new
google.maps.LatLng(-25.05725,31.24832), new
google.maps.LatLng(-24.73402,31.799640000000004), new
google.maps.LatLng(-25.05752,31.247759999999996), new
google.maps.LatLng(-24.7352799999999,31.79768), new
google.maps.LatLng(-25.05826,31.2475799999999), new
google.maps.LatLng(-24.73508,31.797290000000004), new
google.maps.LatLng(-25.05875,31.246890000000004), new
google.maps.LatLng(-24.735229999999998,31.79607), new
google.maps.LatLng(-24.735529999999997,31.7954599999999), new
google.maps.LatLng(-24.7352099999999,31.79447), new
google.maps.LatLng(-24.7348299999999,31.7941399999999), new
google.maps.LatLng(-25.05882,31.24682), new
google.maps.LatLng(-24.73488,31.7941), new
google.maps.LatLng(-24.7349999999999,31.7941499999999), new
google.maps.LatLng(-24.7340699999999,31.7931199999999), new
google.maps.LatLng(-24.7342,31.79322), new
google.maps.LatLng(-25.05927,31.2429799999999), new
google.maps.LatLng(-24.7340899999999,31.7941), new
google.maps.LatLng(-25.0588599999999,31.242729999999998), new
google.maps.LatLng(-25.0583899999999,31.24097), new
google.maps.LatLng(-25.0583899999999,31.2403499999999), new
google.maps.LatLng(-24.73263,31.7952699999999), new
google.maps.LatLng(-25.0580199999999,31.2388499999999), new
google.maps.LatLng(-24.73261,31.7948799999999), new
google.maps.LatLng(-25.0568199999999,31.2374499999999), new
google.maps.LatLng(-24.73252,31.79477), new
google.maps.LatLng(-25.05433,31.2372), new
google.maps.LatLng(-24.73265,31.79457), new
google.maps.LatLng(-25.05228,31.2371), new
google.maps.LatLng(-24.7328699999999,31.7942199999999), new
google.maps.LatLng(-25.050539999999998,31.235529999999997), new
google.maps.LatLng(-25.05037,31.234779999999997), new
google.maps.LatLng(-25.0516,31.2330599999999), new
google.maps.LatLng(-24.73328,31.79407), new
google.maps.LatLng(-24.7332,31.7941399999999), new
google.maps.LatLng(-24.73325,31.7941499999999), new
google.maps.LatLng(-24.73327,31.7946099999999), new
google.maps.LatLng(-25.05348,31.2257), new
google.maps.LatLng(-25.05275,31.22699), new
google.maps.LatLng(-25.05256,31.22765), new
google.maps.LatLng(-25.05245,31.2283), new
google.maps.LatLng(-25.05264,31.2285299999999), new
google.maps.LatLng(-25.05345,31.22819), new
google.maps.LatLng(-25.05946,31.229809999999997), new
google.maps.LatLng(-25.06294,31.2313499999999), new
google.maps.LatLng(-25.06557,31.2300499999999), new
google.maps.LatLng(-25.06624,31.23027), new
google.maps.LatLng(-25.06625,31.231890000000003), new
google.maps.LatLng(-25.067989999999998,31.2317399999999), new
google.maps.LatLng(-25.07035,31.2344599999999), new
google.maps.LatLng(-25.0714299999999,31.2362399999999), new
google.maps.LatLng(-25.0704899999999,31.237479999999998), new
google.maps.LatLng(-25.06943,31.238429999999997), new
google.maps.LatLng(-25.0691899999999,31.2388), new
google.maps.LatLng(-25.0683599999999,31.23994), new
google.maps.LatLng(-25.0681499999999,31.2404699999999), new
google.maps.LatLng(-25.067429999999998,31.240609999999997), new
google.maps.LatLng(-25.06736,31.2405499999999), new
google.maps.LatLng(-25.0673999999999,31.2405599999999), new
google.maps.LatLng(-25.06739,31.240509999999997), new
google.maps.LatLng(-25.0674999999999,31.240509999999997), new
google.maps.LatLng(-25.06748,31.2403499999999), new
google.maps.LatLng(-25.06736,31.2406599999999), new
google.maps.LatLng(-25.06738,31.24118), new
google.maps.LatLng(-25.06711,31.2413999999999), new
google.maps.LatLng(-25.066999999999997,31.2411299999999), new
google.maps.LatLng(-25.0665499999999,31.2406299999999), new
google.maps.LatLng(-25.0657099999999,31.239390000000004), new
google.maps.LatLng(-25.0649699999999,31.23817), new
google.maps.LatLng(-25.06417,31.2371699999999), new
google.maps.LatLng(-25.06363,31.2357799999999), new
google.maps.LatLng(-25.0630999999999,31.235429999999997), new
google.maps.LatLng(-25.0623399999999,31.23457), new
google.maps.LatLng(-25.0620599999999,31.2341599999999), new
google.maps.LatLng(-25.0618799999999,31.2336999999999), new
google.maps.LatLng(-25.0612199999999,31.231109999999997), new
google.maps.LatLng(-25.05946,31.229509999999998), new
google.maps.LatLng(-25.0568199999999,31.228), new
google.maps.LatLng(-25.05636,31.2281599999999), new
google.maps.LatLng(-25.05537,31.228109999999997), new
google.maps.LatLng(-25.05451,31.22802), new
google.maps.LatLng(-25.0540899999999,31.2279599999999), new
google.maps.LatLng(-25.0559699999999,31.2295799999999), new
google.maps.LatLng(-25.05779,31.2316399999999), new
google.maps.LatLng(-25.05997,31.2345299999999), new
google.maps.LatLng(-25.05995,31.234659999999998), new
google.maps.LatLng(-25.0594299999999,31.23443), new
google.maps.LatLng(-25.0596199999999,31.2361), new
google.maps.LatLng(-25.06213,31.240340000000003), new
google.maps.LatLng(-25.0642299999999,31.243029999999997), new
google.maps.LatLng(-25.06428,31.2434499999999), new
google.maps.LatLng(-25.0649799999999,31.24367), new
google.maps.LatLng(-25.06493,31.243509999999997), new
google.maps.LatLng(-25.06631,31.2439), new
google.maps.LatLng(-25.0657199999999,31.2428999999999), new
google.maps.LatLng(-25.06522,31.241529999999997), new
google.maps.LatLng(-25.06482,31.240029999999997), new
google.maps.LatLng(-25.0646899999999,31.23992), new
google.maps.LatLng(-25.0646099999999,31.2395199999999), new
google.maps.LatLng(-25.0636399999999,31.238459999999996), new
google.maps.LatLng(-25.0641299999999,31.240409999999997), new
google.maps.LatLng(-25.06483,31.2425), new
google.maps.LatLng(-25.064729999999997,31.24254), new
google.maps.LatLng(-25.06481,31.24258), new
google.maps.LatLng(-25.06482,31.2425999999999), new
google.maps.LatLng(-25.0653299999999,31.24258)
        ];
        
      }
    </script>

    <script async defer src="https://maps.googleapis.com/maps/api/js?key=AIzaSyBn7ge2QXDUzChRXagXYNfjpPne7Gos9Uc&libraries=visualization&callback=initMap"
    async defer></script>
  </body>
</html>
"""

f.write(message)
f.close()

#Change path to reflect file location
filename = 'file:///Users/Martina/Desktop/Projects/Hackathons/Railx/' + 'railx.html'
webbrowser.open_new_tab(filename)
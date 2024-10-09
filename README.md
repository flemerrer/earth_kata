
### Intro

Objective of the kata : find the greatest distance between two points diametrically opposed on Earth that pass through the center of the Earth.

### Notes & Ideas

#### Approach
TDD etc. learning python blabla

#### Todo
- Fix import of elevation 
- Add summits data to pool of data used in find_max_diam
- refactor functions for optimization and elegance
- add a function to use reverse geocoding via an API call to name points / couple

#### To improve the project
- Take into account the fact that Earth isn't perfectly flat. Diameter is bigger at the Equator (about +42km)
- Optimize the algorithm that finds the most probable candidates and filter the list to only test those and not ALL 
  the points on Earth
- Check the precision of the dataset and try to make it more precise (m to cm)
- !use satellite data to obtain a 3D mesh and convert functions to use 3D coordinates instead of latitude / longitude 
  coordinates
- Possible improvements to extend the project's scope :
  - Use Nominatim API from OSM to reverse geocode the locations found (https://nominatim.openstreetmap.org/reverse?lat=[value]&lon=[value]&[params])
  - Man-machine interface
  - Parametrize search

#### Highest summits on Earth (7 summits)

* Everest : 27.9880556,86.92500000000001
* Aconcagua : -32.6531111,-70.01205555555556
* Denali : 63.0694444,-151.0075
* Kilimanjaro : -3.0758333,37.35333333333333
* Vinson : -78.5255556,-85.61722222222221
* Elbrus : 43.355,42.439166666666665
* Mount Wilhelm : -5.8,145.03333333333333

### Intro

Objective of the kata : find the greatest distance between two points diametrically opposed on Earth that pass through the center of the Earth.

### Todo

1. Import json file as a dictionary to use in the project
2. Find a way to get only the most probables points that could give the desired result 
3. Parameters to take into account to filter the data : 
    - throw all points whose altitude is <= 0
    - altitude is > 4000 (Everest) 
    - antipodal points altitude <= 0 (Ocean)
4. Check for points in a range around those points (how big ?)
   - Question : whats the distance between 0,0 and 1,1 (latitude / longitude) ?
5. Revise data structure of points instances (Locations)
8. 

### Notes & Ideas

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


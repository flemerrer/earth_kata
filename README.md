### Intro

Objective of the kata : find the greatest distance between two points diametrically opposed on Earth that pass 
through the center of the Earth.

### Notes & Ideas

#### Approach

I've started using a Test Driven Development approach to code the first functions that used 2D coordinates to 
calculate the distance between two points. I've tried to iterate on this first version and looked for solutions to 
calculate the opposite point on Earth of any given point using 3D coordinates ; it seemed hard to implement. So I 
changed direction and looked into the method used to reverse latitude and longitude to calculate the antipodal point.

I've stumbled into some Python problems that I had to discover and solve, as I am learning the language with this 
project too. So I've jumbled a bit the TDD approach as I was going forward with my development. And I've also found 
difficult to make the API elevation import function to work properly with a wide array of points in time for review. 
So I've decided to generate random elevations for any round coordinates on the latitude / longitude grid. Using a 
pace of 1. Starting with 0,1 to 0,2 and up to 0,180 before starting over at 1,0 and going forward. 

I use those coordinates to calculate their respective antipodal points and pair them in a "couple" object that 
returns the distance between those points, using an approximation for the base diameter of Earth. I then use filters 
to reduce the list of probable couples and use an algorithm on the rest to find the greatest value possible.

I still have some fixes and tweaks to do. 

More thoughts about how I could improve the project below. 

#### Todo

- Fix import of elevation ; mass API call doesn't work as of yet
- Refactor functions for optimization and elegance
- Add a function to use reverse geocoding via an API call to name points / couple

#### To improve the project

- Take into account the fact that Earth isn't perfectly flat. Diameter is bigger at the Equator (about +42km)
- Optimize the algorithm that finds the most probable candidates and filter the list to only test those and not ALL
  the points on Earth
- Check the precision of the dataset and try to make it more precise (m to cm)
- !use satellite data to obtain a 3D mesh and convert functions to use 3D coordinates instead of latitude / longitude
  coordinates
- Possible improvements to extend the project's scope :
    - Use Nominatim API from OSM to reverse geocode the locations
      found (https://nominatim.openstreetmap.org/reverse?lat=[value]&lon=[value]&[params])
    - Man-machine interface
    - Parametrize search
- Look for a Postgres dataset of the Earth 

#### Highest summits on Earth (7 summits)

* Everest : 27.9880556,86.92500000000001
* Aconcagua : -32.6531111,-70.01205555555556
* Denali : 63.0694444,-151.0075
* Kilimanjaro : -3.0758333,37.35333333333333
* Vinson : -78.5255556,-85.61722222222221
* Elbrus : 43.355,42.439166666666665
* Mount Wilhelm : -5.8,145.03333333333333
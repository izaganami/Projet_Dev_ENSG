# Proj_Dev_ENSG

Demo website based on KeplerGl

## Getting Started

Clone this repository in your local server if you're willing to run it locally and avoid loading screens. (htdocs folder if using XAMPP)

To access the production server where the application is hosted click on the link below :                                         
[Production link](https://mapflow.herokuapp.com/)

### Prerequisites
Kepler is built upon [mapbox](https://www.mapbox.com/)

Here is a temporary MapBox Access Token which is used as part of our project
```
const MAPBOX_TOKEN = 'pk.eyJ1IjoiY3NhbWJvdW4iLCJhIjoiY2szM2txdHNjMDAyYTNocGVsb2pyMnY4OCJ9.7hHziezMIxIKxesfL3j_Yw';
```
If the page doesn't load, please make sure to have an Internet connection, or replace the line above in all pages with a new MapBox Access Token

## Deployment

To create a new page:

* Go to the [Kepler website demo](https://kepler.gl/demo)

* Drag your geojson or csv files in the browser

* Configure your parameters using the panel control on the left

* Export the map using the sharing button at the top right corner of the panel control and do not forget to paste the MapBox Access Token above

## Data

The data are divided into multiple files. 

Based on the database generation, certain attributes can be fictitious and others can be real. 

You can identify them in the panel control of kepler by clicking on it.

* *France wide*:  199 469 students, 496 505 arcs

* *Paris wide*: 21 138 students, 52 829 arcs

* *MLV wide*: 2 958 students, 7 446 arcs

* *Points: Domicile parentale*: same amount as student's, fictitious position

* *Points: résidence étudiante* (obtained by filtering Domicile courant): real position

* *Points: Lieu d'étude*: same amount as student's, real position

* *Points: Lieu de travail*: based on *lieu d'étude*, fictitious position

* *Hexbins*: same amount as points, real position for *étude*, fictitious for *domicile* and *travail*

* *Arc*: same amount as data's row, link between two points

* *Trips: étude*: 2 per student (round-trip)

* *Trips: travail*: 2 per student worker (round-trip)



## Authors

* **Jallouf Younes** - *Initial work* - [Izaganami](https://github.com/izaganami)
* **Alfred Mengin** - *Initial work* - [alfredmng](https://github.com/alfredmng)
* **Christophe Samboun** - *Initial work* - [csamboun](https://github.com/csamboun)
* **Arthur Genet** - *Initial work* - [ArthurGenet](https://github.com/ArthurGenet)






End.

# Proj_Dev_ENSG

A project designed to esthetically visualize dynamic data based on real and fictionally generated data.

## Getting Started

Clone this repository in your local server if you're willing to run it locally and avoid loading screens. (htdocs folder if using XAMPP)

To access the production server where the application is hosted click on the link below :                                         
[Production link](https://mapflow.herokuapp.com/)

### Prerequisites

For local use, after cloning make sure nodejs is running well on your side:

```
node -v
```
Same thing with npm in case you want to manage packages.

```
npm -v
```

Assuming everything works fine up to now, we are going to make sure you are running the appropriate python version (v 3.6.7) by running this command:
```
python --version
```

### Installing

Assuming we have all the prerequisites, the following step is making sure all the libraries are included. 

To skip this step all we got to do is including the .idea in our project locally which contains everything needed.

Otherwise, we can install them one by one using the commands below:

```
npm install express --save
npm install fs
npm install jsonl

pip install unittest
pip install psycopg2
pip install geojson
pip install numpy
pip install csv
pip install France
pip install shapely
pip install matplotlib
pip install socket
pip install urllib
pip install itertools
pip install geopy
pip install uuid
pip install re
pip install codecs
```
Sample data are available in the DataBase/Data_Created folder. You can use them directly with kepler.gl.

To create the data by yourself, open the file Main in the DataBase folder and run it. It creates the file "data_stud_200k" in the Data_Created folder. Then, run the Create_flow file, it will produce 4 files you can use with kepler.gl : "arc_200k.csv", "hexbin_200k.csv", "trip_etude_200k.csv" and "trip_travail_200k.csv"


## Deployment

The repository is linked with heroku's settings, which means all we have to do to deploy the application is pushing our modifications and changes into the right branch (beta for now) and it will be automatically built in case no errors are detected.

The port used for the deployment is specified server side by this variable:
```
const PORT = process.env.PORT || 3000;
```

## Built With

* [Kepler](https://kepler.gl/) - Geospatial analysis tool for large-scale data sets
* [Heroku](https://dashboard.heroku.com/apps) - Platform as a service (PaaS)
* [Nodejs](https://nodejs.org/en/) - JavaScript runtime
* [unittest](https://docs.python.org/2/library/unittest.html) - Unit testing framework for python
* [npm](https://www.npmjs.com/) - Node package manager
* [Express](https://expressjs.com/) - Web framework for Node.js





## Authors

* **Jallouf Younes** - *Initial work* - [Izaganami](https://github.com/izaganami)
* **Alfred Mengin** - *Initial work* - [alfredmng](https://github.com/alfredmng)
* **Christophe Samboun** - *Initial work* - [csamboun](https://github.com/csamboun)
* **Arthur Genet** - *Initial work* - [ArthurGenet](https://github.com/ArthurGenet)






End.

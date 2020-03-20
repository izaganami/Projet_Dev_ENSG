// Variables globales
var jours = [
    'Lundi',
    'Mardi',
    'Mercredi',
    'Jeudi',
    'Vendredi',
    'Samedi',
    'Dimanche'
    ];

// Table étudiants
    var etudiant = {"0" : {"id" : 0, "domicile_courant" :0, "domicile_familial" : 15, "lieu_etude" :34 , "lieu_travail" :40 , "trajet_courant_familial" :-1 , "trajet_courant_etude" : -1, "trajet_courant_travail" :-1  , "filiere" : "Médecine", "bourse" : true},
    "1" : {"id" : 1, "domicile_courant" : 1, "domicile_familial" : 16, "lieu_etude" : 35, "lieu_travail" : -1, "trajet_courant_familial" : -1, "trajet_courant_etude" :-1 , "trajet_courant_travail" : -1, "filiere" : "Mathématique", "bourse" : true},
    "2" : {"id" : 2, "domicile_courant" : 2, "domicile_familial" : 17, "lieu_etude" : 35, "lieu_travail" : -1, "trajet_courant_familial" : -1, "trajet_courant_etude" : -1, "trajet_courant_travail" :-1 , "filiere" :"Géographie" , "bourse" : true},
    "3" : {"id" : 3, "domicile_courant" :3 , "domicile_familial" : 18, "lieu_etude" : 35, "lieu_travail" : -1, "trajet_courant_familial" :-1 , "trajet_courant_etude" :-1 , "trajet_courant_travail" : -1 , "filiere" :"Droit" , "bourse" : true},
    "4" : {"id" : 4, "domicile_courant" : 4, "domicile_familial" : 19, "lieu_etude" : 36, "lieu_travail" :40 , "trajet_courant_familial" : -1, "trajet_courant_etude" :-1 , "trajet_courant_travail" : -1, "filiere" :"Ingénieur" , "bourse" :true },
    "5" : {"id" : 5, "domicile_courant" : 5, "domicile_familial" : 20, "lieu_etude" : 38, "lieu_travail" : -1, "trajet_courant_familial" : -1, "trajet_courant_etude" :-1 , "trajet_courant_travail" : -1, "filiere" : "Ingénieur", "bourse" :true },
    "6" : {"id" : 6, "domicile_courant" : 6, "domicile_familial" : 21, "lieu_etude" : 38, "lieu_travail" : 41, "trajet_courant_familial" : -1, "trajet_courant_etude" :-1 , "trajet_courant_travail" : -1, "filiere" : "Droit", "bourse" : true},
    "7" : {"id" : 7, "domicile_courant" :7 , "domicile_familial" : 22, "lieu_etude" : 38, "lieu_travail" : -1, "trajet_courant_familial" : -1, "trajet_courant_etude" :-1 , "trajet_courant_travail" : -1, "filiere" : "Droit", "bourse" : true},
    "8" : {"id" : 8, "domicile_courant" : 8, "domicile_familial" : 23, "lieu_etude" : 38, "lieu_travail" : -1, "trajet_courant_familial" : -1, "trajet_courant_etude" :-1 , "trajet_courant_travail" : -1 , "filiere" : "Droit", "bourse" : false},
    "9" : {"id" : 9, "domicile_courant" : 9, "domicile_familial" : 24, "lieu_etude" : 37, "lieu_travail" : -1, "trajet_courant_familial" : -1, "trajet_courant_etude" :-1 , "trajet_courant_travail" : -1 , "filiere" : "Médecine", "bourse" :false },
    "10" : {"id" : 10, "domicile_courant" :10 , "domicile_familial" : 25 , "lieu_etude" : 37, "lieu_travail" :42 , "trajet_courant_familial" : -1, "trajet_courant_etude" :-1 , "trajet_courant_travail" : -1 , "filiere" :"Médecine" , "bourse" :false },
    "11" : {"id" : 11, "domicile_courant" : 11, "domicile_familial" : 26, "lieu_etude" : 39, "lieu_travail" :-1 , "trajet_courant_familial" : -1, "trajet_courant_etude" :-1 , "trajet_courant_travail" : -1, "filiere" : "Informatique", "bourse" : false},
    "12" : {"id" : 12, "domicile_courant" : 12, "domicile_familial" : 27, "lieu_etude" : 39, "lieu_travail" : -1, "trajet_courant_familial" : -1, "trajet_courant_etude" :-1 , "trajet_courant_travail" : -1, "filiere" :"Informatique" , "bourse" :false },
    "13" : {"id" : 13, "domicile_courant" :13 , "domicile_familial" : 28, "lieu_etude" : 34, "lieu_travail" : -1, "trajet_courant_familial" : -1, "trajet_courant_etude" :-1 , "trajet_courant_travail" : -1, "filiere" : "Informatique", "bourse" : false},
    "14" : {"id" : 14, "domicile_courant" : 13, "domicile_familial" : 29, "lieu_etude" : 35, "lieu_travail" : -1, "trajet_courant_familial" : -1, "trajet_courant_etude" :-1 , "trajet_courant_travail" : -1, "filiere" :"Géographie" , "bourse" :false },
    "15" : {"id" : 15, "domicile_courant" : 13, "domicile_familial" : 30, "lieu_etude" : 36, "lieu_travail" :41 , "trajet_courant_familial" : -1, "trajet_courant_etude" :-1 , "trajet_courant_travail" : -1, "filiere" :"Ingénieur" , "bourse" : false},
    "16" : {"id" : 16, "domicile_courant" : 14, "domicile_familial" : 31, "lieu_etude" : 37, "lieu_travail" : -1, "trajet_courant_familial" :-1 , "trajet_courant_etude" :-1 , "trajet_courant_travail" : -1 , "filiere" : "Ingénieur", "bourse" : false},
    "17" : {"id" : 17, "domicile_courant" : 14, "domicile_familial" : 32, "lieu_etude" : 38, "lieu_travail" :41 , "trajet_courant_familial" : -1,"trajet_courant_etude" :-1 , "trajet_courant_travail" : -1, "filiere" : "Ingénieur", "bourse" : false},
    "18" : {"id" : 18, "domicile_courant" : 14, "domicile_familial" : 33, "lieu_etude" : 39, "lieu_travail" : -1, "trajet_courant_familial" : -1, "trajet_courant_etude" :-1 , "trajet_courant_travail" : -1, "filiere" : "Ingénieur", "bourse" : false},
    "19" : {"id" : 17, "domicile_courant" :14, "domicile_familial" : 33, "lieu_etude" :36 , "lieu_travail" :42 , "trajet_courant_familial" : -1, "trajet_courant_etude" :-1 , "trajet_courant_travail" : -1, "filiere" :"Ingénieur" , "bourse" :false }
    };
    
    var logement = {"0" : {"id" : 0, "lat" : 48.8393948, "lng" :2.6482998 , "nom" : "Torcy"},
    "1" : {"id" : 1, "lat" : 48.853927, "lng" :2.6657376 , "nom" :"Saint-Thibault-des-vignes" },
    "2" : {"id" : 2, "lat" : 48.840852, "lng" :2.7106282 , "nom" : "Bussy-Saint-Georges"},
    "3" : {"id" : 3, "lat" :48.8796624 , "lng" : 2.5864375, "nom" :"Chelles" },
    "4" : {"id" : 4, "lat" :48.848906 , "lng" : 2.6046848, "nom" : "Champs-sur-Marne"},
    "5" : {"id" : 5, "lat" : 48.8685686, "lng" : 2.5205634, "nom" :"Neuilly-sur-Marne" },
    "6" : {"id" : 6, "lat" :48.8359511 , "lng" :2.6351754 , "nom" : "Lognes"},
    "7" : {"id" : 7, "lat" : 48.8488202, "lng" : 2.5533365, "nom" : "Noisy-le-Grand"},
    "8" : {"id" : 8, "lat" : 48.8535759, "lng" :2.5992486 , "nom" : "Champs-sur-Marne"},
    "9" : {"id" : 9, "lat" :48.8755478 , "lng" :2.705576 , "nom" :"Lagny-sur-Marne" },
    "10" : {"id" : 10, "lat" :48.8455411 , "lng" :2.5709662 , "nom" :"Noisy-le-Grand"},
    "11" : {"id" : 11, "lat" : 48.7990104, "lng" : 2.6045298, "nom" :"Pontault-Combault"},
    "12" : {"id" : 12, "lat" : 48.852584, "lng" : 2.6659695, "nom" :"Saint-Thibault-des-vignes" },
    "13" : {"id" : 13, "lat" :48.8533567 , "lng" : 2.5200354, "nom" :"ARPEJ" },
    "14" : {"id" : 14, "lat" : 48.8424127, "lng" : 2.5858051, "nom" : "CROUS"},
    "15" : {"id" : 15, "lat" :50.359092 , "lng" :3.083795 , "nom" : "Douai"},
    "16" : {"id" : 16, "lat" :49.047820 , "lng" :2.040596 , "nom" : "Cergy"},
    "17" : {"id" : 17, "lat" : 48.542928, "lng" :2.661065 , "nom" : "Melun"},
    "18" : {"id" : 18, "lat" : 47.381229, "lng" : 0.689101, "nom" : "Tours"},
    "19" : {"id" : 19, "lat" : 47.248776, "lng" : 6.026342, "nom" : "Besançon" },
    "20" : {"id" : 20, "lat" : 44.896968, "lng" :6.636316 , "nom" :"Briançon" },
    "21" : {"id" : 21, "lat" : 46.807333, "lng" : 1.684283, "nom" :"Chateauroux" },
    "22" : {"id" : 22, "lat" : 49.027165, "lng" : 2.466378, "nom" :"Goussainville" },
    "23" : {"id" : 23, "lat" : 43.926249, "lng" : 2.157360, "nom" : "Albi"},
    "24" : {"id" : 24, "lat" :47.906491 , "lng" : 7.209693, "nom" :"Guebwiller" },
    "25" : {"id" : 25, "lat" : 43.584747, "lng" : 7.117548, "nom" : "Antibes"},
    "26" : {"id" : 26, "lat" :49.174906 , "lng" : 2.459616, "nom" :"Chantilly" },
    "27" : {"id" : 27, "lat" : 49.415927, "lng" : 0.232603, "nom" :"Honfleur" },
    "28" : {"id" : 28, "lat" : 48.904477, "lng" :2.813539 , "nom" : "Esbly"},
    "29" : {"id" : 29, "lat" : 48.771035, "lng" : 2.027973, "nom" : "Montigny-le-Bretonneux"},
    "30" : {"id" : 30, "lat" : 47.998854, "lng" : 2.729425, "nom" : "Montargis" },
    "31" : {"id" : 31, "lat" : 48.895474, "lng" : 2.203011, "nom" : "Nanterre"},
    "32" : {"id" : 32, "lat" : 49.354821, "lng" : 6.156334, "nom" : "Thionville"},
    "33" : {"id" : 33, "lat" : 48.440074, "lng" : 1.483170, "nom" :"Chartres" },
    "34" : {"id" : 34, "lat" :48.8410265 , "lng" : 2.5851349, "nom" : "ENSG"},
    "35" : {"id" : 35, "lat" :48.839605 , "lng" :2.587186 , "nom" : "UPEM"},
    "36" : {"id" : 36, "lat" :48.8396339 , "lng" : 2.5840083, "nom" : "ESIEE"},
    "37" : {"id" : 37, "lat" : 48.8411598, "lng" : 2.5918843, "nom" : "École d’architecture de la ville & des territoires Paris-Est"},
    "38" : {"id" : 38, "lat" : 48.8407092, "lng" : 2.5849027, "nom" : "ENPC"},
    "39" : {"id" : 39, "lat" : 48.8365277, "lng" :2.5896857 , "nom" : "ESO"},
    "40" : {"id" : 40, "lat" : 48.8339272, "lng" :2.6418314 , "nom" : "McdoLognes"},
    "41" : {"id" : 40, "lat" : 48.8371823, "lng" :2.6611877 , "nom" : "CarrefourBay2"},
    
    }



mapboxgl.accessToken = 'pk.eyJ1IjoiY3NhbWJvdW4iLCJhIjoiY2szM2txdHNjMDAyYTNocGVsb2pyMnY4OCJ9.7hHziezMIxIKxesfL3j_Yw'
var map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/streets-v9',
    center: [1.71,46.74], // starting position [lng, lat]
    zoom: 5 // starting zoom
    });

// Faire un map on load de cette partie
function filterBy(jour) {
    // Set the label to the month
    document.getElementById('jour').textContent = jours[jour];
    }
    
filterBy(0, jours);
var slider = document.getElementById('slider');
slider.addEventListener('input', function(e) {
    let jour = parseInt(e.target.value, 10);
    console.log(jour, e.target.value)
    filterBy(jour);
    });
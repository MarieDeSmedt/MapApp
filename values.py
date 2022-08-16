import json


typeDrive_list = ['AUCHAN DRIVE','CASINO DRIVE', 'CARREFOUR DRIVE','CHRONODRIVE','CORA DRIVE', 'E. LECLERC DRIVE', 'HOURA DRIVE',
'LE DRIVE INTERMARCHE','LEADER DRIVE', 'MATCH DRIVE', 'METRO DRIVE',
'MONOPRIX DRIVE','PROMOCASH DRIVE','SIMPLY DRIVE',
'SPAR DRIVE']

icons ={
    'drive':[
        {
            'nom_enseigne' : 'AUCHAN DRIVE',
            'icon_url' : "marker_auchan.png" ,
            'icon_size': (25,25)
        },
        {
            'nom_enseigne' : 'CARREFOUR DRIVE',
            'icon_url' : "carrefour.jfif" ,
            'icon_size': (25,25)
        },
        {
            'nom_enseigne' : 'E. LECLERC DRIVE',
            'icon_url' : "leclerc.jfif" ,
            'icon_size': (20,20)
            
        },
        {
            'nom_enseigne' : 'LE DRIVE INTERMARCHE',
            'icon_url' : "intermarche.jfif" ,
            'icon_size': (25,25)
            
        },
        {
            'nom_enseigne' : 'LEADER DRIVE',
            'icon_url' : "leader.png" ,
            'icon_size': (25,25)
            
        },
        {
            'nom_enseigne' : 'CHRONODRIVE',
            'icon_url' : "chrono.jfif" ,
            'icon_size': (25,25)
            
        },
        {
            'nom_enseigne' : 'CASINO DRIVE',
            'icon_url' : "casino.jfif" ,
            'icon_size': (25,25)
            
        },
        {
            'nom_enseigne' : 'MONOPRIX DRIVE',
            'icon_url' : "monoprix.png" ,
            'icon_size': (25,25)
            
        },
        {
            'nom_enseigne' : 'HOURA DRIVE',
            'icon_url' : "houra.jfif" ,
            'icon_size': (25,25)
            
        },
        {
            'nom_enseigne' : 'METRO DRIVE',
            'icon_url' : "metro.png" ,
            'icon_size': (25,25)
            
        },
        {
            'nom_enseigne' : 'SIMPLY DRIVE',
            'icon_url' : "simply.png" ,
            'icon_size': (25,25)
            
        },
        {
            'nom_enseigne' : 'U DRIVE',
            'icon_url' : "Udrive.jfif" ,
            'icon_size': (25,25)
            
        },
        {
            'nom_enseigne' : 'PROMOCASH DRIVE',
            'icon_url' : "promocash.png" ,
            'icon_size': (25,25)
            
        },
        {
            'nom_enseigne' : 'CORA DRIVE',
            'icon_url' : "cora.png" ,
            'icon_size': (25,25)
            
        },
        {
            'nom_enseigne' : 'MATCH DRIVE',
            'icon_url' : "match.png" ,
            'icon_size': (25,25)
            
        },
        {
            'nom_enseigne' : 'SPAR DRIVE',
            'icon_url' : "spar.png" ,
            'icon_size': (25,25)
            
        }
    ],
    'darkstore':[{'nom_enseigne' : 'darkstore',
            'icon_url' : "bicycle.png" ,
            'icon_size': (25,25)}]
    
}


formats_list = ['DRIVE','QUICK COMMERCE','LAD','PIETON']

cities = {
    'city' : [
        {
            'nom' : 'Bordeaux',
            'latitude' : 44.8367,
            'longitude' : -0.58107
        },
        {
            'nom' : 'Brest',
            'latitude' : 48.39043,
            'longitude' : -4.48658
        },
        {
            'nom' : 'Lille',
            'latitude' : 50.6282,
            'longitude' : 3.06881
        },
        {
            'nom' : 'Lyon',
            'latitude' : 45.75917,
            'longitude' : 4.82965
        },
        {
            'nom' : 'Marseille',
            'latitude' : 43.29337,
            'longitude' : 5.37131
        },
        {
            'nom' : 'Nantes',
            'latitude' : 47.21811,
            'longitude' : -1.55306
        },
        {
            'nom' : 'Paris',
            'latitude' : 48.85717,
            'longitude' : 2.3414
        },
        {
            'nom' : 'Strasbourg',
            'latitude' : 48.58504,
            'longitude' : 7.73642
        },
        {
            'nom' : 'Toulouse',
            'latitude' : 43.60579,
            'longitude' : 1.44863
        }
    ]
}



territories = {
    'territory' : [

  {
    "territoryLabel": "EST",
    "longitude": 5.60984605583475,
    "latitude": 48.69586941510869
  },
  {
    "territoryLabel": "ILE-DE-FRANCE",
    "longitude": 2.4805003703964954,
    "latitude": 48.73474076615772
  },
  {
    "territoryLabel": "NORD",
    "longitude": 2.4051971453298817,
    "latitude": 49.900511291438335
  },
  {
    "territoryLabel": "OUEST",
    "longitude": -1.5304054701174363,
    "latitude": 48.51127854716114
  },
  {
    "territoryLabel": "SUD",
    "longitude": 5.161922427725334,
    "latitude": 43.799676346633056
  }
    ]
}


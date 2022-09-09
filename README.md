<h1 align="center">Welcome to hltv-data 👋 🎮</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-0.3.0-blue.svg?cacheSeconds=2592000" />
  <a href="#" target="_blank">
    <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg" />
  </a>
</p>

> Data from popular CS:GO website hltv.org

## Install

```sh
pip install hltv-data
```

## Usage

The public methods can be reached using ```HLTVClient```
```sh
from hltv_data import HLTVClient

hltv_client = HLTVClient()

```

#### Current ranking
```sh
hltv_client.get_ranking()
```

```sh
Response:

[
    {"position": 1, "name": "Natus Vincere", "points": 1000},
    {"position": 2, "name": "Gambit", "points": 822},
    {"position": 3, "name": "G2", "points": 629},
    {"position": 4, "name": "FaZe", "points": 409},
    {"position": 5, "name": "Virtus.pro", "points": 362},
    {"position": 6, "name": "Astralis", "points": 346},
    {"position": 7, "name": "Heroic", "points": 333},
    {"position": 8, "name": "NIP", "points": 287},
    {"position": 9, "name": "Vitality", "points": 282},
    {"position": 10, "name": "OG", "points": 241},
    {"position": 11, "name": "BIG", "points": 239},
    {"position": 12, "name": "Spirit", "points": 231},
    {"position": 13, "name": "Liquid", "points": 196},
    {"position": 14, "name": "mousesports", "points": 183},
    {"position": 15, "name": "forZe", "points": 179},
    {"position": 16, "name": "FURIA", "points": 176},
    {"position": 17, "name": "Complexity", "points": 164},
    {"position": 18, "name": "Entropiq", "points": 151},
    {"position": 19, "name": "Sinners", "points": 102},
    {"position": 20, "name": "ENCE", "points": 100},
    {"position": 21, "name": "Renegades", "points": 94},
    {"position": 22, "name": "SKADE", "points": 94},
    {"position": 23, "name": "AGO", "points": 89},
    {"position": 24, "name": "K23", "points": 82},
    {"position": 25, "name": "Extra Salt", "points": 79},
    {"position": 26, "name": "Endpoint", "points": 77},
    {"position": 27, "name": "Copenhagen Flames", "points": 76},
    {"position": 28, "name": "Evil Geniuses", "points": 71},
    {"position": 29, "name": "FunPlus Phoenix", "points": 60},
    {"position": 30, "name": "DBL PONEY", "points": 58},
]
```


#### Matches
```sh
hltv_client.get_matches()
```

```sh
Response:

[
    {
        "event": "ESL Pro League Season 16",
        "date": "2022-09-10T16:00:00",
        "team_1": "Outsiders",
        "team_2": "MIBR",
        "star_rating": 1
    },
    {
        "event": "ESL Pro League Season 16",
        "date": "2022-09-10T19:30:00",
        "team_1": "FaZe",
        "team_2": "G2",
        "star_rating": 3
    },
    ...
]
```


#### Results
```sh
hltv_client.get_results()
```

```sh
Response:

[
    {
        "event": "ESL Pro League Season 14",
        "team_1": {
            "name": "Vitality",
            "result": 2
        },
        "team_2": {
            "name": "Natus Vincere",
            "result": 3
        }
    },
    {
        "event": "Fragadelphia 15",
        "team_1": {
            "name": "Third Impact",
            "result": 1
        },
        "team_2": {
            "name": "Coldest Riders",
            "result": 2
        }
    },
    ...
]
```


## Author

👤 **Dariusz Choruzy**

* Website: http://choruzy.com/
* Github: [@dchoruzy](https://github.com/dchoruzy)
* LinkedIn: [@dchoruzy](https://www.linkedin.com/in/dchoruzy/)

## 🤝 Contributing

Contributions, issues and feature requests are welcome!<br />Feel free to check [issues page](https://github.com/dchoruzy/hltv-data/issues). 

## Show your support

Give a ⭐️ if this project helped you!

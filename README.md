# Public API gateway in the University of Illinois at Urbana-Champaign
[![Build Status][travis-image]][travis-url] [![Deploy Status](https://img.shields.io/badge/deploy-unknown-yellow.svg)](https://img.shields.io)  
The University of Illinois at Urbana-Champaign API gateway allows anyone to build applications using data of the campus easily. It integrates data from multiple sources and websites in the public gateway, with the help of AWS chalice. 

#### Notes: 
- This is an unofficial development and is not supported or controlled by the University of Illinois at Urbana-Champaign itself.
- These skills are currently being developed in progess, they are not guaranteed to function properly.

## Accessing the API
All calls are made to the following URL with the required parameters for a given service.
```
https://69smoo2dc6.execute-api.us-east-1.amazonaws.com/api
```
The data is returned in `json` format.

## Endpoints
#### EWS/ICS Workstation
- /ews
- /ics
- /ics/{department}

#### Sports
- /sports/check
- /sports/list
- /spots/{sport}

#### Dining
- /dining/{hall}
- /dining/{hall}/{date}
- /dining/{hall}/{date_from}/{date_to}

#### Library
- /library
- /library/{library_id}/{year}/{month}/{date}

#### Buildings 
- /buildings
- /buildings/{building_id}

## Developers
### Student Innovation Lab, TechService, the University of Illinois at Urbana-Champaign
[Feng Xiyang](https://github.com/andyfengHKU)  
[Wang Jikun](https://github.com/WagJK)  

## Disclaimer
This project is initially developed by Student Innovation Lab of TechService of the University of Illinois at Urbana-Champaign.

[travis-url]: https://travis-ci.org/andyfengHKU/uiuc-api-chalice
[travis-image]: https://travis-ci.org/andyfengHKU/uiuc-api-chalice.svg?branch=master

<img src="LogoColor.png" alt="logo" width="200">

# What To Watch [![Build Status](https://travis-ci.com/chodges7/WhatToWatch.svg?branch=master)](https://travis-ci.com/chodges7/WhatToWatch)

## Developers
* Product Owner: Christian Hodges, [chodges7](https://github.com/chodges7)
* Scrum Master: Lukas Pecson, [lpecson](https://github.com/lpecson)
* Developer: Vidit Dhaka, [vdhaka](https://github.com/vdhaka)

## Entrepreneurs
* Matthew Martell
* Nate Rehm
* Nicholas Whitley

## Getting started
### Dependancies that you need:
* pip
* python3
* pillow

### How to get it running on your own machine
* First you need to make a virtual enviornment (venv) to run python  
```python3 -m venv ./```
* Next, boot up the venv by running the command  
Mac: ```source bin/activate```  
Windows: ```whattowatch/bin/activate```  
* then install the requirements for the project  
```pip install -r requirements.txt```
* there also might be some migrations that need to happen in the database so run this command  
Mac: ```python3 manage.py migrate```  
Windows: ```py manage.py migrate```  
* finally, boot up the local server  
Mac: ```python3 manage.py runserver```  
Windows: ```py manage.py runserver```

The website should be avalible on the local host website [http://127.0.0.1:8000](http://127.0.0.1:8000)

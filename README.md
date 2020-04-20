# simpleCalculatorRestAPI
A flask Rest API for simple calculations


In order to locally deploy the application : 

* git clone the repo
* In case of linux/mac :
```bash
export FLASK_APP=app.py
export FLASK_ENV=development
```
For Windows system : 

```cmd
set FLASK_APP=app.py
set FLASK_ENV=development
```

then simply run the application using : 

```bash
flask run
```

**Please note : DO NOT USE FLASK_ENV=development in case of a public IP machine or production environment**

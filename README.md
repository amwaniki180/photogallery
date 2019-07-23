# [PHOTO GALLERY][(https://agile-inlet-62008.herokuapp.com/)]
### Simple photo gallery web application to showcase beautiful pictures and designs 
### July 22, 2019
#### By **[ANTONY MWANIKI](https://github.com/amwaniki180)**
## Description
[PHOTO GALLERY]((https://agile-inlet-62008.herokuapp.com/)) is a simple photo gallery web application to showcase beautiful pictures and designs. Users get to view photos updated by the site admin. Users can see photos based on the location, by clicking on the listed locations in the menu. They can also copy the link to a photo to paste at their discretion. The search functionality will search photos based on the categories. 

## Set Up and Installations
### Prerequisites
1. Ubuntu Software
2. Python3.6
3. [Postgres](https://www.postgresql.org/download/)
4. [python virtualenv](https://gist.github.com/Geoyi/d9fab4f609e9f75941946be45000632b)
### Clone the Repo
Run the following command on the terminal:
`git clone https://github.com/amwaniki180/photogallery`
### Activate virtual environment
Activate virtual environment using python3.6 as default handler
```bash
virtualenv -p /usr/bin/python3.6 venv && source venv/bin/activate
```
### Install dependancies
Install dependancies that will create an environment for the app to run
`pip3 install -r requirements.txt`
### Create the Database
```bash
psql
CREATE DATABASE photos;
```
### .env file
Create .env file and paste paste the following filling where appropriate:
```python
SECRET_KEY = '<Secret_key>'
DBNAME = 'photos'
USER = '<Username>'
PASSWORD = '<password>'
DEBUG = True
```
### Run initial Migration
```bash
python3.6 manage.py makemigrations photos
python3.6 manage.py migrate
```
### Run the app
```bash
python3.6 manage.py runserver
```
Open terminal on `localhost:8000`
## Known bugs
Copy functionality does not work
## Technologies used
    - Python 3.6
    - HTML
    - Bootstrap 4
    - Bootstrap 3
    - JavaScript
    - Heroku
    - Postgresql
## Support and contact details
Contact me on developer on amwaniki180@gmail.com for any comments, reviews or advice.
## License
MIT License Copyright (c) {2019} ANTONY MWANIKI



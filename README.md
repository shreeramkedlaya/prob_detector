## <div align="center">COVID-19 PROBABILITY DETECTOR</div>
This project is designed to predict whether a patient is COVID-19 positive or not using Django and Python.

## Prerequisites

- Python 3.x installed on your system
- pip (Python package installer) installed on your system

## Project Setup

### Step 1: Clone the Repository

```sh
git clone https://github.com/shreeramkedlaya/prob_detector.git
cd prob_detector
```
### Step 2: Create a Virtual Environment

Create and use virtual environment to manage dependencies for the project.

```sh
python -m venv venv
```

### Step 3: Activate the Virtual Environment
 - On Windows
 ```sh
 .\venv\Scripts\activate
 ```
  - On macOS and Linux:
  ```sh
  source venv/bin/activate
  ```
### Step 4: Install the required packages
```sh
pip install -r requirements.txt
```
### Step 5: Create the Django Project
```sh
django-admin startproject prob_detector
```

### Step 7: Go inside the prob_detector folder and migrate the packages
```sh
cd prob_detector
python manage.py makemigrations
python manage.py migrate
```
This will create a *db.sqlite3* database file that is used by the project
### Step 8: Start your server
```sh
python manage.py runserver
```
Visit your website on your favorite browser at [127.0.0.1:8000](http://127.0.0.1:8000)

# Starbucks Coffee Menu Web App

A small Flask web application that collects Starbucks Taiwan coffee menu data, stores it in a SQLite database, and displays the drinks on a web page.

## Project Overview

This project originated from a group assignment for a Database course during my undergraduate studies. I later reorganized and refactored the project to improve its structure and make it easier to run and maintain.

## Features

- Scrape coffee menu data from the Starbucks Taiwan website.
- Store drink information in a SQLite database.
- Prevent duplicate records when inserting data.
- Display Chinese and English drink names through a Flask web application.

## Technologies

- Python
- Flask
- SQLite
- Requests
- BeautifulSoup
- HTML
- Jinja2

## Project Structure

```text
starbucks-menu-web-app/
├── app.py
├── database.py
├── scraper.py
├── seed_data.py
├── requirements.txt
├── .gitignore
└── templates/
    └── index.html
```

## Getting Started

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Initialize the database with sample data

```bash
python seed_data.py
```

### 3. Run the web application

```bash
python app.py
```

Open your browser and visit:

http://127.0.0.1:5000

### 4. Update menu data

```bash
python scraper.py
```

## What I Learned

- Retrieving and parsing data from web pages.
- Designing and interacting with a relational database.
- Connecting a Flask backend with an HTML frontend.
- Organizing Python code into separate modules.
- Handling duplicate records in a database.

## Notes

This project is an educational project and is not affiliated with Starbucks.

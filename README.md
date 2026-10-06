# Calorie Counter

## Project Description

Calorie Counter is a simple Django web application that helps users keep track of the food they eat and the calories they consume. Users can add food items, view their food list, see the total calories, delete food items, and reset the calorie count.

## Features

- Add food items
- Enter calories for each food item
- View all added food items
- Calculate total calories
- Delete individual food items
- Reset all food items and calories
- Form validation
- Responsive design
- Django template inheritance
- Clean and simple user interface

## Technologies

- Python
- Django
- HTML5
- Tailwind CSS
- SQLite
- Git
- GitHub

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/calorie_counter.git
```

### 2. Open the project

```bash
cd calorie_counter
```

### 3. Create a virtual environment

```bash
python -m venv myenv
```

### 4. Activate the virtual environment

#### Windows

```bash
myenv\Scripts\activate
```

#### macOS/Linux

```bash
source myenv/bin/activate
```

### 5. Install Django

```bash
pip install django
```

### 6. Apply migrations

```bash
python manage.py migrate
```

## Project Structure

```text
calorie_counter/
│
├── manage.py
├── db.sqlite3
├── .gitignore
├── README.md
│
├── calorie_counter/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
└── calorie_tracker/
    ├── migrations/
    │   └── __init__.py
    ├── templates/
    │   ├── base.html
    │   ├── navbar.html
    │   └── index.html
    ├── admin.py
    ├── apps.py
    ├── forms.py
    ├── models.py
    ├── urls.py
    ├── views.py
    └── tests.py
```

## How It Works

The application uses a Django form to collect the food name and calorie amount from the user.

After submitting the form, the food item is saved to the database and displayed on the home page.

The application calculates the total calories from all stored food items.

Users can also delete food items or reset all food records.

## How to Run

Start the Django development server:

```bash
python manage.py runserver
```

Then open the application in your browser:

```text
http://127.0.0.1:8000/
```

## Author

**Nimo Ali**

Software Engineering Student

Interested in Web Development and Software Engineering.
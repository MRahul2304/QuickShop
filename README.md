# QuickShop - E-commerce Project

QuickShop is a full-featured e-commerce web application built with Django. It offers a user-friendly interface for browsing, searching, and purchasing products. The project includes features like product listings, product details, cart management, user registration, and authentication.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Contributing](#contributing)
- 
## Features

- User registration and authentication
- Product listings by categories
- Product detail pages with add-to-cart functionality
- Shopping cart management
- Search functionality
- Responsive design with Bootstrap
- Admin interface for managing products and categories
- Static and media file management

## Technologies Used

- Python 3.8+
- Django 5.0
- MySQL
- Bootstrap 5
- JavaScript (ES6)
- HTML5 & CSS3

## Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

- Python 3.8 or higher
- MySQL database
- Git

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/your_username/e_commerce_project.git
   ```
2. Change to the project directory
   ```sh
   cd e_commerce_project
   ```
3. Create and activate a virtual environment
   ```sh
   python -m venv env
   source env/bin/activate   # On Windows use `env\Scripts\activate`
   ```
4. Install the required packages
   ```sh
   pip install -r requirements.txt
   ```
5. Set up the database
   ```sh
   python manage.py migrate
   ```
6. Create a superuser for the admin interface
   ```sh
   python manage.py createsuperuser
   ```
7. Run the development server
   ```sh
   python manage.py runserver
   ```

### Configuration

Update the `DATABASES` setting in `e_commerce_project/settings.py` with your MySQL database credentials.

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'quickshop',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

## Project Structure

```bash
e_commerce_project/
├── e_commerce_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── shop/
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
├── static/
│   ├── css/
│   ├── images/
├── templates/
│   ├── shop/
│   ├── base.html
├── manage.py
├── requirements.txt
```

## Usage

### Running the application

Start the Django development server:

```sh
python manage.py runserver
```

Open your browser and navigate to `http://127.0.0.1:8000/` to see the application in action.

### Admin Interface

To access the admin interface, go to `http://127.0.0.1:8000/admin` and log in with the superuser credentials created earlier.

### Adding Products and Categories

1. Log in to the admin interface.
2. Add categories and products via the respective sections.

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/your-feature`)
3. Commit your Changes (`git commit -m 'Add some feature'`)
4. Push to the Branch (`git push origin feature/your-feature`)
5. Open a Pull Request



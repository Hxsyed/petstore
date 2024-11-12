# PetStore Flask Application

This is a simple web application for managing pets, built with Flask, SQLite, and Docker. The application provides a user-friendly interface to view, add, delete, and search pets. It includes a backend API that can be tested with Postman.

## Features

- View a list of pets with details
- Search for pets by name or type
- Add new pets to the database
- Delete pets by name (all entries with the given name)
- Basic UI for interaction (built with HTML templates)
- RESTful API for CRUD operations

## Tech Stack

- **Backend**: Flask (Python)
- **Database**: SQLite
- **Frontend**: HTML templates (Jinja2)
- **Containerization**: Docker
- **API Testing**: Postman

## Folder Structure

```plaintext
petstore/
├── backend/
│   ├── app.py             # Main Flask application
│   ├── pets.db            # SQLite database
├── frontend/
│   ├── home.html          # Main page template
│   ├── base.html          # Base template with shared layout
│   ├── pet_details.html   # Template for individual pet details
│   ├── contact.html       # Contact page template
├── static/
│   └── style.css          # CSS for styling
└── Dockerfile             # Docker configuration
└── docker-compose.yml     # Docker Compose file
└── .gitignore             # Git ignore file
└── README.md              # This file

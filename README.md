```markdown
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
```

## Setup and Installation

### Prerequisites

- Python 3.7 or higher
- Docker and Docker Compose

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/petstore.git
cd petstore
```

### 2. Set up a Virtual Environment (optional but recommended)

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Initialize the Database

If you don’t have a `pets.db` file, create an empty one in `backend/pets.db`. Ensure your `app.py` file points to this path.

### 5. Run the Application

```bash
export FLASK_APP=backend/app.py
flask run
```

### 6. Run with Docker

You can use Docker to containerize and run the application:

```bash
docker-compose up --build
```

The application will be available at `http://localhost:5000`.

## API Endpoints

| Endpoint                       | Method | Description                       |
|--------------------------------|--------|-----------------------------------|
| `/`                            | GET    | Displays the list of pets         |
| `/pet/<int:pet_id>`            | GET    | View details of a specific pet    |
| `/add_pet`                     | POST   | Add a new pet                     |
| `/delete_pet_by_name/<string:name>` | DELETE | Delete pets by name        |
| `/contact`                     | GET/POST | Contact form for the application |

## Testing with Postman

To test the API endpoints:
1. Open Postman and create a new request.
2. Use the URL `http://localhost:5000` with the specific endpoint and method.
3. Send JSON data for POST requests as needed (e.g., for adding a new pet).

## Known Issues

- **Database Locked**: If you encounter a `database is locked` error, ensure that only one connection is active at a time.
- **Image Loading**: Verify that images are accessible through the provided URL, or use placeholder images as needed.

## License

This project is licensed under the MIT License.
```

This `README.md` includes installation, usage, and troubleshooting steps to help users set up and run the project effectively. Adjust any URLs and other project details specific to your setup before sharing.

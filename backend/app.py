from flask import Flask, request, g, render_template, redirect, url_for
import sqlite3

app = Flask(__name__, template_folder='../frontend')

DATABASE = 'backend/pets.db'

# Open a new database connection for each request
def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row  # To return rows as dictionaries
    return g.db

# Close the database connection after each request
@app.teardown_appcontext
def close_db(error):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

# This function initializes the database if it's not already set up
def init_db():
    conn = get_db()
    with app.app_context():  # Ensure it's within the app context
        conn.execute('''
            CREATE TABLE IF NOT EXISTS pets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                type TEXT NOT NULL,
                age INTEGER
            )
        ''')
        conn.commit()

# Initialize the database on startup
with app.app_context():
    init_db()

@app.route("/")
def home():
    search_query = request.args.get('search', '').strip()
    conn = get_db()

    # Fetch pets based on search query or show all pets
    if search_query:
        pets = conn.execute("SELECT * FROM pets WHERE name LIKE ? OR type LIKE ?", 
                            (f"%{search_query}%", f"%{search_query}%")).fetchall()
    else:
        pets = conn.execute("SELECT * FROM pets").fetchall()
    
    conn.close()
    return render_template("home.html", pets=pets, search_query=search_query)

@app.route("/pet/<int:pet_id>")
def pet_details(pet_id):
    conn = get_db()
    pet = conn.execute("SELECT * FROM pets WHERE id = ?", (pet_id,)).fetchone()
    
    if pet is None:
        return "Pet not found", 404
    
    return render_template("pet_details.html", pet=pet)

@app.route("/add_pet", methods=["GET", "POST"])
def add_pet():
    if request.method == "POST":
        name = request.form.get('name')  # Get the 'name' field from the form
        type_ = request.form.get('type')
        age = request.form.get('age')

        if not name:
            return "Error: Pet name is required.", 400  # If the name is missing, show an error

        # Check if the pet already exists
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM pets WHERE name = ? AND type = ?', (name, type_))
        existing_pet = cursor.fetchone()

        if existing_pet:
            return "Error: This pet already exists.", 400  # Return error if duplicate exists

        # Insert new pet if it doesn't exist
        conn.execute('INSERT INTO pets (name, type, age) VALUES (?, ?, ?)', (name, type_, age))
        conn.commit()

        return redirect(url_for('home'))  # Redirect to home page after adding the pet

    return render_template("add_pet.html")  # Render the form if it's a GET request

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        # Process contact form (e.g., send an email or store the message)
        return redirect(url_for("home"))  # Redirect to home page after submission
    return render_template("contact.html")

@app.route("/removeduplicates", methods=["GET", "POST"])
def remove_duplicates():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    # Remove duplicates by keeping only one entry for each name and type
    cursor.execute('''
        DELETE FROM pets
        WHERE rowid NOT IN (
            SELECT MIN(rowid)
            FROM pets
            GROUP BY name, type
        );
    ''')
    conn.commit()
    conn.close()

@app.route("/delete_pet_by_name/<string:pet_name>", methods=["DELETE"])
def delete_pet_by_name(pet_name):
    conn = get_db()
    cursor = conn.cursor()

    # Check if any pets with the given name exist
    pets = cursor.execute("SELECT * FROM pets WHERE name = ?", (pet_name,)).fetchall()
    if not pets:
        return {"error": f"No pets found with the name '{pet_name}'"}, 404

    # Delete all pets with the given name
    cursor.execute("DELETE FROM pets WHERE name = ?", (pet_name,))
    conn.commit()
    conn.close()
    return {"message": f"All pets with the name '{pet_name}' have been deleted successfully."}, 200

if __name__ == "__main__":
    app.run(debug=True)

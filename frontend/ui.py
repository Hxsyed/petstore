import tkinter as tk
from tkinter import messagebox

class PetStoreApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pet Store")
        self.root.geometry("600x400")

        # Navigation Frame
        nav_frame = tk.Frame(root)
        nav_frame.pack(side="top", fill="x")

        tk.Button(nav_frame, text="Home", command=self.show_home).pack(side="left")
        tk.Button(nav_frame, text="Pets", command=self.show_pets).pack(side="left")
        tk.Button(nav_frame, text="Contact", command=self.show_contact).pack(side="left")

        # Container for dynamic content
        self.content_frame = tk.Frame(root)
        self.content_frame.pack(fill="both", expand=True)

        # Show home page by default
        self.show_home()

    def clear_content_frame(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def show_home(self):
        self.clear_content_frame()
        frame = tk.Frame(self.content_frame)
        frame.pack(fill="both", expand=True)

        tk.Label(frame, text="Welcome to the Pet Store!", font=("Arial", 18)).pack(pady=20)
        tk.Label(frame, text="Browse and adopt a pet that suits you!").pack(pady=10)

    def show_pets(self):
        self.clear_content_frame()
        frame = tk.Frame(self.content_frame)
        frame.pack(fill="both", expand=True)

        tk.Label(frame, text="Available Pets", font=("Arial", 18)).pack(pady=20)

        # Sample pet listings
        pets = [
            {"name": "Bella", "type": "Dog", "age": "2 years"},
            {"name": "Whiskers", "type": "Cat", "age": "3 years"}
        ]

        for pet in pets:
            pet_frame = tk.Frame(frame, pady=5)
            tk.Label(pet_frame, text=f"{pet['name']} - {pet['type']} ({pet['age']})").pack(side="left")
            tk.Button(pet_frame, text="View Details", command=lambda p=pet: self.show_pet_details(p)).pack(side="right")
            pet_frame.pack(fill="x")

    def show_pet_details(self, pet):
        self.clear_content_frame()
        frame = tk.Frame(self.content_frame)
        frame.pack(fill="both", expand=True)

        tk.Label(frame, text=f"Details of {pet['name']}", font=("Arial", 18)).pack(pady=20)
        tk.Label(frame, text=f"Type: {pet['type']}").pack(pady=5)
        tk.Label(frame, text=f"Age: {pet['age']}").pack(pady=5)
        tk.Button(frame, text="Back to Pets", command=self.show_pets).pack(pady=10)

    def show_contact(self):
        self.clear_content_frame()
        frame = tk.Frame(self.content_frame)
        frame.pack(fill="both", expand=True)

        tk.Label(frame, text="Contact Us", font=("Arial", 18)).pack(pady=20)

        tk.Label(frame, text="Name:").pack(anchor="w")
        name_entry = tk.Entry(frame, width=30)
        name_entry.pack()

        tk.Label(frame, text="Email:").pack(anchor="w")
        email_entry = tk.Entry(frame, width=30)
        email_entry.pack()

        tk.Label(frame, text="Message:").pack(anchor="w")
        message_text = tk.Text(frame, width=30, height=5)
        message_text.pack()

        tk.Button(frame, text="Submit", command=lambda: self.submit_contact(name_entry, email_entry, message_text)).pack(pady=10)

    def submit_contact(self, name_entry, email_entry, message_text):
        name = name_entry.get()
        email = email_entry.get()
        message = message_text.get("1.0", "end-1c")
        messagebox.showinfo("Contact Submitted", f"Thank you, {name}! We'll be in touch.")

# Run the app
root = tk.Tk()
app = PetStoreApp(root)
root.mainloop()

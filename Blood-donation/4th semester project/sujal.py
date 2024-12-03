import tkinter as tk
from tkinter import ttk

def create_gui():
    root = tk.Tk()
    root.title("Taxi Service Registration")

    # Title
    title_label = tk.Label(root, text="Register", font=("Helvetica", 24, "bold"), fg="pink")
    title_label.grid(row=0, column=0, columnspan=2, pady=10)

    # Subtitle
    subtitle_label = tk.Label(root, text="Passenger", font=("Helvetica", 16), fg="purple")
    subtitle_label.grid(row=0, column=2, pady=10)

    # Form fields
    fields = ["Name", "E-mail", "Address", "Password", "Phone Number"]
    for idx, field in enumerate(fields):
        label = tk.Label(root, text=field, font=("Helvetica", 14), fg="green")
        label.grid(row=idx + 1, column=0, padx=10, pady=5, sticky="e")
        entry = tk.Entry(root, font=("Helvetica", 14))
        entry.grid(row=idx + 1, column=1, padx=10, pady=5)

    # Sign-Up as
    signup_label = tk.Label(root, text="Sign-Up as:", font=("Helvetica", 14), fg="blue")
    signup_label.grid(row=1, column=2, padx=10, pady=5, sticky="w")

    passenger_radio = tk.Radiobutton(root, text="Passenger", font=("Helvetica", 14), fg="purple")
    passenger_radio.grid(row=2, column=2, padx=10, pady=5, sticky="w")

    driver_radio = tk.Radiobutton(root, text="Driver", font=("Helvetica", 14), fg="purple")
    driver_radio.grid(row=3, column=2, padx=10, pady=5, sticky="w")

    # Register button
    register_button = tk.Button(root, text="Register", font=("Helvetica", 14), fg="purple")
    register_button.grid(row=6, column=1, pady=20)

    # Cartoon character and taxi sign
    character_label = tk.Label(root, text="🚖", font=("Helvetica", 48))
    character_label.grid(row=6, column=0, padx=10, pady=5, sticky="e")

    taxi_sign = tk.Label(root, text="TAXI", font=("Helvetica", 24, "bold"), fg="black", bg="tan")
    taxi_sign.grid(row=0, column=3, padx=10, pady=5, sticky="w")

    root.mainloop()

create_gui()
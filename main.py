import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Define the correct graphical password (image filename)
correct_password = "correct_password.jpg"

# Create a list of images for the user to select as the password
password_images = ["image1.jpg", "image2.jpg", "image3.jpg"]

# Create a function to check if the selected image is the correct password
def check_password(selected_image):
    if selected_image == correct_password:
        messagebox.showinfo("Authentication", "Access Granted")
    else:
        messagebox.showerror("Authentication", "Access Denied")

# Create the main application window
root = tk.Tk()
root.title("Graphical Password Authentication")

# Create a label to display instructions
instruction_label = tk.Label(root, text="Select the correct image:")
instruction_label.pack()

# Create buttons for each image
image_buttons = []
for img_file in password_images:
    img = Image.open(img_file)
    img.thumbnail((100, 100))
    img = ImageTk.PhotoImage(img)
    button = tk.Button(root, image=img, command=lambda img_file=img_file: check_password(img_file))
    button.image = img
    image_buttons.append(button)
    button.pack()

# Run the application
root.mainloop()

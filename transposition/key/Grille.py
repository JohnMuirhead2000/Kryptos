import numpy as np


def rotate_key_90_degrees(key):
    # Convert the key list to a NumPy array and reshape it into an 8x8 grid
    key_grid = np.array(key).reshape(8, 8)
    # Rotate the key grid 90 degrees clockwise
    rotated_key_grid = np.rot90(key_grid, k=-1)
    return rotated_key_grid


def grille_cipher(key, cipher_text):
    # Convert the cipher_text to a 2D list by splitting each row by spaces
    cipher_text_grid = [row.split() for row in cipher_text]

    # Initialize an empty string to store the final message
    message = ""

    # Rotate the key and extract letters from the cipher text four times
    for _ in range(4):
        # Convert the key list to a NumPy array and reshape it into an 8x8 grid
        key_grid = np.array(key).reshape(8, 8)

        # Extract letters from the cipher text based on the positions of zeros in the key grid
        for i in range(8):
            for j in range(8):
                if key_grid[i, j] == 0:
                    message += cipher_text_grid[i][j]

        # Rotate the key 90 degrees clockwise for the next iteration
        key = rotate_key_90_degrees(key).flatten().tolist()

    return message


# Test with the provided key and cipher text
key = [1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 0, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 0, 1, 1, 0, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1,
       1, 0, 1, 1, 1, 1, 1, 1]
import tkinter as tk
from functools import partial
from tkmacosx import Button

# Scaling factor
scale_factor = 2

# Cipher text (replace with actual cipher text)
cipher_text = [
    "p o a u s l e l",
    "w i b c g e r r",
    "n h a t r t r l",
    "y g p Z Z e r o",
    "f i e Z Z p l c",
    "o l a d e s r i",
    "k l e k n f d t",
    "r s x t r o o x"
]
cipher_text_grid = [row.split() for row in cipher_text]

# Initial key grid (all 1s)
key_grid = [[1] * 8 for _ in range(8)]


def on_button_click(i, j, button):
    # Toggle button state and update key grid
    print("HWERE RINT")
    if button["bg"] == "white":
        button["bg"] = "green"
        key_grid[i][j] = 0
    else:
        button["bg"] = "white"
        key_grid[i][j] = 1


def decode():
    # Convert key grid to a 1D list
    key = [val for sublist in key_grid for val in sublist]
    # Decode using grille cipher method
    message = grille_cipher(key, cipher_text)
    # Update label with decoded message
    plaintext_label["text"] = "Plaintext: " + message


def reset():
    # Reset key grid to all 1s (unselected)
    global key_grid
    key_grid = [[1] * 8 for _ in range(8)]
    # Set the background color of all buttons to white
    for button_row in buttons:
        for button in button_row:
            button["bg"] = "white"
    # Clear the plaintext label
    plaintext_label["text"] = "Plaintext: "


# Create main window
root = tk.Tk()
root.title("Grille Cipher Decoder")

# Create grid of buttons
buttons = []
for i in range(8):
    button_row = []
    for j in range(8):
        button = Button(root, text=cipher_text_grid[i][j], bg="white",
                           width=75 * scale_factor, height=40 * scale_factor,
                           font=("Helvetica", 5 * scale_factor))
        # Use the partial function to fix the arguments of on_button_click function
        button["command"] = lambda i=i, j=j, button=button: on_button_click(i, j, button)
        button.grid(row=i, column=j)
        button_row.append(button)
    buttons.append(button_row)


def rotate_cipher_text():
    global cipher_text_grid
    # Rotate the cipher text grid 90 degrees clockwise
    cipher_text_grid = list(zip(*cipher_text_grid[::-1]))
    # Update button labels in the GUI
    for i in range(8):
        for j in range(8):
            buttons[i][j]["text"] = cipher_text_grid[i][j]


# Create "Rotate Cipher Text" button
rotate_cipher_text_button = tk.Button(root, text="Rotate Cipher Text", command=rotate_cipher_text,
                                      font=("Helvetica", 5 * scale_factor))
rotate_cipher_text_button.grid(row=10, column=0, columnspan=8)

# Create "Decode" button
decode_button = tk.Button(root, text="Decode", command=decode,
                          font=("Helvetica", 5 * scale_factor))
decode_button.grid(row=8, column=0, columnspan=4)

# Create "Reset" button
reset_button = tk.Button(root, text="Reset", command=reset,
                         font=("Helvetica", 5 * scale_factor))
reset_button.grid(row=8, column=4, columnspan=4)

# Create label to display decoded plaintext
plaintext_label = tk.Label(root, text="Plaintext: ")
plaintext_label.grid(row=9, column=0, columnspan=8)

# Start GUI event loop
root.mainloop()

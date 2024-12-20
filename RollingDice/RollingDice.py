import tkinter
from PIL import Image, ImageTk
import random

# Create the main window
root = tkinter.Tk()
root.geometry('400x400')
root.title('Roll the Dice')

# Heading label
HeadingLabel = tkinter.Label(
    root,
    text="Roll the Dice!",
    fg="light green",
    bg="dark green",
    font="Helvetica 16 bold italic"
)
HeadingLabel.pack()

# List of dice image paths
dice_images = [
    'RollingDice/die1.png',
    'RollingDice/die2.png',
    'RollingDice/die3.png',
    'RollingDice/die4.png',
    'RollingDice/die5.png',
    'RollingDice/die6.png'
]

# Load all dice images into memory
loaded_images = [ImageTk.PhotoImage(Image.open(img)) for img in dice_images]

# Create the label to display the dice image
ImageLabel = tkinter.Label(root, image=loaded_images[0])
ImageLabel.pack(expand=True)

# Function to roll the dice
def rolling_dice():
    random_image = random.choice(loaded_images)
    ImageLabel.configure(image=random_image)
    ImageLabel.image = random_image  # Keep a reference to avoid garbage collection

# Button to roll the dice
button = tkinter.Button(root, text='Roll the Dice', fg='blue', command=rolling_dice)
button.pack(expand=True)

# Start the Tkinter event loop
root.mainloop()

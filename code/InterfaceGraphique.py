from tkinter import *
from PIL import Image, ImageTk  # Necessary for resizing images if needed
from WelshPowell import welsh_powell
from Kruskal import kruskal
from PotentielMetra import potentiel_metra
from BellmanFord import bellman_ford
from SteppingStone import stepping_stone_gui
from Dijkstra import dijkstra
from FordFulkerson import ford_fulkerson_gui
from Nord_west_Moindre_Cout import transport_gui
import os  # To manage relative paths

# Create the main window
gui = Tk()
gui.geometry("1000x700")  # Window size
gui.title("Operational Research")

# Main colors
bg_color = "white"  # Background color
button_color = "#87CEFA"  # Button color

# Main background
gui.config(bg=bg_color)

# Add the logo
try:
    # Load the logo image
    image_path = os.path.join(os.path.dirname(__file__), "emsi.jpeg")  # Relative path to your image file
    with open(image_path, "rb") as f:  # Open in binary mode to avoid encoding errors
        img = Image.open(f)
        img_resized = img.resize((200, 100))  # Resize for a larger width (200x100)
        logo_image = ImageTk.PhotoImage(img_resized)  # Convert to Tkinter-compatible format

    # Display the logo
    logo_label = Label(gui, image=logo_image, bg=bg_color)
    logo_label.image = logo_image  # Prevent the image from being garbage-collected
    logo_label.pack(pady=10)  # Position at the top with spacing
except Exception as e:
    print(f"Error loading the logo: {e}")

# Add the title
title_label = Label(gui, text="Tkinter Graphical Interface", font=("Arial", 18, "bold"), fg="darkred", bg=bg_color)
title_label.pack(pady=5)

# Add the name and institution
student_info_label = Label(gui, text="Name: Fahd Jabbar   | Supervised by: EL MKHALET MOUNA", 
                          font=("Arial", 12), fg="black", bg=bg_color)
student_info_label.pack(pady=5)

# Main frame for algorithms
main_frame = Frame(gui, relief="solid", bd=3, padx=20, pady=20, bg="#FFC0CB")
main_frame.pack(pady=30)

# Secondary title for algorithms
algo_label = Label(main_frame, text="Operational Research Algorithms", font=("Arial", 12, "bold"), bg="#FFC0CB")
algo_label.pack(pady=10)

# Function to open a new window
def algorithms():
    guiA = Toplevel(gui)
    guiA.geometry("1000x700")
    guiA.config(bg=bg_color)

    # Output label to display results
    output_label = Label(guiA, text="", font=("Arial", 12), fg="blue", wraplength=900, bg=bg_color)
    output_label.place(x=50, y=400)

    # Algorithm functions
    def run_welsh_powell():
        try:
            output_label.config(text="Running the Welsh-Powell algorithm...")
            welsh_powell(guiA, output_label)
        except Exception as e:
            output_label.config(text=f"Error: {str(e)}")

    def run_kruskal():
        try:
            output_label.config(text="Running the Kruskal algorithm...")
            kruskal(guiA, output_label)
        except Exception as e:
            output_label.config(text=f"Error: {str(e)}")

    def run_potentiel_metra():
        try:
            output_label.config(text="Running the Potentiel Metra algorithm...")
            potentiel_metra(guiA, output_label)
        except Exception as e:
            output_label.config(text=f"Error: {str(e)}")

    def run_bellman_ford():
        try:
            output_label.config(text="Running the Bellman-Ford algorithm...")
            bellman_ford(guiA, output_label)
        except Exception as e:
            output_label.config(text=f"Error: {str(e)}")

    def run_stepping_stone():
        try:
            output_label.config(text="Running the Stepping Stone algorithm...")
            stepping_stone_gui(guiA, output_label)
        except Exception as e:
            output_label.config(text=f"Error: {str(e)}")

    def run_dijkstra():
        try:
            output_label.config(text="Running the Dijkstra algorithm...")
            dijkstra(guiA, output_label)
        except Exception as e:
            output_label.config(text=f"Error: {str(e)}")

    def run_ford_fulkerson():
        try:
            output_label.config(text="Running the Ford-Fulkerson algorithm...")
            ford_fulkerson_gui(guiA, output_label)
        except Exception as e:
            output_label.config(text=f"Error: {str(e)}")

    def run_transport():
        try:
            output_label.config(text="Running transportation algorithms...")
            transport_gui(guiA, output_label)
        except Exception as e:
            output_label.config(text=f"Error: {str(e)}")

    # Algorithm buttons
    welsh_powell_button = Button(guiA, text="Welsh Powell", command=run_welsh_powell, bg=button_color, font=("Arial", 10, "bold"))
    welsh_powell_button.place(x=50, y=50, width=150, height=50)

    kruskal_button = Button(guiA, text="Kruskal", command=run_kruskal, bg=button_color, font=("Arial", 10, "bold"))
    kruskal_button.place(x=250, y=50, width=150, height=50)

    potentiel_metra_button = Button(guiA, text="Potentiel Metra", command=run_potentiel_metra, bg=button_color, font=("Arial", 10, "bold"))
    potentiel_metra_button.place(x=450, y=50, width=150, height=50)

    bellman_ford_button = Button(guiA, text="Bellman-Ford", command=run_bellman_ford, bg=button_color, font=("Arial", 10, "bold"))
    bellman_ford_button.place(x=650, y=50, width=150, height=50)

    stepping_stone_button = Button(guiA, text="Stepping Stone", command=run_stepping_stone, bg=button_color, font=("Arial", 10, "bold"))
    stepping_stone_button.place(x=50, y=150, width=150, height=50)

    dijkstra_button = Button(guiA, text="Dijkstra", command=run_dijkstra, bg=button_color, font=("Arial", 10, "bold"))
    dijkstra_button.place(x=250, y=150, width=150, height=50)

    ford_fulkerson_button = Button(guiA, text="Ford-Fulkerson", command=run_ford_fulkerson, bg=button_color, font=("Arial", 10, "bold"))
    ford_fulkerson_button.place(x=450, y=150, width=150, height=50)

    transport_button = Button(guiA, text="Transport", command=run_transport, bg=button_color, font=("Arial", 10, "bold"))
    transport_button.place(x=650, y=150, width=150, height=50)

# Buttons in the main window (placed just below the main frame)
button_frame = Frame(gui, bg=bg_color)  # Frame for the "Enter" and "Quit" buttons
button_frame.pack(pady=10)  # Position just below the main frame with spacing

btn1 = Button(button_frame, text="Enter", command=algorithms, bg=button_color, font=("Arial", 12, "bold"), relief="solid", bd=3)
btn1.pack(side=LEFT, padx=10)  # Position to the left with spacing

btn2 = Button(button_frame, text="Quit", command=gui.destroy, bg=button_color, font=("Arial", 12, "bold"), relief="solid", bd=3)
btn2.pack(side=RIGHT, padx=10)  # Position to the right with spacing

gui.mainloop()

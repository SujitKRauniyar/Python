from owlready2 import get_ontology  # type: ignore
from tkinter import Tk, Label, Button, Listbox, Scrollbar, VERTICAL, RIGHT, Y, Frame, X, LEFT, BOTH
from tkinter import ttk

# Load the ontology
ontology_file = "ComputerOntology.owx"  # RDF/XML format
ontology = get_ontology(ontology_file).load()

# Function to fetch classes
def fetch_classes():
    listbox.delete(0, "end")  # Clear the listbox
    for cls in ontology.classes():
        listbox.insert("end", f"Class: {cls.name}")

# Function to fetch individuals
def fetch_individuals():
    listbox.delete(0, "end")  # Clear the listbox
    for individual in ontology.individuals():
        listbox.insert("end", f"Individual: {individual.name}")

# Function to fetch object properties
def fetch_object_properties():
    listbox.delete(0, "end")  # Clear the listbox
    for prop in ontology.object_properties():
        listbox.insert("end", f"Object Property: {prop.name}")

# Function to fetch data properties
def fetch_data_properties():
    listbox.delete(0, "end")  # Clear the listbox
    for prop in ontology.data_properties():
        listbox.insert("end", f"Data Property: {prop.name}")

# Build the enhanced UI
root = Tk()
root.title("Computer Ontology Viewer")
root.geometry("700x600")
root.configure(bg="#2e3b4e")  # Set the background color to a dark blue-gray

# Header Label
header = Label(
    root,
    text="Computer Ontology Viewer",
    font=("Helvetica", 20, "bold"),
    fg="white",
    bg="#4a6d8c",  # SteelBlue
    pady=15
)
header.pack(fill=X)

# Frame for buttons
button_frame = Frame(root, bg="#2e3b4e", pady=15)
button_frame.pack(fill=X)

# Styled Buttons
style = ttk.Style()
style.configure("TButton", font=("Arial", 12, "bold"), padding=8, relief="flat", width=20)

class_button = ttk.Button(
    button_frame, text="Show Classes", style="TButton", command=fetch_classes
)
class_button.pack(side=LEFT, padx=20)

individual_button = ttk.Button(
    button_frame, text="Show Individuals", style="TButton", command=fetch_individuals
)
individual_button.pack(side=LEFT, padx=20)

object_prop_button = ttk.Button(
    button_frame, text="Show Object Properties", style="TButton", command=fetch_object_properties
)
object_prop_button.pack(side=LEFT, padx=20)

data_prop_button = ttk.Button(
    button_frame, text="Show Data Properties", style="TButton", command=fetch_data_properties
)
data_prop_button.pack(side=LEFT, padx=20)

# Frame for listbox
listbox_frame = Frame(root, bg="#2e3b4e")
listbox_frame.pack(fill=BOTH, expand=True, padx=20, pady=20)

# Scrollbar and Listbox
scrollbar = Scrollbar(listbox_frame, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=Y)

listbox = Listbox(
    listbox_frame,
    yscrollcommand=scrollbar.set,
    font=("Courier", 14),
    bg="#f3f4f6",  # Light gray
    fg="black",
    height=15,
    selectbackground="#4a6d8c",  # SteelBlue
    selectforeground="white",
    relief="flat",
    bd=0
)
listbox.pack(side=LEFT, fill=BOTH, expand=True)
scrollbar.config(command=listbox.yview)

# Footer Label
footer = Label(
    root,
    text="Ontology Viewer - Developed in Python",
    font=("Arial", 12),
    bg="#4a6d8c",  # SteelBlue
    fg="white",
    pady=10
)
footer.pack(fill=X)

# Run the application
root.mainloop()

# tkinter -> is a module (single py file) & library (collection of modules) both

# import tkinter for creating GUI apps
import tkinter as tk

from tkinter import filedialog, messagebox 
# submodule -> for opening & saving files | for popup message box

# Main window code
root = tk.Tk() # dialog box will open which is a text editor
root.title("Text Editor App")
root.geometry("800x600") # size of text editor dialog box

# create text area
text = tk.Text(
    root, # we say it you are in parent window
    wrap=tk.WORD, # wrap text by words and not characters
    font=("Helvetica", 12)
)
text.pack(expand=True, fill=tk.BOTH) # expads the text covering full area

# main logic starts now

# function -> to create a new file
def new_file():
    text.delete(1.0, tk.END) # we get to know index and end of file (as we dont know length of file)

# function -> to open a new file
def openFile():
    # open file dialogue & check file is there or not
    file_path = filedialog.askopenfilename( # we will get file path
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt")]                            
        ) 
    
    if file_path:
        with open(file_path, "r") as file:
            # clear old text
            text.delete(1.0, tk.END) 
            # inserting contents from file
            text.insert(tk.END, file.read()) # START FROM TK.END
            
# function -> to save the file
def save_file():
    # open save file dialogue
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt")]    
    )    
    
    if file_path:
        with open(file_path, "w") as file:
            file.write(text.get(1.0, tk.END)) 
            
    messagebox.showinfo("Info", "File saved succesfully.")
    
# create Menu bar
menu = tk.Menu(root)
root.config(menu=menu) # to connect it with menu

file_menu = tk.Menu(menu)

# New, Open file, save, exit

# add file menu to menu bar and options
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=openFile)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# -------------------- RUN APPLICATION --------------------

# Run the application continuously
# Starts and keeps the window open

root.mainloop() # starts and keeps the window open


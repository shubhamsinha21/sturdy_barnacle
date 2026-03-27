import tkinter as tk
import time
from PIL import Image, ImageTk

# main window
root = tk.Tk()
root.title("Photo Booth")
root.geometry("900x900")

# list of image paths
image_paths = [
    r"/Users/shubhamsinha/Desktop/learning/Photo Album/img0.jpg",  
    # -> r will not let the / or // gets treated as special characters
    r"/Users/shubhamsinha/Desktop/learning/Photo Album/img1.jpg",  
    r"/Users/shubhamsinha/Desktop/learning/Photo Album/img2.jpg",  
    r"/Users/shubhamsinha/Desktop/learning/Photo Album/img3.jpg",  
    r"/Users/shubhamsinha/Desktop/learning/Photo Album/img4.jpg",  
]

img_resize = (700, 800)
images = [] # list of images
for path in image_paths: # converting path to image and will add here
    try:
        img = Image.open(path) # opening path of image
        img = img.resize(img_resize, Image.Resampling.LANCZOS)
        img = img.convert("RGB")
        images.append(img)
        
    except Exception as e:
        print("Error loading: ", e)
    
# convert PIL image to Tkinter compatible images
final_images = []
for eachImage in images:
    photo = ImageTk.PhotoImage(eachImage)
    final_images.append(photo)

# label widget to keep photo
image_label = tk.Label(root)
image_label.pack(pady=30) 
# organizes widgets into horizontal and vertical blocks within a parent container.


# slideshow function
def slideshow():
    for photo in final_images:
        image_label.config(image=photo) # we are adding images into image label widget
        image_label.image = photo # we are saying again that -> image is attached to this label
        root.update() # keeps updating image
        time.sleep(2)
        
# create a button
play_button = tk.Button(
    root, # considering that you are attached to root
    text= "Play the slideshow",
    font=("Arial", 18),
    command=slideshow
)

play_button.pack(pady=14)
        
# running the application

root.mainloop()
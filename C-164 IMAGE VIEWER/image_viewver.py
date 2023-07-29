from tkinter import* 
from tkinter import filedialog
from PIL import ImageTk, Image
root=Tk()

root.geometry("600x600")
root.title("Image Viewer")
root.configure(bg="lightblue")

label_image = Label(root,bg="white",highlightthickness=5)
label_image.place(relx=0.5, rely=0.5, anchor=CENTER)

Img_path= ""
def OpenFile():
    global Img_path
    Img_path= filedialog.askopenfilename(title="open text file", filetypes=[("Image Files","*.jpg *.gif *.jpg *.png *.jpeg")])
    print(Img_path)
    im= Image.open(Img_path)
    img = ImageTk.PhotoImage(im)
    label_image["image"]= img
    img.close()

Btn = Button(root, text="open_image", font=("Times New Roman0", 12), bg="grey", fg="white", command=OpenFile, relief=SOLID)
Btn.place(relx=0.5, rely=0.1, anchor=CENTER)

root.mainloop()
    




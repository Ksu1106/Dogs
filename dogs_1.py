from tkinter import *
import requests
from PIL import Image, ImageTk
from io import BytesIO

window = Tk()
window.title('Картинка с собачками')
window.geometry('360x420')

label = Label()
label.pack(pady = 10)

button = Button(text='', command=show_image)
button.pack(pady = 10)

window.mainloop()
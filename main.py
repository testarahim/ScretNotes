from tkinter import *
from tkinter import  messagebox
from PIL import ImageTk, Image
import os

window = Tk()
window.title("Secret Notes")
window.minsize(width=400, height=500)

img = ImageTk.PhotoImage(Image.open("img.png"))
img_Label = Label(image=img)
img_Label.pack()

#title label and entry packing
title_label = Label(text="Enter your title", font=("Arial", 12, "bold"), pady=10)
title_label.pack()
title_entry = Entry(width=40)
title_entry.pack()

#Notes label and text packing
notes_label = Label(text="Enter your secret", font=("Arial", 12, "bold"), pady=10)
notes_label.pack()
notes_text = Text(width=40)
notes_text.pack()

#Master key label and entry packing
masterKey_label = Label(text="Enter master key", font=("Arial", 12, "bold"), pady=10)
masterKey_label.pack()
masterKey_entry = Entry(width=40)
masterKey_entry.pack()

def save_and_enc_button_check():
    title = title_entry.get()
    note = notes_text.get()
    if title == "" or note == "":
    messagebox.showwarning("Warning!", "Please enter all information")

#TODO save butonuna basıldığında öncelikle entry'leri kontrol et boşsa utarı mesajı bas,
#TODO save butonuna basıldığında bir adet txt dosyası oluştur ve bu dosya içerisine title ve notu yazdır
#TODO save butonuna basılınca notu encrypt'li bir şekilde yazdır.
#TODO Decrpyt butonuna basıldığında kriptolanmış not dekirpto şekilde gözükmesini sağla
#TODO Decrpyt butonuna basıldığında master key doğru girildiyse mesajı doğru bir şekilde decrptyt et değilse yanlış yap yada hata ver.
def save_button():
    pass

#Save&Encrpy button packing
save_encrypt_button = Button(text="Save & Encrypt",command=save_button)
save_encrypt_button.pack()


#Decrypt button packing
decrypt_button = Button(text="Decrypt")
decrypt_button.pack()











window.mainloop()
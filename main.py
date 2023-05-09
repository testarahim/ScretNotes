from tkinter import *
from tkinter import  messagebox
from PIL import ImageTk, Image
import os
import cryptocode

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


# encoded = cryptocode.encrypt(notes_text.get("1.0", END), masterKey_entry.get())
# decoded = cryptocode.decrypt(encoded, masterKey_entry.get())
def save_and_enc_button_check():
    title = title_entry.get()
    note = notes_text.get("1.0",END)
    masterkey = masterKey_entry.get()
    encoded = cryptocode.encrypt(notes_text.get("1.0", END), masterkey)
    if title == "" or note == "" or masterkey == "":
        messagebox.showwarning("Warning!", "Please enter all information")
    else:
        f = open("SecretNotes.txt", "a")
        f.write("\n" + title + "\n")
        f.write(encoded)
        f.close()
        notes_text.delete("1.0", END)
        title_entry.delete(0,"end")
        masterKey_entry.delete(0, "end")
def decrypt():

    note = notes_text.get("1.0", END)
    masterkey = masterKey_entry.get()
    decoded = cryptocode.decrypt(note, masterkey)

    if decoded == False:
        messagebox.showerror("Error!", "Wrong master key, Please enter correct master key!")
    else:
        notes_text.delete("1.0", END)
        notes_text.insert(END, decoded)

#Save&Encrpy button packing
save_encrypt_button = Button(text="Save & Encrypt",command=save_and_enc_button_check)
save_encrypt_button.pack()

#Decrypt button packing
decrypt_button = Button(text="Decrypt", command=decrypt)
decrypt_button.pack()











window.mainloop()
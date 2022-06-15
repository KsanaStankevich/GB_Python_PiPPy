from pytube import YouTube

# vid = input('Вставьте ссылку на видео, которое хотите скачать: ')
# yt = YouTube(vid)

# path = input('Напишите адрес папки, куда скачать файл: ')
# yt.streams.filter(progressive=True, file_extension='mp4')
# yt.streams.order_by('resolution')
# yt.streams.desc()
# yt.streams.first().download(path)


from tkinter import *
from tkinter import messagebox  

def clicked():
    yt = YouTube(vid)
    yt.streams.filter(progressive=True, file_extension='mp4')
    yt.streams.order_by('resolution')
    yt.streams.desc()
    yt.streams.first().download(path)
    messagebox.showinfo(' ', 'Видео скачено!') 

window = Tk()
window.geometry('300x250')
window.title("Скачивание любого видео с Ютуба")

vidlink = Label(window, text="Вставьте ссылку на видео, которое хотите скачать")
vidlink.grid(column = 0, row = 1) 
txtlink = Entry(window, width = 40)  
txtlink.grid(column = 0, row= 2)  
vid = YouTube(txtlink.get())

folderlink = Label(window, text="Напишите адрес папки, куда скачать файл")
folderlink.grid(column = 0, row = 4) 
txtfolder = Entry(window, width = 40)  
txtfolder.grid(column = 0, row= 5)  
path = (txtfolder.get)

btn = Button(window, text="Скачать", command = clicked)
btn.grid(column = 0, row = 10)

window.mainloop()
import io
from tkinter import font
import webbrowser
import requests
from tkinter import *
from urllib.request import urlopen
from PIL import ImageTk,Image

class NewsApp:

    def __init__(self):

        # fetch data
        self.data = requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=57ca879cb3b640d3aff49dbaaa2b905d').json()
        # initial GUI load
        self.load_gui()
        # load the 1st news item
        self.load_news_item(0)

    def load_gui(self):
        self.root = Tk()
        self.root.geometry('350x500')
        self.root.resizable(0,0)
        self.root.iconbitmap('icon.ico')
        self.root.title('News in-short')
        self.root.configure(background='white')

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def load_news_item(self,index):

        # clear the screen for the new news item
        self.clear()

        # image
        try:
            img_url = self.data['articles'][index]['urlToImage']
            raw_data = urlopen(img_url).read()
            im = Image.open(io.BytesIO(raw_data)).resize((350,200))
            photo = ImageTk.PhotoImage(im)
        except:
            img_url = 'https://www.hhireb.com/wp-content/uploads/2019/08/default-no-img.jpg'
            raw_data = urlopen(img_url).read()
            im = Image.open(io.BytesIO(raw_data)).resize((350, 200))
            photo = ImageTk.PhotoImage(im)


        label = Label(self.root,image=photo)
        label.pack()


        heading = Label(self.root,text=self.data['articles'][index]['title'],bg='white',fg='black',wraplength=350,justify='center')
        heading.pack(pady=(10,20))
        heading.config(font=('verdana',12))

        details = Label(self.root, text=self.data['articles'][index]['description'], bg='grey', fg='white', wraplength=350,justify='center')
        details.pack(pady=(2, 20))
        details.config(font=('verdana', 10))

        frame = Frame(self.root,bg='white')
        frame.pack(expand=True,fill=BOTH)

        if index != 0:
            prev = Button(frame,text='Prev', bg='#2c4bff',fg='#ffffff',width=16,height=3,command=lambda :self.load_news_item(index-1))
            prev.pack(side=LEFT)

        read = Button(frame, text='Read More', bg='#2c4bff',fg='#ffffff', width=16, height=3,command=lambda :self.open_link(self.data['articles'][index]['url']))
        read.pack(side=LEFT)

        if index != len(self.data['articles'])-1:
            next = Button(frame, text='Next',bg='#2c4bff',fg='#ffffff', width=16, height=3,command=lambda :self.load_news_item(index+1))
            next.pack(side=LEFT)

        self.root.mainloop()

    def open_link(self,url):
        webbrowser.open(url)


obj = NewsApp()
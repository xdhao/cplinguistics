import pymongo, os
from tkinter import *
import tkinter as tk
from tkinter import ttk
from pymongo import MongoClient


client = MongoClient()
database = client.v102news
news = database.news
tomita = database.tomita
tonality = database.tonality


window = tk.Tk()
window.title("Main Page")
window.geometry("250x300")
window.resizable(width=False, height=False) 

class Table(tk.Frame):
    def __init__(self, parent=None, headings=tuple(), rows=tuple()):
        super().__init__(parent)
  
        table = ttk.Treeview(self, show="headings", selectmode="browse")
        table["columns"] = headings
        table["displaycolumns"] = headings
  
        for head in headings:
            table.heading(head, text=head, anchor=tk.CENTER)
            table.column(head, anchor=tk.CENTER)
  
        for row in rows:
            table.insert('', tk.END, values=tuple(row))
  
        scrolltable = tk.Scrollbar(self, command=table.yview)
        table.configure(yscrollcommand=scrolltable.set)
        scrolltable.pack(side=tk.RIGHT, fill=tk.Y)
        table.pack(expand=tk.YES, fill=tk.BOTH)


def button_news():
    data1 = []
    cursor = news.find({})

    for document in cursor:
        data1.append((document["headline"], document["text"], document["url"], document["time"]))  

    newsdb = tk.Tk()
    newsdb.title("News in DB")
    table = Table(newsdb, headings=('headline', 'text', 'url', 'time'), rows=data1)
    table.pack(expand=tk.YES, fill=tk.BOTH)
    newsdb.mainloop()    

def button_tomita():
    data2 = []
    cursor = tomita.find({})

    for document in cursor:
        data2.append((document["text"], document["name"]))  

    tomitadb = tk.Tk()
    tomitadb.title("Tomita in DB")
    table = Table(tomitadb, headings=('text', 'name'), rows=data2)
    table.pack(expand=tk.YES, fill=tk.BOTH)
    tomitadb.mainloop()    

def button_tonality():
    data3 = []
    cursor = tonality.find({})

    for document in cursor:
        data3.append((document["text"], document["tonal"]))  

    tonalitydb = tk.Tk()
    tonalitydb.title("Tonality in DB")
    table = Table(tonalitydb, headings=('text', 'tonal'), rows=data3)
    table.pack(expand=tk.YES, fill=tk.BOTH)
    tonalitydb.mainloop()  

def button_parsing():
    os.system('python3 parser.py')
    os.system('python3 docToTxt.py')  

def button_delete():
    client.drop_database(database)
    print("database cleared")
    
def button_tomitaparsing():
    os.system('python3 /home/vagrant/tomita-parser/build/bin/tomita.py')
    os.chdir(r"/home/vagrant/kr/")

def button_w2v():
    os.system('python3 /home/vagrant/kr/Word2Vec/Word2Vec.py')  

def button_ton():
    os.system('python3 /home/vagrant/kr/tonality/tonality.py')    
    


l1 = Label(text="База данных", font="Arial 14")

l2 = Label(text="Функции", font="Arial 14")
 
l1.pack()
separator = ttk.Separator(window, orient='horizontal')
separator.pack(fill='x')
btn1 = Button(text="news in DB", command=button_news, width = 15)
btn1.pack()

btn2 = Button(text="tomita in DB", command=button_tomita, width = 15)
btn2.pack()

btn3 = Button(text="tonality in DB", command=button_tonality, width = 15)
btn3.pack()
separator = ttk.Separator(window, orient='horizontal')
separator.pack(fill='x')

l2.pack()
separator = ttk.Separator(window, orient='horizontal')
separator.pack(fill='x')
btn4 = Button(text="start parsing", command=button_parsing, width = 15)
btn4.pack()

btn5 = Button(text="start tomita-parser", command=button_tomitaparsing, width = 15)
btn5.pack()

btn6 = Button(text="start w2v", command=button_w2v, width = 15)
btn6.pack()

btn7 = Button(text="start tonality analysis", command=button_ton, width = 15)
btn7.pack()

btn8 = Button(text="clear DB", command=button_delete, width = 15)
btn8.pack()

window.mainloop()
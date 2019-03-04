import sqlite3
import random
import time
from tkinter import *

window = Tk()

global name, pronoun1, pronoun2, pronoun3
conn = sqlite3.connect("story.db")
crsr = conn.cursor()

crsr.execute("""CREATE TABLE IF NOT EXISTS linebase (
linenumber INTEGER PRIMARY KEY,
mood TEXT,
content BLOB)""")

crsr.execute("""CREATE TABLE IF NOT EXISTS tempprofbase (
pronoun1 TEXT,
pronoun2 TEXT,
pronoun3 TEXT,
name TEXT PRIMARY KEY);""")

def insertLines(linenumber, mood, content):
    conn = sqlite3.connect("story.db")
    crsr = conn.cursor()
    crsr.execute("INSERT OR REPLACE INTO linebase VALUES (?,?,?)", (linenumber, mood, content))
    conn.commit()
    conn.close()

def view(linenumber):
    conn = sqlite3.connect("story.db")
    crsr = conn.cursor()
    crsr.execute("SELECT content FROM linebase WHERE linenumber = (?)",(linenumber,))
    rows = crsr.fetchall()
    conn.close()
    return rows

def basic_function(word, field):
    word = StringVar()
    word = field.get()

name = StringVar()
def insertName(name):
    conn = sqlite3.connect("story.db")
    crsr = conn.cursor()
    crsr.execute("INSERT OR REPLACE INTO tempprofbase VALUES (?,)",(name,))
    conn.commit()
    conn.close()
    return name

welcome = Label(window, text = "Hello! Welcome to the story generator.")

nameE = Label(window, text = "To start, please tell me your name. When you are sure press 'confirm'.")
nameE.pack()

playerName = Entry(window, textvariable = name, width = 30)
playerName.pack()

name = playerName.get()

confirmNButton = Button( window, text = "confirm", command = lambda: basic_function(name, playerName), width = 8, height = 1, fg = "green")
confirmNButton.pack()

#while basic_function(name, nameE) == True:
    #nameE.insert(END,"Please try again.  ")
pronoun1= ""
pronoun2 = ""
pronoun3 = ""

pronoun = Label(window, text = "Hello! Welcome to the story generator.")
pronoun.pack()
pronoun1 = StringVar()

insertLines(1,"happy",f"It was a wonderful sunny day and {name} was taking a walk through the forest when {pronoun2} suddenly found a pile of .")
#insertLines(1,"happy",f"It was the noon of a warm autumn day and {name} was relaxing in the park when all of a sudden a basket of  \
#materialized out of thin air {pronoun2}.")

sheButton = Button( window, text = "she", command = lambda: pronoun1.set("she"), width = 8, height = 1, fg = "green")
sheButton.pack()

heButton = Button( window, text = "he", command= lambda: pronoun1.set("he"),  width = 8, height = 1, fg = "green")
heButton.pack()

themButton = Button( window, text = "them", command = lambda: pronoun1.set("them"), width = 8, height = 1, fg = "green")
themButton.pack()

result = str(random.choice(view(1)))

resultE = Text(window, bg = "white", fg = "black", width = 50, height = 2)
resultE.pack()

def insertresult():
    resultE.insert(END, name)

printButton = Button( window, text = "print", command = lambda: insertresult(), width = 8, height = 1, fg = "green")
printButton.pack()
#def pronoun_function(pronoun1):
    #if pronoun1 == "she":
    #    pronoun2 = "her"
    #    pronoun3 = ""
    #    return pronoun2, pronoun3
    #    return True
    #elif pronoun1 == "he":
    #    pronoun2 = "him"
    #    pronoun3 = "his"
    #    return pronoun2, pronoun3
    #    return True
    #elif pronoun1 == "they":
    #    pronoun2 = "them"
    #    pronoun3 = "their"
    #    return pronoun2, pronoun3
    #    return True
    #else:
    #    return False

#while pronoun_function(pronoun1) == False:
#    pronoun1 = str()
#else:
#    [pronoun2, pronoun3] = pronoun_function(pronoun1)








#phase 0
#name = input("To start, please tell me your name...  ")

#phase 0-1
#pronoun1 = input("...and the pronoun you would like to have used.  ")
#pronoun2 = "none"
#pronoun3 = "none"





#insert mood function!

#phase 1
#fruit = str(input("Wonderful. Please continue by naming a fruit (plural).  "))
#while basic_function(fruit) == True:
    #fruit = input("Please try again.  ")


# phase 2
#animal = str(input("Now, please enter an animal.  "))
#while basic_function(animal) == True:
    #animal = input("Please try again.  ")

# phase 3
#object = input("Next, please name an object of your choosing.  ")
#while basic_function(object) == True:
    #object = input("Please try again.  ")


# phase 4
#emotion = input("Finishing up! Lastly, I'd like you to enter an emotion (adjective, e.g. 'happy').  ")
#while basic_function(emotion) == True:
    #emotion = input("Please try again.  ")

#inserting lines with all names defined

#insertLines(2,"creepy",f"It was a cold, rainy night and {name} was hurrying home through the city when {pronoun2} noticed it had suddenly started raining {fruit}.")


#print(30 *'\n')

#timestr = time.strftime("%d%M%S")
#print (filename)
#f = open(timestr+'.txt', 'a+')
#f.write(result)
#f.close()


#print(2 *'\n')

#print ("Voila: Your very own customized short story!")

window.mainloop()

import tkinter as tk
import random
from tkinter import messagebox
 
window = tk.Tk()
#window.geometry("1400x900")
window.attributes('-fullscreen', True)
#window.config(bg="#065569")
window.resizable(width=False,height=False)
window.title('Word Guessing Game')

bg = tk.PhotoImage(file = "word.png")

label = tk.Label( window, image = bg )

label.place(x = 0, y = 0,relwidth=1,relheight=1)

global SCORE  

RETRIES = 0
SCORE = 0
 
def update_result(text):
    result.configure(text=text)
 
def new_game():
    guess_button.config(state='normal')
    global TARGET, RETRIES 

    fruits =  ['apple', 'tomato', 'litchi', 'mango', 'kiwi', 'grapes', 'cherry','banana', 'apricot', 'guava', 'orange', 'papaya', 'pear', 'peach']
    coding= ["python",'java',"variable","function","loop","algorithm", "debugging","syntax","class","recursion","library"]
    movies= ["action", "comedy", "thriller", "drama", "romance","fantasy", "horror", "animation", "mystery"]
    animals = ['ant', 'panda', 'giraffe', 'bear','cheetah', 'lizard', 'wolf', 'zebra','cobra', 'penguin', 'frog', 'rabbit', 'lion', 'monkey', 'ostrich','peacock', 'raccoon', 'sheep', 'dog','squirrel', 'tiger']
    stationary = ['notebook', 'tape', 'pencil', 'eraser', 'sharpener','files', 'fevicol', 'inkpot', 'chalk', 'duster','glue', 'paper', 'chart', 'colours','stapler', 'marker', 'staples', 'calculator','envelope', 'register']
    words=list(fruits+coding+movies+animals+stationary)
    TARGET = random.choice(words)
    RETRIES = 0

    if TARGET in fruits:  
        update_result(text="Your word is a Fruit.")
    elif TARGET in stationary:
        update_result(text="Your word is related to Stationary.")
    elif TARGET in animals:
        update_result(text="Your word is an Animal")
    elif TARGET in coding:
        update_result(text="Your word is related to Coding.")
    elif TARGET in movies:
        update_result(text="Your word is a movie genre.")
 
def play_game():
    global RETRIES,SCORE
 
    choice = word_form.get()
     
    if choice=="":
        result='Enter the word'
    elif choice != TARGET:
        RETRIES += 1
        result = "Wrong Guess!! Try Again"
    else:
        result = "You guessed the correct word after {} retries".format(RETRIES)
        guess_button.configure(state='disabled')
        result += "\n" + "Click on Play to start a new game"
        SCORE += 3
        result += "\n"+f"Your score is {SCORE}"
     
    update_result(result)

    word_form.delete(0,"end") 

def exit():
    input=messagebox.askyesno('QUIT',"Are you sure that you want to exit ? ")
    if input==True:
        window.destroy()
 
def hint1():
    global RETRIES,TARGET,SCORE
 
    a=TARGET[0]
    result = f"Your word starts with {a} "
    SCORE -= 1
    update_result(result)

def hint2():
    global RETRIES,TARGET,SCORE

    a=len(TARGET)
    result = f"the word is a {a} lettered word" 
    SCORE -= 1
    update_result(result)

def answer():
    global TARGET
    
    guess_button['state']='disabled'
    result=f"The word is {TARGET}"
    result += "\n" + "Click on Play to start a new game"
    update_result(result)

def rules():
    result="Rules to play :"
    result+="\nYou will get 3 points for right guess\nAnd -1 for each hint\nClick on Play Game to continue"
    update_result(result)

def score():
    global SCORE

    result=f"Your score is {SCORE}"
    update_result(result)

   
title = tk.Label(window,text="What's the word",font=("bold",38),fg="black",bg="white")
 
result = tk.Label(window, text="Click on Play to start a new game", font=("Arial", 20, "normal", "italic"),fg = "black",bg="white",justify=tk.LEFT)
 
play_button = tk.Button(window, text="Play Game", font=("Arial", 14), fg = "white", bg="#29c70a", command=new_game)
 
guess_button = tk.Button(window,text="Guess",font=("Arial",15), state='disabled', fg="#13d675",bg="Black", command=play_game)
 
exit_button = tk.Button(window,text="Exit Game",font=("Arial",14), fg="White", bg="#b82741", command=exit)
 
hint1_button = tk.Button(window,text="   HINT 1   ",font=("Arial",14), fg="black", bg="light blue", command=hint1)

hint2_button = tk.Button(window,text="   HINT 2   ",font=("Arial",14), fg="black", bg="light grey", command=hint2)

answer_button = tk.Button(window,text='  Reveal the word  ',font=("Arial",14), fg="black", bg="light yellow", command=answer)

score_button = tk.Button(window,text="    Score    ",font=("Arial",14), fg="black", bg="light pink", command=score)

rules_button = tk.Button(window,text="    Rules    ",font=("Arial",14), fg="black", bg="orange", command=rules)

guessed_word = tk.StringVar()
word_form = tk.Entry(window,font=("Arial",20),textvariable=guessed_word)
 
title.place(x=480, y=200)

result.place(x=480, y=340)

exit_button.place(x=990,y=115)

word_form.place(x=490, y=280)

guess_button.place(x=800, y=280) 

play_button.place(x=910, y=200)

score_button.place(x=910, y=250)

rules_button.place(x=910,y=300)

hint1_button.place(x=550,y=480)

hint2_button.place(x=680,y=480)

answer_button.place(x=580,y=530)

window.mainloop()

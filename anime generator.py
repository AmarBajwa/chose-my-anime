from tkinter import *
import tkinter as tk
import random
root = Tk()
root.geometry('400x300')
                     

#animes
random_shonen_long = ['naruto                     ','bleach                     ','one piece                     ','black clover                     ', 'HunterxHunter                     ',
                     'D.gray-man                     ', 'The Seven Deadly Sins                     ', 'Slam Dunk                     ']

random_shonen_short = ['Magi                     ', 'Senyu                     ', 'Megalo box                     ', 'Cells at work                     ','Death Note                     ', 
                        'Noragami                     ', 'Jujutsu Kaisen                     ' , 'Akame ga Kill                     ']

random_seinen_long = ['Vagabond                     ', 'Berserk                     ','Golden Kamuy                     ', 'Ajin                     ','Shuffle                     ']

random_seinen_short = ['one punch man                     ', 'tokyo ghoul                     ', 'vinland saga                     ', 'food wars                     ', 'erased                     ',
                        'parasite                     ', 'elfen lied                     ', 'bungou stray dogs                     ']

random_shojo_short = ['orange                     ', 'fruits basket                     ', 'cardcaptor sakura                    ', 'Golden time                     ', 'lovely complex                     ']

random_shojo_long = ['monogatori                     ', 'banana fish                     ', 'skip beat                     ', 'nana                     ', 'blue spring ride                     ']

Label1 = Label(root, text="what genre do you feel like: Shonen, Seinen, Shojo")
Label1.place(x=80 ,y=50)


def button2_command():  
    #long shonen
    text2 = entry2.get()
    if text2 == 'long':
        Label4 = Label(root, text= random.choice(random_shonen_long))
        Label4.place(x=160 ,y=190)
    #short shonen
    if text2 == 'short':
        Label4 = Label(root, text= random.choice(random_shonen_short))
        Label4.place(x=160 ,y=190)
    #short seinen
    if text2 == 'concise':
        Label4 = Label(root, text= random.choice(random_seinen_short))
        Label4.place(x=160 ,y=190)
    #long seinen
    if text2 == 'slow burner':
        Label4 = Label(root, text= random.choice(random_seinen_long))
        Label4.place(x=160 ,y=190)
    #long shojo
    if text2 == 'slow':
        Label4 = Label(root, text= random.choice(random_shojo_long))
        Label4.place(x=160 ,y=190)

    if text2 == 'fast':
        Label4 = Label(root, text= random.choice(random_shojo_short))
        Label4.place(x=160 ,y=190)

def button_command():  
    text = entry1.get()
    if text == 'Shonen':
        print(random.choice(random_shonen_long))
        Label2 = Label(root, text="long or short                     ")
        Label2.place(x=160 ,y=100)

    if text == 'Seinen':
        print('Vagabond')
        Label3 = Label(root, text="slow burner or concise                     ")
        Label3.place(x=160 ,y=100)

    if text == 'Shojo':
        print('fruits basket')
        Label3 = Label(root, text="slow or fast                     ")
        Label3.place(x=160 ,y=100)



#entries
entry1 = Entry(root, width = 20)
entry2 = Entry(root, width = 20)
entry2.place(x=140, y =130)
#button 2 placed
button2 = Button(root, text='Enter', command=button2_command)
button2.pack()
button2.place(x=180, y=150)




text = entry1.get()
entry1.pack()


        

        

Button(root, text='Enter', command=button_command).pack()




    







    

        #text2 == entry2.get()


        #text2.place(x=80 ,y=50)
        
        #if text2 == 'Happy':
           # print('Bleach')


        
       # entry2.pack()   







root.mainloop()
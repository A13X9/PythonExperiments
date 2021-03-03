#        ____________          ________ 
# _____ /_   \_____  \___  ___/   __   \
# \__  \ |   | _(__  <\  \/  /\____    /
#  / __ \|   |/       \>    <    /    / 
# (____  /___/______  /__/\_ \  /____/  
#      \/           \/      \/      

#Euromillions
    # TODO: ->Test more with duplicates

import random
import tkinter as tk


def numbers_millions():
    numbers_millions_list = []
    
    for i in range(5):
        i = random.randint(1, 50)
        numbers_millions_list.append(i)

    while numbers_millions_list.count(i) > 1:
        print('duplicated number: ' + str(i))
        print(numbers_millions_list.index(i))
        duplicate_index = numbers_millions_list.index(i)
        newrandom = random.randint(1, 50)
        numbers_millions_list[duplicate_index] = newrandom
        
    numbers_millions_list.sort()
    print('NUMBERS: ')
    print(numbers_millions_list)
    lbl_result_numbers["text"] = numbers_millions_list

def stars_millions():
    stars_millions_list = []
    
    for i in range(2):
        i = random.randint(1, 12)
        stars_millions_list.append(i)
    
    while  stars_millions_list.count(i) > 1:
            print('duplicated star: ' + str(i))
            print(stars_millions_list.index(i))
            duplicate_index = stars_millions_list.index(i)
            newrandom = random.randint(1, 12)     
            stars_millions_list[duplicate_index] = newrandom

    stars_millions_list.sort()
    print('STARS: ')
    print(stars_millions_list)
    lbl_result_stars["text"] = stars_millions_list

window = tk.Tk()
window.columnconfigure(0, minsize=200)
window.columnconfigure(1, minsize=200)
window.title('Euromilhoes')

numbers_btn = tk.Button(text="Numbers", command=numbers_millions, bg='blue', fg='yellow')
stars_btn = tk.Button(text="Stars", command=stars_millions, bg='blue', fg='yellow')

lbl_result_numbers = tk.Label(bg='blue', fg='yellow')
lbl_result_stars = tk.Label(bg='blue', fg='yellow')

numbers_btn.grid(row=0, column=0, sticky="nsew")
lbl_result_numbers.grid(row=0, column=1, sticky="nsew")

stars_btn.grid(row=1, column=0, sticky="nsew")
lbl_result_stars.grid(row=1, column=1, sticky="nsew")

window.mainloop()
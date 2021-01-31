#        ____________          ________ 
# _____ /_   \_____  \___  ___/   __   \
# \__  \ |   | _(__  <\  \/  /\____    /
#  / __ \|   |/       \>    <    /    / 
# (____  /___/______  /__/\_ \  /____/  
#      \/           \/      \/      

#Euromillions
    # TODO: ->Fix duplicates in generated key

import random
import tkinter as tk

def numeros_millions():
    numeros_millions_list = []
    
    for i in range(5):
        i = random.randint(1, 50)
        numeros_millions_list.append(i)

    numeros_millions_list.sort()
    lbl_result_numeros["text"] = numeros_millions_list

def estrelas_millions():
    estrelas_millions_list = []
    
    for i in range(2):
        i = random.randint(1, 12)
        estrelas_millions_list.append(i)

    estrelas_millions_list.sort()
    lbl_result_estrelas["text"] = estrelas_millions_list

window = tk.Tk()
window.columnconfigure(0, minsize=200)
window.columnconfigure(1, minsize=200)
window.title('Euromilhoes')

numeros_roll = tk.Button(text="Numbers", command=numeros_millions, bg='blue', fg='yellow')
estrelas_roll = tk.Button(text="Stars", command=estrelas_millions, bg='blue', fg='yellow')

lbl_result_numeros = tk.Label(bg='blue', fg='yellow')
lbl_result_estrelas = tk.Label(bg='blue', fg='yellow')

numeros_roll.grid(row=0, column=0, sticky="nsew")
lbl_result_numeros.grid(row=0, column=1, sticky="nsew")

estrelas_roll.grid(row=1, column=0, sticky="nsew")
lbl_result_estrelas.grid(row=1, column=1, sticky="nsew")

window.mainloop()
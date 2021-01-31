#        ____________          ________ 
# _____ /_   \_____  \___  ___/   __   \
# \__  \ |   | _(__  <\  \/  /\____    /
#  / __ \|   |/       \>    <    /    / 
# (____  /___/______  /__/\_ \  /____/  
#      \/           \/      \/        

#Dice

import random
import tkinter as tk

def roll():
    lbl_result["text"] = str(random.randint(1, 6))

window = tk.Tk()
window.columnconfigure(0, minsize=200)
window.rowconfigure([0, 1], minsize=200)
window.title('Dice')

btn_roll = tk.Button(text="Roll", command=roll)
lbl_result = tk.Label()

btn_roll.grid(row=0, column=0, sticky="nsew")
lbl_result.grid(row=1, column=0)

window.mainloop()
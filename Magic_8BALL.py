#        ____________          ________ 
# _____ /_   \_____  \___  ___/   __   \
# \__  \ |   | _(__  <\  \/  /\____    /
#  / __ \|   |/       \>    <    /    / 
# (____  /___/______  /__/\_ \  /____/  
#      \/           \/      \/     

#Magic _8BALL
    # TODO: ->Get the actual messages from the actual 8 Ball.

import random
import tkinter as tk


def ball_message():
    lbl_result["text"] = messages[random.randint(0, len(messages)-1)]
    print(lbl_result["text"])

window = tk.Tk()
window.columnconfigure(0, minsize=400)
window.rowconfigure([0, 1], minsize=400)
window.title('Magic 8 ball')

messages = ['It is certain',
            'It is decidedly so',
            'Yes definitly',
            'Reply hazy try again',
            'Ask again later',
            'Concentrate and ask again',
            'My reply is no',
            'Outlook not so good',
            'Very doubtful']

shake_btn = tk.Button(text="Shake the 8 Ball", command=ball_message, bg='black', fg='white')
lbl_result = tk.Label(bg='black', fg='white')

shake_btn.grid(row=0, column=0, sticky="nsew")
lbl_result.grid(row=1, column=0, sticky="nsew")

window.mainloop()



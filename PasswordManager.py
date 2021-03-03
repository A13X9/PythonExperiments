#        ____________          ________ 
# _____ /_   \_____  \___  ___/   __   \
# \__  \ |   | _(__  <\  \/  /\____    /
#  / __ \|   |/       \>    <    /    / 
# (____  /___/______  /__/\_ \  /____/  
#      \/           \/      \/        

"""
PasswordManager

An amazing and not very secure password manager!
Run it with the account you want and it copies your password to the clipboard.
Add your passwords to the password dictionary and give it an easy name.
For example, if you want to add a password for uber eats it should look like this: passwords = {'uber_eats': 'yoursecurepassword'}
Run it -> py password.py uber_eats

"""

#! python3
import sys, pyperclip

passwords = {'email': 'ilovepizza',
            'bank': 'pizzalovesme',
            'youtube': 'pizzalovesyou'}

if len(sys.argv) < 2:
    print('\n***Usage: py password.py [account] - must provide an account name***\n')
    sys.exit

account = sys.argv[1]  #first command line argument is the account name

if account in passwords:
    pyperclip.copy(passwords[account])
    print('\nPassword for ' + account + ' copied to clipboard.\n')
else:
    print('\nThere is no account named ' + account + '\n')
    

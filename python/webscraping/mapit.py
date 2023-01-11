# Excercise from "Automate the Boring Stuff with Python" Chapter 11.
# Launches google maps in the browser that searches for an address in the command's args or clipboard.

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    address = "+".join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open("google.com/maps/place/" + address)

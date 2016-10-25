import sys

def insertname(incoming):
    message = print("Hello ", incoming, "!", sep='')
    return(message)

def generalmessage():
    message = "Hello World!"
    print(message)

try:
    insertname(sys.argv[1])
except IndexError:
    generalmessage()
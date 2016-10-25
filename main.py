import sys

def insertname(incoming):
    message = print("Hello ",incoming,"!", sep='')
    return(message)

try:
    insertname(sys.argv[1])
except IndexError:
    print("Hello World!")
import os
from interactions import interactions
from functions import functions

def main():
    selection = interactions.setContext()
    if selection == "Add Context":
        functions.setContextAccount()
    if selection == "Select Context":
        interactions.selectContext()
if __name__ == "__main__":
    main()
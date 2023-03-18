import os
from simple_term_menu import TerminalMenu

def setContext():
    context = ["Add Context", "Remove Context", "Select Context"]
    terminal_menu = TerminalMenu(context, title="Hachimaru AWS Context")
    os.system("clear")
    menu_entry_index = terminal_menu.show()
    return context[menu_entry_index]

def list_files(directory="./contexts"):
    return (file for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file)))

def selectContext():
    terminal_menu = TerminalMenu(list_files())
    menu_entry_index = terminal_menu.show()
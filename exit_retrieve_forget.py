import sqlite3
from numbers_on_grid import *
import sys
import os
connection = sqlite3.connect('Personal_Wallet.db') #δημιουργούμε την σύνδεση με την βάση δεδομένων.
cursor = connection.cursor()


def forget_all(*args) :
    """makes all widgets from the tkinter window disappear, to create a new interface on the root."""
    for arg in args :
        arg.grid_forget()
def delete_digit(entry) :
    """This function doesn't allow the input of more than 2 decimal places (eg 2.41241) or other mistakes
    such as 2.3..4.21. Used in Withdraw and Deposit"""
    entry.delete(entry.index("end") - 1)


#retrieving every "forgotten" widget (used in every return button, all buttons are parameters in the button function)
def retrieve_all(root,entry,*args):
    entry.unbind("<Key>")
    center_window(root, 343, 830)
    for widget in root.winfo_children():
        widget.grid_forget()

    count = 0
    for i in args :
        i.grid(row=count,column=0)
        count +=1


#New root window, after the press of an exit button (only after login/signup)
def exit_program(root) :
    #these two, offer the functionality of being able to press both on screen or "x" button to exit
    def on_click(event) :
        new_root.destroy()
        sys.exit()
    def on_click_2() :
        new_root.destroy()
        sys.exit()

    def get_resource_path(relative_path):
        """ Get the absolute path to the resource, works for dev and PyInstaller """
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except AttributeError:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

    # Use the function to get the full path to the image
    filepath = get_resource_path('smartphone.png')

    root.destroy()
    new_root = Tk()
    center_window(new_root, 360, 390)
    img = PhotoImage(file=filepath)
    new_root.iconphoto(False, img)
    new_root.title("Goodbye Message")
    new_root.protocol("WM_DELETE_WINDOW",on_click_2)
    new_root.configure(bg="black")
    label_goodbye = Label(new_root, bg='black', fg='white', width=30, font=("Helvetica", 15, 'bold'),
                          text="\n\nThanks for using our app!\n\n\nProduced by : \n\nMaria Papananoy\nAthanasios Seretoudis\nRafail Koutalis\n\n\nPress anywhere to exit.")
    label_goodbye.grid(row=0)
    new_root.bind("<Button>",on_click)





from tkinter import *


#centers every window
def center_window(root, width, height):
    # Get the screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate the position to center the window
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)

    # Set the geometry of the window
    root.geometry(f'{width}x{height}+{x}+{y}')

def numbers(root,entry) :

    #function to prevent wrong input from KEYBOARD (no more than 2 dots, no letters or any other symbols)
    def on_key_press(event):
        entry_string = entry.get()
        count_dots = 0
        count_errors = 0

        for letter in entry_string :

            if not letter.isdigit() and not letter == "." :
                count_errors += 1
                entry.delete(entry.index("end") - 1)

            elif letter == "." :
                count_dots+=1
                string = entry.get()
                number_to_slice = string.index(".")
                string_2 = string[number_to_slice+1:]
                if len(string_2) > 1 :
                    count_errors +=1
                if count_dots > 1 :
                    count_errors +=1

            if count_errors > 0 :
                entry.delete(0,END)

            else :
                continue


    entry.bind("<Key>", on_key_press)

    #function to prevent wrong input on BUTTON PRESS (no more than 2 decimal places)
    def decimal_place_handling(entry):
        """μεριμνά ώστε ο χρήστης να μην μπορεί να περισσότερα από δυο δεκαδικά ψηφία
        γίνεται χρήση της στην επόμενη συνάρτηση"""
        try :
            string_decimals = entry.get()

            x = string_decimals.split(".")
            string_decimals = x[1]
            if len(string_decimals) > 2 :
                entry.delete(entry.index("end") - 1)
        except :
            pass

    #no more than 2 dots.
    def button_click(number, entry):
        """μεριμνά ώστε ο χρήστης να μη μπορεί να βάλει περισσότερα από μία τελείες."""
        entry.insert(END, number)
        if not entry.get().isdigit() :
            string = entry.get()
            sum = 0

            for i in range(len(string)):
                if string[i] == ".":
                    sum += 1
            if sum > 1:
                entry.delete(entry.index("end") - 1)

            decimal_place_handling(entry)


    #placing every number on the grid (used in Deposit and Withdraw functions from other_functions.py)
    button_0 = Button(root, text="0",font='sans 20 bold', width=6, height=2,borderwidth=10, command=lambda: button_click(0,entry))
    button_1 = Button(root, text="1",font='sans 20 bold', width=6, height=2,borderwidth=10, command=lambda: button_click(1,entry))
    button_2 = Button(root, text="2",font='sans 20 bold', width=6, height=2,borderwidth=10, command=lambda: button_click(2,entry))
    button_3 = Button(root, text="3",font='sans 20 bold', width=6, height=2,borderwidth=10, command=lambda: button_click(3,entry))
    button_4 = Button(root, text="4",font='sans 20 bold', width=6, height=2,borderwidth=10, command=lambda: button_click(4,entry))
    button_5 = Button(root, text="5",font='sans 20 bold', width=6, height=2,borderwidth=10, command=lambda: button_click(5,entry))
    button_6 = Button(root, text="6",font='sans 20 bold', width=6, height=2,borderwidth=10, command=lambda: button_click(6,entry))
    button_7 = Button(root, text="7",font='sans 20 bold', width=6, height=2,borderwidth=10, command=lambda: button_click(7,entry))
    button_8 = Button(root, text="8",font='sans 20 bold', width=6, height=2,borderwidth=10, command=lambda: button_click(8,entry))
    button_9 = Button(root, text="9",font='sans 20 bold', width=6, height=2,borderwidth=10, command=lambda: button_click(9,entry))
    button_comma = Button(root, text=".",font='sans 20 bold', width=6, height=2,borderwidth=10, command=lambda: button_click(".",entry))


    button_1.grid(row=2, column=0)
    button_2.grid(row=2, column=1)
    button_3.grid(row=2, column=2)
    button_4.grid(row=3, column=0)
    button_5.grid(row=3, column=1)
    button_6.grid(row=3, column=2)
    button_7.grid(row=4, column=0)
    button_8.grid(row=4, column=1)
    button_9.grid(row=4, column=2)
    button_0.grid(row=5, column=1)
    button_comma.grid(row=5, column=2)


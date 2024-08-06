from other_functions import *
from transaction_history import *
from login_signup import run_module
from graph import *
# from platform import system
#in this file, what happens is the creation of the main menu, the main buttons etc. After pressing
#each button, a function from a different file is called. In every aspect, there has been a serious effort to
#minimize crashes caused by users' wrong inputs.


username = run_module() #called from login_signup file, returns the username, upon which data from the database will be retrieved.

#destroys the old root on press
def on_click(event) :
    root.destroy()
#exits the whole app on press
def on_click_2(event) :
    exit_program(root)

#exits the whole app on button press
def on_closing() :
    exit_program(root)


root = Tk() #first root to create a "welcome" interface. Deletion after
center_window(root,380,320)
root.configure(bg='black')
root.focus()
root.title(f"{username}'s Wallet")

root.bind("<Return>",on_click)
root.bind("<Escape>",on_click_2)
root.protocol("WM_DELETE_WINDOW", on_closing)
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

img = PhotoImage(file= filepath)
root.iconphoto(False, img)


# Create a label
label = Label(root, text=f"Hello {username}.\n"
                         "To access your wallet,\n press the button below.", font=("Helvetica", 16,'bold'),bg='black',fg='white')
Border = LabelFrame(root,bg="black",fg="black",bd=10,relief=RIDGE,highlightcolor='red')
Border.grid(row=1)

button_enter_app = Button(Border,text="Access your Wallet",font=("Helvetica",15,'bold'),bg='blue',fg='white',height=2,width=27,borderwidth=15,command=lambda:root.destroy())
button_exit = Button(Border,text="EXIT",font=("Helvetica",15,'bold'),bg='red',fg='white',height=2,width=27,borderwidth=15,command=lambda:exit_program(root))

label.grid(row=0,columnspan=2,padx=20, pady=20)
button_enter_app.grid(row=1,column=0)
button_exit.grid(row=2,column=0)
root.mainloop()


root = Tk()

center_window(root, 343, 830)
root.bind("<Escape>", on_click_2)
root.protocol("WM_DELETE_WINDOW", on_closing)
root.title(f"{username}'s Wallet")  # user_id will be inserted through fstring
root.configure(bg='black', padx=10, pady=10)
# img = PhotoImage(file=filepath)
# root.iconphoto(False, img)

Border = LabelFrame(root, bg="black", fg="black", bd=10, relief=RIDGE,
                        highlightcolor='red')  # border to aestheticaly improve the project
Border.grid(row=1)

# every button name, displays its use.
# Everything is passed through function parameters.
LABEL = Label(root, bg='black', fg='white', font=("Helvetica", 15, 'bold italic'),
                  text=f"Welcome {username},\nto your Wallet App.\nChoose a function below!\n")


# exiting the program
button_exit = Button(Border, text="Exit Wallet", font=("newspaper", 15, 'bold'), padx=15, pady=12, width=20,
                         height=2, bg='floral white', fg='black', borderwidth=15, command=lambda: exit_program(root))

# money deposit
button_deposit = Button(Border, text="Deposit", font=("Bell Gothic Std Black", 15, 'bold'), padx=15, pady=12,
                            width=20, height=2, bg='deep sky blue',
                            borderwidth=15,
                            command=lambda: deposit(root, username, LABEL, button_deposit, button_withdraw,

                                                    button_show_amount, Button_print_history,button_graph, button_exit, Border))
# money withdrawal
button_withdraw = Button(Border, text="Withdraw", font=("Bell Gothic Std Black", 15, 'bold'), padx=15, pady=12,
                             width=20, height=2, bg='green',
                             borderwidth=15,
                             command=lambda: withdraw(root, username, LABEL, button_deposit, button_withdraw,
                                                      button_show_amount, Button_print_history, button_graph,button_exit, Border))
# displays current account balance
button_show_amount = Button(Border, text="Show amount", font=("newspaper", 15, 'bold'), padx=15, pady=12, width=20,
                                height=2, bg='magenta', fg='black', borderwidth=15,
                                command=lambda: show_amount(username,
                                                            root, LABEL, button_deposit, button_withdraw,
                                                            button_show_amount, Button_print_history, button_graph,button_exit,
                                                            Border))
# prints all user transactions to date
Button_print_history = Button(Border, text="Transaction History", font=("newspaper", 15, 'bold'), padx=15, pady=12,
                                  width=20,
                                  height=2, bg='gold2', fg='black', borderwidth=15,
                                  command=lambda: print_history(root, username, LABEL, button_deposit, button_withdraw,
                                                                button_show_amount, Button_print_history, button_graph,button_exit,Border))
#transaction graph
button_graph  = Button(Border, text="Daily Balance Graph", font=("Bell Gothic Std Black", 15, 'bold'), padx=15, pady=12,
                            width=20, height=2, bg='green2',borderwidth=15,command=lambda: show_graph(username))

# placing everything on the root grid
LABEL.grid(row=0, column=0)
button_deposit.grid(row=1, column=0)
button_withdraw.grid(row=2, column=0)
button_show_amount.grid(row=3, column=0)
Button_print_history.grid(row=4, column=0)
button_graph.grid(row=5,column=0)
button_exit.grid(row=6, column=0)
root.mainloop()



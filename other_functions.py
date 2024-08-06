from transaction_history import *
from exit_retrieve_forget import *

#creates the table in the db, for the user. This table later will be used to update his balance etc.
def create_table():
    try :
        cursor.execute("""
                    CREATE TABLE "Customer" (
                        "NAME" TEXT NOT NULL,
                        "PASSWORD" TEXT NOT NULL,
                        "ACC_AMOUNT" FLOAT NOT NULL,
                        PRIMARY KEY ("NAME")  
                );""")
    except :
        pass
    connection.commit()


#creating the user's profile table
def create_profile(name, password, amount):
    try :
        cursor.execute(
            """INSERT INTO CUSTOMER (NAME, PASSWORD, ACC_AMOUNT)
                VALUES (?, ?, ?);""",
            (name, password, amount)
        )
        connection.commit()
        return 1
    except :
        return 0


#used in log-in, to check if the credentials are valid
def log_in_credentials(name,password) :
    cursor.execute(f"SELECT NAME,PASSWORD FROM Customer WHERE NAME = '{name}' AND PASSWORD = '{password}'")
    list_credentials = cursor.fetchone()
    connection.commit()

    if not list_credentials :
        return 0
    else :
        return 1


#depositing money function, uses next function (update_amount_deposit)
def deposit(root,user_id,label,button_1,button_2,button_3,button_4,button_5,button_6,border):
    """Deposit function, after the DEPOSIT button press.
    Uses forget_all, delete_digit,and update_amount_deposit (from exit_retrive_forget.py)"""
    def on_click(event) :
        update_amount_deposit(root, user_id, entry, button_enter, button_delete_digit)

    forget_all(label, button_1, button_2, button_3,button_4,button_5,button_6,border) #forgets all previous widgets. and creates new ones
    center_window(root, 403, 655)
    myLabel = Label(root, bg='black', fg='white', font=("Helvetica", 13,'bold'), text="Εισάγετε το ποσό κατάθεσης.")
    entry = Entry(borderwidth=10,font=('Arial',20))
    entry.bind("<Return>",on_click)
    entry.bind("<Key>")
    entry.focus_set() #blinking cursor


    #button to return to the previous menu, restores all forgotten widgets (function retrieve from exit_retrieve_forget.py)
    button_prev = Button(root, text="Return",font='sans 20 bold',
                         width=6, height=2,borderwidth=10,
                         command=lambda: retrieve_all(root,entry,label,button_1,button_2,button_3,button_4,button_5,button_6,border))
    #enter completes the transaction
    button_enter = Button(root, text="ENTER", font='sans 20 bold',
                          width=14, height=2, borderwidth=7,command=lambda: (update_amount_deposit(root,user_id, entry,button_enter,button_delete_digit)))
    #button to correct the input, backspace essentially
    button_delete_digit = Button(root,text="⌫",font='sans 19 bold',width=7, height=2,borderwidth=9,command=lambda: (delete_digit(entry)))


    myLabel.grid(row=0, column=0,columnspan=3)
    entry.grid(row=1,column=0,columnspan=3,padx=15,pady=15)
    button_prev.grid(row=5, column=0)
    button_enter.grid(row=6, column=0, columnspan=2)
    button_delete_digit.grid(row=6,column=2)

    #από το αρχείο numbers_on_grid.py. Εμφανίζει όλα τα νούμερα.
    numbers(root,entry)
def update_amount_deposit(root,username,entry,button_enter,button_backspace) :
    """Function that will be called upon the press of DEPOSIT button. Updates the account balance in the DB, and at the same time,
    cares for any user mistakes,such as efforts to type for than 2 decimal digits, an empty input, more than 30000 of deposit/withdraw.συνάρτηση η οποία θα χρησιμοποιηθεί στο κουμπί DEPOSIT. Ενημερώνει το ποσό του λογαριασμου
    Those mistakes are not allowed in any modern ATMs/E-wallets, so precautions were taken for them, as an effort to minimize edge-case bugs.
    Finally, this function updates the tkinter interface."""

    amount = entry.get() #gets the amount input
    entry.focus_set() #blinking cursor in entry

    # on_key_press(entry)
    count_letters = 0
    for letter in amount : #checking if the amount contains "illegal" characters
        if (not letter.isdigit() and letter != '.') :
            count_letters += 1

    if count_letters == 0 :
        try :
            if (amount == "")  or (float(amount) <= 0) or (float(amount) > 30000):  # case of null input, or higher than 30000 euros
                messagebox.showerror("Error","Invalid amount. Please re-enter it,\n without it being higher than 30000 euros.")
                entry.delete(0, END)
            else:
                entry.config(state="disabled")
                center_window(root, 403, 655)
                transaction_save(username,amount,"DEPOSIT")  # updates the transaction history table (function on transaction_history.py)
                # current balance
                sql_statement = f"SELECT ACC_AMOUNT FROM CUSTOMER WHERE NAME  = '{username}'"
                cursor.execute(sql_statement)
                # fetchone, returns a tuple, so by indexing it we get the amount.
                existing_amount = cursor.fetchone()[0]
                connection.commit()
                # updating the balance in the db
                cursor.execute(
                    f"UPDATE CUSTOMER SET ACC_AMOUNT = {existing_amount + float(amount)} WHERE NAME= '{username}'")
                cursor.execute(sql_statement)

                # after one transaction, you have to return to the main menu to do another transaction# so the widgets have to be renewed
                button_enter.configure(state='disabled')
                button_backspace.configure(state='disabled')
                entry.delete(0, END)

                connection.commit()

                messagebox.showinfo("Success",
                                    f"Your account's new balance is :{existing_amount + float(amount):.2f} euro."
                                    f"\nClose this pop-up andress Return if you want to procced,\nelse, press Exit (top right corner).")
        except :
            messagebox.showerror("Error","Invalid amount entered.\nPlease re-enter a correct amount (up to 30000 euros).")
            entry.delete(0, END)
    else :
        messagebox.showerror("Error","Invalid amount entered.\nPlease re-enter a correct amount (up to 30000 euros).")
        entry.delete(0, END)




def withdraw(root,user_id,label,button_1,button_2,button_3,button_4,button_5,button_6,border):
    """Withdraw function, after the WITHDRAW button press.
    Uses forget_all, delete_digit,and update_amount_withdraw (from exit_retrive_forget.py)"""
    def on_click(event) :
        update_amount_withdraw(root, user_id, entry, button_enter, button_delete_digit)
    try :
        cursor.execute(f"SELECT * FROM 'Transaction' WHERE USERNAME = '{user_id}'")
        transaction_data = cursor.fetchall()
        connection.commit()
        if not transaction_data :
            messagebox.showerror("Error", "It is your first time here.\nYou have to deposit an amount first.")
        else :
            forget_all(label, button_1, button_2, button_3,button_4,button_5,button_6,border)
            root.configure(bg='black')
            center_window(root, 403, 655)
            myLabel = Label(root, bg='black', fg='white', font=("Helvetica", 13,'bold'), text="Enter the withdrawal amount.")
            entry = Entry(borderwidth=10,font=('Arial',20))
            entry.bind("<Return>",on_click)
            entry.delete(0,END)
            entry.focus_set()

            #key to return to the previous meny
            button_prev = Button(root, text="Return", font='sans 20 bold',
                                 width=6, height=2, borderwidth=10,
                                 command=lambda: retrieve_all(root,entry,label, button_1, button_2, button_3, button_4,button_5,button_6, border))
            #enter button
            button_enter = Button(root, text="ENTER", font='sans 20 bold',
                                  width=14, height=2, borderwidth=7,
                                  command=lambda: (update_amount_withdraw(root, user_id, entry, button_enter, button_delete_digit)))
            #backspace
            button_delete_digit = Button(root, text="⌫", font='sans 19 bold',
                                         width=7, height=2, borderwidth=9,command=lambda: (delete_digit(entry)))


            myLabel.grid(row=0, column=0,columnspan=3)
            entry.grid(row=1,column=0,columnspan=3,padx=15,pady=15)
            button_prev.grid(row=5, column=0)
            button_enter.grid(row=6, column=0, columnspan=2)
            button_delete_digit.grid(row=6,column=2)

            # από το αρχείο numbers_on_grid.py. Εμφανίζει όλα τα νούμερα.
            numbers(root,entry)
    except :
        messagebox.showerror("Error", "It is your first time here.\nYou have to deposit an amount first.")
def update_amount_withdraw(root,username,entry,button_enter,button_backspace) :
    """Function that will be called upon the press of WITHDRAW button. Updates the account balance in the DB, and at the same time,
    cares for any user mistakes,such as efforts to type for than 2 decimal digits, an empty input, more than 30000 of deposit/withdraw.συνάρτηση η οποία θα χρησιμοποιηθεί στο κουμπί DEPOSIT. Ενημερώνει το ποσό του λογαριασμου
    Those mistakes are not allowed in any modern ATMs/E-wallets, so precautions were taken for them, as an effort to minimize edge-case bugs.
    Finally, this function updates the tkinter interface."""

    amount = entry.get()
    #current balance
    sql_statement = f"SELECT ACC_AMOUNT FROM CUSTOMER WHERE NAME = '{username}'"
    cursor.execute(sql_statement)
    existing_amount = cursor.fetchone()[0]
    entry.focus_set() #blinking cursor

    try :
        if  (amount != "" and (str(amount.isdigit()))  or  (str(amount.isdecimal())) and (30000 > float(amount) or float(amount) < 0)):  # correct input case
            if existing_amount < float(amount):  # case of not enough money, so we grid the not_enough_money label
                entry.delete(0, END)
                messagebox.showerror("Error","Your balance is insufficient\nfor this transaction.\nPlease re-enter the amount.")

            else :  # enough money for the transaction
                # adjusting the interfaced widgets.
                center_window(root, 403, 655)
                entry.config(state="disabled")
                transaction_save(username,amount,"WITHDRAW")  # inserting the transaction in the transaction history table (transaction_history.py)
                # adjusting the various widgets too.
                button_enter.configure(state='disabled')
                button_backspace.configure(state='disabled')

                # updating the balance in the db
                cursor.execute(
                    f"UPDATE CUSTOMER SET ACC_AMOUNT = {existing_amount - float(amount)} WHERE NAME = '{username}'")
                cursor.execute(sql_statement)
                existing_amount_2 = cursor.fetchone()[0]
                connection.commit()

                messagebox.showinfo("Success",f"{amount} euros have been withdrawed.\n\nYour account's new balance is : {existing_amount_2} euro."
                                              "\nClose this pop-up andress Return if you want to procced,\nelse, press Exit (top right corner).")


        else:  # case of empty or wrong input
            center_window(root, 403, 655)
            messagebox.showerror("Error",
                                 "Wrong input,please re-enter the amount.")
            entry.delete(0, END)
    except :
        messagebox.showerror("Error","Invalid amount entered.\nPlease re-enter a correct amount (up to 30000 euros).")
        entry.delete(0,END)


def show_amount(username,root,label,button_1,button_2,button_3,button_4,button_5,button_6,border) :
    """shows the current balance on a new window, upon the Show Amount button press,works even if there have been
    no transactions made"""

    sql_statement = f"SELECT ACC_AMOUNT FROM CUSTOMER WHERE NAME = '{username}'"
    cursor.execute(sql_statement)
    connection.commit()

    try :
        existing_amount = cursor.fetchone()[0]
        my_Label = Label(root, bg='black', fg='white', font=("Helvetica", 13, 'bold'), height=4, width=30,
                         text=f"Your account's balance is :\n\n {existing_amount:.2f} euro.\n")
    except :
        my_Label = Label(root, bg='black', fg='white', font=("Helvetica", 13, 'bold'), height=4, width=30,
                         text="Your account balance is :\n 0 euro.")

    #forgets previous widgets
    forget_all(label, button_1, button_2, button_3,button_4,button_5,button_6,border)
    center_window(root, 370, 230)


    button_prev = Button(root, text="Return",bg='green',fg='white',font=("Helvetica", 15,'bold'),width=27,height=1, borderwidth=13,
                         command=lambda: retrieve_all(root,root, label,button_1, button_2, button_3,button_4,button_5,button_6,border))
    button_exit_program = Button(root, text="EXIT",bg="red",fg="white",font=("Helvetica", 15,'bold'), width=27,height=1, borderwidth=13,
                                 command=lambda: (exit_program(root)))
    my_Label.grid(row=0, column=0)
    button_prev.grid(row=1,column=0)
    button_exit_program.grid(row=2, column=0)
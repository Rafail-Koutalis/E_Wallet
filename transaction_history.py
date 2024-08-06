from exit_retrieve_forget import *
from tkinter import *
from tkinter import messagebox
from datetime import date
def transaction_table_creation() :
    cursor.execute("""
                            CREATE TABLE "Transaction" (
                            "TYPE" TEXT NOT NULL,
                            "USERNAME" TEXT NOT NULL,
                            "AMOUNT" FLOAT NOT NULL,
                            "CURRENT_AMOUNT" FLOAT NOT NULL, 
                            "DATE" TEXT NOT NULL
                            );""")
    connection.commit()


#saves the transaction data in the Transaction Sqlite Table
def transaction_save(username, amount,transaction_type) :
    try :
        transaction_table_creation()
    except :
        today_date = date.today()#get the today date
        rows = cursor.execute(f"""SELECT * FROM "Transaction" WHERE USERNAME = '{username}' """)
        row_count = 0
        for i in rows:
            row_count += 1


        if row_count == 0:
            balance_after = amount
            cursor.execute(
                """INSERT INTO [Transaction] (TYPE, USERNAME,AMOUNT, CURRENT_AMOUNT,DATE)
                   VALUES (?, ?, ?, ?, ?);""",
                (transaction_type, username, amount, balance_after,today_date,)
            )
            connection.commit()

        else:
            cursor.execute(
                f"SELECT ACC_AMOUNT FROM 'Customer' WHERE NAME = '{username}'")

            balance_tuple = cursor.fetchone()
            balance_before = balance_tuple[0]
            connection.commit()


            if transaction_type == "DEPOSIT":
                balance_after = float(amount) + float(balance_before)

            else:
                balance_after = float(balance_before) - float(amount)

            cursor.execute(
                """INSERT INTO [Transaction] (TYPE, USERNAME,AMOUNT, CURRENT_AMOUNT,DATE)
                   VALUES (?, ?, ?, ?,?);""",
                (transaction_type, username, amount, balance_after, today_date)
            )

        connection.commit()

def print_history(root,username,label_hi,button_deposit, button_withdraw, button_show_amount, button_print_history, button_graph,button_exit, border):
    try :
        list_transaction_data = []
        cursor.execute(f"SELECT * FROM 'Transaction' WHERE USERNAME = '{username}'")
        transaction_data = cursor.fetchall()
        connection.commit()
        if not transaction_data :
            messagebox.showerror("Error", "No transactions have been made yet.")
        else :
            for transaction in transaction_data :
                starting_list = []
                for transaction_element in range(5) :
                    starting_list.append(transaction[transaction_element])

                starting_list.pop(1)
                list_transaction_data.append(starting_list)

            center_window(root, 418, 450)
            LABEL = Label(root, bg='black', fg='white', font=("Helvetica", 13, 'bold italic'),
                          text="\nWelcome to your Wallet App.\nChoose a function below!\n\n")
            forget_all(LABEL, button_deposit, button_withdraw, button_show_amount, button_print_history,button_graph, button_exit, border)
              # Set initial window size

            frame = Frame(root, bg="black")  # Set frame background color to black
            frame.grid(row=0, column=0, sticky="nsew",columnspan=2)
            root.grid_rowconfigure(0, weight=1)
            root.grid_columnconfigure(0, weight=1)

            # Create a canvas with a scrollbar
            canvas = Canvas(frame, bg="black", highlightthickness=0)  # Set canvas background to black and remove highlight thickness
            scrollbar = Scrollbar(frame, orient="vertical", command=canvas.yview,highlightthickness=40)
            scrollable_frame = Frame(canvas, bg="black")  # Set scrollable frame background to black

            canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
            canvas.configure(yscrollcommand=scrollbar.set)

            label_header = Label(scrollable_frame, text="  Transaction History", font=("Helvetica", 14, "bold"), bg="black", fg="white")
            label_amount = Label(scrollable_frame, text="\nAmount\n", font=("Helvetica", 14, "bold"), bg="black", fg="white")
            label_type = Label(scrollable_frame, text="\nType\n", font=("Helvetica", 14, "bold"), bg="black", fg="white")
            label_balance = Label(scrollable_frame, text=" Total\n  Balance", font=("Helvetica", 13, "bold"), bg="black", fg="white")
            label_transaction_id = Label(scrollable_frame, text="\nDate\n", font=("Helvetica", 14, "bold"), bg="black",fg="white")



            label_header.grid(row=0, column=0, columnspan=4, sticky="ew")
            label_type.grid(row=1, column=0)
            label_amount.grid(row=1, column=1)
            label_balance.grid(row=1, column=2)
            label_transaction_id.grid(row=1, column=3)

            for idx, transaction in enumerate(list_transaction_data, start=2):
                for col,value in enumerate(transaction):
                    if transaction[0] == "DEPOSIT" :
                        label = Label(scrollable_frame, text=str(f"{value}  "), font=("Helvetica", 11), bg="black", fg="lawn green")
                    else :
                        label = Label(scrollable_frame, text=str(f"{value}  "), font=("Helvetica", 11), bg="black", fg="red")
                    label.grid(row=idx, column=col,padx=5)

            scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

            canvas.grid(row=1, column=0, sticky="ns")
            scrollbar.grid(row=1, column=1, sticky="ns")

            new_button_exit = Button(root, text="EXIT", font='sans 15 bold', width=21, height=1, borderwidth=15,
                                     command=lambda: (exit_program(root)))
            button_prev = Button(root, text="RETURN", font='sans 15 bold', width=21,
                                 height=1, borderwidth=15,command=lambda: retrieve_all(root,LABEL, label_hi, button_deposit, button_withdraw,
                                                               button_show_amount, button_print_history, button_graph,button_exit, border))
            button_prev.grid(row=2, column=0)
            new_button_exit.grid(row=3, column=0)
    except :
            messagebox.showerror("Error", "No transactions have been made yet.")











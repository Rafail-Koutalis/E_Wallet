from exit_retrieve_forget import *
from tkinter import messagebox
import matplotlib.pyplot as plt

def show_graph(username):
        try: #using try/except, cause in case you do a trasaction, press Daily Economic Graph, then do another and press it again, it showed different values on the same plot
            plt.close()
        except :
            pass
        #getting each date, using try/except, and if else, cause table might not exist.
        list_date_data = []
        cursor.execute(f"""SELECT DATE FROM "Transaction" WHERE USERNAME = '{username}' """)
        date_data = cursor.fetchall()
        if not date_data:
            messagebox.showerror("Error", "No transactions have been made yet.")
        else:
            for tuple_date in date_data: #nested for loop, cause the sqlite query returns tuples, and each tuple needs to be parsed separately.
                for key in tuple_date:
                    list_date_data.append(key)

            # getting every current amount after each transaction, placing it on data list
            final_amount_data = []
            cursor.execute((f"""SELECT CURRENT_AMOUNT FROM "Transaction" WHERE USERNAME = '{username}' """))
            amount_data = cursor.fetchall()
            for tuple_amount_data in amount_data:
                for key in tuple_amount_data:
                    final_amount_data.append(key)

            # in this loop, we get all the duplicate elements, so that in the plot, the only thing shown for each day is the amount after every transaction, and not
            #each transaction itself
            list_dates = []
            list_amounts = []
            for value in range(len(list_date_data)):
                try:
                    if list_date_data[value] == list_date_data[value + 1]:
                        list_dates.append(list_date_data[value])  #getting the duplicate dates here
                        list_amounts.append(final_amount_data[value]) #getting the amounts of those duplicate dates here
                except:
                    pass

            # we remove the duplicate dates (and following amounts) to create a plot based on the acc balance at the end of each day
            for date in list_dates:
                list_date_data.remove(date) #based on the contents of list_dates (duplicates), we remove those duplicates from the original list

            for amount in list_amounts: #same thing with the above for loop.
                final_amount_data.remove(amount)

            # rounding each balance value, cause matplotlib will not work with float numbers having decimal places different than 0.
            for value in final_amount_data:
                round(value)

            # plotting our data
            list_date_data.insert(0, "Acc. creation")
            final_amount_data.insert(0, 0)
            plt.ylabel("Account Amount")
            plt.xlabel("Transaction Date")

            plt.title(f"{username}'s economic graph")
            plt.plot(list_date_data, final_amount_data, '-gD')
            plt.gcf().autofmt_xdate()
            plt.show()




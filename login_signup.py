import tkinter as tk
from tkinter import messagebox
from other_functions import create_profile,log_in_credentials,create_table
from exit_retrieve_forget import *
from transaction_history import transaction_table_creation
import os

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
specials = [f'%','@','!','^','*','#','!','$','&','(',')','/']

list_username = []
def run_module() :
    def escape(event):
        sys.exit()
    def on_closing():
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

    root = Tk()
    root.bind("<Escape>", escape)
    img = PhotoImage(file= filepath)
    root.iconphoto(False, img)
    root.protocol("WM_DELETE_WINDOW", on_closing)

    def sign_up(root):
        def on_click(event) :
            confirm_signup(root,entry_username.get(),entry_password.get(),entry_confirm_password.get())
        def retype_credentials() :
            entry_username.delete(0,END)
            entry_password.delete(0,END)
            entry_confirm_password.delete(0,END)
            entry_username.focus()

        def confirm_signup(window, username, password, confirm_password):
            count_specials = 0
            count_numbers = 0
            count_alphabet = 0
            for char in password  :
                if char.isdigit() :
                    count_numbers+=1
                elif char in specials :
                    count_specials +=1
                elif char.lower() in alphabet :
                    count_alphabet += 1


            if username == '' or password == '' or confirm_password == '':
                messagebox.showerror("Error", "Please fill every box!")

            elif len(username) < 6 :
                messagebox.showerror("Error","Username must contain at least 6 characters.")
                retype_credentials()
            elif len(password) < 11 :
                messagebox.showerror("Error", "Password must contain\nat least 11 characters!")
                retype_credentials()
            elif count_alphabet < 5 or count_specials < 1 or count_numbers < 2 :
                messagebox.showerror("Error","Password must contain at least 1 letter\n"
                                             "two numbers and one special character\n"
                                             "{$-%-&-*-!-@-(-)-/-|}\n backslash not included")
                retype_credentials()
            elif password != confirm_password:
                messagebox.showerror("Error", "Passwords do not match!")
                retype_credentials()
            else:
                if create_profile(username, password, 0) == 0: #logw monadikotitas primary key.
                    messagebox.showerror("Error", "Username exists!")
                    retype_credentials()
                else:
                    messagebox.showinfo("Success", "Sign up seccessful!")
                    transaction_table_creation()
                    list_username.append((entry_username.get()))
                    window.destroy()

        #function actual code starts here ===========================================================#
        for widget in root.winfo_children() :
            widget.destroy()

        root.configure(bg='white')
        center_window(root, 300,240)
        root.title("Sign up")
        root.bind("<Return>",on_click)

        label_username = tk.Label(root, text="User name:", font=("Helvetica", 14))
        label_username.pack()

        entry_username = tk.Entry(root, font=("Helvetica", 14))
        entry_username.focus()
        entry_username.pack()

        label_password = tk.Label(root, text="Password:", font=("Helvetica", 14))
        label_password.pack()

        entry_password = tk.Entry(root, show="*", font=("Helvetica", 14))
        entry_password.pack()

        label_confirm_password = tk.Label(root, text="Re-type Password:", font=("Helvetica", 14))
        label_confirm_password.pack()

        entry_confirm_password = tk.Entry(root, show="*", font=("Helvetica", 14))
        entry_confirm_password.pack()

        empty_label = tk.Label(root,text="",bg='white')
        empty_label.pack()

        btn_confirm_signup = tk.Button(root,text='Confirm Credentials', font=("Helvetica", 16,'bold'), height=1,
                                       command=lambda :confirm_signup(root,entry_username.get(),entry_password.get(),entry_confirm_password.get()))
        btn_confirm_signup.pack()

    def sign_in(root):
        def on_click(event):
            confirm_login()

        def confirm_login():
            username = entry_username.get()
            password = entry_password.get()
            if username == '' or password == '':
                messagebox.showerror("Error", "Please fill every box")
            else:
                if log_in_credentials(username,password) == 0 :
                    entry_username.focus()
                    entry_username.delete(0, END)
                    entry_password.delete(0, END)
                    messagebox.showerror("Error", "Credentials invalid!")
                else:
                    messagebox.showinfo("Success", "Log in seccessful!")
                    list_username.append(username)
                    root.destroy()

        # function actual code starts here ===========================================================#
        for widget in root.winfo_children() :
            widget.destroy()
        root.configure(bg='white')
        center_window(root, 300,200)
        root.protocol("WM_DELETE_WINDOW", on_closing)
        root.bind("<Return>",on_click)
        root.title("Log in")


        label_username = tk.Label(root, text="Username:", font=("Helvetica", 16))
        label_username.pack()
        entry_username = tk.Entry(root, font=("Helvetica", 16))
        entry_username.focus()
        entry_username.pack()

        label_password = tk.Label(root, text="Password:", font=("Helvetica", 16))
        label_password.pack()
        entry_password = tk.Entry(root, font=("Helvetica", 16),show="*")
        entry_password.pack()

        empty_welcome = tk.Label(root, text="",bg='white')
        empty_welcome.pack()

        log_in_button = tk.Button(root,text="Log in",font=('helvetica',14,'bold'),width=19,height=1,command=lambda :confirm_login())
        log_in_button.pack()


    def first_time_using_app() :
        def on_click(event) :
            sign_up(root)
        # function actual code starts here ===========================================================#
        center_window(root,400,350)
        root.bind("<Return>",on_click)
        root.title("Virtual Wallet")
        root.resizable(False, False)  # Απαγορεύουμε την αλλαγή μεγέθους
        root.configure(background='#6495ED')

        label_welcome = tk.Label(root, text="We see it is your first\ntime using the app.\nPlease sign up!",
                                 font=("Helvetica", 24, "bold"), background='#6495ED')
        label_welcome_2 = tk.Label(root,text="Enter -> Sign-up\nEsc -> Exit\n\n\n",font=('Helvetica',13),background='#6495ED')
        label_welcome.pack(pady=(30, 10))
        label_welcome_2.pack()
        button_sign_up = tk.Button(root,text='Sign up',font=('helvetica',16,'bold'),height=2,width=20,command=lambda :sign_up(root))
        button_sign_up.pack()
        root.mainloop()


    def not_first_time_using_app() :
        center_window(root,400,340)
        root.title("Virtual Wallet")
        root.configure(background='#6495ED')

        # Ετικέτα καλωσορίσματος
        label_welcome = tk.Label(root, text="Please sign up/log in!",
                                 font=("Helvetica", 24, "bold"), background='#6495ED')
        label_welcome.pack(pady=(30, 10))
        label_exit = tk.Label(root, text="(or press Esc to exit)\n\n", font=('helvetica', 14), background='#6495ED')
        label_exit.pack()

        empty_welcome = tk.Label(root, text=" ", background='#6495ED')
        empty_welcome.pack()

        # Κουμπί για την εγγραφή
        btn_sign_up = tk.Button(root, text="Sign up", command=lambda: sign_up(root), font=("Helvetica", 14),width=25)
        btn_sign_up.pack(pady=10)

        # Κουμπί για την σύνδεση
        btn_sign_in = tk.Button(root, text="Log in", command=lambda: sign_in(root), font=("Helvetica", 14),width=25)
        btn_sign_in.pack(pady=5)
        root.mainloop()

    #code starts here#=============================================================================================#
    #==============================================================================================================#

    username = ""
    create_table() #creating the tables in the db
    cursor.execute("SELECT * FROM Customer")
    list_customers = cursor.fetchall()
    connection.commit()


    if not list_customers :
        first_time_using_app()
        try :
            username = list_username[0]
        except :
            pass
        list_username.clear()

    else :
        not_first_time_using_app()
        try :
            username = list_username[0]
        except :
            pass
        list_username.clear()

    return username





















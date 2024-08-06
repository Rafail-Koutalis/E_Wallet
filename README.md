# E_Wallet
An E_Wallet, to keep track of your economics. Supports more than 1 users per PC.

This is the very first real app i took part in creating.

The App :

-Helps you easily keep track of your day 2 day transactions. -It is build upon an SQLITE3 database, which is stored locally, so each computer can support more than 1 users per installation. -Each user has his own unique credentials. -If its the first time the app is used on a computer (meaning no data have been stored yet and the database is empty) you can only sign in and not log in. -The different actions you can do are : Deposit money/ Withdraw money / see the transaction History / see the daily balance graph (only stores the available balance at the end of the day)

Month-2-month and 3-months to 3-months graphs features will be added in the near future, to store and see your economic progress in a longer time spectrum.

1)If you DONT want to build the app, you can just run the root_main.py file. 2)If you want to build it (through Pyinstaller package),you will need to use CMD, so make sure python is added to PATH. first install pyinstaller using(on the cmd) : pip install pyinstaller Then , use : cd directory_where_you_saved_the_files. Then copy/paste this command : pyinstaller --onefile --windowed --icon=wallet_money_business_coin_dollar_icon_150710.ico --add-data "exit_retrieve_forget.py;." --add-data "graph.py;." --add-data "login_signup.py;." --add-data "numbers_on_grid.py;." --add-data "other_functions.py;." --add-data "transaction_history.py;." --add-data "smartphone.png;." root_main.py

If the installation is complete, go to the original directory (where the .py files are saved), and you will see a filed named "dist". In this file, you will find the executable app. Due to the parameter --onefile, the executable is a bit slower to start. If you want that to change, you can replace it with --onefolder.

Be sure to enjoy, and if you see have any recommendations, dont hesitate :)

import database
import tkinter as tk


MENU_PROMPT = """
1) Add new bean
2) See all beans
3) Find a bean by name
4) See best preparation for a bean
5) Delete bean
6) Update bean

7) Exit

Your Selection: """

def menu():
    connection = database.connect()
    database.create_table(connection)

    while (user_input := input(MENU_PROMPT)) != "7":
        if user_input == "1":
            name = input("Enter bean name: ")
            method = input("Enter preparation method: ")
            rating = int(input("Enter rating: "))
            price = int(input("Enter price: "))
            database.add_bean(connection, name, method, rating, price)

        elif user_input == "2":
            beans = database.get_all_beans(connection)
            #if there is no beans in the database, print a message
            if not beans:
                print("No beans found.")
            for bean in beans:
                #add the price
                print(f"{bean[1]} ({bean[2]}) - {bean[3]} stars - {bean[4]}")
        elif user_input == "3":
            name = input ("Enter bean name: ")
            beans = database.get_beans_by_name(connection, name)

            #if not in database, print message
            if not beans:
                print("Bean not found in database.")
                continue
            for bean in beans:
                print(f"{bean[1]} ({bean[2]}) - {bean[3]} stars - {bean[4]}")
        elif user_input == "4":
            name = input ("Enter bean name: ")
            bean = database.get_best_preparation_for_bean(connection, name)

            #if not in database, print message
            if not bean:
                print("Bean not found in database.")
                continue
            print(f"{bean[1]} ({bean[2]}) - {bean[3]} stars - {bean[4]}")
        elif user_input == "5":
            name = input ("Enter bean name: ")
            database.delete_bean(connection, name)
        elif user_input == "6":
            #get name of bean to modify
            name = input ("Enter bean name: ")
            # if not in database, print message
            if not database.get_beans_by_name(connection, name):
                print("Bean not found in database.")
                continue
            #get new name, method, and rating
            new_name = input ("Enter new bean name: ")
            new_method = input ("Enter new preparation method: ")
            new_rating = int(input ("Enter new rating: "))
            new_price = int(input ("Enter new price: "))
            #update bean
            database.modify_bean(connection, new_name, new_method, new_rating, new_price, name)
        else:
            print("Invalid input, please try again.")


""" 
def menu_tk():
    connection = database.connect()
    database.create_table(connection)

    window = tk.Tk()
    window.title("Bean Database")
    window.geometry("500x300")

    #create a label
    label = tk.Label(text="Welcome to the Bean Database!")
    label.pack()

    #create a button called add a beans
    button = tk.Button(text="Add a bean", command=add_bean_tk)
    button.pack()


    window.mainloop()

#create a function to add the bean
def add_bean_tk():
    #create a new window
    window = tk.Tk()
    window.title("Add Bean")
    window.geometry("500x300")

    #create a label
    label = tk.Label(text="Add a new bean to the database!")
    label.pack()

    #create an entry box
    name_entry = tk.Entry()
    name_entry.pack()

    #create a button and create a function to run when the button is clicked
    button = tk.Button(text="Add bean", command=add_bean_tk)
    button.pack()

    window.mainloop()

"""

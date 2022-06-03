from distutils.command.config import config
import mysql.connector
from mysql.connector import errorcode
import re

config = {
    "user":"whatabook_user",
    "password":"MySQL8IsGreat!",
    "host":"127.0.0.1",
    "database":"whatabook",
    "raise_on_warnings":True
}
def show_menu():
    sel = int(input("\nPlease select an option number and press enter.\n1: View Books\n2: View Store Locations\n3: My Account\n4: Exit Program\n"))
    return sel
def show_books(cursor):
    print("\nAvailable Books:\n")
    cursor.execute("SELECT * FROM book;")
    books = cursor.fetchall()
    for book in books:
        print("{}, {}. ID#:{}\n{}...\n".format(book[1],book[3],book[0], book[2][0:100]))
def show_locations(cursor):
    print("\nLocations:")
    cursor.execute("SELECT locale, store_hours FROM store;")
    stores = cursor.fetchall()
    for store in stores:
        print("\nAddress: {}\nHours: {}\n".format(store[0],store[1]))
def show_account_menu(cursor):
    try:
        accIn = int(input("Please enter your User ID.\n"))
        cursor.execute("SELECT first_name, last_name, user_id FROM user WHERE user_id = {};".format(accIn))
        if cursor.rowcount == 0:
            print("\nUser not found.\n")
        acc = cursor.fetchall()
        for acc in acc: 
            print("Account:") 
            print("\nName: {} {}\n".format(acc[0], acc[1]))
            while True:

                try:
                    sel = int(input("Please select an account menu option.\n1: View Wishlist\n2: Add to Wishlist\n3: Exit to Main Menu\n"))
                    if sel == 1:
                        show_wishlist(cursor,accIn)
                    elif sel == 2:
                        show_books_to_add(cursor,accIn)
                        add_books_to_wishlist(cursor,accIn)
                    elif sel == 3:
                        break
                    else:
                        continue 
                except:
                    print("\nPlease enter valid menu option.\n")       
    except:
        print("\nPlease enter User ID numbers only.\n")
def show_wishlist(cursor,accIn):
    cursor.execute("SELECT book_id FROM wishlist WHERE user_id = {};".format(accIn))
    wlist = cursor.fetchall()
    for item in wlist:
        item = re.sub(r'[^\w]', '', str(item))
        cursor.execute("\nSELECT book_id, book_name, author, details FROM book WHERE book_id = {};".format(item))
        book = cursor.fetchall()
        for book in book:
            print("\n{}, {}. ID#:{}\n{}...\n".format(book[1],book[2],book[0], book[3][0:100]))
def show_books_to_add(cursor,accIn):
    print("\nAvailable Books Not in Wishlist:\n")
    cursor.execute("SELECT book_id, book_name, author, details FROM book WHERE book_id NOT IN ( SELECT book_id FROM wishlist WHERE user_id = {});".format(accIn))
    books = cursor.fetchall()
    for book in books:
        print("\n{}, {}. ID#:{}\n{}...\n".format(book[1],book[2],book[0], book[3][0:100]))

def add_books_to_wishlist(cursor,accIn):
    try:
        sel = int(input("\nPlease enter the ID# of the book you would like to add to your wishlist. Enter 0 if you do not wish to add a book.\n"))
        if sel != 0:
            cursor.execute("INSERT INTO wishlist (book_id, user_id) VALUES ({},{});".format(sel,accIn))
    except:
        print("\nBook ID# not found.\n")
if __name__ == "__main__":
    print("\n\nWelcome to the WhatABook service application.\n")
    db=mysql.connector.connect(**config)
    cursor = db.cursor()
    try:  
        while True:
            sel = show_menu()
            if sel == 1:
                show_books(cursor)
            elif sel == 2:
                show_locations(cursor)
            elif sel == 3:
                show_account_menu(cursor)
            elif sel == 4:
                print("\nExiting...")
                break
            else:
                print("\nPlease enter valid number option.\n")

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("\nThe supplied username or password is invalid.\n")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("\nDatabase does not exist.\n")
        else:
            print(err)
    finally:
        db.close()
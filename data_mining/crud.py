'''
C => Create (INSERT INTO)
R => Read   (SELECT)
U => Update (UPDATE)
D => Delete (DELETE)
'''

from database import con, cur
import os
import bcrypt

status_menu = True
global status_op

def hash_password(passwd):
    return bcrypt.hashpw(passwd.encode(), bcrypt.gensalt())

def create_user(op):
    #Create a new user
    os.system('clear')

    print("::: Signup form :::")
    fname = input("Your firstname: ")
    lname = input("Your lastname: ")
    ident = input("Your ident number: ")
    email = input("Your email: ")
    passwd = input("Your password: ")
    passwd_hashed = hash_password(passwd)

    new_user = f'''
        INSERT INTO 
            users (firstname, lastname, ident_number, email, password) 
            VALUES('{fname}', '{lname}', '{ident}', '{email}', "{passwd_hashed}")
    '''
    con.execute(new_user)
    con.commit()

    print("::: New user has been created sucessfully :::")
    os.system('pause')
    menu()

def list_users(op):
    #Read all the data from table users
    os.system('clear')
    cur.execute("SELECT * FROM users")
    print(cur.fetchall())

    os.system('pause')
    menu()

def search_user(op):
    os.system('clear')
    print("::: SEARCH USER BY IDENTIFICATION NUMBER :::")
    ident_num = input("Identification number: ")

    cur.execute(f"SELECT email FROM users WHERE ident_number = '{ident_num}' ")
    print(cur.fetchall())

    os.system('pause')
    menu()

def menu():
    global opt
    status_opt = True
    while status_menu: 
        os.system('clear')
        print(":::::::::::::::::::::::")
        print(":::::: MAIN MENU ::::::")
        print(":::::::::::::::::::::::")
        print("[1]. Create a new user")
        print("[2]. List users")
        print("[3]. Search user")
        print("[4]. Update user")
        print("[5]. Delete user")
        print("[6]. Exit")
        
        while status_opt:
            opt = input("Press an option: ")
            if opt < '1' or opt > '6':
                print(".:::::: Invalid option, try again.")
            else :
                status_opt = False

        if opt == '1':
            create_user(opt)
        elif opt == '2':
            list_users(opt)
        elif opt == '3':
            search_user(opt)
        elif opt == '6':
            print("::: See 'u soon :::")
            exit()
        
menu()

#Close connection
con.close()
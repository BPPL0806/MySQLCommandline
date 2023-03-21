import mysql.connector
from os import system

close = exit

def exit():
    print("\nExiting...\n")
    system("pause")
    close(0)

def clear():
    system("cls")

def help():
    print("\nhelp   Display this message\nclear   Clear the screen\nexit   Quit commandline\n")

commands = {
    "exit" : exit,
    "clear" : clear,
    "help" : help,
    #"save" : save
}

v = "2.0.0"

print(f"MySQL Commandline [Version {v}]\n(c) MIT License\n\n(Press CTRL+C to exit.)\n")

while True:
    try:
        host_input = input("Enter database address: ")
        username_input = input(f"Enter username for {host_input}: ")
        passw_input = input(f"Enter password for {username_input}: ")
        
        database = mysql.connector.connect(
        host = host_input,
        user = username_input,
        password = passw_input
        )
        break
    
    except KeyboardInterrupt:
        exit()

    except mysql.connector.errors.ProgrammingError:
        print("\n[Invalid credentials.]\n")
        continue

    except mysql.connector.errors.InterfaceError:
        print("\n[Invalid address.]\n")
        continue
        

username = database.user
host = database._host

system("cls")
print(f'Connected to {host} as {username}.\n')

dbcursor = database.cursor()

while True:
    try:
        query = input("["+username+"@"+host+"]> ")
        if query.lower() in commands:
            commands[query]()
            continue
        dbcursor.execute(query)
        result = dbcursor.fetchall()
        print("\n====================================")
        for x in result:
            print(f'{x}')
        print("====================================\n")
        continue
    except KeyboardInterrupt:
        exit()
    except mysql.connector.Error as error:
        if str(error) == "No result set to fetch from.":
            continue
        print("\n====================================")
        print(f"[{error}]")
        print("====================================\n")
        continue

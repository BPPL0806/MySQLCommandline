#!/usr/bin/env python3

import mysql.connector
from os import system

host_input = input("Enter database address: ")
username_input = input(f"Enter username for {host_input}: ")
passw_input = input(f"Enter password for {username_input}: ")

try:
    database = mysql.connector.connect(
    host = host_input,
    user = username_input,
    password = passw_input
    )
    
except:
    print("\n[Invalid credentials.]")
    input("Press Enter to exit...")
    exit()

username = database.user
host = database._host

print(f'Connected to {host} as {username}.\n(Use CTRL-C to exit.)\n')

dbcursor = database.cursor()

while True:
    try:
        query = input("["+username+"@"+host+"]> ")
        dbcursor.execute(query)
        result = dbcursor.fetchall()
        print("\n====================================")
        for x in dbcursor:
            print(f'{x}')
        for x in result:
            print(f'{x}')
        print("====================================\n")
        continue
    except KeyboardInterrupt:
        print(f'\n[Disconnecting from {host}...]\n')
        input("Press enter to exit...")
        exit(0)
    except mysql.connector.Error as error:
        if str(error) == "No result set to fetch from.":
            continue
        print("\n====================================")
        print(f"[{error}]")
        print("====================================\n")
        continue

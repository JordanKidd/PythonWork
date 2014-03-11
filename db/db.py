import sqlite3 as sql
import sys


def main():
    con = None
    try:
        con = sql.connect('test.db')
        cur = con.cursor()
        #createMembersTable(con)
        menu(cur)
        #cur.execute('SELECT SQLITE_VERSION()')
        #data = cur.fetchone()
        #print("SQLite version: %s" % data)
    except sql.Error as e:
        print("Error %s:" % e.args[0])
        sys.exit(1)
    finally:
        if con:
            con.close()


def menu(cur):
    """Prints out the menu to user"""
    userNum = 0
    while userNum != 6:
        print("""What do you want to do?
    1. Add new member(s)
    2. Add item(s)
    3. Show members
    4. Show items
    5. Begin transaction loop
    6. Exit""")
        print("==> ", end = "")
        userNum = input()
        isInt = False
        try:
            userNum = int(userNum)
        except:
            print("Please input a number...")

        if userNum == 1:
            addMember(cur)
        elif userNum == 2:
            addItem()
        elif userNum == 3:
            showMembers(cur)
        elif userNum == 4:
            showItems()
        elif userNum == 5:
            transactionLoop(cur)
        elif userNum == 6:
            print("Goodbye!")
            break
        else:
            userNum = 0


def addMember(cur):
    """Grabs user's data and places it into the db"""
    userConfirm = ""
    print("Starting user creation. Type 'exit' at confirmation to about / end")
    while userConfirm != "exit":
        print("Enter First Name: ", end = "")
        userFName = input()
        print("Enter Last Name: ", end = "")
        userLName = input()
        print("Enter user handle: ", end = "")
        userHandle = input()
        print("Enter contact number (FORMAT: XXX-XXX-XXXX): ", end = "")
        userNumber = input()
        print("Enter user email: ", end = "")
        userEmail = input()

        confirmLine = ""
        print("""
    First:  {0}
    Last:   {1}
    Handle: {2}
    Number: {3}
    Email:  {4}
    """.format(userFName, userLName, userHandle, userNumber, userEmail))
        print("Confirm with 'y' to commit, 'n' to restart, 'exit' to end: ",
            end = "")
        userConfirm = input()
        if userConfirm == "y":
            insertUser(cur, userFName, userLName, userHandle,
                userNumber, userEmail)
            break
        elif userConfirm == "n":
            print("Restarting!")
        else:
            break


def addItem():
    print("2 TODO")


def showMembers(cur):
    cur.execute('SELECT * FROM MEMBERS')
    print(cur.fetchall())


def showItems():
    print("4 TODO")


def transactionLoop(cur):
    print("5 TODO")


def insertUser(cur, fr, la, handle, num, e):
    #INSERT INTO Ints(Val) VALUES (1), (3), (5), (6), (7), (8), (6), (4), (9);
    toInsert = "INSERT INTO MEMBERS (TEXT,TEXT,TEXT,CHAR(30),TEXT) VALUES "
    toInsert.join("{0}, {1}, {2}, {3}, {4});")
    toInsert.format(handle, fr, la, e, num)
    print(toInsert)
    cur.execute(toInsert)


def createMembersTable(conn):
    """This creates the tables for the db"""

    conn.execute('''CREATE TABLE MEMBERS(
    HANDLE      TEXT PRIMARY KEY     NOT NULL,
    FIRSTNAME   TEXT                 NOT NULL,
    LASTNAME    TEXT                 NOT NULL,
    EMAIL       CHAR(30),
    PHONE       TEXT);''')


if __name__ == '__main__':
    main()

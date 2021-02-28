import time,datetime
from getpass import getpass

def write_user():
    f.write("User: " + user + '\n')
    f.write("Pass: " + password + '\n')
    f.write("Login Date : " + str(datetime.datetime.now()) + '\n')
print("Welcome")
login_f = 0
while True:
    user = input("Enter Username: ")
    password = getpass("Enter Password: ")
    if user=="Test" and password=="1234":
        print("Success!!")
        f = open("DB.txt","a")
        f.write(chr(92)*4 + "Login Success" + "\n")
        write_user()
        f.close()
        break
    else:
        print("Error!!!")
        f = open("DB.txt","a")
        f.write("Login Error!!" + "\n")
        write_user()
        f.close()
        login_f = login_f + 1
        if login_f >= 3:
            print("Prevent Brute Force Attack!!!")
            print("Please wait 30s")
            time.sleep(30)

    
    

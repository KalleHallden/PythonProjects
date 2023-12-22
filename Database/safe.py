
import sqlite3
import base64
import imageio
import cv2

# /Users/kalle/Desktop/myfile.py
PASSWORD = "123456"

# Password input
connect = input("What is your password?\n")

# Verifying that entered password
# is same as the actual password
while connect != PASSWORD:
    connect = input("What is your password?\n")
    if connect == "q":
        break

if connect == PASSWORD:
    conn = sqlite3.connect('mysafe.db')

    # mysafe.db has a table with format
    # Full Name(text), name(text), extension(text), files(text)
    try:
        conn.execute('''CREATE TABLE SAFE
            (FULL_NAME TEXT PRIMARY KEY NOT NULL,
            NAME TEXT NOT NULL,
            EXTENSION TEXT NOT NULL,
            FILES TEXT NOT NULL);''')
        print("Your safe has been created!\n")
        print("What would you like to store in it today?")
    except:
        print("You have a safe, what would you like to do today?")
    
    
    while True:
        print("\n"+ "*"*15)
        print("Commands:")

        # There are 3 operations
        # quit(q), open file(o), store file(s)
        print("q = quit program")
        print("o = open file")
        print("s = store file")
        print("_"*15)
        input_ = input(":")

        # quitting the program (break)
        if input_ == "q":
            break

        # opening the file 
        if input_ == "o":
            file_type = input("What is the filetype of the file you want to open?\n")
            file_name = input("What is the name of the file you want to open?\n")
            FILE_ = file_name + "." + file_type

            cursor = conn.execute("SELECT * from SAFE WHERE FULL_NAME=" + '"' + FILE_ + '"')

            file_string = ""
            for row in cursor:
                file_string = row[3]
            with open(FILE_, 'wb') as f_output:
                print(file_string)
                f_output.write(base64.b64decode(file_string))



        # Storing the file
        if input_ == "s":
            PATH = input("Type in the full path to the file you want to store.\nExample: /Users/kalle/Desktop/myfile.py\n")

            FILE_TYPES = {
                "txt": "TEXT",
                "java": "TEXT",
                "dart": "TEXT",
                "py": "TEXT",
                "jpg": "IMAGE",
                "png": "IMAGE",
                "jpeg": "IMAGE"
            }

            file_name = PATH.split("/")
            file_name = file_name[len(file_name) - 1]
            file_string = ""

            NAME = file_name.split(".")[0]
            EXTENSION = file_name.split(".")[1]

            try:
                EXTENSION = FILE_TYPES[EXTENSION]
            except:
                Exception()


            if EXTENSION == "IMAGE":
                IMAGE = cv2.imread(PATH)
                file_string = base64.b64encode(cv2.imencode('.jpg', IMAGE)[1]).decode()

            elif EXTENSION == "TEXT":
                file_string = open(PATH, "r").read()
                file_string = base64.b64encode(file_string)

            EXTENSION = file_name.split(".")[1]
            
            command = 'INSERT INTO SAFE (FULL_NAME, NAME, EXTENSION, FILES) VALUES (%s, %s, %s, %s);' %('"' + file_name +'"', '"' + NAME +'"', '"' + EXTENSION +'"', '"' + file_string +'"')
            
            conn.execute(command)
            conn.commit()
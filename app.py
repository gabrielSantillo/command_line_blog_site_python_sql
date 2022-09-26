import dbcreds
import mariadb

# this function make the connection to the db and get back all posts of all users
def get_all_posts():
    # trying to connect to the db
    try:
        conn = mariadb.connect(password=dbcreds.pasword, user=dbcreds.user, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
    # if some exception occurs print this message
    except:
        print("Something went wrong. The appropriate person has been notified.")
    # this cursor function pass our calls to mariadb and get the results
    cursor = conn.cursor()
    # calling the function that is in our db
    cursor.execute('CALL get_all_posts()')
    # getting the results of our query
    result = cursor.fetchall()
    # closing our connection to the db
    cursor.close()
    conn.close()

    for post in result:
        print("\n",post[0], post[1],"\n")

# this function make the connection to the db and add a new post based on its user id
def post_user_content(user_id):
    # asking the user the content of the post and storing its value
    content = input("Type your content:\n")
    # asking the user the title of the post and storing its value
    title = input("Type your title:\n")
    # trying to connect to the db
    try:
        conn = mariadb.connect(password=dbcreds.pasword, user=dbcreds.user, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
    # if some exception occurs print this message
    except:
        print("Something went wrong. The appropriate person has been notified.")
    # this cursor function pass our calls to mariadb and get the results
    cursor = conn.cursor()
    # calling the function that is in our db and sending 3 arguments
    cursor.execute('CALL add_post_user(?,?,?)', [user_id, content, title])
    # closing our connection to the db
    cursor.close()
    conn.close()

# this function make the connection to the db and log the user in
def log_in_user():
    # asking the username and storing its value
    username = input("Username: ")
    # asking the password and storing its value
    password = input("Password: ")
    # trying to connect to the db
    try:
        conn = mariadb.connect(password=dbcreds.pasword, user=dbcreds.user, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
    # if some exception occurs print this message
    except:
        print("Something went wrong. The appropriate person has been notified.")
    # this cursor function pass our calls to mariadb and get the results
    cursor = conn.cursor()
    # calling the function that is in our db and sending 2 arguments
    cursor.execute('CALL select_user_id(?,?)', [username, password])
    # getting the results of our query
    result = cursor.fetchall()
    # closing our connection to the db
    cursor.close()
    conn.close()

    # checking if the result lenght is equal to one, which it has content inside
    if(len(result) == 1):
        # printing the id by looping the result 
        for id in result:
            return id[0]
    # if it empty, show a message to the user
    else:
        print("Your username or password is incorrect. Try again.")
        return

# this function get the user selection
def get_user_selection():
    print("\n1. Insert a post?")
    print("2. Read all posts?")
    print("3. Read only your posts?")
    print("4. See all usernames?")
    print("5. Wanna see posts based in a username?")
    print("6. Quit?")
    user_selection = input("Chose between 1, 2, 3, 4, 5 or 6.\n")
    # returning the user selection 
    return user_selection

# this function make the connection to the db and gets the post by its user id
def get_user_post(user_id):
    # trying to connect to the db
    try:
        conn = mariadb.connect(password=dbcreds.pasword, user=dbcreds.user, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
    # if some exception occurs print this message
    except:
        print("Something went wrong. The appropriate person has been notified.")
    # this cursor function pass our calls to mariadb and get the results
    cursor = conn.cursor()
    # calling the function that is in our db and sending 1 arguments
    cursor.execute('CALL get_post_by_id(?)', [user_id])
    # getting the results of our query
    result = cursor.fetchall()
    # closing our connection to the db  
    cursor.close()
    conn.close()
    # looping the results and printing its content and title
    for post in result:
        print("\n",post[0], post[1],"\n")

# this function make the connection to the db and gets all usernames
def get_all_usernames():
    # trying to connect to the db
    try:
        conn = mariadb.connect(password=dbcreds.pasword, user=dbcreds.user, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
    # if some exception occurs print this message
    except:
        print("Something went wrong. The appropriate person has been notified.")
    # this cursor function pass our calls to mariadb and get the results
    cursor = conn.cursor()
    # calling the function that is in our db
    cursor.execute('CALL get_all_usernames()')
    # getting the results of our query
    result = cursor.fetchall()
    # closing our connection to the db 
    cursor.close()
    conn.close()

    # looping the results and printing all usernames
    for post in result:
        print("\n",post[0],"\n")

# this function make the connection to the db and get posts by username
def get_post_by_username():
    # asking the username and storing its value
    username = input("What is the username you want see the posts?\n")
    # trying to connect to the db
    try:
        conn = mariadb.connect(password=dbcreds.pasword, user=dbcreds.user, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
    # if some exception occurs print this message
    except:
        print("Something went wrong. The appropriate person has been notified.")
    # this cursor function pass our calls to mariadb and get the results
    cursor = conn.cursor()
    # calling the function that is in our db and sending 1 arguments
    cursor.execute('CALL get_post_by_username(?)', [username])
    # getting the results of our query
    result = cursor.fetchall()
    # closing our connection to the db 
    cursor.close()
    conn.close()

    # checking if the result has a lenght of at least 1
    if(len(result) >= 1):
        # if yes, print the post and content
        for post in result:
            print("\n",post[0], post[1],"\n")
    # if not, print a message to the user
    else:
        print("This username is wrong or doesn't exist. Try again.")

# this function run the application
def run_app():
    # calling the function that will log in the user and storing its return
    user_id = log_in_user()
    # if the return is None, run the application again
    if(user_id == None):
        run_app()
    # infinite while loop
    while(True):
        # calling the function that will get the user selection, and based on that will call a function that match the selection
        user_selection = get_user_selection()
        # if the selection was 1, call the function that will post the content for the user
        if(user_selection == "1"):
            post_user_content(user_id)
        # if the selection was 2, call the function that will get all posts
        elif(user_selection == "2"):
            get_all_posts()
        # if the selection was 3, call the function that will get all user posts
        elif(user_selection == "3"):
            get_user_post(user_id)
        # if the selection was 4, call the function that will get all usernames
        elif(user_selection == "4"):
            get_all_usernames()
        # if the selection was 5, call the function that will get all posts based in a username
        elif(user_selection == "5"):
            get_post_by_username()
        # if the selection was 6, break the infite loop and exit the application
        elif(user_selection == "6"):
            return
        # if the selection was anything but these numbers, print this message and the while loop will make the application runs again
        else:
            print("You must type only numbers between 1, 2, 3, 4, 5 or 6.")

# starting the application
run_app()
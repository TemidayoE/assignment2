# Create a simple username and password authentication.
# If the username and password specified are correct, then print
# a success message, else print "You're are wrong!" five times.

import getpass
users= {'John':'password111', 'Jon':'password112', 'Joe':'password113'}

def login():
  username = input("Enter your username: ")
  password = input("Enter your password: ")
  if username in users and users[username] == password:
    print( "Login successfully")
  else:
    print("You are wrong! " *5)
    
login()
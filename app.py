import os

Cami = input("Comment t'appelles-tu ? ")
message = os.getenv("MESSAGE_SECRET" , "Bonjour")
print(message + " " + Cami + " !") 



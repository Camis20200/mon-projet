import os 

def create_message(name):
    message = os.getenv("MESSAGE_SECRET", "Bonjour")
    name = name.strip()
    return f"{message} {name} !"

if __name__ == "__main__":
    Cami = input("Comment t'appelles-tu ? ")  # nosec  
    print(create_message(Cami))

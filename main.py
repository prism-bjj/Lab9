def encode(strinput):
    for i in range (0, len(strinput)):
        print(((int(strinput[i]) + 3) % 10), end='') 

def menu():
    print("""Menu1. Encode
          2. Decode
          3. Exit""")
    
if __name__ == "__main__":
    password = []
    menu()
    choice = input("Please enter an option")
    while True:
        if choice == 1:
            strinput = input("Please enter your password to encode: ")
            password.append(encode(strinput))
            print("Your password has been encoded and stored!")
        if choice == 2:
            if len(password) < 1:
                print("No password yet:")
            else:
                print(f"The encoded password is {password.pop}")
        if choice == 3:
            break

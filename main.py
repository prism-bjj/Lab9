def encode(strinput):
    encoded_pass = []
    for i in strinput:
        new_pass = (int(i) + 3) % 10
        encoded_pass.append(str(new_pass))
    return ''.join(encoded_pass)

def decode(code):
    decoded_pass = []
    for i in code:
        new_pass = (int(i) - 3) % 10
        decoded_pass.append(str(new_pass))
    return ''.join(decoded_pass)

def menu():
    print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
    
if __name__ == "__main__":
    menu()
    choice = int(input("Please enter an option: "))
    while True:
        if choice == 1:
            strinput = input("Please enter your password to encode: ")
            encoded = encode(strinput)
            print(encode(strinput))
            print("\nYour password has been encoded and stored!\n")
            menu()
            choice = int(input("Please enter an option: "))

        if choice == 2:
            print(f"The encoded password is {encoded}, and the original password is {decode(encoded)}.")
            menu()
            choice = int(input("Please enter an option: "))

        if choice == 3:
            break

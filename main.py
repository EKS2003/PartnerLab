def encoded_password():
    input_string = input("Please enter your password to encode:")
    result_string = ""

    for char in input_string:
        if char.isdigit():
            new_char = str((int(char) + 3) % 10)
            result_string += new_char
        else:
            result_string += char
    return result_string


def menu():

        while True:
            print("""
    Menu
    -------------
    1. Encode
    2. Decode
    3. Quit
                   """)
            menu_option = int(input("Please enter an option: "))
            if menu_option == 1:
                password_encoded = encoded_password()
                print(password_encoded)



            # elif menu_option == 2:
            #     decoded_password()
            elif menu_option == 3:
                print("Exiting the program.")
                break
            else:
                print("Invalid option. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    menu()

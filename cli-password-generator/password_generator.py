import string
import random

def print_banner():
    
    #Prints the ASCII art banner for the password generator.
    
    banner = """==================================================================
  _____           _____  _____ __          __ ____  _____  _____  
 |  __ \   /\    / ____|/ ____|\ \        / // __ \|  __ \|  __ \ 
 | |__) | /  \  | (___ | (___   \ \  /\  / /| |  | | |__) | |  | |
 |  ___/ / /\ \  \___ \ \___ \   \ \/  \/ / | |  | |  _  /| |  | |
 | |    / ____ \ ____) |____) |   \  /\  /  | |__| | | \ \| |__| |
 |_|   /_/    \_\_____/|_____/     \/  \/    \____/|_|  \_\_____/ 
=================================================================="""
    print(banner)


def length():
    """
    Prompts the user for the desired password length.
    Ensures the user provides a length of at least 8 characters.
    """
    loop = 0
    
    # Loop continues until a valid length is provided
    while(loop == 0):
        length = (int(input("\n[?] Enter your password length (min 8): ")))
        
        # Input validation: Check if the length meets the minimum requirement
        if(length < 8):
            print("[!] Please enter a number of 8 or higher.\n")
        else:
            # Incrementing the loop variable breaks the while loop
            loop += 1
            
    return length


def condition():
    """
    Prompts the user to select the character sets to include in the password.
    Ensures that at least one character type is selected before proceeding.
    """
    loop = 0
    print("\n--- Character Selection ---")
    
    # Loop continues until a valid combination of character sets is selected
    while(loop == 0):
        char = input("[?] Input letters? (y/n): ")
        number = input("[?] Input numbers? (y/n): ")
        symbols = input("[?] Input symbols? (y/n): ")
        
        # Validation: Prevent the user from rejecting all character types
        if char == "n" and number == "n" and symbols == "n":
            print("[!] Error: Minimum 1 element needed to make a password... Try again.\n")
            
        # Check every possible valid combination and build the character pool accordingly
        elif char == "y" and number == "y" and symbols == "y":
            password = string.ascii_letters + string.digits + string.punctuation
            loop += 1
        elif char == "y" and number == "n" and symbols == "n":
            password = string.ascii_letters
            loop += 1
        elif char == "n" and number == "y" and symbols == "n":
            password = string.digits
            loop += 1
        elif char == "n" and number == "n" and symbols == "y":
            password = string.punctuation
            loop += 1
        elif char == "y" and number == "y" and symbols == "n":
            password = string.ascii_letters + string.digits
            loop += 1
        elif char == "y" and number == "n" and symbols == "y":
            password = string.ascii_letters + string.punctuation
            loop += 1
        elif char == "n" and number == "y" and symbols == "y":
            password = string.digits + string.punctuation
            loop += 1
    
    # Resetting the loop variable (Note: this is kept to preserve original logic)
    loop = 0
    
    return password
    
def main():
    
    #Main function to orchestrate the password generation process.
    
    # Display the startup banner
    print_banner()
    
    # Get the desired length of the password
    n = length()
    
    # Get the string of allowed characters based on user preferences
    value = condition()
    
    # Initialize the final password string (Note: initialized with a space)
    finalPassword = " " 
    
    # Randomly select a character from the allowed pool 'n' times
    for i in range(n):
        finalPassword += random.choice(value)
    
    # Display the final generated result to the user
    print("\n************************************************")
    print("  GENERATED PASSWORD : " , finalPassword)
    print("************************************************")
    

# Trigger the main function to run the program
main()

import random  # Import the random module to generate the secret number

# Function to print the game's title banner using ASCII art
def print_banner():
    banner = """==================================================================
  _____ _            _____ _    _ ______  _____ _____ 
 |_   _| |          / ____| |  | |  ____|/ ____/ ____|
   | | | |__   ___ | |  __| |  | | |__  | (___| (___  
   | | | '_ \\ / _ \\| | |_ | |  | |  __|  \\___ \\\\___ \\ 
   | | | | | |  __/| |__| | |__| | |____ ____) |___) |
   |_| |_| |_|\\___| \\_____|\\____/|______|_____/_____/ 
==================================================================
"""
    print(banner)

# Display the welcome banner at startup
print_banner()

# Initialize variables for the game setup loop and attempt counter
loop = 0
attempt = 1

print("⚙️ [Game setup]")
# Setup loop: Keep asking for range until a valid maximum number is provided
while(loop == 0):
    min_number = int(input("Enter minimum number:"))
    max_number = int(input("Enter maximum number:"))
    
    # Validation: Ensure the maximum number is strictly greater than the minimum
    if(max_number > min_number):
        loop = loop + 1  # Exit the setup loop
    else: 
        print("⚠️ Maximum must be greater than minimum !")
        
# Refresh the banner and display the finalized game configurations
print_banner()
print("🎯 Target Range: [", min_number, " to ", max_number, "]")
print("💡 Good luck! Type your guess below.\n")
print("----------------------------------------------------\n\n")

# Generate the random secret number within the user-defined range
random_num = random.randint(min_number, max_number)

# Reset the loop control variable for the main gameplay loop
loop = 0

# Main gameplay loop: Continues until the player guesses the correct number
while(loop == 0):
    print("Attempt #", attempt)
    guess = int(input("🎲 Your Guess:"))
    
    # Check if the player's guess is too high
    if(random_num < guess):
        print("📈 TOO HIGH! Try lower.\n")
    # Check if the player's guess is too low
    elif(random_num > guess):
        print("📉 TOO LOW! Try higher.\n")
    # Triggered when the player guesses the correct number
    else:
        print("\n====================================================\n")
        print(" 🎉 VICTORY! You guessed the secret number(", random_num, ") !")
        print(" 📊 Total Attempts:", attempt)
        
        # Determine the player's performance rank based on total attempts
        if(attempt <= 3):
            print(" 🌟 Rank: GODLIKE GUESSER!")
        elif(attempt <= 7):
            print(" 👍 Rank: SHARPSHOOTER!")
        else:
            print(" 🐢 Rank: SLOW & STEADY!")
            
        print("====================================================\n\n")
        
        loop += 1  # Exit the gameplay loop
        
    attempt += 1  # Increment the attempt counter for the next round

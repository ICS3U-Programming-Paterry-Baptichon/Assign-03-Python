#!/usr/bin/env python3

# Created by Paterry Baptichon J
# Created: 2022-04-11
# This program will calculate weather a user is old enough to vote or not

def main():
    
    try:
    # This is where the user enter's their age
        user_age = input("Enter your age here: ")
        print("")
        
        user_age_int = int(user_age)
        
    # This function tells the user if they are old enough to vote in an election
        if user_age_int >= 18:
            print("You are old enough to vote!")
        else:
            print("Sorry, you are not old enough to vote.")
            print("")
            
        #Ask user if they want to calculate again
        
            print("Would you like to try with a again")
        play_again = str(input("Y or N:"))

        if(play_again == ("Y") or (play_again ==  "y")):
            main()
    except Exception:
    
        print("That's not a number! Try again.")

if __name__ == "__main__":
    main()
    
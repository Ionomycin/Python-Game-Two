#-------------------------------------------------------------------------------------------------------
# Import the RNG module.
import random
#-------------------------------------------------------------------------------------------------------
# Import the time module.
# The time module allows your computer to be a little more efficient by purposely
# causing your program to lag for a pre-determined amount of time (I have alrady established such time)
import time
#-------------------------------------------------------------------------------------------------------
# Beginning of file includes: a welcome message and how the agmes works.
# including how many attemps you have.
print("I want to play another game. This one is a little different.\n")
print("You will get five turns. Win three times? You win.")

print("Loose twice? You'll lose. OH, there's a little more to the game than just this, but I'm not going to spoil it for you!\n")
print("Enough talk... Have fun!")
#-------------------------------------------------------------------------------------------------------
# Main Function Code:
# Takes in RNG value between 1-100 and stores it in a variable called valueRandom.
# Sets your attempts to zero, wins to zero, and the RNG's wins to zero.

def main(valueRandom = random.randint(1,100), attempts = 0, wins = 0, winsRNG = 0):

    # Crucial error checking. If you input anything other than an integer value,
    # it will raise an exception error.
    while True:

        try:

            # Have enough attempts? Allow the user to input a number.
            # Typecasted to an integer. You will recieve errors for strings and float values.
            userNumber = int(input("Type an integer from 1-100: "))


        except (TypeError, ValueError, UnboundLocalError):

            # Catches typecast errors, value errors, and unbound local errors only.
            print("\nThat doesn't seem to be a correct value.\n")

            continue
            # Until the exception is caught, contine. Otherwise, if no error exists,
            # continue on to the if statement.


        if (attempts < 5):


            # If the user's input is greater than zero, enter the if-elif statement.
            if (userNumber > 0):


                # Tell the user that the program will purposely lag for a moment.
                print("Please wait. This will take 1.5 seconds.\n")


                # Initiates the time module and sets the lag time to 1.5 seonds.
                time.sleep(1.5)


            # Once the lag-time has passed, print out your input and the RNG's output in string form.
            # Also output the responses in reverse. The reversed value will be used to decide
            # the winner of the round.
            
            print("Your number was: " + str(userNumber) + " | Reversed: " + str(userNumber)[::-1])
            print("RNG's number was: " + str(valueRandom) + " | Reversed: " + str(valueRandom)[::-1] + "\n")


            # If the user's number was greater than that of the RNG's, output they won the round.
            if (userNumber > valueRandom):
                print("You won this round... Congratulations!")
                # Increment the number of wins by one.
                wins += 1


            # If the user's number was less than that of the RNG's, output the RNG system won the round.
            if (userNumber < valueRandom):
                print("You DIDN'T win this round. Try again (Show the RNG who's boss)!!")
                winsRNG += 1


            # Else, if the user's input matches the RNG's value, you will type and won't recieve
            # any points.     
            elif (userNumber == valueRandom):
                print("You tied with the RNG! No points were awarded to either of you this round.")


            # Increment the number of attempts. Everytime this happens you lose an attempt
            # so five attempts, becomes four, and so on.
            attempts += 1


            # Did you win three times in a row? Then you won!
            if (wins == 3):
                print("CONGRATULATIONS you won the game! Program will now self-terminate.")
                # Break isn't neccessarily good, but I'm going to use it in this case to
                # force the program to exit itself.
                break


            # Did the RNG system win two times? Then you lost!
            elif(winsRNG == 2):
                print("UNFORTUNATELY the bot won against you... Program will now self-terminate.")
                # Break isn't neccessarily good, but I'm going to use it in this case to
                # force the program to exit itself.
                break
#-------------------------------------------------------------------------------------------------------
# Finally, call the main method so that the entire program runs. This program
# is contained inside one giant main function (known as a method in Java IDE's)

main()

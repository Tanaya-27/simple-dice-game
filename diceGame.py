##external file work 
def storingScores(totalScore1,totalScore2,user1,user2): 
    file = open("highScores.txt", "a") 
    totalScore1 = str(totalScore1) 
    totalScore2 = str(totalScore2) 
    #appends username and total score into an external file 
    file.write(user1 + ", " + totalScore1 + "\n") 
    file.write(user2 + ", " + totalScore2 + "\n") 
    file.close() 
    print("Your scores have been stored in an external text file") 
    topFive() 
  
#displays top 5 from file 
#code used from teacher example 
def topFive(): 
    import csv 
    file = open("highScores.txt", "r") 
    data = csv.reader(file) 
    #sorts file into score order 
    orderedList = sorted(data, key=lambda test:int(test[1]), reverse=True) 
    top5 = orderedList[0:5] 
    print("These are the top 5 scores from this dice game:") 
    print("") 
    for line in top5: 
        print(str(line)[2:-2]) #sorce-quora:slice string to remove brackets and '' 
    file.close() 
  
  
import random 
#procedure to play the game 
def playGame(user1, user2): 
    evenNumbers = [2, 4, 6, 8, 10, 12] 
    oddNumbers = [1, 3, 5, 7, 9, 11] 
    totalScore1 = 0 
    totalScore2 = 0 
    for x in range(5): 
        print("") 
        print("***PLAYER 1- ",user1,"***") 
        input("Press ENTER to continue...") 
        die1 = random.randint(1,6) 
        die2 = random.randint(1,6) 
        #outputs user 1's score 
        print(user1, "rolled a" ,die1, "and a", die2) 
        diceTotal = die1 + die2 
        #adds points to total depending on score 
        if diceTotal in evenNumbers: 
            points = 10 
        elif diceTotal in oddNumbers: 
            points = -5 
        if die1 == die2: 
            print("You rolled a double!") 
            points = double() 
        #adds to total score for that player 
        totalScore1 = totalScore1 + points  
        if totalScore1 < 0: 
            totalScore1 = 0 
        print(user1,"'s current total is", totalScore1) 
        #repeats code for next player 
        print("") 
        print("***PLAYER 2- ",user2,"***") 
        input("Press ENTER to continue...") 
        die1 = random.randint(1,6) 
        die2 = random.randint(1,6) 
        #outputs user 2's score 
        print(user2, "rolled a" ,die1, "and a", die2) 
        diceTotal = die1 + die2 
        if diceTotal in evenNumbers: 
            points = 10 
        elif diceTotal in oddNumbers: 
            points = -5 
        if die1 == die2: 
            print("You rolled a double!") 
            points = double() 
        #adds to total score for that player 
        totalScore2 = totalScore2 + points 
        if totalScore2 < 0: 
            totalScore2 = 0 
        print(user2,"'s current total is", totalScore2) 
    else: 
        #end of five rounds 
        #outputs winner 
        print("") 
        if totalScore1 > totalScore2: 
            print("Congratulations",user1,"! Player One wins :)") 
            print(user1,"'s score is" , totalScore1) 
            print(user2,"'s score is" , totalScore2) 
        elif totalScore2 > totalScore1: 
            print("Congratulations",user2,"! Player Two wins :)") 
            print(user2,"'s score is" , totalScore2) 
            print(user1,"'s score is" , totalScore1) 
        else: 
            print("The scores are the same! You must now roll again") 
            rollAgain(user1,user2) 
        #call subroutine to append scores into text file 
        storingScores(totalScore1,totalScore2,user1,user2) 
  
  
def rollAgain(user1,user2): 
    #allows players to roll a single die and outputs a winner 
    print("") 
    print("***ROLLING AGAIN***") 
    input("Press ENTER to continue...") 
    print("") 
    #outputs each players roll 
  
     
    rollOne = random.randint(1,6) 
    print(user1,", you rolled a", rollOne) 
    rollTwo = random.randint(1,6) 
    print(user2,", you rolled a", rollTwo) 
    #outputs a winner 
    if rollOne > rollTwo: 
            print("Congratulations ",user1,"! ",user1," wins :)") 
    elif rollTwo > rollOne: 
            print("Congratulations ",user2,"! ",user2," wins :)") 
    else: 
            print("The scores are the same! You must now roll again") 
            rollAgain(user1,user2) 
  
def double(): 
    #allows player to roll one die and adds this value to score 
    print("You must now roll one extra die...") 
    roll = random.randint(0,6) 
    print("Your rolled a",roll,"!") 
    roll = roll +10 
    return roll 
  
  
  
#AUTHENTICATION 
  
#2 dimentional list to store exising login details 
loginDetails = ["test", "test123"] , ["Tanaya", "Password1"] , [] 
validUser = True 
  
def intro1(user1): 
    print("***PLAYER ONE***") 
    input("Press ENTER to continue...") 
    print("Welcome to the Dice Game. Please choose your option") 
    print("1. Sign in with your existing details") 
    print("2. Sign up with a username and password") 
    print("") 
    #user inputs what they want to do 
    choice = input("Please choose a number: ") 
    if choice == "1": 
        user1 = input("Enter Username: ") 
        for i in range(len(loginDetails)): 
            if user1 in loginDetails[i][0]:  
                print("Valid username") 
                validUser == True 
                password1 = input("Enter Password: ") 
                if password1 in loginDetails[i][1]: 
                    validUser == True 
                    print("Valid password") 
                    intro2(user1,user2) 
                    #returns username to use in playGame subroutine 
                    return user1 
                else: 
                    print("Invalid password") 
                    break 
            elif user1 not in loginDetails[i][0]: 
                validUser == False 
            if validUser == False: 
                print("invalid username") 
    #allows user to append username and password into 2d list 
                 
    elif choice == "2": 
        newUsername = input("Enter a new username: ") 
        loginDetails[2].append(newUsername) 
        newPassword = input("Enter a new password: ") 
        #makes sure password contains at least one number and letter; no special characters 
        import re 
        valid = re.match("[a-zA-Z]+[0-9]+", newPassword) 
        if valid: 
            print("That password is valid") 
            loginDetails[2].append(newPassword) 
            #intro1(user1) 
        else: 
            print("Sorry, your password must include at least 1 letter and at least 1 number") 
        intro1(user1) 
    else: 
        print("Invalid input") 
        
  
  
#authentication FOR PLAYER 2 
  
def intro2(user1,user2): 
    #same code as for intro1, but uses 'user2' 
    print("***PLAYER TWO***") 
    input("Press ENTER to continue...") 
    print("Welcome to the Dice Game. Please choose your option") 
    print("1. Sign in with your existing details") 
    print("2. Sign up with a username and password") 
    print("") 
    choice = input("Please choose a number: ") 
    if choice == "1": 
        user2 = input("Enter Username: ") 
        for i in range(len(loginDetails)): 
            if user2 in loginDetails[i][0]: 
                print("Valid username") 
                password2 = input("Enter Password: ") 
                if password2 in loginDetails[i][1]: 
                    validUser == True 
                    print("Valid password") 
                    ("You are now through to the dice game!") 
                    playGame(user1, user2) 
                    break 
                else: 
                    print("Invalid password") 
                    break 
            else: 
                validUser == False 
            if validUser == False: 
                print("invalid username") 
                 
    elif choice == "2": 
        newUsername = input("Enter a new username: ") 
        loginDetails[2].append(newUsername) 
        newPassword = input("Enter a new password: ") 
        import re 
        valid = re.match("[a-zA-Z]+[0-9]+", newPassword) 
        if valid: 
            print("That password is valid") 
            loginDetails[2].append(newPassword) 
            #intro2(user1,user2) 
        else: 
            print("Sorry, your password must include at least 1 letter and at least 1 number") 
        intro2(user1,user2) 
    else: 
        print("Invalid input") 
         
     
###MAIN CODE 
user1 = "user" 
user2 = "user2" 
intro1(user1) 

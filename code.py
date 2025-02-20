import random
def user_choice():
    user=input("Choose one: Rock / Paper / Scissors....  ").lower()
    while user not in ["rock","paper","scissors"]:
        print("Inavlid Choice:")
        user=input("Choose one: Rock / Paper / Scissors   ").lower()
    return user
def computer_choice():
    choices=["rock","paper","scissors"]
    return random.choice(choices)
def winner(user,computer):
    if user==computer:
        print("It is Tie! Both chose ",user)
    elif (user=="rock" and computer=="scissors" or
         user=="paper" and computer=="rock"    or
         user=="scissors" and computer=="paper"):
         print("You Win!",user.capitalize(),"beats",computer)
    else:
        print("Computer Win!",computer.capitalize(),"beats",user)
print("Welcome to Rock, Paper, Scissors Game!")
while True:
    user=user_choice()
    computer=computer_choice()
    print("Computer Chose:",computer.capitalize())
    winner(user,computer)

    play_again=input("Do you want to play again? (yes/no): ").lower()
    if play_again!="yes":
        print("Bye Bye")
        break
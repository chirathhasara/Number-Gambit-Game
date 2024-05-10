import random

def roll():
    roll=random.randint(1,6)
    return roll
while True:
    print()
    print("********* Welcome to Number Gambit Game **********")
    print()
    name=input("Please Enter Your Name:")
    print()
    print("welcome "+name+" to this game")
    print("the game rules are very simple you will get a chance to roll a die as much times as you want ")
    print("And each turn you will add the number that roll as your score")
    print("but if die turn in to 1 you will LOSE YOUR ALL SCORE")
    print("you can leave the game any time you want with your score")

    print()
    score=0
    play=input("Do you like to play this game ?(yes/no):")
    if play.lower()=="yes":
        while True:
            rolling=input("would you like to roll a die:(yes/no)")
            if rolling.lower()=="yes":
                value=roll()
                if value!=1:
                    score+=value
                    print("your score is="+str(score))
                    continue
                else:
                    print()
                    print("Oh! sorry "+name+" you roll 1 so you are out:")
                    break
            else:
                print()
                print("Oh you diside to leave the game!")
                print("your score is:"+str(score))
                break
                
                



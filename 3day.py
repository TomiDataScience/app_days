print("Welcome to Tresure Island. Your mission is to find the treasure the tresure.")
choice_left_right=input("What you choice left or right?")
if(choice_left_right=="left"):
    choice_swim_wait=input("What you choice swim or wait?")
    if(choice_swim_wait=="wait"):
        choice_door=input("What you choice blue, red or yellow?")
        if(choice_door=="yellow"):
            print("You found .the treasure. You won")
        elif(choice_door=="blue"):
            print("game over")
        elif(choice_door=="red"):
            print("game over")
    elif(choice_swim_wait=="swim"):
        print("game over")
elif(choice_left_right=="right"):
    print("game over")
    
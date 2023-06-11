import time
import random
Score = int(0)


def start():  # Game's Name
    print('"EVERYONE CAN"')
    name_and_age()


def name_and_age():  # Take info about user
    name = input("Enter your name")
    print(f"Welcome, {name}")
    age = input("Enter your age")
    crossing_river()
    return age and name


def crossing_river():  # Crossing river's scenario
    print("It's the evening")
    time.sleep(2)
    print("You are standing by the bank of the river")
    time.sleep(2)
    print("There are many trees along the river on both sides")
    time.sleep(2)
    print("You must cross the river....But!!")
    time.sleep(2)
    print("There is a beast overthere...in the river...ohh")
    time.sleep(2)
    print("You have a lifejacket...small boat and a rope")
    time.sleep(1)
    print("what will You do?")
    time.sleep(1)
    print("1. Use the boat")
    time.sleep(0.5)
    print("2. Tie the rope between both sides and use it to cross")
    time.sleep(0.5)
    print("3. Wear the life jacket and swim")
    time.sleep(0.5)
    first_choice()


def first_choice():
    # first choice >> How to cross the river....every way has different results
    Score = 0
    Choice_1 = input("(please enter 1 or 2 or 3 )")
    if Choice_1.isdigit() is True and 1 <= int(Choice_1) <= 3:
        # check input type and value
        print("Good Job...You have crossed the river successfully")
        if int(Choice_1) == 1:  # using boat >>> +1
            print("The beast hit you")
            time.sleep(0.5)
            print("Don't worry...it's so small injury....not dangerous")
            Score = Score + 1
            print(f"Score = {Score}")
            dogs(Score)
        if int(Choice_1) == 2:  # using rope >>> +2
            print("You haven't been hurted")
            time.sleep(1)
            print("You work smart not hard")
            Score = Score + 2
            print(f"Score = {Score}")
            dogs(Score)
        if int(Choice_1) == 3:  # using life jacket >>> -1
            print("But..")
            time.sleep(0.5)
            print("AWW!!..You were hit badly by the beast")
            Score = Score - 1
            print(f"Score = {Score}")
            time.sleep(0.5)
            sec_choice(Score)  # taking medicine or not
    else:
        print("foo...")
        time.sleep(1)
        first_choice()  # repeat taking input if it's not suitable


def sec_choice(Sco):  # medicine Function
    print("You should take medicine")
    print("1. Take")
    print("2. Not take")
    choice_2 = input("(please enter 1 or 2)")
    if choice_2.isdigit() is True and 1 <= int(choice_2) <= 2:
        # check input type and value
        if int(choice_2) == 1:
            Score_2 = Sco + 1  # taking >>>> +1
            print(f"Score = {Score_2}")
            dogs(Score_2)
        else:
            Score_2 = Sco - 1  # taking >>>> -1
            print(f"Score = {Score_2}")
            dogs(Score_2)
    else:
        print("foo...")
        time.sleep(1)
        sec_choice()  # repeat taking input if it's not suitable


def dogs(Sco):  # Dogs scenario after crossing the river
    print("Look out!!")
    time.sleep(1)
    print("You stepped on a dead dog")
    time.sleep(1)
    print("You hear this??!!!!")
    time.sleep(1)
    print("ohh!!...A flock of wild dogs running towards you")
    time.sleep(0.5)
    print("You must take action")
    time.sleep(1)
    print("what will you do ??")
    print("1. Run away")
    print("2. Face them")
    thi_choice(Sco)


def thi_choice(Sco):
    '''This Function>> do conditions according to
      user's input about dealing with dogs'''
    choice_3 = input("(please enter 1 or 2)")
    if choice_3.isdigit() is True and 1 <= int(choice_3) <= 2:
        # check input type and value
        if int(choice_3) == 1:
            Score_3 = Sco + 2  # running away >> +2
            print(f"Score = {Score_3}")
            print("Wahooo.....You did it!!")
            time.sleep(0.5)
            print("You escaped from them and survived!!")
            cave(Score_3)
        else:  # choices about dealing with dogs
            print("How will you get rid of them??")
            time.sleep(1)
            print("1. Scaring them with fire")
            print("2. Use your shootgun")
            print("3. Hit them with rocks")
            fou_choice(Sco)
    else:
        print("foo..")
        time.sleep(1)
        thi_choice(Sco)
# repeat taking input if it's not suitable


def fou_choice(Sco):
    # this function>>  give specific result to each deal with dogs
    choice_4 = input("(please enter 1 or 2 or 3)")
    if choice_4.isdigit() is True and 1 <= int(choice_4) <= 3:
        # check input type and value
        if int(choice_4) == 1:
            Score_4 = Sco + 2  # Using fire to scare dogs >> +2
            print(f"Score = {Score_4}")
            print("Great job!!..:)")
            time.sleep(1)
            print("You scared them....They ran away")
            cave(Score_4)
        if int(choice_4) == 2:
            Score_4 = Sco + 1
            # Using shootgun >> +1...#as the player gets injured
            print(f"Score = {Score_4}")
            print("Good job!!..:)")
            time.sleep(1)
            print("You killed three....but a dog hit you")
            time.sleep(0.5)
            cave(Score_4)
        if int(choice_4) == 3:
            Score_4 = Sco + 1  # Using rocks to hit dogs >> +1
            print(f"Score = {Score_4}")
            print("Good job!!..:)")
            time.sleep(1)
            print("The ran away.....You haven't been injured")
            cave(Score_4)
    else:
        print("foo...")
        fou_choice(Sco)  # repeat taking input if it's not suitable


def cave(Sco):  # Cave scenario after surviving from dogs
    print("Heeeyy....Look there!!")
    time.sleep(1)
    print("It's a cave")
    time.sleep(1)
    print("Go...and take some rest")
    time.sleep(1)
    print("Walk slowly..don't make noise")
    if int(random.choice(range(2))) == 1:  # Pick one event randomly
        Cubra(Sco)
    else:
        poisonous_insects(Sco)


def Cubra(Sco):  # cubra scenario
    print("ohh :O")
    time.sleep(1)
    print("It's a Cubraaa")
    time.sleep(1)
    print("You must do something")
    time.sleep(1)
    Cubra_choice(Sco)


def Cubra_choice(Sco):  # Cubra actions
    print("1. Scare it with fire")
    print("2. Shoot it with the shoot gun")
    print("3. Try to sink it with water")
    choice_5 = input("(please enter 1 or 2 or 3)")
    if choice_5.isdigit() is True and 1 <= int(choice_5) <= 3:
        if int(choice_5) == 1:
            Score_5 = Sco + 1
            print(f"Score = {Score_5}")
            print("Snakes don't get scared from fire")
            time.sleep(1)
            print("Cubra bit you")
            print("You are dead")
            time.sleep(1)
            print("Game Over")
            # Game over as Snakes don't get scared from fire
            restart()  # restart the game
        if int(choice_5) == 2:
            Score_5 = Sco + 2  # shootgun kills Cubra
            print(f"Score = {Score_5}")
            print("Good Job")
            print("You killed the Cubra")
            cave_2(Score_5)
        if int(choice_5) == 3:
            Score_5 = Sco - 2
            print("YOU ARE DUMB")
            print("It's still alive")
            time.sleep(1)
            print("Cubra bit you")
            print("You are dead")
            time.sleep(1)
            print("Game Over")
            # Water can't sink Cubra or affect it...so game over
            restart()  # restart the game
    else:
        print("foo...")
        Cubra_choice(Sco)


def poisonous_insects(Sco):  # poisonous insects scenario
    print("ohh :O")
    time.sleep(1)
    print("There're a Poisonous Insects")
    time.sleep(1)
    print("You must do something")
    time.sleep(1)
    insects_choice(Sco)


def insects_choice(Sco):  # poisonous insects actions
    print("1. Put them on fire")
    print("2. Toxic gas")
    print("3. Try to sink them with water")
    choice_5 = input("(please enter 1 or 2 or 3)")
    if choice_5.isdigit() is True and 1 <= int(choice_5) <= 3:
        if int(choice_5) == 1:
            Score_5 = Sco + 2
            print(f"Score = {Score_5}")  # Put them on fire is killing them
            print("Fantastic!!")
            print("Good Job...You killed them and the rest escaped")
            time.sleep(1)
            cave_2(Score_5)
        if int(choice_5) == 2:  # toxic gas affect player more than insects
            Score_5 = Sco - 2
            print(f"Score = {Score_5}")
            print("SOO DUMB")
            print("You killed YOURSELF")
            time.sleep(1)
            print("GAME OVER")
            restart()
        if int(choice_5) == 3:  # sink them with water is killing them
            Score_5 = Sco + 2
            print("GOOD JOB")
            print("They died without hurting you")
            cave_2(Score_5)
    else:
        print("foo...")
        insects_choice(Sco)


def restart():  # restart the game
    restart_choice = input("(enter 1 to RESTART or 2 to END THE GAME)")
    if restart_choice.isdigit() is True and 1 <= int(restart_choice) <= 2:
        # check input's type and value
        if int(restart_choice) == 1:
            crossing_river()
        elif int(restart_choice) == 2:
            return
    else:
        print("foo...")
        restart()


def cave_2(Sco):
    # Scenario of what will happen after overcoming the insects or the cubra
    print("Eww....it was terrible")
    time.sleep(1)
    print("what you will do?")
    print("1. Stay till the morning")
    print("2. Leave the cave now")
    six_choice(Sco)


def six_choice(Sco):
    # make decision to leave the cave or not
    choice_6 = input("(please enter 1 or 2)")
    if choice_6.isdigit() is True and 1 <= int(choice_6) <= 2:
        # check input's type and value
        if int(choice_6) == 1:
            finding_house(Sco)
        if int(choice_6) == 2:
            leaving_cave(Sco)
    else:
        print("foo...")
        six_choice(Sco)


def leaving_cave(Sco):  # leaving cave scenario
    print("It's still dark")
    time.sleep(1)
    print("Look out where you walk")
    time.sleep(1)
    print("Oww :O")
    random.choice(range(3))  # randomly the user face an animal form 3 animals
    if int(random.choice(range(3))) == 0:
        bear(Sco)
    if int(random.choice(range(3))) == 1:
        lion(Sco)
    if int(random.choice(range(3))) == 2:
        gorilla(Sco)
    else:
        pass


def bear(Sco):  # facing bear scenario
    print("It's Beeeaarrr")
    time.sleep(1)
    print("It was better to stay until the morning")
    time.sleep(1)
    print("what you will do??")
    time.sleep(1)
    print("1. Hit his face with a the knife")
    print("2. Inject him with toxic liquid")
    print("3. Burn him")
    bear_choice(Sco)


def bear_choice(Sco):  # Actions against the bear
    choice_7 = input("(please enter 1 or 2 or 3)")
    if choice_7.isdigit() is True and 1 <= int(choice_7) <= 3:
        # check input's type and value
        if int(choice_7) == 1:
            Score_7 = Sco + 1
            print(f"Score = {Score_7}")
            print("Good job")
            time.sleep(1)
            print("You hit him")
            finding_house(Score_7)
        if int(choice_7) == 2:
            Score_7 = Sco + 1
            print(f"Score = {Score_7}")
            print("Good job")
            time.sleep(1)
            print("He's dead")
            finding_house(Score_7)
        if int(choice_7) == 3:
            Score_7 = Sco + 2
            print(f"Score = {Score_7}")
            print("Great job")
            time.sleep(1)
            print("He's on fire now")
            finding_house(Score_7)
    else:
        print("foo...")
        bear_choice(Sco)


def gorilla(Sco):  # facing gorilla scenario
    print("It's goorilla")
    time.sleep(1)
    print("It was better to stay until the morning")
    time.sleep(1)
    print("what you will do??")
    time.sleep(1)
    print("1. Hit it face with a the knife")
    print("2. Inject it with toxic liquid")
    print("3. Burn it")
    gorilla_choice(Sco)


def gorilla_choice(Sco):  # Actions against the gorilla
    choice_7 = input("(please enter 1 or 2 or 3)")
    if choice_7.isdigit() is True and 1 <= int(choice_7) <= 3:
        # check input's type and value
        if int(choice_7) == 1:
            Score_7 = Sco + 1
            print(f"Score = {Score_7}")
            print("Good job")
            time.sleep(1)
            print("You hit it")
            finding_house(Score_7)
        if int(choice_7) == 2:
            Score_7 = Sco + 1
            print(f"Score = {Score_7}")
            print("Good job")
            time.sleep(1)
            print("It's dead")
            finding_house(Score_7)
        if int(choice_7) == 3:
            Score_7 = Sco + 2
            print(f"Score = {Score_7}")
            print("Great job")
            time.sleep(1)
            print("It's on fire now")
            finding_house(Score_7)
    else:
        print("foo...")
        gorilla_choice(Sco)


def lion(Sco):  # facing lion scenario
    print("It's lion")
    time.sleep(1)
    print("It was better to stay until the morning")
    time.sleep(1)
    print("what you will do??")
    time.sleep(1)
    print("1. Hit him with a the knife")
    print("2. Inject him with toxic liquid")
    print("3. Burn him")
    lion_choice(Sco)


def lion_choice(Sco):
    # Actions against the lion
    choice_7 = input("(please enter 1 or 2 or 3)")
    if choice_7.isdigit() is True and 1 <= int(choice_7) <= 3:
        # check input's type and value
        if int(choice_7) == 1:
            Score_7 = Sco
            print(f"Score = {Score_7}")
            print("Are you dumb??!")
            time.sleep(1)
            print("The lion killed you")
            print("Game Over")
            restart()
        if int(choice_7) == 2:
            Score_7 = Sco + 1
            print(f"Score = {Score_7}")
            print("Good job")
            time.sleep(1)
            print("It's dead")
            finding_house(Score_7)
        if int(choice_7) == 3:
            Score_7 = Sco + 2
            print(f"Score = {Score_7}")
            print("Great job")
            time.sleep(1)
            print("It's on fire now")
            finding_house(Score_7)
    else:
        print("foo...")
        lion_choice(Sco)


def finding_house(Sco):  # Finding house scenario
    print("The sun is overthere")
    time.sleep(1)
    print("It's about 5 am")
    time.sleep(1)
    print("You see this ??!")
    time.sleep(1)
    print("It's a house")
    time.sleep(1)
    print("Go discover it....")
    time.sleep(1)
    print("Take some rest and food")
    time.sleep(1)
    print("Knock...Knock")
    enter_house(Sco)


def enter_house(Sco):  # Entering house scenario
    print("You entered")
    time.sleep(1)
    print("Ohh..:O")
    time.sleep(1)
    print("There're three rooms")
    time.sleep(1)
    print("Which room will you enter?")
    time.sleep(1)
    print("1. Room 1")
    print("2. Room 2")
    print("3. Room 3")
    choosing_room(Sco)


def choosing_room(Sco):  # Choosing which room will be entered
    choice_8 = input("(please enter 1 or 2 or 3)")
    if choice_8.isdigit() is True and 1 <= int(choice_8) <= 3:
        # check input's type and value
        if int(choice_8) == 1:
            room_1(Sco)
        if int(choice_8) == 2:
            room_2(Sco)
        if int(choice_8) == 3:
            room_3(Sco)
    else:
        print("foo...")
        choosing_room(Sco)


def room_1(Sco):  # Entering room1 scenario
    print("ohh...terrible")
    time.sleep(1)
    print("It's on fire")
    time.sleep(1)
    print("But there is a dinner on that table there")
    time.sleep(1)
    print("Chicken Dinner")
    time.sleep(1)
    print("What will you do ??")
    time.sleep(1)
    print("1. Put out the fire and have the chicken dinner")
    print("2. Skip this room and enter room 2")
    room_1_choice(Sco)


def room_1_choice(Sco):  # actions in room1
    choice_9 = input("(please enter 1 or 2)")
    if choice_9.isdigit() is True and 1 <= int(choice_9) <= 2:
        # check input's type and value
        if int(choice_9) == 1:
            Score_9 = Sco + 2
            print(f"Score = {Score_9}")
            print("Good Job")
            time.sleep(1)
            print("You deserve this meal")
            time.sleep(1)
            print("Let's enter room 2")
            room_2(Score_9)
        if int(choice_9) == 2:
            Score_9 = Sco - 1
            print(f"Score = {Score_9}")
            room_2(Score_9)


def room_2(Sco):  # Entering room2 scenario
    print("YOHOO  :)")
    time.sleep(1)
    print("It's a bed")
    time.sleep(1)
    print("You need some rest")
    time.sleep(1)
    print("But there is a tiger sleeping on the bed")
    time.sleep(1)
    print("You should get rid of it to sleep")
    time.sleep(1)
    print("What will you do ??")
    time.sleep(1)
    print("1. Headshot with your Shoot gun")
    print("2. Skip this room and enter room 3")
    room_2_choice(Sco)


def room_2_choice(Sco):
    # actions in room2
    choice_10 = input("(please enter 1 or 2)")
    if choice_10.isdigit() is True and 1 <= int(choice_10) <= 2:
        # check input's type and value
        if int(choice_10) == 1:
            Score_10 = Sco + 2
            print(f"Score = {Score_10}")
            print("Good Job")
            time.sleep(1)
            print("You deserve this nap")
            time.sleep(1)
            print("Wake up....you've slept well")
            time.sleep(1)
            print("Let's enter room 3")
            room_2(Score_10)
        if int(choice_10) == 2:
            Score_10 = Sco
            print(f"Score = {Score_10}")
            time.sleep(1)
            print("The tiger attacked you while you were leaving the room")
            time.sleep(1)
            print("You Are Dead")
            time.sleep(1)
            print("Game Over")
            restart()


def room_3(Sco):  # Entering room3 scenario
    print("ohh...look there")
    time.sleep(1)
    print("It's  a door")
    time.sleep(1)
    print("It can be the end of this journey")
    time.sleep(1)
    print("How will you open it")
    time.sleep(1)
    print("1. Push the door")
    print("2. Pull the door")
    room_3_choice(Sco)


def room_3_choice(Sco):
    # actions in room3
    choice_11 = input("(please enter 1 or 2)")
    if choice_11.isdigit() is True and 1 <= int(choice_11) <= 2:
        # check input's type and value
        if int(choice_11) == 1:
            Score_11 = Sco + 2
            print(f"Score = {Score_11}")
            time.sleep(1)
            print("It's level 2")
            time.sleep(1)
            print("Stay tuned for the update 2")
            check_win_or_not(Sco)
        if int(choice_11) == 2:
            Score_11 = Sco - 1
            print(f"Score = {Score_11}")
            print("A big stone fell on you")
            check_win_or_not(Score_11)


def check_win_or_not(Sco):
    # check score to make descision if winning or losing
    if int(Sco) >= 10:
        print(f"Score = {Sco}")
        print("Congrats!!")
        print("You won")
        restart()
    else:
        restart()


start()

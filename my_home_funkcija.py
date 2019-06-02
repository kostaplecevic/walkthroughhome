import random

def outside():
    result = 0
    place = "outside"
    while place == "outside":
        print("You are in front of the house")
        choice = input("Would you like to come in?\n")
        if choice == "no":
            input("Exiting program after Enter")
            place = "street"
            result = 0
        elif choice == "yes":
            result = 1
        return result
            

def hallway(result):
    while result == 1:
        print("You are in the hallway.")
        place = "hallway"
        place = ""
        choice = input("""Where do you wish to go?
kitchen?
living room?
first bedroom?
bathroom?
pantry?
outside\n""")
        if choice == "outside":
            result = 0
        elif choice == "kitchen":
            result = 2
        elif choice == "living room":
            result = 3
        elif choice == "first bedroom":
            result = 4
        elif choice == "bathroom":
            result = 5
        elif choice == "pantry":
            result = 6
        return result

def kitchen(result):
    while result == 2:
        print("You are in the kitchen")
        #print("There are", list_kitchen)
        choice = input("Would you like to do something?\n")
        while choice == "yes":
            kitchen_action = int(input("""what would you like to do?
1 Turn the owen on?
2 Open the fridge?
3 Wash the dishes?
4 Put a plate in the dishwasher?
0 Go back to doing nothing?\n"""))
            choice_kitchen = "yes"
            while kitchen_action == 1:
                print("You turned on the owen. Pitty you don't know how to cook :P")
                input("Don't forget to turn it off :P\n")
                kitchen_action = ""
            while kitchen_action == 2:
                print("You opened the fridge")
                fridge_luck = random.randint(1,2)
                if fridge_luck == 1:
                    print("You have food! You eat it.\n")
                    input("Čvarci gooooood :3")
                    kitchen_action = ""
                elif fridge_luck == 2:
                    print("There's no food!\n")
                    input("Your tummy aches :(")
                    kitchen_action = ""
            while kitchen_action == 3:
                dishes_choice = input("Do you really want to wash the dishes? XD\n")
                if dishes_choice == "yes":
                    print("You are crazy! You have a dishwasher you brainiac!")
                    kitchen_action = ""
                    input("Come on, you will do better")
                elif dishes_choice == "no":
                    print("You are a smart one. The dishwasher is next to you and you acctually noticed it.")
                    kitchen_action = ""
                    input("Keep going like that!")
            while kitchen_action == 4:
                print("You are a reasonable one. Use the machines GOD gave us!")
                kitchen_action = ""
                input("I think I like you")
            if kitchen_action == 0:
                input("To cool for the kitchen,huh?")
                result = 1
                return result

def living_room(result):
    while result == 3:
        print("You are in the living room")
        #print("There are", list_living_room)
        choice = input("Would you like to do something?\n")
        while choice == "yes":
            living_room_action = int(input("""what would you like to do?
1 Sit at the table?
2 Take a book?
3 Sit on the sofa?
4 Watch TV?
0 Go back to doing nothing?\n"""))
            choice = "yes"
            while living_room_action == 1:
                print("You are sitting at the table.")
                input("What do you want to do next?\n")
                living_room_action = ""
            while living_room_action == 2:
                print("You go to the shelf.")
                book_choice = input("""Which book would you like?
1 Lord of the Rings
2 One Hundred Years of Solitude
3 The Last Werewolf
4 The Last Ringbearer
5 I don't want to read a book\n""")
                if book_choice == "1":
                    print("You have chosen Lord of the Rings!\n")
                    lotr_choice = input("Would you like to know more about the book?\n")
                    if lotr_choice == "yes":
                        print("""The Lord of the Rings is an epic high-fantasy novel written by English author J. R. R. Tolkien.
The story began as a sequel to Tolkien's 1937 fantasy novel The Hobbit, but eventually developed into a much larger work.
Written in stages between 1937 and 1949, The Lord of the Rings is one of the best-selling novels ever written,
with over 150 million copies sold.""")
                        input("Press Enter")
                    elif lotr_choice == "no":
                        input("Press Enter")
                        book_choice = ""
                elif book_choice == "2":
                    print("You have chosen One Hundred Years of Solitude!\n")
                    hundred_years_choice = input("Would you like to know more about the book?\n")
                    if hundred_years_choice == "yes":
                        print("""One Hundred Years of Solitude
(Spanish: Cien años de soledad, American Spanish: [sjen ˈaɲoz ðe soleˈðað])
is a landmark 1967 novel by Colombian author Gabriel García Márquez that tells the multi-generational story of the Buendía family,
whose patriarch, José Arcadio Buendía, founds the town of Macondo, the metaphoric Colombia.""")
                    elif hundred_years_choice == "no":
                        input("Press Enter")
                elif book_choice == "3":
                    print("You have chosen The Last Werewolf!\n")
                    werewolf_choice = input("Would you like to know more about the book?\n")
                    if werewolf_choice == "yes":
                        print("""The Last Werewolf trilogy (sometimes alternatively called The Bloodlines Trilogy)
is a Supernatural Horror series written by contemporary author Glen Duncan. The first novel follows the titular Last Werewolf,
Jake, as he counts down to his expected death.""")
                    elif werewolf_choice == "no":
                        input("Press Enter")
                elif book_choice == "4":
                    print("You have chosen The Last Ringbearer!")
                    ringbearer_choice = input("Would you like to know more about the book?\n")
                    if ringbearer_choice == "yes":
                        print("""The Last Ringbearer (Russian: Последний кольценосец) is a 1999 fantasy book by
Russian author Kirill Eskov. It is an alternative account of, and an informal sequel to, the events of
J.R.R. Tolkien's The Lord of the Rings from the viewing point of Mordor and its allies.""")
                    elif ringbearer_choice == "no":
                        print("Press Enter")
                elif book_choice == 5:
                    print("I don't like you cause you don't like books!")
                living_room_action = ""
            while living_room_action == 3:
                print("You chose to relax yourself and sit on the sofa")
                input("You might wanna turn the TV on or something like that.")
                living_room_action = ""
            while living_room_action == 4:
                print("You chose to watch the TV!")
                tv_choice = input("""What would you like to watch?
1 Sports
2 A documentary
3 Cartoons
4 A Sitcom
5 A good movie
6 Turn the TV off
>>>""")
                while tv_choice == "1":
                    print("Sports fan,huh?")
                    sport_choice = input("""Which sport do you prefer?
1 Football
2 Basketball
3 Tennis
4 American Football
5 Athletics
6 I've changed my mind
>>>""")
                    if sport_choice == "1":
                        print("You chose football \o/")
                        mufc_choice = input("Which football club do you like the most?\n")
                        if mufc_choice == "manchester united":
                            print("You're awesome!")
                            input("I like you")
                        elif mufc_choice == "manchester city":
                            print("You disgust me!")
                            input("How could you like a lowborn club like that?...")
                        elif mufc_choice == "liverpool":
                            print("Not a bad choice, indeed")
                            input("But we all know who's the better team in the north :3")
                    elif sport_choice == "2":
                        print("You chose basketball!")
                        input("I don't like it very much though.")
                    elif sport_choice == "3":
                        print("You chose tennis!")
                        input("A healthy dose of Nole never hurts")
                    elif sport_choice == "4":
                        print("You chose american football!")
                        input("No, it's not same as rugby...")
                    elif sport_choice == "5":
                        print("You chose athletics!")
                        choice_athletics = input("Which discipline do you like the most?\n")
                        if choice_athletics == "marathon":
                            input("I used to be pretty good at that :(")
                        else:
                            print("Good for you/n")
                    elif sport_choice == "6":
                        print("Fed up wth sports?")
                        input("Very well...")
                        sport_choice = ""
                        tv_choice = ""
                while tv_choice == "2":
                    print("I bet you changed to History, National Geographic or Discovery.")
                    input("Press Enter if you had enogh")
                    tv_choice = ""
                while tv_choice == "3":
                    print("You have chosen cartoons!")
                    tv_choice = ""
                    input("Some of my favorite ones are SpongeBob, Gumball")
                while tv_choice == "4":
                    print("You have chosen a Sitcom")
                    input("What's your favorite one?")
                    tv_choice= ""
                    input("I don't really care. I was just trying to be polite :P")
                while tv_choice == "5":
                    print("A good movie?")
                    genre_choice = input("What genre?")
                    if genre_choice == "horror" or "sci-fi" or "adventure":
                        print("You're my kind of man! Or girl!")
                        tv_choice = ""
                    else:
                        print("Any movie is a good movie.")
                        tv_choice = ""
                while tv_choice == "6":
                    input("Yep, TV is bad for your eyes")
                    tv_choice = ""
                living_room_action = ""
            if living_room_action == 0:
                input("Going back to the hallway, huh?")
                result = 1
                return result

def first_bedroom(result):
    while result == 4:
        print("You are in first bedroom")
        while result == 4:
            choice = int(input("""What would you like to do?
0 Go to the hallway
1 Sleep
2 Watch TV
3 Change clothes
4 Read a book
5 Go to the computer room\n"""))
            while choice == 1:
                print("I don't like to sleep during the day, or during the night")
                choice = ""
                input("But you chose when you go to sleep, just like me")
            while choice == 2:
                print("You chose to watch the TV!")
                tv_choice = input("""What would you like to watch?
1 Sports
2 A documentary
3 Cartoons
4 A Sitcom
5 A good movie
6 Turn the TV off
>>>""")
                while tv_choice == "1":
                        print("Sports fan,huh?")
                        sport_choice = input("""Which sport do you prefer?
1 Football
2 Basketball
3 Tennis
4 American Football
5 Athletics
6 I've changed my mind
>>>""")
                        if sport_choice == "1":
                            print("You chose football \o/")
                            mufc_choice = input("Which football club do you like the most?")
                            if mufc_choice == "manchester united":
                                print("You're awesome!")
                                input("I like you")
                            elif mufc_choice == "manchester city":
                                print("You disgust me!")
                                input("How could you like a lowborn club like that?...")
                            elif mufc_choice == "liverpool":
                                print("Not a bad choice, indeed")
                                input("But we all know who's the better team in the north :3")
                        elif sport_choice == "2":
                            print("You chose basketball!")
                            input("I don't like it very much though.")
                        elif sport_choice == "3":
                            print("You chose tennis!")
                            input("A healthy dose of Nole never hurts")
                        elif sport_choice == "4":
                            print("You chose american football!")
                            input("No, it's not same as rugby...")
                        elif sport_choice == "5":
                            print("You chose athletics!")
                            choice_athletics = input("Which discipline do you like the most?")
                            if choice_athletics == "marathon":
                                input("I used to be pretty good at that :(")
                            else:
                                print("Good for you/n")
                        elif sport_choice == "6":
                            print("Fed up wth sports?")
                            input("Very well...")
                            sport_choice = ""
                            tv_choice = ""
                while tv_choice == "2":
                        print("I bet you changed to History, National Geographic or Discovery.")
                        input("Press Enter if you had enogh")
                while tv_choice == "3":
                        print("You have chosen cartoons!")
                        tv_choice = ""
                        input("Some of my favorite ones are SpongeBob, Gumball")
                while tv_choice == "4":
                        print("You have chosen a Sitcom")
                        input("What's your favorite one?")
                        tv_choice= ""
                        input("I don't really care. I was just trying to be polite :P")
                while tv_choice == "5":
                        print("A good movie?")
                        genre_choice = input("What genre?")
                        if genre_choice == "horror" or "sci-fi" or "adventure":
                            print("You're my kind of man! Or girl!")
                            tv_choice = ""
                        else:
                            print("Any movie is a good movie.")
                            tv_choice = ""
                while tv_choice == "6":
                        input("Yep, TV is bad for your eyes")
                        tv_choice = ""
                        choice = ""
            while choice == 3:
                print("You want different clothes?")
                weather_choice = random.randrange(1,5)
                choice = ""
                if weather_choice == 1:
                    print("It's cold outside, take something warm")
                    input("Like this jacket and sweater")
                elif weather_choice == 2:
                    print("It's raining outside :(")
                    input("It's a rainy day, hallelujah! Well, not really a big yeeeey...")
                elif weather_choice == 3:
                    print("It's snowing! Take a warm coat, some boots and a few layers before going outside!")
                    input("Maybe put a snowball in someones mouth :3")
                elif weather_choice == 4:
                    print("It's the peak of the summer! It's so hot it feels like your skin might melt off!")
                    input("Be good and put some light clothes on")
                elif weather_choice == 5:
                    print("It's warm, but very cloudy though.")
                    input("Maybe take something light on you, and bring a raincoat and an umbrella with you")
            while choice == 4:
                print("You go to the shelf.")
                book_choice = input("""Which book would you like?
1 Lord of the Rings
2 One Hundred Years of Solitude
3 The Last Werewolf
4 The Last Ringbearer
5 I don't want to read a book\n""")
                if book_choice == "1":
                    print("You have chosen Lord of the Rings!\n")
                    lotr_choice = input("Would you like to know more about the book?\n")
                    if lotr_choice == "yes":
                        print("""The Lord of the Rings is an epic high-fantasy novel written by English author J. R. R. Tolkien.
The story began as a sequel to Tolkien's 1937 fantasy novel The Hobbit, but eventually developed into a much larger work.
Written in stages between 1937 and 1949, The Lord of the Rings is one of the best-selling novels ever written,
with over 150 million copies sold.""")
                        input("Press Enter")
                    elif lotr_choice == "no":
                        input("Press Enter")
                        book_choice = ""
                elif book_choice == "2":
                    print("You have chosen One Hundred Years of Solitude!\n")
                    hundred_years_choice = input("Would you like to know more about the book?\n")
                    if hundred_years_choice == "yes":
                        print("""One Hundred Years of Solitude
(Spanish: Cien años de soledad, American Spanish: [sjen ˈaɲoz ðe soleˈðað])
is a landmark 1967 novel by Colombian author Gabriel García Márquez that tells the multi-generational story of the Buendía family,
whose patriarch, José Arcadio Buendía, founds the town of Macondo, the metaphoric Colombia.""")
                    elif hundred_years_choice == "no":
                        input("Press Enter")
                elif book_choice == "3":
                    print("You have chosen The Last Werewolf!\n")
                    werewolf_choice = input("Would you like to know more about the book?\n")
                    if werewolf_choice == "yes":
                        print("""The Last Werewolf trilogy (sometimes alternatively called The Bloodlines Trilogy)
is a Supernatural Horror series written by contemporary author Glen Duncan. The first novel follows the titular Last Werewolf,
Jake, as he counts down to his expected death.""")
                    elif werewolf_choice == "no":
                        input("Press Enter")
                elif book_choice == "4":
                    print("You have chosen The Last Ringbearer!")
                    ringbearer_choice = input("Would you like to know more about the book?\n")
                    if ringbearer_choice == "yes":
                        print("""The Last Ringbearer (Russian: Последний кольценосец) is a 1999 fantasy book by
Russian author Kirill Eskov. It is an alternative account of, and an informal sequel to, the events of
J.R.R. Tolkien's The Lord of the Rings from the viewing point of Mordor and its allies.""")
                    if ringbearer_choice == "no":
                        print("Press Enter")
                elif book_choice == 5:
                    print("I don't like you cause you don't like books!")
                    book_choice = ""
                choice = " "
            while choice == 5:
                print("You chose to go to the computer room! Gaming time! \o/")
                comproom_choice = input("""I'm guessing that you want to turn the computer on, but let me ask you what you want anyway.
0 Go back to first bedroom
1 Turn on the computer
2 Take clothes from the cupboard\n""")
                if comproom_choice == "0":
                    print("Don't want to play games?")
                    input("You can do other stuff there.")
                    choice = ""
                elif comproom_choice == "2":
                    print("Aren't all the clothes back in bedroom?")
                    input("If you want em,go get em!")
                while comproom_choice == "1":
                    print("You turn on the computer")
                    computer_choice = input("""What do you want to do?
0 Turn off the computer
1 Play games
2 Go to the internet
3 Watch a movie
4 Do school stuff\n""")
                    while computer_choice == "0":
                        print("Turning off the comuter?")
                        comproom_choice = ""
                        computer_choice = ""
                        input("Well, go do something outside maybe?")
                    while computer_choice == "1":
                        print("Game time! \o/")
                        game_choice = input("""Play more or stop?
1 I want to play more
0 I don't want to play games\n""")
                        if game_choice == "0":
                            print("you're not a game lover")
                            computer_choice = ""
                            input("Not like me anyway")
                        elif game_choice == "1":
                            print("Games all you want :3")
                    while computer_choice == "2":
                        print("Google knows everything!")
                        input("But so does your girlfriend,if you have one")
                        computer_choice = ""
                    while computer_choice == "3":
                        print("Oh! Oh! A movie fan!")
                        input("Have fun whatever you decide to watch")
                        computer_choice = ""
                    while computer_choice == "4":
                        print("Something boring, it has to be...")
                        input("Math or physics, they make me puke")
                        computer_choice = ""
            while choice == 0:
                result = 1
                input("Back to the hallway")
                return result

def bathroom(result):
    while result == 5:
        print("You are in the bathroom!")
        while result == 5:
            choice  = int(input("""What would you like to do? XD
0 Go back to the hallway
1 Wash your hands
2 Wash your face
3 Brush your teeth
4 Take a shower
5 Take a number 1
6 Take a number 2
"""))
            if choice == 0:
                print("Finished with what you got,huh? :P")
                result = 1
                input("Back to the hallway")
                return result
            elif choice == 1:
                print("You open the tap and start washing")
                input("Squeky clean :3")
            elif choice == 2:
                print("It's probably morning, and your disoriented af")
                input("But it's part of your morning routine")
            elif choice == 3:
                print("You take your brush and toothpaste and start scrubing")
                input("Over and under and that stuff, they say it should last five minutes ")
            elif choice == 4:
                print("Did you bring a towel?")
                input("So cleeeean :3")
            elif choice == 5:
                print("Well, no need to say anything about this XD")
                input("Basic physiological need number 1")
            elif choice == 6:
                print("Well, no need to say anything about this XD")
                input("Basic physiological need number 2")

def pantry(result):
    while result == 6:
        print("You are in the pantry")
        pantry_choice = input("""Contents are always changing, so you can:
0 Close the door
1 Stay looking inside and take what you need\n""")
        while pantry_choice == "1":
            in_pantry = input("Found what you were looking for?\n")
            if in_pantry == "yes":
                input("I guess you're going back to the hallway now\n")
                pantry_choice = ""
                result = 1
                return result
            else:
                print("Sorry, keep looking")
        while pantry_choice == "0":
            result = 1
            return result
            input("Going back to the hallway")

def main():
    position = 0
    program = "active"
    while program == "active":
        if position == 0:
            position = outside()
            if position == 0:
                input("Goodbye :(")
                program = "inactive"
        elif position == 1:
            position = hallway(position)
        elif position == 2:
            position = kitchen(position)
        elif position == 3:
            position = living_room(position)
        elif position == 4:
            position = first_bedroom(position)
        elif position == 5:
            position = bathroom(position)
        elif position == 6:
            position = pantry(position)

main()

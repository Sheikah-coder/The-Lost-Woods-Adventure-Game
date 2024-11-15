##############################################################################################################################################################
# Sheikah-coder
# The Lost Woods Adventure Game
# 1. Initialize key, gatekeeping, and inventory item variables.
# 2. Introduce the player to the story.
# 3. Ask the player to decide between three pathways.
# 4. Branch into different scenarios for each path, validating their input. 
# 5. If the player chooses the 'left' path (moderate difficulty):
# 6. Completing a number guessing game rewards a key.
# 7. Unlike the other paths, there are options to return to previous encounters.
# 8. Obtaining two keys rewards a weapon and ends the game.
# 9. If the player chooses the 'right' path (easy difficulty):
# 10. Two new inventory items are obtainable.
# 11. Obtaining one key rewards a spellbook and ends the game.
# 12. If the player chooses the 'forward' path (hard difficulty):
# 13. Completing a riddle guessing game rewards a key.
# 14. A trap chest teleports the player back to path selection if opened.
# 15. Obtaining two keys rewards a treasure room and ends the game.
# 16. If the player does not have the key(s) to open a treasure chest and continues on a path,
#     they will get lost and be returned to path selection (retain inventory). 
##############################################################################################################################################################
# Initialize key variables.
key_1_left = 0
key_2_left = 0
keys_left = 0
key_right = 0
key_forward = 0

# Initialize gatekeeping variables.
raccoon_choice = 0 # Store decision of raccoon encounter. 
owl_choice = 0 # Store decision of owl encounter.
start_over = 0 # Use in condition to return to the path selection.
raccoon_return = 0 # Use in condition to return to the raccoon encounter.
owl_return = 0 # Use in condition to return to the owl encounter.
trap_chest_skip = 0 # Use in condition to skip the trap chest encounter if it has been opened before. 
path_choice = 0 # Use in condition to output original narration for the beginning of the story.
open_trap_chest = 0 # Use to output alternative narration for the beginning of the story. 
path_choice_return = 0 # Use in condition to bypass nested loops in order to return to the path selection.

# Initialize inventory item variables.
jewel = 0
bird_seed = 0

# Story introduction. Return to path selection if lost. 
while start_over == 0:
    
    # If first time.
    if path_choice == 0:
        print("You are a wandering explorer, hoping to encounter an interesting location that is safe to explore and even discover treasure if you're lucky.\n"
              "You happen to enter a dense, uncharted forest that seems uninhabited. Magical lights float about the trees, signaling that this is not an ordinary place,\n"
              "but they don't look ominous. So, you keep walking until you reach a clearing with three different paths.\n\n"
              "You must choose a path:\n")

    # If not first time.
    else:

        # If got lost.
        if open_trap_chest == 0:
            path_choice_return = 0
            print("You venture deeper into the forest, the path starts winding, and you become lost. Somehow, you end up all the way back to the clearing where you chose one of three paths.\n"
                  "Should you start on the same path and make different choices this time, or try a different path?\n\n"
                  "You must choose a path:\n")

        # If opened trap chest.
        else:
            path_choice_return = 0
            open_trap_chest = 0
            print("The light fades, revealing the clearing where you chose one of three paths. The chest must have been a trap that teleported you back here.\n"
                  "Should you start on the same path and make different choices this time, or try a different path?\n\n"
                  "You must choose a path:\n")
            
    # Choose a path.
    print("* Left: A narrow, overgrown path with many tree branches to move aside or break through.\n"
          "* Right: A spacious path with more sunlight filtering through the trees.\n"
          "* Forward: A darkened continuation of your current path where the magic lights turn dim.\n")
    path_choice = input("Enter one option: left / right / forward\n\n")
    print()

    # Validate choice.
    while path_choice not in ['left', 'right', 'forward']:
        print("Please enter a valid option.\n")
        path_choice = input("Enter one option: left / right / forward\n\n")
        print()

    # Branch into different scenarios for each path.

    # If left path.
    if path_choice == 'left':
        
        # First left path encounter. Allow to return to this encounter if skipped. 
        while raccoon_return == 0 and path_choice_return == 0:
            
            # If key/completion check passed.
            if key_1_left == 0:
                
                # If not returning.
                if raccoon_choice == 0:
                    print("You begin to work your way through the left path. After breaking or weaving your way through many tree branches, you notice a raccoon locked in a cage.\n"
                          "You must decide to free the raccoon or continue on the path.\n")
                    raccoon_choice = input("Enter one option: free raccoon / continue\n\n")
                    print()
            
                    # Validate choice.
                    while raccoon_choice not in ['free raccoon', 'continue']:
                        print("Please enter a valid option.\n")
                        raccoon_choice = input("Enter one option: free raccoon / continue\n\n")
                        print()

                # If returning.
                else:
                    owl_return = 0
                    print("You return to the raccoon locked in a cage.\n")
                    
                # If free raccoon.
                if raccoon_choice == 'free raccoon':
            
                    # Number guessing game. Asks for three numbers within the range of 1-3. Correct answer is: 231.
                    print("The lock on the cage requires a combination of three numbers in the range of 1-3.\n")

                    # Create list to store input numbers.
                    combination = [ ]
                    
                    # Initialize variable to count iterations. 
                    count = 0

                    # Condition. 
                    while count == 0:

                        # Makes 0-2 into a variable, to ask for input three times. 
                        for i in range(3):
                            print("Guess a number.")
                            num = int(input("Options: 1 / 2 / 3\n\n"))
                            print()

                            # Validate number.
                            while num not in range(1, 4):
                                print("Please enter a valid number.")
                                num = int(input("Options: 1 / 2 / 3\n\n"))
                                print()

                            # Increment while loop variable.     
                            count += 1

                            # Add input number to list. 
                            combination.append(num)
                            
                            if count == 3:

                                # If correct.
                                if combination == [2, 3, 1]:
                                    print("The lock clicks open, and you open the cage. The raccoon chitters in thanks and darts out, dropping a key behind it.\n"
                                          "You take the key, not sure if the raccoon intended to drop it.\n")
                                    key_1_left = 1
                                    break

                                # If incorrect.
                                else:
                                    
                                    # Try again?
                                    print("The lock does not to open. You must decide to try again or continue on the path.\n")
                                    lock_choice = input("Enter one option: try again / continue\n\n")
                            
                                    # Validate choice.
                                    while lock_choice not in ['try again', 'continue']:
                                        print("Please enter a valid option.\n")
                                        lock_choice = input("Enter one option: try again / continue\n\n")
                                        print()

                                    # If try again.    
                                    if lock_choice == 'try again':
                                        combination = [ ]
                                        count = 0
                                        print()
                                
                                    # If continue.
                                    else:
                                        print()
                                        break

            # Second left path encounter. Allow to return to this encounter if skipped.
            while owl_return == 0 and path_choice_return == 0:

                # If key/completion check passed.
                if key_2_left == 0:

                    # If not returning.
                    if owl_choice == 0:
                        print("You progress through the difficult path with significatn effort. After traversing a short distance, you behold the glowing, white spirit of a great horned owl\n"
                              "perched in a tree before you. It observes you in silence, undisturbed. You wonder what wisdom it has, being a timeless spirit.\n"
                              "You must decide to try and communicate with the forest spirit owl or continue on the path.\n")
                        owl_choice = input("Enter one option: speak to owl / continue\n\n")
                        print()

                        # Validate choice.
                        while owl_choice not in ['speak to owl', 'continue']:
                            print("Please enter a valid option.")
                            lock_choice = input("Enter one option: speak to owl / continue\n\n")
                            print()
                
                    # If returning.
                    else:
                        raccoon_return = 0
                        print("You return to the forest spirit owl.\n")
                        
                    # If speak to owl.
                    if owl_choice == 'speak to owl':

                        # If key/completion check passed.
                        if key_1_left == 1:
                            print("Before you can speak to the owl, the raccoon reappears, jumping down from a tree beside you. It talks to the owl in a chittering and purring language\n"
                                  "unknown to you and the owl hoots back in return. They understand each other. The owl drops a key on the ground and gestures for you to take it.\n"
                                  "They want to help, and you presume the raccoon had intentionally dropped the previous key. You thank them, take the key, and continue on the path.\n")
                            key_2_left = 1

                        # If key/completion check not passed.   
                        else:
                            print("You greet the owl with respect and begin to introduce yourself, but it shakes its head in confusion. The raccoon could help you communicate with the owl.\n"
                                  "You must decide to return and free the raccoon or continue on the path.\n")
                            raccoon_choice = input("Enter one option: free raccoon / continue\n\n")
                            print()

                            # Validate choice.
                            while raccoon_choice not in ['free raccoon', 'continue']:
                                print("Please enter a valid option.\n")
                                raccoon_choice = input("Enter one option: free raccoon / continue\n\n")
                                print()

                            # If free raccoon. 
                            if raccoon_choice == 'free raccoon':
                                owl_choice = 0
                                owl_return = 1
                                continue

                # Evaluate key inventory.
                if key_1_left == 1 and key_2_left == 1:
                    keys_left = 2
                elif key_1_left == 1 or key_2_left == 1:
                    keys_left = 1
                
                # Final left path encounter.

                # If both keys possessed.
                if keys_left == 2:
                    print("Not far past the owl, you find a locked treasure chest with two keyholes under a tree. You open it with two keys that fit and obtain a beautifully crafted bow and quiver of arrows.")
                    print("Happy with your new treasure, you leave the forest to seek out a new adventure.\n")
                    path_choice_return = 1
                    start_over = 1
                
                # If first obtainable key possessed.
                elif key_1_left == 1 and key_2_left == 0:
                    print("Not far past the owl, you find a locked treasure chest with two keyholes under a tree.\n"
                          "You only have one key that fits, so you must decide to return and speak to the owl or continue on the path.\n")
                    owl_choice = input("Enter one option: speak to owl / continue\n\n")
                    print()

                    # Validate choice.
                    while owl_choice not in ['speak to owl', 'continue']:
                            print("Please enter a valid option.\n")
                            owl_choice = input("Enter one option: speak to owl / continue\n\n")
                            print()

                    # If speak to owl.
                    if owl_choice == 'speak to owl':
                        raccoon_return = 1
                        continue

                    # If continue.
                    else:
                        path_choice_return = 1
                        owl_choice = 0
                        continue

                # If second obtainable key possessed.
                elif key_1_left == 0 and key_2_left == 1:
                    print("Not far past the owl, you find a locked treasure chest with two keyholes under a tree.\n"
                          "You only have one key that fits, so you must decide to return and free the raccoon or continue on the path.\n")
                    raccoon_choice = input("Enter one option: free raccoon / continue\n\n")
                    print()

                    # Validate choice.
                    while raccoon_choice not in ['free raccoon', 'continue']:
                        print("Please enter a valid option.\n")
                        raccoon_choice = input("Enter one option: free raccoon / continue\n\n")
                        print()

                    # If free raccoon.
                    if raccoon_choice == 'free raccoon':
                        owl_return = 1
                        continue

                    # If continue.
                    else:
                        path_choice_return = 1
                        raccoon_choice = 0
                        continue

                # If no keys possessed.   
                else:
                    print("Not far past the owl, you find a locked treasure chest with two keyholes under a tree.\n"
                          "You don't have any keys that fit, so you must decide to return to the raccoon and free it, return to the owl and speak to it, or continue on the path.\n")
                    raccoon_owl_choice = input("Enter one option: free raccoon / speak to owl / continue\n\n")
                    print()

                    # Validate choice.
                    while raccoon_owl_choice not in ['free raccoon', 'speak to owl', 'continue']:
                        print("Please enter a valid option.\n")
                        racoon_owl_choice = input("Enter one option: free raccoon / speak to owl / continue\n\n")
                        print()
                    
                    # If free raccoon.
                    if raccoon_owl_choice == 'free raccoon':
                        raccoon_choice = 'free raccoon'
                        owl_choice = 0
                        owl_return = 1
                        continue
                    
                    # If speak to owl.
                    elif raccoon_owl_choice == 'speak to owl':
                        owl_choice = 'speak to owl'
                        raccoon_return = 1
                        continue

                    # If continue.
                    else:
                        path_choice_return = 1
                        raccoon_choice = 0
                        owl_choice = 0
                        continue
                        
    # If right path.
    elif path_choice == 'right':
        while path_choice_return == 0:

            # First right path encounter.
            
            # If jewel not possessed or bird seed possessed.
            if jewel == 0 or bird_seed == 1:
                print("You wander down the right path with no plain challenges. The scenery, clear and vivid in the lighting, brightens your mood.\n"
                      "After a pleasant stroll, you see an enchanting forest garden ahead. Highlights of a few vibrant flowers are scattered among the green shrubs and plants.\n"
                      "The glowing lights are flittering about, and when you move closer you can see that they are fairies playing tag. They look friendly enough to talk to.\n"
                      "You must decide to talk to the fairies or continue on the path.\n")                                          
                fairies_choice = input("Enter one option: talk to fairies / continue\n\n")
                print()

                #Validate choice.
                while fairies_choice not in ['talk to fairies', 'continue']:
                    print("Please enter a valid option.\n")
                    fairies_choice = input("Enter one option: talk to fairies / continue\n\n")
                    print()
                        
                # If talk to fairies.
                if fairies_choice == 'talk to fairies':

                    # If bird seed not possessed.
                    if bird_seed == 0:
                        print("You approach the fairies without moving too fast or slow, hoping you will not startle them. One by one, they sense your presence and flutter around you in curiosity.\n"
                              "You give a polite greeting and introduce yourself as an explorer. A blue-lit fairy hovers in front of you and says something, but her voice is too tiny to hear.\n"
                              "You are surprised when she offers you a red, pocket-sized jewel. Considering that it might prove useful, you accept the gift by holding out your hand.\n"
                              "The fairies are quick to lose interest and resume their game of tag.\n")
                        jewel = 1

                    # If bird seed possessed.
                    else:
                        print("You approach the fairies again. Since you spent the jewel on bird seed instead of the key, you hope they will give you another jewel.\n"
                              "You are disappointed when they do not regain interest and remain focused on their game of tag.\n")

            # Second right path encounter.
            print("While hiking on the clear trail, you enjoy viewing the luxuriant, woodland vegetation. The melodious sound of birdsong, which grows louder as you draw near,\n"
                      "soon diverts your attention. The source is an adorable, red bird that you recognize as a scarlet tanager. You are amazed to see that it is running\n"
                      "a charming, little shop beside the path. Alerted to your arrival, it switches to adorable chirping and hops about in excitement.\n"
                      "You must decide to browse the bird's shop or continue on the path.\n")
            shop_choice = input("Enter one option: browse the shop / continue\n\n")
            print()

            #Validate choice.
            while shop_choice not in ['browse the shop', 'continue']:
                print("Please enter a valid option.\n")
                shop_choice = input("Enter one option: browse the shop / continue\n\n")
                print()

            # If browse the shop.
            if shop_choice == 'browse the shop':
                
                # If jewel possessed.
                if jewel == 1:
                    print("A key and a bag of bird seed catch your eye, and you have a jewel you could use as payment. You pull out the jewel from your pocket and the bird chirps in approval.\n" 
                          "You must decide whether to buy a key, a bag of bird seed, or nothing.\n")
                    buy_choice = input("Enter one option: key / bird seed / nothing\n\n")
                    print()

                    # Validate choice.
                    while buy_choice not in ['key', 'bird seed', 'nothing']:
                        print("Please enter a valid option.\n")
                        buy_choice = input("Enter one option: key / bird seed / nothing\n\n")
                        print()
                    
                    # If buy a key.
                    if buy_choice == 'key':
                        print("You set down the jewel on the shop counter and point at the key. The bird picks up the key with its beak and drops it on the counter in exchange.\n"
                              "You take the key and the bird waves goodbye, before resuming its happy tune.\n")
                        jewel = 0
                        key_right = 1

                    # If buy bird seed.
                    elif buy_choice == 'bird seed':
                        print("You set down the jewel on the shop counter and point at the bird seed. The bird nudges the bag over to you in exchange.\n"
                              "You take the bird seed and the bird waves goodbye, before resuming its happy tune.\n")
                        jewel = 0
                        bird_seed = 1

                    # If buy nothing.
                    else:
                        print("You take back the jewel, not ready to part with it. The bird flips its attitude without warning.\n"
                              "Annoyed, it flies into the air and chases you away.\n")

                # If bird seed possessed. 
                elif bird_seed == 1:
                    print("You see that the same key is still for sale, but all you have is a bag of bird seed. You pull out the bird seed and the bird chirps in approval.\n"
                          "You must decide whether to trade the bird seed or not.\n")
                    trade_choice = input("Enter one option: trade / no trade\n\n")
                    print()

                    # Validate choice.
                    while trade_choice not in ['trade', 'no trade']:
                        print("Please enter a valid option.\n")
                        trade_choice = input("Enter one option: trade / no trade\n\n")
                        print()

                    # If trade bird seed.
                    if trade_choice == 'trade':
                        print("You set down the bird seed on the shop counter and point at the key. The bird picks up the key with its beak and drops it on the counter in exchange.\n"
                              "You take the key and the bird waves goodbye, before resuming its happy tune.\n")
                        bird_seed = 0
                        key_right = 1

                    # If not trade bird seed.
                    else:
                        print("You take back the bird seed, not ready to part with it. The bird flips its attitude without warning.\n"
                              "Annoyed, it flies into the air and chases you away.\n")
            
                # If jewel or bird seed not possessed. 
                else:
                    print("A key and a bag of bird seed catch your eye, but you don't have any form of payment. The bird realizes this and flips its attitude without warning.\n"
                          "Annoyed, it flies into the air and chases you away.\n")
 
            # Final right path encounter.

            # If key possessed.
            if key_right == 1:
                print("Not far past the shop, you come across a small cave. You light your lantern and explore the cave to find a locked treasure chest with a keyhole. You open it with a key that fits\n"
                      "and obtain an ancient healing spellbook of fairy magic.")
                print("Happy with your new treasure, you leave the forest to seek out a new adventure.\n")
                path_choice_return = 1
                start_over = 1
                
            # if key not possessed. 
            else:
                print("Not far past the shop, you come across a small cave. You light your lantern and explore the cave to find a locked treasure chest with a keyhole. You don't have a key that fits,\n"
                      "so you exit the cave and continue on the path.\n")
                path_choice_return = 1
                continue

    # If forward path.
    elif path_choice == 'forward':
        while path_choice_return == 0:
            
            # First forward path encounter.
            
            # If key/completion check passed.
            if key_forward == 0:
                print("You light your lantern and press forward on the shaded path. You don’t sense any danger, but the mystery of darkness intrigues you.\n"
                      "The lantern casts shadows upon the small circle it unveils around you. The undergrowth diminishes and the trees become increasingly large and twisted.\n"
                      "After a careful walk, you spot a locked door confined within the trunk of a tree. It has two keyholes.\n"
                      "You must decide to search the area for keys or continue on the path.\n")
                search_choice = input("Enter one option: search area / continue\n\n")
                print()

                #Validate choice.
                while search_choice not in ['search area', 'continue']:
                    print("Please enter a valid option.\n")
                    search_choice = input("Enter one option: search area / continue\n\n")
                    print()

                # If search area.
                if search_choice == 'search area':
                    print('You search out a mossy stone pedestal with a glowing inscription on top of it. The inscription reads: "What is not alive but grows, does not breathe but needs air?"\n'
                          "You must decide to try and solve the riddle or continue on the path.\n")
                    riddle_choice = input("Enter one option: solve riddle / continue\n\n")
                    print()

                    #Validate choice.
                    while riddle_choice not in ['solve riddle', 'continue']:
                        print("Please enter a valid option.\n")
                        riddle_choice = input("Enter one option: solve riddle / continue\n\n")
                        print()

                    # If solve riddle.
                    if riddle_choice == 'solve riddle':

                        # Riddle guessing game.

                        # Initialize variable to end iterations. 
                        quit_riddle = 0

                        # Condition.
                        while quit_riddle == 0:

                            # Input answer.
                            print("What is the answer to the riddle?\n")
                            riddle_answer = input("Enter a word in lowercase letters:\n\n")
                            print()

                            # If correct. 
                            if riddle_answer == 'fire':
                                print("There are two torches, one on each side of the pedestal. Instead of answering the riddle aloud, you light them with your lantern.\n"
                                      "A shining light appears in front of the pedestal, and forms into a treasure chest while it fades.\n"
                                      "You open the chest to obtain a key.\n")
                                key_forward = 1
                                quit_riddle = 1

                            # If incorrect.
                            else:
                                print("Nothing happens.\n"
                                      "You must decide to guess again or continue on the path.\n")
                                riddle_choice = input("Enter one option: guess again / continue\n\n")
                                print()

                                # Validate choice.
                                while riddle_choice not in ['guess again', 'continue']:
                                    print("Please enter a valid option.\n")
                                    riddle_choice = input("Enter one option: guess again / continue\n\n")
                                    print()

                                # If continue
                                if riddle_choice == 'continue':
                                    quit_riddle = 1

            # Second forward path encounter.

            # If trap chest not opened before.
            if trap_chest_skip == 0:
                print("Intending to return to the door when you get both keys, you continue on the path. It isn’t long before you see another source of torchlight ahead.\n"
                      "You seek it out to find a treasure chest on a well-lit platform. It doesn't have a keyhole and appears to be unlocked.\n"
                      "This seems too obvious and incongruous with the setting. You are suspicious about what may be inside.\n"
                      "You must decide to open the chest or continue on the path.")
                trap_chest_choice = input("Enter one option: open chest / continue\n\n")
                print()

                # Validate choice.
                while trap_chest_choice not in ['open chest', 'continue']:
                    print("Please enter a valid option.\n")
                    riddle_choice = input("Enter one option: open chest / continue\n\n")
                    print()

                # If open chest.
                if trap_chest_choice == 'open chest':
                    print("You open the chest, and it emits a shining light that surrounds you and makes everything disappear. You step back and look around in shock.\n") 
                    trap_chest_skip = 1
                    open_trap_chest = 1
                    path_choice_return = 1
                    continue

            # Final forward path encounter.
            
            # If key possessed.
            if key_forward == 1:
                print("You persist in your quest for keys to unlock the hidden door. While traversing over gnarled tree roots, you stumble upon a half-buried treasure chest.\n"
                      "You dig the chest out of the ground and inspect it to see that it is locked with one keyhole. Its peculiar location makes you feel uneasy about what may be inside.\n"
                      "You must decide to unlock the chest or continue on the path.")
                unlock_chest_choice = input("Enter one option: unlock chest / continue\n\n")
                print()

                # Validate choice. 
                while unlock_chest_choice not in ['unlock chest', 'continue']:
                    print("Please enter a valid option.\n")
                    unlock_chest_choice = input("Enter one option: unlock chest / continue\n\n")
                    print()

                # If open chest.
                if unlock_chest_choice == 'unlock chest':
                    print("You unlock the chest and open it to obtain a key. There is nothing to worry about. Now that you have two keys, you retrace your steps to the locked door.\n"
                          "The keys unlock the door,and it opens to reveal a treasure room filled with piles of gold coins. You fill your money bag but decide not to take any more than that.\n"
                          "It would be wise to hold onto the keys and return when you run out.")
                    print("Happy with your new treasure, you leave the forest to seek out a new adventure.\n")
                    path_choice_return = 1
                    start_over = 1

                # If continue.
                else:
                    path_choice_return = 1
                    continue

            # If key not possessed.
            else:
                print("You persist in your quest for keys to unlock the hidden door. While traversing over gnarled tree roots, you stumble upon a half-buried treasure chest.\n"
                      "You dig the chest out of the ground and inspect it to see that it is locked with one keyhole. Its peculiar location makes you feel uneasy about what may be inside,\n"
                      "but you don't have a key that fits, so you continue on the path.\n")
                path_choice_return = 1
                continue

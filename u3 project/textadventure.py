#im not creative so i used ai for plot, i made my own code tho, i made it so if you type an something but an integer it wont break, and will say it is not a valid choice, try again. So it isnt breakable
import random

bag = []
drops = 0
done = {"gothic": False, "pirate": False, "romance": False}


def check_choice(choice, choices):
    for item in choices:
        if item == choice:
            return True
    return False


def choose(prompt, choices):
    while True:
        try:
            choice = input(prompt).strip().lower()
            if choice == "":
                raise ValueError("No input entered.")
        except (EOFError, ValueError):
            print("Invalid input. Please try again.")
            continue

        if check_choice(choice, choices):
            return choice

        print("That is not a valid choice. Try again.")


def has_item(item):
    for thing in bag:
        if thing == item:
            return True
    return False


def get_word(word):
    if has_item(word):
        print(f"You already have the word '{word}'.")
    else:
        bag.append(word)
        print(f"You pick up the word '{word}'.")


def get_drop():
    global drops
    drops += 1
    print(f"You found a drop of the Master Inkwell. Total: {drops}/5")


def start():
    print("\n--- The Inkbound Clerk ---")
    print("You are a low-level clerk in the Great Imperial Library.")
    print("A bottle of strange ink spills across the forbidden journals.")
    print("The paper swallows you and drops you into a world made of words.")
    print("To get home, you must collect five drops of the Master Inkwell.")
    print("1. Walk through the glowing page door")
    print("2. Read the nearby note")
    print("3. Freeze in fear")

    choice = choose("> ", ["1", "2", "3"])
    if choice == "1":
        hall()
    elif choice == "2":
        note()
    else:
        print("The page whispers: 'The story will not wait.'")
        hall()


def note():
    print("\nThe margins are full of tiny notes and strange symbols.")
    print("You find a silver key and a raven-shaped mark.")
    print("1. Take the silver key")
    print("2. Take the raven mark")
    print("3. Keep walking")

    choice = choose("> ", ["1", "2", "3"])
    if choice == "1":
        get_word("silver")
    elif choice == "2":
        get_word("raven")
    else:
        print("You keep moving toward the chapter doors.")

    hall()


def hall():
    print("\nYou stand in the Library of Lost Chapters.")
    print("Three glowing doors are in front of you: Gothic, Pirate, and Romance.")
    print("1. Enter the Gothic Hall")
    print("2. Enter the Pirate Ledger")
    print("3. Enter the Romance Vault")
    print("4. Look at the desk")
    print("5. Explore the Hidden Stacks")
    print("6. Read the Whispering Index")

    choice = choose("> ", ["1", "2", "3", "4", "5", "6"])
    if choice == "1":
        goth()
    elif choice == "2":
        boat()
    elif choice == "3":
        love_room()
    elif choice == "4":
        print("The desk has a map and a note: 'Five drops are hidden inside the story.'")
        get_word("map")
        hall()
    elif choice == "5":
        hidden()
    else:
        index()


def hidden():
    print("\nThe Hidden Stacks are full of dusty books and whispers.")
    print("A loose page floats near a cracked ladder.")
    print("1. Take the loose page")
    print("2. Climb the ladder")
    print("3. Go back")

    choice = choose("> ", ["1", "2", "3"])
    if choice == "1":
        get_word("page")
        hall()
    elif choice == "2":
        print("You find a secret note: 'The story grows stronger where it is broken.'")
        bridge()
    else:
        hall()


def bridge():
    print("\nA paper bridge stretches over a river of flowing words.")
    print("A sign reads: 'The shortest road is not always the strongest.'")
    print("1. Cross the bridge")
    print("2. Read the sign again")
    print("3. Return to the stacks")

    choice = choose("> ", ["1", "2", "3"])
    if choice == "1":
        print("The bridge leads to a quiet alcove. You find a silver bookmark.")
        get_word("bookmark")
        hall()
    elif choice == "2":
        print("The words change before your eyes. You feel braver.")
        hall()
    else:
        hidden()


def index():
    print("\nThe Whispering Index is a long list of stories that mutter as you pass.")
    print("One title glows: 'The Last Clerk Before Dawn.'")
    print("1. Open the glowing entry")
    print("2. Ignore it")
    print("3. Pull a chapter from the shelf")

    choice = choose("> ", ["1", "2", "3"])
    if choice == "1":
        print("You uncover a hidden route to a forgotten archive.")
        read_room()
    elif choice == "2":
        print("You stay on your path and keep moving.")
        hall()
    else:
        print("You choose a chapter called 'Dawn of the Third Draft.'")
        get_word("dawn")
        hall()


def read_room():
    print("\nThe reading room is quiet except for turning pages and soft breathing.")
    print("A lamp burns beside a locked drawer and a warm chair.")
    print("1. Open the drawer")
    print("2. Sit in the chair")
    print("3. Leave")

    choice = choose("> ", ["1", "2", "3"])
    if choice == "1":
        print("Inside is a bottle of blue ink and a note: 'The true story is never finished.'")
        get_word("blue")
        hall()
    elif choice == "2":
        print("The chair hums with magic. You feel wiser and calmer.")
        get_word("courage")
        hall()
    else:
        hall()


def goth():
    print("\nYou enter the Gothic Hall. Fog fills the air, and stone walls rise around you.")
    print("A heavy iron gate blocks your path. A stone golem guards it.")
    print("1. Take the word 'heavy'")
    print("2. Take the word 'angry'")
    print("3. Use both words on the gate")
    print("4. Return to the library")

    choice = choose("> ", ["1", "2", "3", "4"])
    if choice == "1":
        get_word("heavy")
        goth()
    elif choice == "2":
        get_word("angry")
        goth()
    elif choice == "3":
        if has_item("heavy"):
            if has_item("angry"):
                print("The gate bends, and the golem loses its strength.")
                done["gothic"] = True
                get_drop()
                chapel()
            else:
                print("You need both words before the gate will move.")
                goth()
        else:
            print("You need both words before the gate will move.")
            goth()
    else:
        hall()


def chapel():
    print("\nIn a hidden chapel, a glowing reliquary waits under a candle.")
    print("1. Take the inkwell drop")
    print("2. Read the note")
    print("3. Go to the Pirate Ledger")

    choice = choose("> ", ["1", "2", "3"])
    if choice == "1":
        get_drop()
        boat()
    elif choice == "2":
        print("The note says: 'To cross the dark, unmake the weight.'")
        boat()
    else:
        boat()


def boat():
    print("\nYou enter the Pirate Ledger. A ship rocks in the clouds.")
    print("A storm chart, a gold cannonball, and a captain's cabin all wait for you.")
    print("1. Take the word 'storm'")
    print("2. Take the word 'gold'")
    print("3. Use both words on the chart")
    print("4. Enter the cabin")

    choice = choose("> ", ["1", "2", "3", "4"])
    if choice == "1":
        get_word("storm")
        boat()
    elif choice == "2":
        get_word("gold")
        boat()
    elif choice == "3":
        if has_item("storm"):
            if has_item("gold"):
                print("The chart reveals a safe path, and the cannonball glows.")
                done["pirate"] = True
                cabin()
            else:
                print("The sea will not reveal the route until you have both words.")
                boat()
        else:
            print("The sea will not reveal the route until you have both words.")
            boat()
    else:
        cabin()


def cabin():
    print("\nInside the cabin, a bronze compass spins and a locked chest hums.")
    print("1. Open the chest with the compass")
    print("2. Take the black sail ink bottle")
    print("3. Return to the deck")

    choice = choose("> ", ["1", "2", "3"])
    if choice == "1":
        print("The chest opens and reveals a drop of the Master Inkwell.")
        get_drop()
        moon_path()
    elif choice == "2":
        get_word("ink")
        moon_path()
    else:
        moon_path()


def moon_path():
    print("\nA silver road leads through a moonlit harbor.")
    print("1. Enter the lighthouse")
    print("2. Follow the road to the harbor")
    print("3. Go back to the library")

    choice = choose("> ", ["1", "2", "3"])
    if choice == "1":
        print("The lighthouse holds a third drop of the Master Inkwell.")
        get_drop()
        love_room()
    elif choice == "2":
        print("The harbor leads you into a hopeful love story.")
        love_room()
    else:
        hall()


def love_room():
    print("\nYou enter the Rose-lit Romance Vault.")
    print("A rose gate hangs over a broken vow and a lonely fountain.")
    print("1. Take the word 'rose'")
    print("2. Take the word 'broken'")
    print("3. Repair the vow with both words")
    print("4. Speak to the poet")

    choice = choose("> ", ["1", "2", "3", "4"])
    if choice == "1":
        get_word("rose")
        love_room()
    elif choice == "2":
        get_word("broken")
        love_room()
    elif choice == "3":
        if has_item("rose"):
            if has_item("broken"):
                print("The vow mends itself, and the fountain glows with golden light.")
                done["romance"] = True
                poet()
            else:
                print("The vow will not heal until both words are yours.")
                love_room()
        else:
            print("The vow will not heal until both words are yours.")
            love_room()
    else:
        poet()


def poet():
    print("\nThe poet asks, 'What is love without a final line?'")
    print("A heart-shaped box sits near a letter.")
    print("1. Open the heart-shaped box")
    print("2. Take the letter")
    print("3. Walk to the final gate")

    choice = choose("> ", ["1", "2", "3"])
    if choice == "1":
        print("The box reveals a fourth drop of the Master Inkwell.")
        get_drop()
        final_door()
    elif choice == "2":
        get_word("letter")
        final_door()
    else:
        final_door()


def all_done():
    if done["gothic"] == True:
        if done["pirate"] == True:
            if done["romance"] == True:
                return True
    return False


def final_door():
    print("\nYou stand at the Final Gate, a giant sentence holding the whole story together.")
    print("You have many words and some drops of ink. The last page waits.")
    print("1. Rewrite yourself home")
    print("2. Stay and become the keeper of the pages")
    print("3. Rewrite the world into peace")
    print("4. Take the inkwell for yourself")
    print("5. Remove all authors from the world")

    choice = choose("> ", ["1", "2", "3", "4", "5"])

    if choice == "1":
        if drops >= 5:
            if all_done():
                home_end()
            else:
                lost_end()
        else:
            lost_end()
    elif choice == "2":
        if has_item("map"):
            if has_item("silver"):
                keeper_end()
            else:
                bound_end()
        else:
            bound_end()
    elif choice == "3":
        if random.randint(1, 2) == 1:
            peace_end()
        else:
            bound_end()
    elif choice == "4":
        ruler_end()
    else:
        no_author_end()


def home_end():
    print("\nEnding 1: Home by the Last Page")
    print("You speak the final sentence and pour the inkwell drops into the empty bottle.")
    print("The story untangles itself and throws you back into the Great Imperial Library.")
    print("The forbidden wing is still a mess, but now you know the true power of words.")


def lost_end():
    print("\nEnding 2: Lost in the Margins")
    print("The story closes before you can escape.")
    print("You are stuck between the lines forever, becoming part of the page.")


def keeper_end():
    print("\nEnding 3: Keeper of the Story")
    print("You remain in the world of text and become its guardian.")
    print("The library keeps your name alive in every chapter.")


def bound_end():
    print("\nEnding 4: Bound in Ink")
    print("The page accepts your choice, but not your shape.")
    print("You become a ghost of annotations, trapped in the margins forever.")


def peace_end():
    print("\nEnding 5: A Library of Harmony")
    print("You rewrite the world so fear, treasure, and love can all exist together.")
    print("The story becomes gentle, balanced, and whole.")


def ruler_end():
    print("\nEnding 6: The Ink Sovereign")
    print("You take the Master Inkwell for yourself and command every page.")
    print("The library bows to you, but your heart grows cold.")


def no_author_end():
    print("\nEnding 7: The Unwritten World")
    print("You erase the need for authors and let every story write itself.")
    print("The world becomes wild, free, and endlessly changing.")


def play():
    print("Welcome to the Great Imperial Library.")
    print("A spill of experimental ink has pulled you into a world of written words.")
    start()
    print("\nThe story ends here. The ink still remembers your name.")


if __name__ == "__main__":
    play()


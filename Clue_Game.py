
"""
🎯 Goal:
A simple text-based Clue game in Python, where:

There’s one murderer, one weapon, one room.

A set of suspects, weapons, and rooms.

The player makes guesses until they solve the mystery!

"""

import random

# Game elements
suspects = ["Professor Plum", "Miss Scarlet", "Colonel Mustard", "Mrs. Peacock", "Mr. Green"]
weapons = ["Candlestick", "Revolver", "Rope", "Wrench", "Knife"]
rooms = ["Kitchen", "Ballroom", "Conservatory", "Dining Room", "Library"]

# Secret solution
solution = {
    "suspect": random.choice(suspects),
    "weapon": random.choice(weapons),
    "room": random.choice(rooms)
}





def play_clue():
    print("🎩 Welcome to the Clue Game!")
    print("Try to solve the murder mystery.\n")

    attempts = 0
    while True:
        guess_suspect = input(f"Guess the suspect {suspects}: ")
        guess_weapon = input(f"Guess the weapon {weapons}: ")
        guess_room = input(f"Guess the room {rooms}: ")

        attempts += 1

        if (guess_suspect == solution["suspect"] and
            guess_weapon == solution["weapon"] and
            guess_room == solution["room"]):
            print(f"\n✅ Correct! It was {guess_suspect} with the {guess_weapon} in the {guess_room}!")
            print(f"You solved the case in {attempts} attempts.")
            break
        else:
            print("\n❌ Not quite. Here's what we can tell you:")
            if guess_suspect != solution["suspect"]:
                print("  - The suspect is incorrect.")
            if guess_weapon != solution["weapon"]:
                print("  - The weapon is incorrect.")
            if guess_room != solution["room"]:
                print("  - The room is incorrect.")
            print("Try again!\n")


if __name__ == "__main__":
    play_clue()



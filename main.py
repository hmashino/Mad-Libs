print("Welcome to the Mad Libs Game!")

while True:
    print("\nSelect a mode:")
    print("1 - Normal Mode")
    print("2 - Adventure Mode")
    mode = input("Enter 1 or 2: ").strip()

    if mode == "1":
        print("\nNormal Mode")
        print("Please answer the following questions:\n")

        noun1 = input("Noun ①: ").strip().capitalize()
        noun2 = input("Noun ②: ").strip().capitalize()
        noun3 = input("Noun ③: ").strip().capitalize()
        place = input("Place: ").strip().capitalize()
        verb1 = input("Verb (base form): ").strip().lower()
        past_verb1 = input("Past tense verb ①: ").strip().lower()
        past_verb2 = input("Past tense verb ②: ").strip().lower()
        adjective1 = input("Adjective ①: ").strip().lower()
        adjective2 = input("Adjective ②: ").strip().lower()
        adjective3 = input("Adjective ③: ").strip().lower()
        adverb = input("Adverb: ").strip().lower()
        animal = input("Animal name: ").strip().lower()

        print("\nYour Story:\n")
        story = f"""
One day, you {past_verb1} a {adjective1} {noun1} in {place}.
Suddenly, {noun2} {past_verb2} from the sky and made you {verb1}.
{adverb}, you ran like a {animal} into a {adjective2} {noun3}.
That was a truly {adjective3} day.
"""
        print(story)

    elif mode == "2":
        print("\nAdventure Mode")
        print("Please answer the following questions:\n")

        noun1 = input("Noun ① (e.g., box): ").strip().capitalize()
        noun2 = input("Noun ②: ").strip().capitalize()
        noun3 = input("Noun ③: ").strip().capitalize()
        noun4 = input("Noun ④: ").strip().capitalize()
        place = input("Place (e.g., forest, school): ").strip().capitalize()
        verb1 = input("Verb (base form): ").strip().lower()
        past_verb1 = input("Past tense verb ①: ").strip().lower()
        past_verb2 = input("Past tense verb ②: ").strip().lower()
        past_verb3 = input("Past tense verb ③: ").strip().lower()
        past_verb5 = input("Past tense verb ⑤: ").strip().lower()
        past_verb9 = input("Past tense verb ⑨: ").strip().lower()
        adjective1 = input("Adjective ①: ").strip().lower()
        adjective2 = input("Adjective ②: ").strip().lower()
        adjective3 = input("Adjective ③: ").strip().lower()
        adverb = input("Adverb: ").strip().lower()
        animal = input("Animal name (e.g., cat): ").strip().lower()

        print("\n Your Story:\n")
        story = f"""
One day, you {past_verb1} a very {adjective1} {noun1} in {place}.
Surprised, you {past_verb2} to {verb1} it, but suddenly {noun2} {past_verb3} from the sky!
You began to {past_verb5}, shouting.
{adverb}, you ran like a {animal} and hid inside {noun3}.
Then there was a {adjective2} {noun4} waiting for you, and it {past_verb9}.
Thus ended your day of {adjective3}.
"""
        print(story)

    else:
        print("Invalid input. Please enter 1 or 2.")
        continue

    again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if again not in ("yes", "y"):
        print("Thanks for playing! Goodbye.")
        break
import random
import os

class Game:
    def __init__(self):
        self.score = 0
        self.satanic_score = 0
        self.hunger = 0
        self.revisit_list = []
        self.religions = ['Evangelist', 'Jehovah\'s Witness', 'Mormon', 'Custom']
        self.conversion_rates = {'Evangelist': 0.3, 'Jehovah\'s Witness': 0.2, 'Mormon': 0.25, 'Custom': 0.15, 'Satanic': 0.5}

    def start_game(self):
        print("Welcome to Belen Torres Preaching The Truth\n")
        print("In this game, you play as a preacher for a chosen religion. Your goal is to win as many souls as you can by going door-to-door and preaching your faith. Your performance is scored based on the number of souls won.\n")
        print("Each day you will encounter various responses from people behind the doors, and your hunger will increase as you continue preaching. When your hunger reaches 100, the day ends and you must go home to rest.\n")
        print("Now, let's begin. Choose your religion...\n")
        self.choose_religion()
        for _ in range(7):  # Game lasts for 7 days
            self.new_day()
            while self.hunger < 100:  # Each day ends when your hunger reaches 100
                self.door_to_door()
            self.hunger = 0  # Reset hunger for the next day
        self.end_game()

    def choose_religion(self):
        print("Choose your religion:\n")
        for i, religion in enumerate(self.religions, start=1):
            print(f"{i}. {religion}")
        while True:
            try:
                choice = int(input("Enter the number of your choice: "))
                if 1 <= choice <= len(self.religions):
                    break
                else:
                    print(f"Invalid choice. Please enter a number between 1 and {len(self.religions)}.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        self.religion = self.religions[choice - 1]
        print(f"You've chosen: {self.religion}\n")

    def new_day(self):
        self.weather = random.choice(['hot', 'cold', 'nice'])
        print(f"\nA new day begins... The weather is {self.weather}.\n")

    def door_to_door(self):
        self.clear_console()
        if self.revisit_list:
            revisit = input("Would you like to revisit a house that asked you to return? (y/n) ")
            if revisit.lower() == 'y':
                print("Revisiting a house...\n")
                self.revisit_list.pop()  # Remove the house from the revisit list
            else:
                print("Knocking on a new door...\n")
        else:
            print("Knocking on the next door...\n")
        self.choose_strategy()
        self.encounter()
        self.hunger_increase()

    def hunger_increase(self):
        if self.weather == 'hot' or self.weather == 'cold':
            self.hunger += 15
        else:
            self.hunger += 10
        print(f"Your hunger level is now {self.hunger}.\n")
        if self.hunger >= 100:
            print("You're too hungry to continue. Time to go home and rest.\n")

    def choose_strategy(self):
        print("Choose your preaching strategy:\n")
        strategies = ['Preach Softly', 'Preach Intensely']
        for i, strategy in enumerate(strategies, start=1):
            print(f"{i}. {strategy}")
        while True:
            try:
                choice = int(input("Enter the number of your choice: "))
                if 1 <= choice <= len(strategies):
                    break
                else:
                    print(f"Invalid choice. Please enter a number between 1 and {len(strategies)}.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        self.strategy = strategies[choice - 1]
        print(f"You've chosen to: {self.strategy}\n")

    def encounter(self):
        responses = ['bad', 'nice', 'no answer', 'skeptical', 'curious']
        response = random.choices(
            responses,
            weights=[0.4, self.conversion_rates[self.religion], 0.1, 0.2, 0.2] if self.strategy == 'Preach Softly' else [0.5, self.conversion_rates[self.religion]*0.75, 0.15, 0.15, 0.05],
            k=1
        )[0]
        if response == 'bad':
            print("The person is not interested.\n")
            self.bad_response()
        elif response == 'nice':
            print("The person is interested and converts!\n")
            if self.religion == 'Satanic':
                self.satanic_score += 1
            else:
                self.score += 1
            if random.random() < 0.2:  # 20% chance of receiving a food donation
                self.food_donation()
        elif response == 'skeptical':
            print("The person is skeptical, but promises to think about it.\n")
            self.revisit_list.append(1)  # Add this house to the revisit list
        elif response == 'curious':
            print("The person is curious and asks you to come back another time.\n")
            self.revisit_list.append(1)  # Add this house to the revisit list
        else:
            print("There's no answer.\n")
            if random.random() < 0.05:  # 5% chance of finding food
                self.find_food()
        input("Press Enter to continue...")

    def food_donation(self):
        print("The person donates some food to you!\n")
        self.hunger = max(0, self.hunger - 20)

    def find_food(self):
        take_food = input("You find some food. Do you want to take it? (y/n) ")
        if take_food.lower() == 'y':
            print("You take the food and eat it.\n")
            self.hunger = max(0, self.hunger - 15)

    def bad_response(self):
        if random.random() < 0.1:  # 10% chance of receiving a food donation or meeting another Satanic preacher
            if random.random() < 0.5:  # 50% chance of receiving a food donation
                self.food_donation()
            elif self.religion != 'Satanic':  # Satanic Bible can still be received if the player is not already a Satanic preacher
                self.receive_satanic_bible()
            else:  # If the player is a Satanic preacher, they meet another Satanic preacher
                self.meet_satanic_preacher()

    def receive_satanic_bible(self):
        print("The person throws a Satanic Bible at you!\n")
        take_bible = input("Do you want to take the Satanic Bible and become a Satanic preacher? (y/n) ")
        if take_bible.lower() == 'y':
            print("You take the Satanic Bible and become a Satanic preacher!\n")
            self.religion = 'Satanic'

    def meet_satanic_preacher(self):
        print("You meet another Satanic preacher who joins your cause!\n")
        self.conversion_rates['Satanic'] *= 2

    def end_game(self):
        print(f"You've won {self.score} souls!\n")
        if self.satanic_score >= 10:
            self.become_supernatural()

    def become_supernatural(self):
        while True:
            choice = input("You've won 10 souls to Satanism! Would you like to become a vampire or a werewolf? (v/w) ")
            if choice.lower() in ['v', 'w']:
                break
            else:
                print("Invalid input. Please enter 'v' for vampire or 'w' for werewolf.")
        if choice.lower() == 'v':
            print("You become a vampire and win the game!\n")
        else:
            print("You become a werewolf and win the game!\n")

    def clear_console(self):
        if os.name == 'nt':  # If the operating system is Windows
            os.system('cls')
        else:  # If the operating system is Linux or Unix
            os.system('clear')

game = Game()
game.start_game()

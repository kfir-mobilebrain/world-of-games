import random


class GuessGame:
    def __init__(self, difficulty, user_name):
        self.difficulty = difficulty
        self.user_name = user_name
        self.generated_secret_number = self.generate_number()
        self.user_input_value = 0
        self.result = False

    def compare_results(self):
        return self.user_input_value == self.generated_secret_number

    def generate_number(self):
        return random.randint(1,self.difficulty)

    def get_guess_from_user(self):
        tmp = input("Can you Guess What number i'm Thinking of ? it's between {} and {}\n".format(1,self.difficulty))
        if tmp.isdigit() and 1 <= int(tmp) <= self.difficulty:
            return int(tmp)
        else:
            print("Wrong input..")
            self.get_guess_from_user()

    def welcome_user(self):
        print(""" Welcome {} to Guess Game! """.format(self.user_name))

    def play(self):
        self.welcome_user()
        self.user_input_value = self.get_guess_from_user()
        self.result = self.compare_results()
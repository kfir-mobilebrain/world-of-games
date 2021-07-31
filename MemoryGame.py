import sys,time,os,random


class MemoryGame:
    def __init__(self, difficulty, user_name):
        self.difficulty = difficulty
        self.user_name = user_name
        self.generated_numbers = []
        self.user_inputs = []
        self.generate_numbers()
        self.result = False

    def generate_numbers(self):
        for _ in range(self.difficulty):
            self.generated_numbers.append(random.randint(1, 100))

    def show_numbers(self):
        sys.stdout.write('1')
        time.sleep(2)
        sys.stdout.write('\r2')

    def clear_screen(self):
        os.system('cls')

    def play(self):
        self.clear_screen()
        self.welcome_user()
        self.show_numbers_to_user()
        sys.stdout.write('\r Please Type in your answer\n')
        self.collect_user_inputs()
        self.result = self.compare_results()

    def compare_results(self):
        return self.user_inputs == self.generated_numbers

    def collect_user_inputs(self):
        self.user_inputs = []
        for _ in range(self.difficulty):
            tmp = input()
            if tmp.isdigit():
                self.user_inputs.append(int(tmp))
            else:
                print("{} is NOT a digit. Please re-insert your numbers".format(tmp))
                self.collect_user_inputs()

    def show_numbers_to_user(self):
        for item in self.generated_numbers:
            sys.stdout.write('\r {}'.format(item))
            time.sleep(0.7)

    def welcome_user(self):
        print(""" Welcome {} I'll give you {} amount of numbers 1 by 1 """.format(self.user_name, self.difficulty))
        print('And you need to guess by the SAME ORDER')
        print('Ready?')
        time.sleep(2)
        sys.stdout.write('\r 3')
        time.sleep(1)
        sys.stdout.write('\r 2')
        time.sleep(1)
        sys.stdout.write('\r 1')
        time.sleep(1)
        sys.stdout.write('\r Go!')
        time.sleep(1)


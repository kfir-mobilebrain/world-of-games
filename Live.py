class Live:

    def welcome(self):
        user_name = input("Please type here your name: ")
        self.user_name = user_name
        return("""
                Hello {} and welcome to the World of Games (WoG).
                Here you can find many cool games to play.
                """.format(user_name))

    def load_game(self):
        output = """Please choose a game to play:
                1. Memory Game - a sequence of numbers will appear for 1 second and you have to
                guess it back
                2. Guess Game - guess a number and see if you chose like the computer
                3. Currency Roulette - try and guess the value of a random amount of USD in ILS"""
        print(output)
        self.user_choise = self.get_user_game_choise()
        self.user_difficulty = self.get_user_difficulty()

    def get_user_game_choise(self):
        valid = False
        user_choise = input("What you like to play? ")
        if user_choise.isdigit():
            user_choise = int(user_choise)
            if 1 <= user_choise <= 3:
                valid = True
        if not valid:
            self.get_user_game_choise()
        else:
            return user_choise

    def get_user_difficulty(self):
        valid = False
        user_choise = input("What Difficulty you like to play? 1-5 ")
        if user_choise.isdigit():
            user_choise = int(user_choise)
            if 1 <= user_choise <= 5:
                valid = True
        if not valid:
            self.get_user_difficulty()
        else:
            return user_choise
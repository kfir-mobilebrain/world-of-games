import random, requests, json

class CurrencyRouletteGame:
    def __init__(self, difficulty, user_name):
        self.exchangerateAPIKey = "3966595590cfec8b922f35ce"
        self.difficulty = difficulty
        self.user_name = user_name
        self.user_input_value = 0
        self.currency_rate = self.get_USD_currency_rate()
        self.usd_value = self.generate_usd_value()
        self.game_interval = self.generate_interval()
        self.result = False

    def play(self):
        self.welcome_user()
        self.showTheUserUSDAmount()
        print('1 dollar is {} ILS'.format(self.currency_rate['ILS']))
        self.user_input_value = self.get_guess_from_user()
        self.result = self.checkResult()

    def checkResult(self):
        return self.game_interval[0] <= self.user_input_value <= self.game_interval[1]

    def showTheUserUSDAmount(self):
        print("How many is {}$ in Israeli Shekels? ".format(self.usd_value))
        print(self.game_interval)

    def get_guess_from_user(self):
        tmp = input()
        if tmp.isdigit() and int(tmp) >=1 :
            return int(tmp)
        else:
            print("Please insert ONLY numbers")
            self.get_guess_from_user()

    def get_USD_currency_rate(self):
        url = "https://v6.exchangerate-api.com/v6/{}/latest/USD".format(self.exchangerateAPIKey)
        res = requests.get(url)
        return json.loads(res.text)['conversion_rates']

    def generate_usd_value(self):
        return random.randint(1, 100)

    def generate_interval(self):
        return self.usd_value * self.currency_rate['ILS'] - (5 - self.difficulty), self.usd_value * self.currency_rate['ILS'] + (5 - self.difficulty)

    def welcome_user(self):
        print(""" Welcome {} to Currency Roulette Game ! """.format(self.user_name))

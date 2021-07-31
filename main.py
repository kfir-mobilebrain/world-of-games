from Live import Live
from MemoryGame import MemoryGame
from GuessGame import GuessGame
from CurrencyRouletteGame import CurrencyRouletteGame

game = Live()
print(game.welcome())
game.load_game()
difficulty = game.user_difficulty
user_win = False

if game.user_choise == 1:
    memory_game = MemoryGame(difficulty, game.user_name)
    memory_game.play()
    user_win = memory_game.result
elif game.user_choise == 2:
    guess_game = GuessGame(difficulty, game.user_name)
    guess_game.play()
    user_win = guess_game.result
elif game.user_choise == 3:
    currency_roulette = CurrencyRouletteGame(difficulty, game.user_name)
    currency_roulette.play()
    user_win = currency_roulette.result
if user_win:
    print("Win!")
else:
    print("Lose")
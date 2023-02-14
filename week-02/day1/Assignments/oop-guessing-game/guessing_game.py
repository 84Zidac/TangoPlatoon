import random


class GuessingGame():
    def __init__(self, answer):
        self.answer = int(answer)
        self.puzzle_solved = False

    def solved(self):
        return (self.puzzle_solved)

    def guess(self, num):
        if int(num) > self.answer:
            return ("high")
        if int(num) < self.answer:
            return ('low')
        if int(num) == self.answer:
            self.puzzle_solved = True
            return ('correct')


game1 = GuessingGame(10)
# game1.solved()   # => False

# game1.guess(5)  # => 'low'
# game1.guess(20) # => 'high'
# game1.solved()   # => False

# game1.guess(10) # => 'correct'
# game1.solved()   # => True

game_2 = GuessingGame(random.randint(1, 100))
last_guess = None
last_result = None

while game_2.solved() == False:
    if last_guess != None:
        print(f"Oops! Your last guess ({last_guess}) was {last_result}.")
        print("")

    last_guess = input("Enter your guess: ")
    last_result = game_2.guess(last_guess)


print(f"{last_guess} was correct!")

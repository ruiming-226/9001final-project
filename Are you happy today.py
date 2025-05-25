# This is a game related to the status of people today
class status:
    def __init__(self, energy: int = 2, emotion: int = 2):
        self.energy = energy
        self.emotion = emotion
        self._validate()
        if energy < 0 or emotion < 0:
            raise ValueError

    # Play basketball make me happy, but tired
    def play_basketball(self):
        self.emotion += 2
        self.energy -= 1
        self._validate()

    # Play computer game make me happy, but tired, too
    def play_computer_game(self):
        self.emotion += 2
        self.energy -= 1
        self._validate()

    # Enjoy music make me happy
    def enjoy_music(self):
        self.emotion += 1
        self._validate()

    # Have breakfast gives me energy
    def have_breakfast(self):
        self.energy += 1
        self._validate()

    # Have lunch gives me energy
    def have_lunch(self):
        self.energy += 1
        self._validate()

    # Have dinner gives me energy
    def have_dinner(self):
        self.energy += 1
        self._validate()

    # Have a drink gives me energy and make me happy
    def have_a_drink(self):
        self.energy += 1
        self.emotion += 1
        self._validate()

    # Do homework make me sad and tired
    def do_homework(self):
        self.energy -= 1
        self.emotion -= 1
        self._validate()

    # Clean house make me tired
    def clean_house(self):
        self.energy -= 2
        self._validate()

    # Check the type of today
    def day_state(self) -> str:
        total = self.energy + self.emotion
        if total >= 5 and self.energy >= 1 and self.emotion >= 1:
            return "happy day"
        if 0 <= self.emotion < 1:
            return "sad day"
        if 0 <= self.energy < 1:
            return "tired day"
        return "ordinary day"

    # Avoid the invalid
    def _validate(self):
        if self.energy < 0 or self.emotion < 0:
            raise ValueError

    # Show the status of today
    def summary(self) -> str:
        return (f"Energy = {self.energy}, Emotion = {self.emotion}, "
                f"Day Type → {self.day_state()}")

    def __str__(self):
        return self.summary()


if __name__ == '__main__':
    s = status(energy=2, emotion=2)
    print(s)

    # All of the commands are here
    commands = {
        "basketball": s.play_basketball,
        "computer_game": s.play_computer_game,
        "music": s.enjoy_music,
        "breakfast": s.have_breakfast,
        "lunch": s.have_lunch,
        "dinner": s.have_dinner,
        "drink": s.have_a_drink,
        "homework": s.do_homework,
        "clean": s.clean_house,
    }

    while True:  # Infinite loop
        command = input("What will you do?").strip().lower()

        # Quit the game
        if command == "quit":
            print("That's all")
            print("Now:", s.summary())
            break

        # The command is invalid
        if command not in commands:
            print("That's error")
            continue

        # The command is valid
        try:
            commands[command]()
            print("Now:", s.summary())

        # The command is ValueError
        except ValueError as err:
            print("Error:", err)
            break

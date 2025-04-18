# Pet.Py file.
class Pet:
    def __init__(self, name, hunger=0, energy=0, happiness=0):
        # Initialize the pet with default values
        self.name = name
        self.hunger = hunger  # Hunger level (0-10)
        self.energy = energy  # Energy level (0-10)
        self.happiness = happiness  # Happiness level (0-10).

    def eat(self):
        # A method that reduces hunger and increases happiness when the pet eats
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} enjoyed the meal!")

    def sleep(self):
        # A method that increases energy by 5 when the pet sleeps.
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} is sleeping, energy level is {self.energy}")

    def play(self):
        # A method that reduces energy by 2 and increases happiness by 2 when the pet plays.
        self.energy = max(0, self.energy - 2)
        self.happiness = min(10, self.happiness + 2)
        self.hunger = min(10, self.hunger + 1)
        print(f"{self.name} is playing!")

    def get_status(self):
        # A method that prints the current status of the pet.
        print(f"\n{self.name}'s status:")
        print(f"Hunger: {self.hunger}")
        print(f"Energy: {self.energy}")
        print(f"Happiness: {self.happiness}")
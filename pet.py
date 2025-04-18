class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []
        self.available_tricks = [
            "sit", "roll over", "play dead", 
            "shake hands", "spin", "jump", 
            "fetch", "beg", "speak", "high five"]
       
    def eat(self):
        print(f"{self.name} is eating...")
        self.hunger = max(0, self.hunger - 3)
        self.energy = min(10, self.energy + 2)
        self.happiness = min(10, self.happiness + 3)
       

    def sleep(self):
        print(f"{self.name} is sleeping...")
        self.hunger = min(10, self.hunger + 4 )
        self.energy = min(10, self.energy + 5)
        self.happiness = max(0, self.happiness - 2)

    def play(self):
        if self.energy <= 0:
            print(f"{self.name} is too tired to play. Let {self.name} rest.")
            return
        print(f"{self.name} is playing")
        self.hunger = min(10, self.hunger + 3)
        self.energy = max(0, self.energy - 3)
        self.happiness = min(10, self.happiness + 3)

    def train(self, trick):
        if self.energy <= 0:
            print(f"{self.name} is too tired to train.")
            return
        if trick in self.tricks:
            print(f"{self.name} already knows '{trick}'!")
            return
        if trick not in self.available_tricks:
            print(f"{self.name} can't learn '{trick}'! Try: {', '.join(self.available_tricks)}")
            return
        print(f"{self.name} is learning a new trick: {trick}!")
        self.tricks.append(trick)
        self.happiness = min(10, self.happiness + 1)
        self.energy = max(0, self.energy - 1)

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows these tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} doesn't know any tricks yet.")

    def get_status(self):
        print(f"\n{self.name}'s Current Status:")
        print(f"Hunger: {self.hunger}")
        print(f"Energy: {self.energy}")
        print(f"Happiness: {self.happiness}")
        self.show_tricks()
        print("--------------------------\n") # to visually separate from the rest of the output,
            


    
   
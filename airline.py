class Flight():
    def __init__ (self, capacity):
        self.capacity = capacity
        self.pacenger = []

    def add_pacenger (self, name):
        if not self.capacity - len(self.pacenger):
            return False
        else:
            self.pacenger.append(name)
            return True

flight = Flight(3)

people =["saman", "raj", "namal", "kumara"]
for person in people:
    if flight.add_pacenger(person):
        print(f"added {person} successfully")
    else:
        print(f"not avalibale seats for {person}. ")

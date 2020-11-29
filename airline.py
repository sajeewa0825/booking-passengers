class Flight():
    def capacity (self, capacity):
        self.capacity = capacity
        self.pacenger = []

    def add_pacenger (self, name):
        if not self.open_seats:
            return False
        else:
            self.pacenger.append(name)
            return True
    def open_seats (self):
        return self.capacity- len(self.pacenger)

flight = Flight(3)

people =["saman", "raj", "namal", "kumara"]
for person in people:
    success = Flight.add_pecenger(persn)
    if sccess:
        print(f"added {person} successfully")
    else:
        print(f"not avalibale seats for {person}. ")

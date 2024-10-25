# Create a class called `Seat` with two attributes: free (boolean), occupant (string)
class Seat:
    def __init__(self):
        self.free = True
        self.occupant = None

    def __str__(self):
        occupant = self.occupant if self.occupant else "Empty"
        return f"Seat({occupant}, {'Free' if self.free else 'Occupied'})"

    #This function assigns someone a seat if it's free
    def set_occupant(self, name):
        if self.free is True:
            self.occupant = name
            self.free = False

    #This function allows to remove someone from a seat and return the name of the person occupying the seat before   
    def remove_occupant(self):
        if self.free is False:
            occupant_name = self.occupant
            self.occupant = ""
            self.free = True
            return occupant_name

# Create a class `Table` with 2 attributes: capacity and seats as a list of Seat objects
class Table:
    def __init__(self, capacity = 4):
        # Initialize the table with the given capacity and create that many Seat objects
        self.capacity = capacity
        self.seats = [Seat() for _ in range(capacity)]

    #This function defines the number of left seats
    def left_capacity(self):
        left_seats = 0
        for seat in self.seats:
            if seat.free is True:
                left_seats +=1
        return left_seats

    #This function defines if a spot is available (at least one seat is free)    
    def has_free_spot(self):
        if self.left_capacity() > 0:
            return True

    #This function assigns the person to the first available seat at the table
    def assign_seat(self, name):
        if self.has_free_spot() is True:
            for seat in self.seats:
                if seat.free is True:
                    seat.set_occupant(name)
                    return f"{name} has been assigned a seat."
        return "No free seat available."
# Create a class called `Seat` with two attributes
class Seat:
    # Seat starts as free with no occupant
    """Attributes:
        free (boolean) indicates whether the seat is available.
        occupant (string) stores the name of the current occupant.
    """
    def __init__(self):
        self.free = True
        self.occupant = None        

    def set_occupant(self, name):
        if self.free is True:
            self.occupant = name
            self.free = False
        #else:
            #print(f"Seat is already occupied by {self.occupant}.")
        
    def remove_occupant(self):
        if self.free is False:
            occupant_name = self.occupant
            self.occupant = ""
            self.free = True
            return occupant_name
        #else:
            #print("Seat is already free.")
            #return None
            """
            Functions:
            set_occupant(name) assigns a person to the seat if it's free.
            remove_occupant() removes the occupant from the seat and returns their name.
            """

# Create a class `Table` with ? attributes
class Table:
    def __init__(self, capacity = 4):
        # Initialize the table with the given capacity and create that many Seat objects
        self.capacity = capacity
        self.seats = [Seat() for _ in range(capacity)]
        """
        Attributes:
        capacity (integer) defines the number of seats at the table.
        seats (list) holds Seat objects initialized with the size of the capacity.
        """
    def left_capacity(self):
        # Return the number of free seats
        left_seats = 0
        for seat in self.seats:
            if seat.free is True:
                left_seats +=1
        return left_seats
        
    def has_free_spot(self):
        # Return True if any seat is free, otherwise False
        if self.left_capacity() > 0:
            return True

    def assign_seat(self, name):
        # Assign the person to the first available seat
        if self.has_free_spot() is True:
            for seat in self.seats:
                if seat.free is True:
                    seat.set_occupant(name)
                    return f"{name} has been assigned a seat."
        return "No free seat available."


        """
        Functions:
        has_free_spot() checks if there is at least one free seat and returns True or False.
        assign_seat(name) assigns a person to the first available free seat.
        left_capacity() returns the number of free seats left at the table.
        """
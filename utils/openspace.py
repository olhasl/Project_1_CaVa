from typing import List, Dict
import random
import pandas as pd
#from table import Table

class Openspace:
    def __init__(self, number_of_tables: int):
        self.number_of_tables = number_of_tables
        self.tables = [Table(i + 1) for i in range(number_of_tables)]  # Create a list of table

    def __str__(self):
        return f"Openspace with {self.number_of_tables} tables."
    
    def organize(self, names: list):
        random(names)
        total_seats = sum([table.num_seats for table in self.tables])
        if len(names) > total_seats:
            raise ValueError
        index = 0
        for table in self.tables:
            for seat in table.seats:
                if index < len(names):
                    seat.occupant = names[index]
                    index += 1

    def display(self):
        for table in self.tables:
            print(f"Table {table.number}:")
            for seat in table.seats:
                occupant = seat.occupant if seat.occupant else "Empty"
                print(f"Seat {seat.number}: {occupant}")

    def store(self, filename: str):
        data = []
        for table in self.tables:
            for seat in table.seats:
                occupant = seat.occupant if seat.occupant else "Empty"
                data.append([table.number, seat.number, occupant])

        df = pd.DataFrame(data, columns=["Table Number", "Seat Number", "Occupant"])
        df.to_excel(filename, index=False)
        print(f"The distribution is stored in: {filename}")
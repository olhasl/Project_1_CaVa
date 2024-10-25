from typing import List
import random
import pandas as pd
from .table import Table

class Openspace:
    def __init__(self, number_of_tables: int):
        self.number_of_tables = number_of_tables
        self.tables = [Table() for _ in range(self.number_of_tables)]  # Create a list of table

    def __str__(self):
        return f"Openspace with {self.number_of_tables} tables."
    
    def organize(self, names: list):
        random.shuffle(names)
        '''total_seats = sum([table.num_seats for table in self.tables])
        if len(names) > total_seats:
            raise ValueError'''
        remaining_people = []
        for name in names:
            assigned = False
            for table in self.tables:
                if table.has_free_spot():
                    table.assign_seat(name)
                    assigned = True
                    break
            if not assigned:
                remaining_people.append(name)
        return remaining_people

    def display(self):
        for i, table in enumerate(self.tables, 1):
            occupants = [seat.occupant if seat.occupant else "Empty" for seat in table.seats]
            print(f"Table {i}: {', '.join(occupants)}")


    def store(self, filename: str):
        data = []
        for i, table in enumerate(self.tables, start=1):
            for seat in table.seats:
                data.append({'Table': i, 'Occupant': seat.occupant if seat.occupant else 'Empty'})


        df = pd.DataFrame(data)
        df.to_excel(filename, index=False)
        print(f"The distribution is stored in: {filename}")

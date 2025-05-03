#!/bin/python

#Defaults constant values
DEFAULT_ROWS = 10
DEFAULT_COLUMNS = 10


class SALA:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.seats = [["L" for y in range(self.columns)] for x in range(self.rows)]

    def get_seats_map(self):
        for x in range(self.rows):
            for s in range(self.columns):
                print("[" + self.seats[x][s] + "]", end="")
            print("")

    def select_seat(self, selection_row, selection_column):
        if self.seats[selection_row][selection_column] != "L":
            return "not available, please try anotherone"
        else:
            self.seats[selection_row][selection_column] = "X"
            return "seat selected"


            

            
sala_teatro = SALA(DEFAULT_ROWS, DEFAULT_COLUMNS)

print(" - - - - - - TICKET RESERVATION SYSTEM - - - - - -\n\n")

system_active = True 
while system_active == True:
    option = input("Wolud you like to select a seat or show the current availability? \n press 'S' for selection, any other key to show availability: ")

    if option == "s" or option == "S":
        selection_row = -1
        while selection_row < 0 or selection_row > 9:
            selection_row = int(input("please select the row you whant to seat on ( value must be between 1 and 10 ): \n")) - 1
            if selection_row < 0 or selection_row > 9:
                print("your selection is out of the specified range, please try again\n")
        
        selection_column = -1
        while selection_column < 0 or selection_column > 9:
            selection_column = int(input("please select the column number you whant to seat on ( value must be between 1 and 10 ): \n")) - 1
            if selection_column < 0 or selection_column > 9:
                print("your selection is out of the specified range, please try again\n")
       
        print(sala_teatro.select_seat(selection_row, selection_column))
        select_more= input("select more seats? ")
        if select_more in [ "Y", "y", "YES", "yes", "Yes"]: 
            continue
        else:
            break

    
    else:
        sala_teatro.get_seats_map()





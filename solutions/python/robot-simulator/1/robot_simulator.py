# Globals for the directions
# Change the values as you see fit
EAST = 'EAST'
NORTH = 'NORTH'
WEST = 'WEST'
SOUTH = 'SOUTH'
EAST_TURNS = ('NORTH', 'SOUTH')
NORTH_TURNS = ('WEST', 'EAST')
WEST_TURNS = ('SOUTH', 'NORTH')
SOUTH_TURNS = ('EAST', 'WEST')


class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self.coordinates = (x_pos, y_pos)

    def move(self, movements):
        for action in movements:
            if action == 'A':
                if self.direction == 'NORTH':
                    self.coordinates = (self.coordinates[0], self.coordinates[1] + 1)
                if self.direction == 'EAST':
                    self.coordinates = (self.coordinates[0] + 1, self.coordinates[1])
                if self.direction == 'SOUTH':
                    self.coordinates = (self.coordinates[0], self.coordinates[1] - 1)
                if self.direction == 'WEST':
                    self.coordinates = (self.coordinates[0] - 1, self.coordinates[1])

            if action == 'R':
                self.direction = globals()[self.direction + "_TURNS"][1]

            if action == 'L':
                self.direction = globals()[self.direction + "_TURNS"][0]

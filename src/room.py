# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, direction):
        super().__init__()
        self.name = name 
        self.direction = direction
    pass
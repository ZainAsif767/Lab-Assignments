# Room class

#The Room class is a simple class that models a room object with its location and status.

class Room:
    def __init__(self,location,status="dirty"):
        self.location = location
        self.status = status
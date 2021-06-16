class Package:
    def __init__(self, id, address, city, state, zip, deadline, mass):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.mass = mass

    def __str__(self):
        return str(self.id) + ' ' + str(self.address)
# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE

class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

test = LatLon(40, 50)
print(test.lat)
print(test.lon)

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE

class Waypoint(LatLon):
    def __init__(self, name, lat, lon):
        super().__init__(lat, lon)
        self.name = name
    def __str__(self):
        return 'Waypoint(name='+self.name+', lat='+str(self.lat)+ ', lon='+str(self.lon)+ ')'

test2 = Waypoint('test', 10, 20)
print(test2.name)
print(test2.lat)
print(test2.lon)

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE

class Geocache(Waypoint):
    def __init__(self, name, difficulty, size, lat, lon):
        super().__init__(name, lat, lon)
        self.difficulty = difficulty
        self.size = size
    def __str__(self):
        return 'Geocache(name='+self.name+', difficulty='+str(self.difficulty)+', size='+str(self.size)+', lat='+str(self.lat)+ ', lon='+str(self.lon)+ ')'

test3 = Geocache('test', 'hard', 'big', 10, 20)
print(test3.name)
print(test3.difficulty)
print(test3.size)
print(test3.lat)
print(test3.lon)

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE

waypoint1 = Waypoint("Catacombs", 41.70505, -121.51521)
print('"{}", {}, {}'.format(waypoint1.name, waypoint1.lat, waypoint1.lon))
# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
waypoint = Waypoint("Catacombs", 41.70505, -121.51521)
print(waypoint.__str__())

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE

geocache = Geocache("Newberry Views", 1.5, 2, 44.052137, -121.41556)

# Print it--also make this print more nicely
print(geocache)

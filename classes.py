class Toolbox:
    def __init__(self):
        self.tools = []

    def addTool(self, tool):
        self.tools.append(tool)

    def removeTool(self, tool):
        self.tools.remove(tool)


class Screwdriver:
    def __init__(self, size):
        self.size = size

    def tightenScrew(self, screw):
        screw.tighten()

    def loosenScrew(self, screw):
        screw.loosen()


class Hammer:
    def __init__(self, color):
        self.color = color

    def paint(self, newColor):
        self.color = newColor

    def hammerIn(self, nail):
        nail.nail_in()

    def remove(self, nail):
        nail.remove()


class Screw:
    MAX_TIGHTNESS = 5

    def __init__(self):
        self.tightness = 0

    def loosen(self):
        if self.tightness > 0:
            self.tightness -= 1

    def tighten(self):
        if self.tightness < self.MAX_TIGHTNESS:
            self.tightness += 1

    def __str__(self):
        return "Screw with tightness {}".format(self.tightness)


class Nail:

    def __init__(self):
        self.in_wall = False

    def nail_in(self):
        if not self.in_wall:
            self.in_wall = True

    def remove(self):
        if self.in_wall:
            self.in_wall = False

    def __str__(self):
        return "Nail {}in wall.".format("" if self.in_wall else "not ")


# Instantiate objects
toolbox = Toolbox()
screwdriver = Screwdriver(size="Medium")
hammer = Hammer(color="Black")

# put hammer and screwdriver inside the toolbox
toolbox.addTool(screwdriver)
toolbox.addTool(hammer)

# Instantiate a screw and tighten it using a screwdriver
screw = Screw()
print("Screw before tightening: ", screw)
screwdriver.tightenScrew(screw)
print("Screw after tightening: ", screw)

# instantiate a nail and hammer it in using a hammer
nail = Nail()
print("Nail before hammering: ", nail)
hammer.hammerIn(nail)
print("Nail after hammering: ", nail)

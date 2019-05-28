class Coordinate:
	def __init__(self, x_coord, y_coord):
		self.x_coord = x_coord
		self.y_coord = y_coord

	def toString(self):
		return '(' + str(self.x_coord) + ',' + str(self.y_coord) + ')'
		
class Pixel:
	def __init__(self, coordinate):
		self.coordinate = coordinate
		self.filled = False

	def fill(self):
		self.filled = True

	def toString(self):
		return '[' + self.coordinate.toString() + ' - ' + str(self.filled) + ']'

class Brick:
	def __init__(self, height, width):
		self.height = height
		self.width = width

	def setOrigin(self, coordinate):
		self.origin = coordinate

	def setColor(self, color):
		self.color = color

	def toString(self):
		return '[' + str(self.height) + ' x ' + str(self.width) + ' - ' + self.origin.toString() + ']'

class Cell:
	def __init__(self):
		

c1 = Coordinate(1,1)
p1 = Pixel(c1)
p1.fill()
print(p1.toString())
b1 = Brick(1,3)
b1.setOrigin(Coordinate(0,0))
print(b1.toString())
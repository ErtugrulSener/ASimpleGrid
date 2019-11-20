# from globals import *

class Grid:
	def __init__(self, max_width, max_height):
		self.max_width = max_width
		self.max_height = max_height
		self.MAX_SLOT_COUNT = self.GetSize()

		self.__Initialize()

	def __Initialize(self):
		self.grid = {}

		self.Clear()

	def Clear(self):
		for i in range(self.MAX_SLOT_COUNT):
			self.grid[i] = 0

	def IsEmpty(self, pos, height):
		row = pos / self.max_width

		if row + height > self.max_height:
			return False

		for y in range(height):
			index = pos + (y * self.max_width)

			if self.grid[index]:
				return False

		return True

	def FindBlank(self, height):
		if height > self.max_height:
			return -1

		for row in range(self.max_height):
			for column in range(self.max_width):
				index = row * self.max_width + column

				if self.IsEmpty(index, height):
					return index

		return -1

	def Put(self, pos, height, value = True):
		if not self.IsEmpty(pos, height):
			return False

		for y in range(height):
			index = pos + (y * self.max_width)
			self.grid[index] = value

	def Print(self):
		for row in range(self.max_height):
			for column in range(self.max_width):
				print("%d" % (self.grid[row * self.max_width + column]), end=" ")

			print("")

	def GetSize(self):
		return self.max_width * self.max_height

#classes

class BoxContainer:
	def __init__(self):
		self.value=None
		self.bgcolor='white'
		self.fgcolor='black'
	def set(self,val):
		self.value=val
		if val:
			self.bgcolor='green'
			self.fgcolor='red'
		else:
			self.bgcolor='red'
			self.fgcolor='green'
	def reset(self):
		self.value=None
		self.bgcolor='white'
class Handler:
	def __init__(self):
		self.boxs = []
		for i in range(9):
			self.boxs.append(BoxContainer())
	def play(self,box_index,val):
		if box_index >= 0 and box_index < 9:
			self.boxs[box_index].set(val)
			return self.boxs[box_index].color
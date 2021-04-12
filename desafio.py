class VeicRover(object):
	def __init__(self, h, v, d):
		self.h = h
		self.v = v
		self.d = d    
	# Orienta frente do rover no sentido anti-horario
	def Right(self, x):
		self.b = x
		if self.b == 'N':
			return 'E'
		elif self.b == 'E':
			return 'S'
		elif self.b == 'W':
			return 'N'
		elif self.b == 'S':
			return 'W'
	# Orienta frente do rover no sentido horario
	def Left(self, x):
		self.b = x
		if self.b == 'N':
			return 'W'
		elif self.b == 'E':
			return 'N'
		elif self.b == 'W':
			return 'S'
		elif self.b == 'S':
			return 'E'

	# Move uma posição
	def Moviment(self):
		if self.d == 'N':
			self.v = self.v + 1
		elif self.d == 'E':
			self.h = self.h + 1
		elif self.d== 'W':
			self.h = self.h - 1
		elif self.d== 'S':
			self.v = self.v - 1

	def Rotate(self,Rotate):
		if Rotate == 'L':
			# self.Dir = self.Left[self.Dir]
			self.d = Rover.Left(self.d)
		elif m == 'R': 
			# self.Dir = self.Right[self.Dir]
			self.d = Rover.Right(self.d)

	def __str__(self):
		res = '%d %d %s' % (self.h, self.v, self.d)
		return res

class Plane(object):
	# Conf plano
	def __init__(self, PlanoSize):
		self.PlanoSize = PlanoSize

	# Configura o rover
	def ConfRover(self, Rover):
		self.Rover = Rover

	# Começa a mover o rover
	def MoveRover(self, Move):
		for m in Move:
			if m == 'L' or m == 'R':
				self.Rover.Rotate(m)
			elif m == 'M': 
				self.Rover.Moviment()

if __name__=="__main__":

	PlanoInp = input("plano: ")
	PlanoSize = map(int, PlanoInp.split())

	# Chama func e configura o plano
	PlanoLine = Plane(PlanoSize)

	while True:
		# Recebe a posição
		Pos = input("posição: ")
		# Recebe o movimento
		Mov = input("movimento: ")
		# x y e d recebem seus valores
		(h, v, d) = Pos.split() # (1 2 N)
		# Remove espaços em branco
		Movim = Mov.strip() # (LMLMLMLMM)
		# Chama func e configura posição inicial (1 2 N)
		Rover = VeicRover(int(h), int(v), d)
		# Configura posição inicial do rover
		PlanoLine.ConfRover(Rover)
		# Move o rover
		PlanoLine.MoveRover(Movim)

		print ("Saida: ",Rover)
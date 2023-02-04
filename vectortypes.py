from enum import Enum
from math import atan2, degrees, hypot
from typing import Self


class _ERROR(Enum):
	IncorrectCoordinatesType = 'Vector coords must be type "int" or "float"'
	IncorrectVector2Args = 'Vector2 only accepts X and Y values'
	IncorrectVector3Args = 'Vector3 only accepts X, Y and Z values'
	InvalidXValue = 'Value of X must be type "int" or "float"'
	InvalidYValue = 'Value of Y must be type "int" or "float"'
	InvalidZValue = 'Value of Z must be type "int" or "float"'
	IncorrectVectorComparison = 'Vectors can only be compared with other vectors of same dimensions'
	InvalidKeyValue = 'Key value must be type "int" or "str"'


class _Vector:
	def __init__(self, *coords):
		if isinstance(self, Vector2):
			if len(coords) == 2:
				if not all(isinstance(_, int | float) for _ in coords):
					raise TypeError(_ERROR.IncorrectCoordinatesType)
				self.__x = coords[0]
				self.__y = coords[1]
			elif len(coords) == 1:
				if not isinstance(coords[0], int | float):
					raise TypeError(_ERROR.IncorrectCoordinatesType)
				self.__x = coords[0]
				self.__y = coords[0]
			elif not len(coords):
				self.__x = 0
				self.__y = 0
			else:
				raise ValueError(_ERROR.IncorrectVector2Args)
		elif isinstance(self, Vector3):
			if len(coords) == 3:
				if not all(isinstance(_, int | float) for _ in coords):
					raise TypeError(_ERROR.IncorrectCoordinatesType)
				self.__x = coords[0]
				self.__y = coords[1]
				self.__z = coords[2]
			elif len(coords) == 1:
				if not isinstance(coords[0], int | float):
					raise TypeError(_ERROR.IncorrectCoordinatesType)
				self.__x = coords[0]
				self.__y = coords[0]
				self.__z = coords[0]
			elif not len(coords):
				self.__x = 0
				self.__y = 0
				self.__z = 0
			else:
				raise ValueError(_ERROR.IncorrectVector3Args)
	
	def __len__(self):
		if isinstance(self, Vector2):
			return 2
		elif isinstance(self, Vector3):
			return 3

	def __repr__(self):
		if isinstance(self, Vector2):
			return f"Vector2({self.x},{self.y})"
		elif isinstance(self, Vector3):
			return f"Vector3({self.x},{self.y},{self.z})"
		
	def __str__(self):
		if isinstance(self, Vector2):
			return f"{{'x': {self.x}, 'y': {self.y}, 'magnitude': {self.magnitude}, 'angle': {self.angle}}}"
		elif isinstance(self, Vector3):
			return f"{{'x': {self.x}, 'y': {self.y}, 'z': {self.z}, 'magnitude': {self.magnitude}}}"
		
	def __eq__(self, other: Self):
		if all(isinstance(_, Vector2) for _ in [self, other]):
			return self.x == other.x and self.y == other.y
		elif all(isinstance(_, Vector3) for _ in [self, other]):
			return self.x == other.x and self.y == other.y and self.z == other.z
		else:
			raise TypeError(_ERROR.IncorrectVectorComparison)

	def __ne__(self, other: Self):	
		if all(isinstance(_, Vector2) for _ in [self, other]):
			return self.x != other.x or self.y != other.y
		elif all(isinstance(_, Vector3) for _ in [self, other]):
			return self.x != other.x or self.y != other.y or self.z != other.z
		else:
			raise TypeError(_ERROR.IncorrectVectorComparison)

	def __iter__(self):
		self.iter_index = 0
		return self

	def __next__(self):
		if isinstance(self, Vector2):
			limit = 2
		elif isinstance(self, Vector3):
			limit = 3

		if self.iter_index < limit:
			value = self[self.iter_index]
			self.iter_index+=1
			return value
		else:
			raise StopIteration
		
	def __getitem__(self, item: int | str) -> int | float:
		if isinstance(item, int):
			if isinstance(self, Vector2):
				valid_int_keys = [0,1]
			elif isinstance(self, Vector3):
				valid_int_keys = [0,1,2]

			if item not in valid_int_keys:
				raise KeyError(f'Invalid key value "{item}"')

			if item == 0:
				return self.x
			elif item == 1:
				return self.y
			elif item == 2:
				return self.z
		elif isinstance(item, str):
			valid_str_keys = {
				'x': self.x,
				'y': self.y,
				'magnitude': self.magnitude,
			}

			if isinstance(self, Vector2):
				valid_str_keys['angle'] = self.angle

			value = valid_str_keys.get(item)

			if value is None:
				raise KeyError(f'Invalid key value "{item}"')

			return value

		raise TypeError(_ERROR.InvalidKeyValue)
	
	@property
	def x(self) -> int | float:
		return self.__x

	@x.setter
	def x(self, new_x: int | float):
		if not isinstance(new_x, int | float):
			raise TypeError(_ERROR.InvalidXValue)
		self.__x = new_x

	@property
	def y(self) -> int | float:
		return self.__y

	@y.setter
	def y(self, new_y: int | float):
		if not isinstance(new_y, int | float):
			raise TypeError(_ERROR.InvalidYValue)
		self.__y = new_y

	@property
	def magnitude(self) -> float:
		return hypot(*[_ for _ in self])


class Vector2(_Vector):
	@property
	def angle(self) -> float:
		return degrees(atan2(self.y, self.x))

class Vector3(_Vector):
	...


class Rectangle:
  def __init__(self, width: int, height: int):
    self.width = width
    self.height = height

  def get_area(self):
    return self.width * self.height
  
  def set_width(self, width: int):
    self.width = width

  def set_height(self, height: int):
    self.height = height

  def get_perimeter(self):
    return 2 * self.width + 2 * self.height
  
  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** .5
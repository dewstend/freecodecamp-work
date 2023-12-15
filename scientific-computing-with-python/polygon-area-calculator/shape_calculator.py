class Rectangle:
  def __str__(self):
    return f'Rectangle(width={self.width}, height={self.height})'

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
  
  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    
    return "\n".join(['*' * self.width for _ in range(self.height)]) + "\n"
  
class Square(Rectangle):
  def __str__(self):
    return f'Square(side={self.width})'
  
  def __init__(self, side: int):
    self.width = side
    self.height = side

  def set_side(self, side: int):
    self.width = side
    self.height = side
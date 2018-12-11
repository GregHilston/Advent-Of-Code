import sys

class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    
  def __str__(self):
    return f"Point({self.x}, {self.y})"

class Claim:
  def __init__(self, identifier, start_x, start_y, width, height):
    self.identifier = identifier
    self.start_x = start_x
    self.start_y = start_y
    self.width = width
    self.height = height

  def get_points(self):
    for y in range(self.start_y, self.start_y + self.height):
      for x in range(self.start_x, self.start_x + self.width):
        yield Point(x, y)
"""
#1 @ 236,827: 24x17
"""
def build_data_structure(input_file):
  dis_diccct = {}
  with open(input_file) as fin:
    for line in fin:
      tokens = line.split(' ')
      
      identifier = tokens[0].replace('#', '')
      start_x = int(tokens[2].split(',')[0])
      start_y = int(tokens[2].split(',')[1].replace(':', ''))
      width = int(tokens[3].split('x')[0])
      height = int(tokens[3].split('x')[1])

      c = Claim(identifier, start_x, start_y, width, height)

      for point in c.get_points():
        if str(point) in dis_diccct:
          dis_diccct[str(point)].append(identifier)
        else:
          dis_diccct[str(point)] = [identifier]

  return dis_diccct

d = build_data_structure("input.txt")

running_total_of_overlaps = 0

for key, val in d.items():
  if len(val) >= 2:
    running_total_of_overlaps += 1

print(running_total_of_overlaps)
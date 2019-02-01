class Pet():
  def __init__(self, name, types):
    self.name = name
    self.types = types
    
  def getName(self):
    return self.name
  
   def getName(self):
    return self.types
  
  def __str__(self):
    return "%s is a %s" % (self.name, self.types)
  

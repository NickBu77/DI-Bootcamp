class MyClass:
  __counter = 2

  @classmethod
  def add(cls,a): 
    return cls.__counter + a



class1 = MyClass()
print(class1.__counter)
class1.__counter = 4
print(class1.__counter)
class1.add(8)
print(class1.__counter)



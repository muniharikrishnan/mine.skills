"""class student:
    pass
muni=student()
muni.gender="m"
muni.age="20"
print(muni.gender)
print(muni)"""
"""class student:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
muni=student("muni","25","male")
print(muni.name)
print(muni.age)
print(muni.gender)"""
class student:
    def __init__(self,name,gender,age):
        self.name=name
        self.gender=gender
        self.age=age   
    
    """def student_attributes(self):
        return f"{self.name} {self.gender} {self.age}
muni=student("muni","male",24)

#print(muni.student_attributes())#
hari=student("hari","male",20)"""

"""for nm in (hari,muni):
    print("enter something:",nm)
    print(nm.age)
    print(nm.name)"""





"""def sitting(self):
    print(f"{self.name_} is sitting")

def __str__(self):
    return self.breed

@staticmethod
def bark():
    print("dogs can bark")"""


class cat:
    def __init__(self,color,age):
        self.color=color
        self.age=age
    def __str__(self):
        return f"{self.color} \n {self.age}"
    
catcutie=cat("white",5)
print(catcutie)

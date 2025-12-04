
class student:
    roll_number = 8

    def __init__(self, roll_number):
        self.roll_number = roll_number

    def learn(self):
        return "learning"

kushal = student(123)
print(kushal.roll_number)
print(kushal.learn())

class faculty:
    college = "ITM" 
    def college(cls):
        return cls.college
    def __init__(self,name):
        self.name = name 
        self.skills = ["python"]
    def add_skill(self, skill):
        self.skills.append(skill)
        return self.skills



prasad = faculty("prasad")
prasad.add_skill = ["ts" , "js"]
print (prasad.skills)
print (prasad.college())
















class user:
    def __init__(self, fname , lname):
        self.fname = fname 
        self.lname = lname


        def print_full_name(self):
            return self.fname + " " +  self.lname
    
    
    
    
class user(kushal):
    pass


person_one = user("kushal", "doe")
print(person_one.fname)
print(person_one.lname)


user_one = user("kushal" , "doe")
print(user_one.fname)
print(user_one.lname)







        
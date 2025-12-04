try:
    print(x)
except Exception as e:
    print("error ",e)
except :
    print("default")
else:
    print("inside else")
finally:
    print("inside finally")

my_set = {9,2,4,True , 1}

for x in my_set:
    print(x)
my_set.add("Q")
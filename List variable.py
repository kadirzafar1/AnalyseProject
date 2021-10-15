values = [1, 2, "rahul", 4, 5]

print(values[0])
print(values[1])
print(values[2])
print(values[-1])

values.insert(3,"shetty")    #to add values
print(values)

print(values[1:3])

values.append("end")     #to add values at last
print(values)

values[2] = "RAHUL"       #to update values
print(values)

del values[0]              #to delete values
print(values)
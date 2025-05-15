tuple = ("imdad", "ali", "ahmed", "imdad")

print(tuple.count("imdad")) # 2
print(tuple.index("imdad")) # 0     

print("imdad" in tuple) # True
print("imdad" not in tuple) # False
print("imdad" or "ali" in tuple) # True
print("imdad" and "ali" in tuple) # True
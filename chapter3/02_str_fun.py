name = "imdad"
print(len(name)) # 5
print(name.startswith("i")) # True
print(name.endswith("d")) # True
print(name.find("d")) # 3
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.title())
print(name.replace("i", "I"))
print(name.split("i")) # ['I', 'mdad']
print(name.split("a")) # ['imd', 'd']
print(name.count("d")) # 1

#escape sequence


setence = "hello \n world \"imdad\""
print(setence)
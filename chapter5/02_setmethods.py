sets = {1,2,3,4,2}

sets.add(5) # add 5 to the set
print(sets) # {1, 2, 3, 4, 5}

sets1 = {1,2,3,4,2}
setunion = sets.union(sets1) # union of two sets
print(setunion) # {1, 2, 3, 4, 5}
setintersection = sets.intersection(sets1) # intersection of two sets   
print(setintersection) # {1, 2, 3, 4}
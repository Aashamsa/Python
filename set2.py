set1 = {"a", "b", "c"}
set2 = {1,2,3,"a"}
set3 = {"apple", "banana"}
myset = set1.union(set2,set3)
print(myset)
set4 = set1 & set2
print(set4)
set1.intersection_update(set4)
print(set1)
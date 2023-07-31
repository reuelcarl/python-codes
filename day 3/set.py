# this is a collection that is unordered and unindexed

# it does not allow duplicatebvalues

utensils = {"fork", "spoon", "knife"}
# utensils.remove("knife")

dishes = {"bowl", "plate", "cup"}
dinner_table = utensils.union(dishes)
differnce = utensils.difference(dishes)
print(difference)
print(dinner_table)



for utensil in utensils:
    print(utensil)

intersection = utensils
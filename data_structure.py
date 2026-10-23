fruits=["Apple","Banana","Mango"]
print(type(fruits))

fruits_set=set(fruits)
print(type(fruits_set))

fruits_set.add("Orange")
print(fruits_set)

fruits_set.add("Berry")
print(fruits_set)

fruits_set.update(["Grapes","Pineapple"])
print(fruits_set)

fruits_set.remove("Banana")
print(fruits_set)
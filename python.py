# a = [1, 2, 3, 4]
# b = a
# print(b is a)
# print("Hello""World!")
#
#
#
# print("This is a string"[1])
# #.format can be used to format strings, like this:
# print("{} can be {} ".format("Strings", "interpolated"))
#
# #you can repeat the formatting arguments to save some typing
# print("{0} fuck {1}".format("python", "java"))
#
# #you can use keywords if you dont want to count
# print("{name} wants to eat {food}".format(name = 'Bob',food = 'lasagna'))
#
# #if your python3 code also needs to run on Python
# print("%s want to eat %s way %s"%("Bob", "lasagna",'old'))
#
# print(bool(0))
#
#
li=[]
li.append(1)
li.append(2)
li.append(4)
li.append(3)
li.pop()
li.append(3)
print(li[1:3])
print(li)
print(li[2:])
print(li[::2])
print(li[::3])
print(li[::-1])
print(li[1:2:2])
other = [2, 4, 5, 6]
print("love")
print(li+other)

print(li.extend(other))
print(li)

tup = (1, [2,3], 4)
tup[0]

print(type((0, 1)))
print(len(tup))
print(tup + (4, 5, 6))
print(tup[:2])
print(2 in tup)
a, *b, c =1, 2, 3 , 4
print(a)
print(b)
print(c)
a, b = b, a
print(a)
print(b)
print(c)

empty_dict ={}
filled_dict = {"one":1,"three":3,"two":2}

# invalid_dict ={(1,[2,3]):"123"}
print(filled_dict['one'])
print(list(filled_dict.keys()))
print(set(filled_dict.keys()))
print(list(filled_dict.values()))

print("one" in filled_dict)
print(1 in filled_dict)

print(filled_dict.get("one", 4))
print(filled_dict.get("four", 4))

filled_dict.setdefault("five", 5)
print(filled_dict)
filled_dict.setdefault("five", 6)
print(filled_dict)
# filled_dict.update({"four":4});
filled_dict["four"] = 4
print(filled_dict)

del filled_dict["one"]

print(filled_dict)


other_dict={"six":6, "serven":7}

#Sets store ... well sets
empty_set = set()
some_set = {1, 1, 2, 2, 3, 4}
print(some_set)
filled_set = some_set;
filled_set.add(5)
print(filled_set)

other_set={3, 4, 5, 6}
print(some_set & other_set)
print(filled_set | other_set)
print({1, 2, 3, 4} - {2, 3, 5})
print({1, 2, 3, 4} ^ {2, 3, 5})
print({1, 3} >= {1, 2, 3})
print({1, 3} <= {1, 2, 3})

print(2 in filled_set)
print(10 in filled_set)




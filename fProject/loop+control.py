list1=["hi","hello","welcome"]
names=["kamal","nimal","amal"]
for item in list1:
    for name in names:
        print(item,name)
        if item=="hello" and name=="nimal":
            break
    print("outer the inner loop")
print("out from outer loop")

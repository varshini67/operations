data1 =input("data1: ")
data2 =input("data2: ")
list1 = data1,split(",")
list2 = data2,split(",")
mydict = dict(Zip(list1,list2))
key = input("key: ")
if key in mydict:
  print("value:",mydict[key])
else:
  print("value: None")

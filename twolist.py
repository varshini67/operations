L1 =input("data1:").split(",")
L2 =input("data2:").split(",")
d1 = {}
if(len(L1) == len(L2)):
  for i in range(len(L1)):
    d1[L1[i]] = L2[i]
  print(sorted(d1.items()))
else:
  print("length should be equal")

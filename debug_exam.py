#The answer for 5b corrected code ENG19cs0052

def uniqueUpdate(data1, data2):
# Initially empty dictionary
    dupKeys = {}
# Examine every (k, v2) pair in data2
    for [k, v2] in data2:
# Check if there is a key-value pair with key = k in data1
        if k in data1:
            v1 = data1[k]
# (k, v1) in dict1 Check if v1 != v2
            if v1 != v2:
# Add (k, [v1, v2]) to dictionary
                dupKeys[k] = [v1, v2]
# Remove (k, v1) from data1
                del data1[k]
        else:
# Add (k, v2) to data1
            data1[k] = v2
# After processing all (k, v2) in data2, return the dictionary
    return dupKeys


## DO NOT MODIFY BELOW THIS LINE! ##


import sys
if _name_ == '_main_':
    data1 = {}
n1 = int(input())
for _ in range(n1):
    k, v = map(int, input().split())
if k in data1:
    sys.exit("Illegal: data1")
data1[k] = v
data2 = []
n2 = int(input())
for _ in range(n2):
    k, v = map(int, input().split())
for [k2, v2] in data2:
    if k2 == k:
        sys.exit("Illegal: data2")
data2.append([k, v])
dup = uniqueUpdate(data1, data2)
print(data1)
print(data2)
print(dup)

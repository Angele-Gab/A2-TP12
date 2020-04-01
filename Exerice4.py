
def listSum(lst):
    if len(lst) == 0 :
        return 0
    return listSum(lst[1:]) + int(lst[0])

print(listSum([])) # 0
print(listSum([42])) # 42
print(listSum([3,1,5,2])) # 11

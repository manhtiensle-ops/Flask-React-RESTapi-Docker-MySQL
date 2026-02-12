def inputfunc(name):
    print(name)
def otherInputfunc(a):
    return int(a)

def funcInFunc(otherfunc):
    return otherfunc

print(funcInFunc(inputfunc("Peter")))
print(funcInFunc(otherInputfunc(1)))

        

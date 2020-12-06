print("Hello World")

def hair(name, color):
    out=name +" has " + color + " hair"
    print(out)
hair("Shubham","black")

def hair2(name, color):
    print(f"{name} has {color} hair.")
hair2("Rohan","white")

def prod(x,y):
    print(x * y)
prod(5,7)

def bye(na):
    print(f"thank you {na}")
bye("Shubham")

def difference(x,y):
    diff = y - x
    return diff
print(difference(6,12))

print(6/2)

def mult_loop(x,y):
    i=0
    z=0
    while(i<y):
        z=z+x
        i=i+1
    return z
print(mult_loop(6,6))
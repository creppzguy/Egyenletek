import math
a=float(input("Írd ide az első számot: "))
b=float(input("Írd ide a második számot: "))
c=float(input("Írd ide a harmadik számot: "))
d=b*b-4*a*c
if d<0:
    print("Nincs ilyen megoldás")

else:
    if d==0:
        d1=(-b+math.sqrt(b**2-4*a*c))/2*a
        print("Egyetlen megoldás van: ", d1)
    else:
        if d>0:
           d2=(-b + math.sqrt(d)) / (2*a)
           d3=(-b - math.sqrt(d)) / (2*a)
           print("Kettő megoldás van megoldás: ", d2, "vagy", d3)


    

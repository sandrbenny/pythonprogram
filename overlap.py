from shapely.geometry import Point
print("First triangle is in leftside and below")
print("Input first triangle :x1,y1,x2,y2,x3,y3,second triangle :X1,Y1,X2,Y2,X3,Y3:")
x1,y1,x2,y2,x3,y3,X1,Y1,X2,Y2,X3,Y3 = map(float, input().split())
l1 = Point(x1, y2)
r1 = Point(X1, Y1)
l2 = Point(x2, y2)
r2 = Point(X2, Y2)
l3 = Point(x3, y3)
r3 = Point(X3, Y3)
f=0
if (l3.x >= r1.x and r2.x >= l3.x):#consider first triangle is left

    if (l2.y >= r1.y and l2.y >= r3.y):#consider first triangle is below
        f=1
if(f==1):
    print("triangles overlap")
else:
    print("triangles dont overlaps")
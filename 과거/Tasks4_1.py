from cs1media import *
threshold=150
threshold2=100
yellow = (255,255,0)
green=(0,255,0)
blue=(0,0,255)

img = load_picture("./cs101_students.jpg")
w,h=img.size()
img.show()

for i in range(w):
    for j in range(h):
        r,g,b=img.get(i,j)
        tmp=(r+g+b)//3
        if tmp>threshold:
            img.set(i,j,yellow)
        elif threshold2<tmp<threshold:
            img.set(i,j,green)
        else:
            img.set(i,j,blue)
img.show()
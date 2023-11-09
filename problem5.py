from cs1media import *

red = (255,0,0)
img = load_picture("./sejong.jpg")
img2 = create_picture(220,184,red)
w,h=img.size()
for i in range(w):
    for j in range(h):
        color = img.get(i,j)
        img2.set(10+i,10+j,color)
img2.show()
print(img.size())
print(img2.size())
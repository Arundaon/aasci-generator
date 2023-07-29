from warnings import catch_warnings
from PIL import Image
import sys

def get_brightness(r,g,b):
    # return (r+g+b)/3
    # return max(r,g,b)+min(r,g,b)/2
    return 0.21*r+0.72*g+0.07*b

def get_ascii(x):
    level = " `^\",:;Il!i<>~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
    c = round(x*(len(level)-1)/255)
    return level[c]

# gambar = Image.open("./ascii-pineapple.jpg")
gambar = Image.open(sys.argv[1])


try:
    ratio=float(sys.argv[2])
except:
    if gambar.width>400 and gambar.width>1.5*gambar.height:
        ratio=300/gambar.width
    else:
        ratio=180/gambar.height



gambar = gambar.resize([round(gambar.width*ratio),round(gambar.height*ratio)],Image.ANTIALIAS)

print("image size : ",gambar.width,"x",gambar.height)
for x in range(gambar.height):
    for y in range(gambar.width):
        pixel = gambar.getpixel((y,x))
        print(get_ascii(get_brightness(pixel[0],pixel[1],pixel[2])),end="")
        print(get_ascii(get_brightness(pixel[0],pixel[1],pixel[2])),end="")
    print()
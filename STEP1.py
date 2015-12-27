import PIL
from PIL import Image
eld = []
def recpic():
    img = Image.open('newpic.gif').convert('1')
    for i in range(5):
        x = 5 + 9*i
        y = 4
        eld.append(img.crop((x,y,x+8,y+14)))
    piclib=[]
    for i in range(10):
        piclib.append(Image.open('piclib\%d.bmp' %i))
    result = ''
    for target in eld :
        result += str(match(target,piclib))
    return result

def match(tareget_pic,pic_lib):
    sizeofpic =tareget_pic.size
    diffs =[]
    for i in range(10):
        diffs.append(0)
        for xi in range(sizeofpic[0]):
            for yi in range(sizeofpic[1]):
                if tareget_pic.getpixel((xi,yi)) != pic_lib[i].getpixel((xi,yi)):
                    diffs[i] += 1
    copy = diffs[:]#不是复制地址
    copy.sort()
    return diffs.index(copy[0])
'''piclib = []
for i in range(10):
    piclib.append(Image.open('piclib\%d.bmp' %i))

temp = Image.open('piclib\%d.bmp' %2)
match(temp,piclib)'''

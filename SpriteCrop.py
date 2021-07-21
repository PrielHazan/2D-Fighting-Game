from PIL import Image, ImageOps

def CreateAndSaveMirrorImage(RightImage, name):
    mirrored_image = ImageOps.mirror(RightImage)
    mirrored_image.save(f'{name}')

def CreatingRightAndLeftPic(sprites, name, Stand_index, WalkStartIndex, WalkEndIndex, size, interval=0):
    for i in range(0, WalkEndIndex + 1):
        if i == Stand_index:
            area = (i*size+interval*i, 0, i*size+interval*i+size, size)
            RightImage = sprites.crop(area)
            RightImage.save(f'{name}StandingR.bmp')
            CreateAndSaveMirrorImage(RightImage, f'{name}StandingL.bmp')
        if i >= WalkStartIndex and i <= WalkEndIndex:
            area = (i*size+interval*i, 0, i*size+interval*i+size, size)
            RightImage = sprites.crop(area)
            RealI = i - WalkStartIndex + 1
            RightImage.save(f'LucasWalkR{RealI}.bmp')
            CreateAndSaveMirrorImage(RightImage, f'LucasWalkL{RealI}.bmp')

def CreatingPics(sprites, name, ext, StartIndex, EndIndex, row_index, size, numerate=0, interval=0, direction=False):
    for i in range(StartIndex, EndIndex + 1):
        area = (i*size+interval*i, row_index*size+interval*row_index, i*size+interval*i+size, row_index*size+interval*row_index+size)
        RightImage = sprites.crop(area)
        RealI = i - StartIndex + 1
        if numerate != None:
            RealI += numerate - 1
        if direction:
            RightImage.save(f'{name}R{RealI}.{ext}')
            CreateAndSaveMirrorImage(RightImage, f'{name}L{RealI}.{ext}')
        else:
            RightImage.save(f'{name}{RealI}.{ext}')



Sprites = Image.open('pedzik_1.bmp')
# CreatingRightAndLeftPic(LucasSprites, 'Lucas', 0, 3, 7, 79, interval=1)
# AssasinSprites = Image.open('0.bmp')
# CreatingPics(AssasinSprites, 'AssasinLightning', 'bmp', 0, 5, 15, 79, interval=1)
CreatingPics(Sprites, 'LucasKick', 'bmp', 0, 6, 3, 79, numerate=None, interval=1, direction=True)

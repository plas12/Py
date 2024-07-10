'''
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

area = (300, 200, 700, 600)
size = (640, 200)

lion_img = Image.open("Lion.jpg")
fruit_img = Image.open("fruit.png")

print(lion_img.size, lion_img.format, lion_img.mode)
print(fruit_img.size, fruit_img.format, fruit_img.mode)

fruit_resz = fruit_img.resize(size)
lion_cropped = lion_img.crop(area)
lion_img.show()

lion_cropped.save("lion_cropped.jpg")
fruit_resz.save("fruit_resized.png")


from PIL import Image

size = (128, 128)

lion_img = Image.open("Lion.jpg")
lion_rotated = lion_img.rotate(90)
lion_converted = lion_img.convert('L')
lion_transpose = lion_img.transpose(Image.FLIP_LEFT_RIGHT)
lion_img.thumbnail(size)
print("lion_converted.mode =", lion_converted.mode)#.mode는 저거의 모드를 나타내는거
print("lion_img.size =", lion_img.size)#위와 같음

lion_converted.show()
lion_transpose.show()
lion_rotated.save("lion_rotated.jpg")
lion_img.save("lion_thumb.jpg")


from PIL import Image

fruit_img = Image.open("fruit.png")
fruit_rotate = fruit_img.rotate(270)
fruit_convert = fruit_img.convert("L")

fruit_rotate.show()
fruit_convert.show()
fruit_rotate.save("fruit_cotate.png")
fruit_convert.save("fruit_convert.png")


from PIL import Image
from PIL import ImageDraw

canvas_size = (200, 200)
rect_area = [(0, 0), (100, 100)]
line_cor = [(0, 200), (200,  0)]
circle_area = [(100, 100), (200, 200)]

new_img = Image.new("RGB", canvas_size, "orange")
draw_imgs = ImageDraw.Draw(new_img)
draw_imgs.rectangle(rect_area, fill = "red", outline = "yellow")
draw_imgs.line(line_cor, fill = "blue", width = 4)
draw_imgs.ellipse(circle_area, fill = "green", outline = "red")

new_img.show()
new_img.save("imagedraw.jpg")
'''

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

lion_img = Image.open("Lion.jpg")
c3coding_img = Image.open("c3coding_rt.jpg")
c3coding_img.thumbnail((120, 120))
draw = ImageDraw.Draw(lion_img)

stx,sty = (150, 285)
c3x,c3y = c3coding_img.size
msg1 = "The               is"
msg2 = "the best"

mfont = ImageFont.truetype("c:/windows/fonts/framd.ttf", 40)
m2font = ImageFont.truetype("c:/windows/fonts/Candara.ttf", 52)
draw.text((70, 280), msg1, (255, 255, 0), font = mfont, align = "Left")
draw.text((70, 330), msg2, (255, 0, 0), font = m2font, align = "Left")
lion_img.paste(c3coding_img, (stx, sty, stx + c3x, sty + c3y))

lion_img.show()
lion_img.save("c3lion.jpg")

from PIL import Image, ImageColor
from flask import Flask, request

class Pixel_calc(object):

    def pixel(patch_full):

        try:
            im = Image.open(patch_full)
            if str(im.format) in ['JPG', 'JPEG']:
                black = 0
                white = 0

                for px in im.getdata():
                    if px == (0, 0, 0):
                        black += 1
                    if px == (255, 255, 255):
                        white += 1

                if black > white:
                    return 'Чёрных пикселей больше. Чёрных пикселей = ' + str (black) + ', белых пикселей = ' + str(white)+ '.'

                if black < white:
                    return 'Белых пикселей больше. Белых пикселей = ' + str(white) + ', чёрных пикселей = ' + str (black)+ '.'
                else:
                    return 'Белых и чёрных пикселей одинаковое количество = '+ str (black)+ '.'

            else:
                return 'Неверный формат файла. Допустимые форматы файлов: jpg, jpeg.'

        except:
            return 'Неверный формат файла. Допустимые форматы файлов: jpg, jpeg. Так же, проверьте что в имени файла имеются только цифры и латинские символы.'
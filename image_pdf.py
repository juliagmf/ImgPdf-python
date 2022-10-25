from email.mime import image
from PIL import Image

def Images_Pdf(filename, output):
    images = []

    for file in filename:
            #pegando a imagem
        im = Image.open(file)
            #convertendo a imagem
        im = im.convert('RGB')
        images.append(im)

        images[0].save(output, save_all= True, append_images=images[1:])

Images_Pdf(["hotd.jpg", "dragon.jpg"], "output.pdf")



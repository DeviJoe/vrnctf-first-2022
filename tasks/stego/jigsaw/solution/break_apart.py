from PIL import Image
import random

width = height = S = 90
N = 10
name = 'solution.png'

im = Image.open(name)


names = list(range(N*N))


for i in range(N):
    for j in range(N):
        box = (j * S, i * S, (j + 1) * S, (i + 1) * S)
        a = im.crop(box)

        new_im = Image.new('RGB', (width, height), (255, 255, 255))
        new_im.paste(a, (0, 0))

        name = random.choice(names)
        names.remove(name)

        new_im.save("images/" + str(name) + '.png')






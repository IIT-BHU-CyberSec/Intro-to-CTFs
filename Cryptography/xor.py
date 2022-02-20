from PIL import Image


lemur = Image.open(r'./lemur.png')
flag = Image.open(r'./flag.png')

'''.load creates the 2d pixel map of the input image
each point on the map corresponds to a pixel, and each value '''

l = lemur.load()
f = flag.load()

for i in range(flag.size[0]):  # iterating through every row of the map
    for j in range(flag.size[1]):  # iterating through every column of the map

        l_p = l[i, j]
        f_p = f[i, j]

        pixel = []

        pixel.append(l_p[0] ^ f_p[0])  # xoring the two r values
        pixel.append(l_p[1] ^ f_p[1])  # xoring the two g values
        # xoring the two b values, since (b1 ^ s) ^ (b2 ^ s) = b1 ^ b2
        pixel.append(l_p[2] ^ f_p[2])

        f[i, j] = tuple(pixel)

flag.save("answer.png")

input = open('input.txt', 'r')

pixelstring = input.readline()
pixels = list(map(int, pixelstring.strip()))
nr_of_pixels = len(pixels)

#Real input
width = 25
height = 6

#Test input
#width = 3
#height = 2

prop = width * height

layermap = {}
layercount = 0

for i in range(0, nr_of_pixels, prop):
    layercount +=1
    layermap[layercount] = pixels[i:i+prop]

min_zeros = []

for layer in layermap:
    zeros = layermap[layer].count(0)
    if min_zeros == [] or zeros < min_zeros[1]:
        min_zeros = [layer, zeros]


correct_layer = min_zeros[0]
correct_layer_content = layermap[correct_layer]
nr_of_1 = correct_layer_content.count(1)
nr_of_2 = correct_layer_content.count(2)
answer = nr_of_1 * nr_of_2

print(answer)

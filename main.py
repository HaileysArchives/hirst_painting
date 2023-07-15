import colorgram

rgb_colors = []
colors = colorgram.extract('image.jpg', 30) # colorgram.extract(image, number_of_colors)


for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    rgb_colors.append(new_color)


print(rgb_colors)

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)

# for color in colors: 
#     rgb_colors.append(color.rgb)    

# print(rgb_colors) # result: Rgb(r=245, g=238, b=243)
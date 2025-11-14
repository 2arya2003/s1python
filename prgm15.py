from numpy.ma.extras import unique

color_list1=["red","blue","green"]
colo_list2=["blue","yellow","black"]
unique_colors=[color for color in color_list1 if color not in colo_list2]
print(unique_colors)

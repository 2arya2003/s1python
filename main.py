from graphics.rectangle import area as ra,perimeter as rp
from graphics.circle import area as ca,circumference as cp
from graphics.graphic_3d.cuboid import surface_area as cua,volume as cup
from graphics.graphic_3d.sphere import surface_area as sa, volume as sp
print("rectangle area:",ra(10,5))
print("rectangle perimeter:",rp(10,5))
print("\ncircle area:",ca(7))
print("circle perimeter:",cp(7))
print("\ncuboid surface_area:",cua(2,3,4))
print("cuboid volume:",cup(2,3,4))
print("\nsphere surface_area:",sa(5))
print("sphere volume:",sp(5))
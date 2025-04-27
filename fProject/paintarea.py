import math
def paint_calculation(height,width,cover):
    area=height*width
    no_of_cans=math.ceil(area/cover)
    print(f"no of cans {no_of_cans}")


h=int(input("height:"))
w=int(input("weight:"))
coverage=7
paint_calculation(height=h,width=w,cover=coverage)
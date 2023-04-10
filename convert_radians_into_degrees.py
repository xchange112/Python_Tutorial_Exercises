import math
def convert_radian_to_degree(angle_in_radian):
    angle_in_degree = angle_in_radian * 180/math.pi
    return angle_in_degree

radian = convert_radian_to_degree(3)
print(round(radian, 3))
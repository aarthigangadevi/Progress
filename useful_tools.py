import random

feet_in_mile = 5280
meters_in_kilometer = 1000
bts = ["rm","jin","suga","jhope","jimin","v","jk"]

def get_file_ext(filename):
    return filename[filename.index(".")+1:]

def roll_dice(num):
    return random.randint(1,num)

print(get_file_ext("Employee.csv"))
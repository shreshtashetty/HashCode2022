import sys
from fileReader import *
from fileWriter import *
from scoreCalculator import *


# PATH = r'C:\Users\shreshta\Downloads\Hashcode\input_data\e_elaborate.in.txt'


def optimize(like, dislike):
    res = []
    for key in like.keys():
        if key not in dislike:
            res.append(key)
        elif key in dislike and like[key] >= dislike[key]:
            res.append(key)

    return res


if __name__ == '__main__':
    PATH = sys.argv[1]  # To accept user input from cmd line
    like, dislike = fileReader(PATH)
    res = optimize(like, dislike)
    score = scoreCalc(res, PATH)
    print(score)
    fileWriter(res)

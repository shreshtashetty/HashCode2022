import sys
from fileReader import *
from fileWriter import *
from scoreCalculator import *


# PATH = r'C:\Users\shreshta\Downloads\Hashcode\input_data\e_elaborate.in.txt'
def optimizeNew(clients):

    ingredients = clients[0][1]
    for i in range(1, len(clients)):
        if not clients[i][2]:
            ingredients += clients[i][1]
        else:
            flag = 0
            for dis_ing in clients[i][2]:
                if dis_ing in ingredients:
                    flag = 1
                    break
            if flag == 0:
                ingredients += clients[i][1]

    return list(set(ingredients))

def optimizeGreedy(like, dislike):
    res = []
    for key in like.keys():
        if key not in dislike:
            res.append(key)
        elif key in dislike and like[key] >= dislike[key]:
            res.append(key)

    return res



if __name__ == '__main__':
    PATH = sys.argv[1]  # To accept user input from cmd line
    # like, dislike = countLikeDislikeOccur(PATH)
    clients = organizeInput(PATH)
    # print(clients, "\n")
    # print(sorted(clients))
    res = optimizeNew(sorted(clients))
    # res = optimizeGreedy(like, dislike)
    print(res)
    score = scoreCalc(res, PATH)
    print(score)
    fileWriter(res)

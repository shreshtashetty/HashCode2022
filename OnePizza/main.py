import sys
from fileReader import *
from fileWriter import *

def getPizzaIngredients(path):
    l,dl = getLikesDislikes(path)
    if len(dl)<=0:
        return str(len(l)) + ' ' + ' '.join([k for k,v in l.items()])
    if len(l)<=0:
        return "0"
    finalList = [k for k,v in l.items() if k not in dl]
    return str(len(finalList)) + ' ' + ' '.join(finalList)

if __name__ == '__main__':
    PATH = "D:\\Projects\\Python Scripts\\GoogleHashCode2022\\OnePizza\\InputData\\e_elaborate.txt"  
    res = getPizzaIngredients(PATH)
    print(res)
    fileWriter(res)
    '''
    PATH1 = "D:\\Projects\\Python Scripts\\GoogleHashCode2022\\OnePizza\\InputData\\b_basic.txt"  
    res1 = getPizzaIngredients(PATH1)
    print(res1)
    PATH2 = "D:\\Projects\\Python Scripts\\GoogleHashCode2022\\OnePizza\\InputData\\c_coarse.txt"  
    res2 = getPizzaIngredients(PATH2)
    print(res2)
    PATH3 = "D:\\Projects\\Python Scripts\\GoogleHashCode2022\\OnePizza\\InputData\\d_difficult.txt"  
    res3 = getPizzaIngredients(PATH3)
    PATH4 = "D:\\Projects\\Python Scripts\\GoogleHashCode2022\\OnePizza\\InputData\\e_elaborate.txt"  
    res4 = getPizzaIngredients(PATH4)
    print(res4)
    fileWriter(res+'\n'+res1+'\n'+res2+'\n'+res3+'\n'+res4)
    '''
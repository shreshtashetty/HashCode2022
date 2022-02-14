

def fileWriter(res):
    with open('pizza_ingredients.txt', 'w') as f:
        f.write(str(len(res)))

        for i in range(len(res)):
            f.write(" ")
            f.write(res[i])
            
            
            
            

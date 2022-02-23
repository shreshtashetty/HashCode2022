def fileWriter(res):
    with open('pizza_ingredients.txt', 'w') as f:
        for i in range(len(res)):
            f.write(res[i])

def scoreCalc(res, path, score=0):

    res = set(res)

    with open(path, 'r') as f:
        lines = f.readlines()

    for i in range(1, len(lines)-1, 2):
        client_like = lines[i].split()
        client_dislike = lines[i+1].split()
        likes = 0
        dislikes = 0

        for j in range(1, len(client_like)):
            if client_like[j] in res:
                likes += 1
        for j in range(1, len(client_dislike)):
            if client_dislike[j] in res:
                dislikes += 1

        if likes == int(client_like[0]) and dislikes == 0:
            score += 1

    return score




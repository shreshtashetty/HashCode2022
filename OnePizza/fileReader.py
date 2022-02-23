def getLikesDislikes(path):
    clients = getClients(path)
    likes = {}
    dislikes = {}
    for client in clients:
        if len(client[0])>0:
            for ing in client[0]:
                if ing in likes:
                    likes[ing] += 1
                else:
                    likes[ing] = 1
        if len(client[1])>0:
            for ing in client[1]:
                if ing in dislikes:
                    dislikes[ing] += 1
                else:
                    dislikes[ing] = 1
    print(len(likes),len(dislikes))
    return likes,dislikes
                        
def getClients(path):
    with open(path, 'r') as f:
        lines = f.readlines()

    clients = []

    for i in range(1, len(lines)):
        line_chars = lines[i].split()
        # print(line_chars)
        if i % 2 == 1:
            num_likes = int(line_chars[0])
            line_chars.pop(0)
            likes = line_chars
        else:
            line_chars.pop(0)
            dislikes = line_chars
            clients.append([likes, dislikes])

    return clients
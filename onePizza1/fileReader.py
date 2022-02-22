def organizeInput(path):
    with open(path, 'r') as f:
        lines = f.readlines()

    clients = []
    num_clients = int(lines[0])

    for i in range(1, len(lines)):
        line_chars = lines[i].split()
        # print(line_chars)
        if i % 2 == 1:
            num_likes = int(line_chars[0])
            line_chars.pop(0)
            likes = line_chars
        else:
            num_dislikes = int(line_chars[0])
            line_chars.pop(0)
            dislikes = line_chars
            clients.append([num_dislikes, likes, dislikes])

    return clients


def countLikeDislikeOccur(path):
    with open(path, 'r') as f:
        lines = f.readlines()
    like, dislike = {}, {}
    # num_clients = int(lines[0])
    # print(num_clients)
    for i in range(1, len(lines)):
        line_chars = lines[i].split()
        # print(line_chars)
        if i % 2 == 1:
            for j in range(1, len(line_chars)):
                like[line_chars[j]] = 1 + like.get(line_chars[j], 0)
        else:
            for j in range(1, len(line_chars)):
                dislike[line_chars[j]] = 1 + dislike.get(line_chars[j], 0)

    # print(like, dislike, "\n\n")
    return like, dislike

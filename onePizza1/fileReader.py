

def fileReader(path):
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



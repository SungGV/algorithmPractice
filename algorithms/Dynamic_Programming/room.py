num_game = int(input())

for _ in range(num_game):
    round = int(input())

    room = [True for _ in range(round)]
    room.insert(0, False)

    for i in range(2, round+1):
        for j in range(1, len(room)):
            if i*j <= len(room)-1:
                room[i*j] = not room[i*j]


    print(sum(room))
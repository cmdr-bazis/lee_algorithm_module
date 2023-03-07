def wave_expansion(listMap, xLocation, yLocation, xGoal, yGoal):
    waveLevel = 0
    listMap[xGoal][yGoal] = str(waveLevel)
    while True:
        for i in range(len(listMap)):
            for j in range(len(listMap[i])):
                if listMap[i][j] == str(waveLevel):
                    if i - 1 >= 0 and listMap[i - 1][j] != "#":
                        if i - 1 == xLocation and j == yLocation:
                            listMap[i - 1][j] = str(waveLevel + 1)
                            return listMap
                        else:
                            listMap[i - 1][j] = str(waveLevel + 1)
                    if i + 1 < len(listMap) and listMap[i + 1][j] != "#":
                        if i + 1 == xLocation and j == yLocation:
                            listMap[i + 1][j] = str(waveLevel + 1)
                            return listMap
                        else:
                            listMap[i + 1][j] = str(waveLevel + 1)
                    if j - 1 >= 0 and listMap[i][j - 1] != "#":
                        if i == xLocation and j - 1 == yLocation:
                            listMap[i][j - 1] = str(waveLevel + 1)
                            return listMap
                        else:
                            listMap[i][j - 1] = str(waveLevel + 1)
                    if j + 1 < len(listMap[i]) and listMap[i][j + 1] != "#":
                        if i == xLocation and j + 1 == yLocation:
                            listMap[i][j + 1] = str(waveLevel + 1)
                            return listMap
                        else:
                            listMap[i][j + 1] = str(waveLevel + 1)
        waveLevel += 1


def waveCheck(string):
    for i in range(len(string)):
        if int(ord(string[i])) < 48 or int(ord(string[i]) > 57):
            return False
    return True


def move(listMap, x, y):
    waveMoveLevel = int(listMap[x][y])
    if x + 1 <= len(listMap):
        if waveCheck(listMap[x + 1][y]):
            if int(listMap[x + 1][y]) == waveMoveLevel - 1:
                return "right"
    if x - 1 >= 0:
        if waveCheck(listMap[x - 1][y]):
            if int(listMap[x - 1][y]) == waveMoveLevel - 1:
                return "left"
    if y + 1 < len(listMap[0]):
        if waveCheck(listMap[x][y + 1]):
            if int(listMap[x][y + 1]) == waveMoveLevel - 1:
                return "down"
    if y - 1 >= 0:
        if waveCheck(listMap[x][y - 1]):
            if int(listMap[x][y - 1]) == waveMoveLevel - 1:
                return "up"
    else:
        return " "

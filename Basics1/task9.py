string1 = input("Enter first string: ")
string2 = input("Enter second string: ")
def levenshtein_distance(s1, s2):
    row = len(string1) + 1
    column = len(string2) + 1
    distance = [[0 for i in range(column)] for i in range(row)]
    for i in range(1, row):
        distance[i][0] = i
    for j in range(1, column):
        distance[0][j] = j
    for i in range(1, row):
        for j in range(1, column):
            if s1[i-1] == s2[j-1]:
                cost = 0
            else:
                cost = 1
            distance[i][j] = min(distance[i-1][j] + 1, distance[i][j-1] + 1, distance[i-1][j-1] + cost)
    return distance[-1][-1]
print("Levenshtein distance:", levenshtein_distance(string1, string2))

from numpy import array
from numpy.linalg import det
import copy

lines = []
filename = "data.txt"

with open(filename) as file_object:
    lines.append(file_object.read())

test = lines[0].split("\n")

result = []

for item in test:
    atmp = []
    tmp = item.split(" ")
    for item2 in tmp:
        atmp.append(int(item2))
    result.append(atmp)

if abs(result[0][0]) < abs(result[1][0]) and abs(result[0][0]) < abs(result[2][0]):
    tmp = copy.deepcopy(result[2])
    result[2] = result[0]
    result[0] = tmp
elif abs(result[1][0]) < abs(result[0][0]) and abs(result[1][0]) < abs(result[2][0]):
    tmp = copy.deepcopy(result[2])
    result[2] = result[1]
    result[1] = tmp
if abs(result[0][0]) < abs(result[1][0]):
    tmp = copy.deepcopy(result[0])
    result[0] = result[1]
    result[1] = tmp

if abs(result[0][0]) == abs(result[1][0]) and abs(result[0][0]) == abs(result[2][0]):
    if abs(result[0][1]) < abs(result[1][1]) and abs(result[0][1]) < abs(result[2][1]):
        tmp = copy.deepcopy(result[2])
        result[2] = result[0]
        result[0] = tmp
    elif abs(result[1][1]) < abs(result[0][1]) and abs(result[1][1]) < abs(
        result[2][1]
    ):
        tmp = copy.deepcopy(result[2])
        result[2] = result[1]
        result[1] = tmp
    if abs(result[0][1]) < abs(result[1][1]):
        tmp = copy.deepcopy(result[0])
        result[0] = result[1]
        result[1] = tmp
elif abs(result[0][0]) == abs(result[1][0]):
    if abs(result[0][1]) < abs(result[1][1]):
        tmp = copy.deepcopy(result[1])
        result[1] = result[0]
        result[0] = tmp
elif abs(result[1][0]) == abs(result[2][0]):
    if abs(result[1][1]) < abs(result[2][1]):
        tmp = copy.deepcopy(result[1])
        result[1] = result[2]
        result[2] = tmp

if result[1][0] == 0:
    if result[2][1] != 0:
        subN = result[2][1] / result[1][1]
        for i in range(3):
            result[2][i] -= subN * result[1][i]
else:
    subN = result[1][0] / result[0][0]
    for i in range(3):
        result[1][i] -= subN * result[0][i]
    if result[2][0] != 0:
        subN = result[2][0] / result[0][0]
        for i in range(3):
            result[2][i] -= subN * result[0][i]
    if abs(result[1][1]) < abs(result[2][1]):
        tmp = copy.deepcopy(result[1])
        result[1] = result[2]
        result[2] = tmp
    if result[2][1] != 0:
        subN = result[2][1] / result[1][1]
        for i in range(3):
            result[2][i] -= subN * result[1][i]

result = array(result)
print(result)

s = [
    [[93, 80], [111, 63], [118, 110]],
    [[111, 63], [118, 110], [287, 64]],
    [[111, 63], [118, 110], [287, 64]],
    [[267, 107], [287, 64], [118, 110],],
    [[267, 107], [287, 64], [296, 79]],
    [[86, 86], [70, 97], [108, 111]],
    [[70, 97], [108, 111], [90, 248]],
    [[90, 248], [49, 251], [70, 97],],
    [[90, 248], [49, 251], [65, 269]],
    [[41, 302], [65, 282], [83, 303],],
    [[41, 302], [83, 303], [62, 440]],
    [[41, 302], [19, 456], [62, 440],],
    [[19, 456], [62, 440], [30, 466]],
    [[71, 277], [96, 252], [90, 299],],
    [[96, 252], [90, 299], [243, 253]],
    [[243, 253], [237, 297], [90, 299]],
    [[243, 253], [237, 297], [262, 274]],
    [[270, 110], [302, 85], [315, 99]],
    [[315, 99], [270, 110], [250, 250]],
    [[315, 100], [291, 251], [250, 250]],
    [[250, 250], [291, 251], [270, 270]],
    [[269, 281], [244, 302], [286, 302],],
    [[244, 302], [286, 302], [266, 453]],
    [[266, 453], [224, 440], [244, 302],],
    [[224, 440], [266, 453], [247, 465]],
    [[48, 489], [37, 474], [70, 442]],
    [[48, 489], [70, 442], [217, 444]],
    [[217, 444], [48, 489], [222, 489]],
    [[222, 489], [217, 444], [240, 474]],
]

for x in s:
    for y in x:
        print(str(y[1] - 50) + ", ", end="")

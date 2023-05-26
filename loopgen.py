def generatestarloop(angle, starange):
    if angle == "right":
        for i in range(0, starange):
            for j in range(0, i+1):
                print("* ", end="")
            print('\r')


def generatenumberloop(numangle, numrange):
    if numangle == "right":
        for i in range(0, numrange):
         for j in range(0, i+1):
            print(f" {j+1}", end="")
        print('\r')
    elif numangle == "left":
        k = numrange*2 - 2
        for i in range(0, numrange):
            for j in range(0, i+1):
                print(f" {k-2}")
            print('\r')

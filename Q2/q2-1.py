import csv
import random
import matplotlib.pyplot as plt

def main():
    f = open('q2.csv','w',encoding='ANSI')
    dice = random.randrange(1,7)
    f.write(str(dice))
    for i in range(99):
        dice = random.randrange(1,7)
        f.write(",")
        f.write(str(dice))

    f.write('\n')

    dice = random.randrange(1,7)
    f.write(str(dice))
    for i in range(999):
        dice = random.randrange(1,7)
        f.write(",")
        f.write(str(dice))

    f.write('\n')

    dice = random.randrange(1,7)
    f.write(str(dice))
    for i in range(9999):
        dice = random.randrange(1,7)
        f.write(",")
        f.write(str(dice))

    f.write('\n')

    dice = random.randrange(1,7)
    f.write(str(dice))
    for i in range(99999):
        dice = random.randrange(1,7)
        f.write(",")
        f.write(str(dice))

        
    f.close()
    
if __name__ == '__main__':
    main()

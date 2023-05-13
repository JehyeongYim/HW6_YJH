import csv
import matplotlib.pyplot as plt


def main():
    h=[]
    t=[]
    tt=[]
    ht=[]
    
    f = open('q2.csv','r',encoding='ANSI')
    data = csv.reader(f)
    
    h = next(data)
    t = next(data)
    tt = next(data)
    ht = next(data)
    
    h.sort()
    t.sort()
    tt.sort()
    ht.sort()
    
    f.close()

    fig, axes = plt.subplots(2,2)
    plt.subplots_adjust(wspace = 0.5, hspace = 0.5)
    axes[0,0].hist(h,bins=range(0,7,1),edgecolor='black')
    axes[0,1].hist(t,bins=range(0,7,1),edgecolor='black')
    axes[1,0].hist(tt,bins=range(0,7,1),edgecolor='black')
    axes[1,1].hist(ht,bins=range(0,7,1),edgecolor='black')
    axes[0,0].set_title("Roll a Dice 100 Times")
    axes[0,1].set_title("Roll a Dice 1000 Times")
    axes[1,0].set_title("Roll a Dice 10000 Times")
    axes[1,1].set_title("Roll a Dice 100000 Times")
    axes[0,0].set_xlabel("Dice Scale")
    axes[0,0].set_ylabel("Number of Result")
    axes[0,1].set_xlabel("Dice Scale")
    axes[0,1].set_ylabel("Number of Result")
    axes[1,0].set_xlabel("Dice Scale")
    axes[1,0].set_ylabel("Number of Result")
    axes[1,1].set_xlabel("Dice Scale")
    axes[1,1].set_ylabel("Number of Result")
    plt.show()
    
if __name__ == '__main__':
    main()

import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def main():
    label = ["Men","Women"]
    color = ["lightblue","hotpink"]

    f = open('2010.csv','r',encoding='ANSI')
    data = csv.reader(f)
    header = next(data)
    first_row = next(data)
    m_2010 = int(first_row[1])
    w_2010 = int(first_row[14])
    l_2010 = [m_2010,w_2010]
    f.close()

    f = open('2014.csv','r',encoding='ANSI')
    data = csv.reader(f)
    header = next(data)
    first_row = next(data)
    m_2014 = int(first_row[1])
    w_2014 = int(first_row[14])
    l_2014 = [m_2014,w_2014]
    f.close()

    f = open('2018.csv','r',encoding='ANSI')
    data = csv.reader(f)
    header = next(data)
    first_row = next(data)
    m_2018 = int(first_row[1])
    w_2018 = int(first_row[14])
    l_2018 = [m_2018,w_2018]
    f.close()

    f = open('2022.csv','r',encoding='ANSI')
    data = csv.reader(f)
    header = next(data)
    first_row = next(data)
    m_2022 = int(first_row[1])
    w_2022 = int(first_row[14])
    l_2022 = [m_2022,w_2022]
    f.close()

    fig, axes = plt.subplots(2,2)
    axes[0,0].pie(l_2010,labels=label, autopct='%.2f%%',colors=color)
    axes[0,1].pie(l_2014,labels=label, autopct='%.2f%%',colors=color)
    axes[1,0].pie(l_2018,labels=label, autopct='%.2f%%',colors=color)
    axes[1,1].pie(l_2022,labels=label, autopct='%.2f%%',colors=color)
    axes[0,0].set_title("Population Ratio of Jeju in 2010")
    axes[0,1].set_title("Population Ratio of Jeju in 2014")
    axes[1,0].set_title("Population Ratio of Jeju in 2018")
    axes[1,1].set_title("Population Ratio of Jeju in 2022")
    axes[0,0].legend(bbox_to_anchor=(0,0))
    plt.show()
       
if __name__ == '__main__':
    main()

import csv
import matplotlib.pyplot as plt


def main():
    whole=[]
    seoul=[]
    daegeon=[]
    busan=[]
    jeju=[]
    
    month = [1,2,3,4,5,6,7,8,9,10,11,12]
    
    f = open('whole.csv','r',encoding='ANSI')
    data = csv.reader(f)
    header = next(data)
    for row in data:
        whole.append(float(row[2]))
    f.close()
    
    f = open('seoul.csv','r',encoding='ANSI')
    data = csv.reader(f)
    header = next(data)
    for row in data:
        seoul.append(float(row[2]))
    f.close()
    
    f = open('daegeon.csv','r',encoding='ANSI')
    data = csv.reader(f)
    header = next(data)
    for row in data:
        daegeon.append(float(row[2]))
    f.close()
    
    f = open('busan.csv','r',encoding='ANSI')
    data = csv.reader(f)
    header = next(data)
    for row in data:
        busan.append(float(row[2]))
    f.close()
    
    f = open('jeju.csv','r',encoding='ANSI')
    data = csv.reader(f)
    header = next(data)
    for row in data:
        jeju.append(float(row[2]))
    f.close()

    plt.title("Locational Temp Difference")
    plt.plot(month, whole, 'g', label="Whole")
    plt.plot(month, seoul, 'purple', label="Seoul")
    plt.plot(month, daegeon, 'b', label="Daegeon")
    plt.plot(month, busan, 'orange', label="Busan")
    plt.plot(month, jeju, 'r', label="Jeju")

    plt.xticks(month)
    plt.yticks(range(-5,31,1))
    plt.legend()
    plt.xlabel("Month")
    plt.ylabel("Temp")
    plt.show()
    
if __name__ == '__main__':
    main()

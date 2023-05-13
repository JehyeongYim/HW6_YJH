import csv
import operator
import matplotlib.pyplot as plt


def main():
    dict1 = {}
    dict2 = {}
    dict3 = {}
    
    f = open('q4.csv','r',encoding='ANSI')
    data = csv.reader(f)
    header1 = next(data)
    header2 = next(data)
    
    for row in data:
        total_in = int(row[10])+int(row[12])
        total_out = int(row[11])+int(row[13])
        total = int(row[10])+int(row[11])+int(row[12])+int(row[13])
    
        if row[3] in dict1:
            dict1.update({row[3]: dict1.get(row[3])+total_in})
        else:
            dict1[row[3]] = total_in

        if row[3] in dict2:
            dict2.update({row[3]: dict2.get(row[3])+total_out})
        else:
            dict2[row[3]] = total_out

        if row[3] in dict3:
            dict3.update({row[3]: dict3.get(row[3])+total})
        else:
            dict3[row[3]] = total

    f.close()

    d1 = sorted(dict1.items(), key=operator.itemgetter(1), reverse=True)
    d2 = sorted(dict2.items(), key=operator.itemgetter(1), reverse=True)
    d3 = sorted(dict3.items(), key=operator.itemgetter(1), reverse=True)
    
    x1 = list(dict(d1).keys())[0:30]
    y1 = list(dict(d1).values())[0:30]
    x2 = list(dict(d2).keys())[0:30]
    y2 = list(dict(d2).values())[0:30]
    x3 = list(dict(d3).keys())[0:30]
    y3 = list(dict(d3).values())[0:30]

    plt.rc('font', family = 'Malgun Gothic')
    plt.rcParams['axes.unicode_minus'] = False

    x1.reverse()
    y1.reverse()
    x2.reverse()
    y2.reverse()
    x3.reverse()
    y3.reverse()

    plt.title("출근시간 최대 승차역 TOP30")
    plt.xlabel("passengers")
    plt.barh(x1,y1)
    plt.show()
    plt.title("출근시간 최대 하차역 TOP30")
    plt.xlabel("passengers")
    plt.barh(x2,y2)
    plt.show()
    plt.title("출근시간 최대 승하차역 TOP30")
    plt.xlabel("passengers")
    plt.barh(x3,y3)
    plt.show()
    
if __name__ == '__main__':
    main()

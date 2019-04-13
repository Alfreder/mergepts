# coding:utf-8
import csv
import time
#https://blog.csdn.net/yzf0011/article/details/72903088
#处理编码问题
start = time.time()
with open('./data/dnacsv.csv','r',encoding="utf-8") as csvfile:
    #print('true')
    reader = csv.reader(csvfile)
    i = 1

    l = []
    for row in reader:
        print("=" * 100)
        print("process line" + str(i))
        i+=1
        l = row[0:2]
        with open('./data/fa.csv', 'r', encoding="utf-8") as csvfile1:
        #print('true')
            reader1 = csv.reader(csvfile1)
            #print('1')
            for rowj in reader1:
                l1 = rowj[0:2]
                if l[0] ==l1[0]:
                    #print(l1[1])
                    l.append(l1[1])
                    print(l)
        if i == 1000:
            break
end = time.time()
print("*"*100)
print('run time')
print(end-start)
#column = [row[1] for row in reader]
#print(column)



'''   
f1 = open('./data/dnacsv.csv', 'r', encoding='utf-8')
f2 = open('./data/fa.csv', 'r', encoding='utf-8')
f3 = open('./data/all_1.txt', 'a+', encoding='utf-8')
d1 = f1.readlines()
d2 = f2.readlines()
# 第二步：读取文件内容
#print(len(d1))
#print(len(d2))
#print(d1[1].replace('\n','').split(","))
#print(d2[1].replace('\n','').split(",")[1])
for row in range(0,10000):
    print("="*30)
    print("process row: "+str(row))
#for i in range(0, len(d1)):
    #print("--")
    #print(d1[i].replace('\n', '').split(","))
    #print(d1[i].replace('\n','').split(",")[0])

    for rowj in range(0,len(d2)):
        #print('**')
        #print(d1[i].replace('\n', '').split(",")[0])
        #print(d1[i].replace('\n', '').split(",")[1])
        #print("---")
        #print(d2[j].replace('\n', '').split(",")[0])
        #print(d2[j].replace('\n', '').split(",")[1])
        #print('***')
        if d1[row].replace('\n','').replace('\r','').split(",")[0] == d2[rowj].replace('\n', '').split(",")[0]:
            #print("true")
            #print(d1[i].replace('\n', '').split(","))
            l = d2[rowj].replace('\n', '').split(",")[1]

            print("| targer line:"+ str(rowj))
            print("| target value:"+l)
            ls = d1[row].replace('\n', '').split(",")[0:-1]
            #print(ls)
            ls.append(l)
            #print(ls)

            for i in range(len(ls)):
                s = str(ls[i]).replace('[', '').replace(']', '') +','
                #f3.write(s)
            #f3.write('\n')
f3.close()
f1.close()
f2.close()
'''

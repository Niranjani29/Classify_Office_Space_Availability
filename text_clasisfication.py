import csv
import math
from sklearn.metrics import accuracy_score

commercial_0 = dict()
commercial_1 = dict()

commercial_0_prob = dict()
commercial_1_prob = dict()

words_count_0=0
words_count_1=0
with open('D:\\RA\\Training_Data.csv', 'r') as rf:
    reader = csv.reader(rf, delimiter=',')
    next(rf)
    for row in reader:
        if row[2]=='0':
            words=row[1].split()
            for word in words:
                if word.isalpha():
                    if word in commercial_0:
                        commercial_0[word]+=1
                    else:
                        commercial_0[word]=1
                    words_count_0+=1
        else:
            words=row[1].split()
            for word in words:
                if word.isalpha():
                    if word in commercial_1:
                        commercial_1[word]+=1
                    else:
                        commercial_1[word]=1
                    words_count_1+=1

total_words= list(set(commercial_0.keys()))+list(set(commercial_1.keys()))
total_words= set(total_words)


for eachword in total_words:


    commercial_0_temp = commercial_0.get(eachword)
    commercial_1_temp = commercial_1.get(eachword)
    if commercial_0_temp:
        commercial_0_prob[eachword] = (commercial_0[eachword] + 1.0)/(words_count_0 + len(total_words))
    else:
        commercial_0_prob[eachword] = (1.0)/(words_count_0 + len(total_words))

    if commercial_1_temp:
        commercial_1_prob[eachword] = (commercial_1[eachword] + 1.0)/(words_count_1 + len(total_words))
    else:
        commercial_1_prob[eachword] = (1.0)/(words_count_1 + len(total_words))

p_0= float(words_count_0)/(words_count_0+words_count_1)
p_1= float(words_count_1)/(words_count_0+words_count_1)


prob_0=math.log(p_0)
prob_1=math.log(p_1)


l=[]
test=[]
with open('D:\\RA\\Testing_Data.csv', 'r') as rf:
    reader = csv.reader(rf, delimiter=',')
    next(rf)
    for row in reader:
        test.append(row[2])
        words=row[1].split()
        for word in words:
            if word.isalpha():
                if commercial_0.get(word):
                    prob_0_temp=prob_0 + math.log(commercial_0[word])
                if commercial_1.get(word):
                    prob_1_temp=prob_1 + math.log(commercial_1[word])
            
        if(prob_0_temp>prob_1_temp):
            l.append('0')
        else:
            l.append('1')


acc=accuracy_score(test, l)
print(acc)
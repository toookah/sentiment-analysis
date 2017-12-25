#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 17:36:56 2017

@author: xuyizhou
"""

filePath='/Users/xuyizhou/Desktop/grade.txt'
fileRead = []
with open(filePath) as fileRaw:
    for line in fileRaw:
        fileRead.append(line)
segs=[]
for i in range(len(fileRead)):
        b=fileRead[i].split("\t")
        segs.append([b[1],b[2],b[6]])
#print(segs)
newSegs=[]
indexes=[]
for i in range(len(fileRead)):
    if(segs[i]!=['', '', ''] and segs[i]!=['课程', '学分', '综合'] 
    and segs[i]!=['', '', '成绩'] and i!=5 and  segs[i]!=['[008201101029]军事训练', '', '通过']):
        #print(i)
        indexes.append(i)
            #newSegs.append([b[1],b[2],b[6]])
grade=[]
for index in indexes:
    grade.append(segs[index])
    #print(grade)
    
def grade2gpa(score):
    if(score=='通过'):
        score=85
    else:
        score=float(score)
    if score>=95:
        gpa=4
    elif score>=90:
        gpa=3.9
    elif score>=85:
        gpa=3.7
    elif score>=81:
        gpa=3.3
    elif score>=78:
        gpa=3.0
    elif score>=75:
        gpa=2.7
    elif score>=71:
        gpa=2.3
    elif score>=68:
        gpa=2.0
    elif score>=64:
        gpa=1.7
    else:
        gpa=1
    return gpa
gpas=[]
for i in range(len(grade)):
    gpas.append(grade2gpa(grade[i][2]))
credit=[]
sumGpa=0
sumCredit=0
for i in range(len(grade)):
    credit=float(grade[i][1])
    sumCredit=credit+sumCredit
    sumGpa=credit*gpas[i]+sumGpa

print(sumGpa/sumCredit)


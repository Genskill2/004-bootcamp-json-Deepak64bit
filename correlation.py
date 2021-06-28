# Add the functions in this file
import json
import math
def load_journal(filename):
    f = open(filename)
    s=f.read()
    content = json.loads(s)
    f.close()
    return content

def compute_phi(filename,event):
    d=load_journal(filename)
    a=[0,0,0,0,0,0,0,0]
    for i in d:
        if(event in i['events']):
            a[4]+=1 
            if(i['squirrel']):
                a[6]+=1
                a[0]+=1
            else :
                a[7]+=1
                a[2]+=1
        else:
            a[5]+=1
            if (i['squirrel']):
                a[6]+=1
                a[3]+=1
            else:
                a[7]+=1
                a[1]+=1
    val=(a[0] * a[1] - a[2] * a[3]) / math.sqrt(a[4] * a[5] * a[6] * a[7])
    return val 

def compute_correlations(filename):
    data={}
    d=load_journal(filename)
    for i in d:
        for j in i['events']:
            if j not in data:
                data[j]=compute_phi(filename,j)
    return data
def diagnose(filename):
    data=compute_correlations(filename)
    maxval = max(data, key = data.get)
    minval = min(data, key = data.get)
    return maxval,minval  
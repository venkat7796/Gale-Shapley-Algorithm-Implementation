import collections
man = {"A":0,"B":1,"C":2}
women = {"D":0,"E":1,"F":2}
manKeyList = list(man.keys())
manValList = list(man.values())
womenKeyList = list(women.keys())
womenValList = list(women.values())
q = collections.deque()
lm = list(man.values())
q.extend(lm)
manMatchList = {0:[0,1,2],1:[1,0,2],2:[0,1,2]}
womenMatchList = {0:[1,0,2],1:[0,1,2],2:[0,1,2]}
womenMatchList1 = {}
manMatching = {0:-1,1:-1,2:-1}
womenMatching = {0:-1,1:-1,2:-1}
def pre_process():
    for k,v in womenMatchList.items():
        nL = [-1] * len(v)
        for val in range(len(v)):
            #print(v[val])
            nL[v[val]] = val
        womenMatchList1[k] = nL
    print(womenMatchList)
    print(womenMatchList1)

def run_algo():
    while q:
        value = q.popleft()
        i = 0
        le = manMatchList[value]
        print(le)
        while i < len(le):
            wo = le[i]
            print(womenMatching)
            if womenMatching[wo] == -1:
                womenMatching[wo] = value
                break
            elif womenMatching[wo] > -1:
                lw = womenMatchList1[wo]
                if lw[value] < lw[womenMatching[wo]]:
                    q.append(womenMatching[wo])
                    womenMatching[wo] = value
                    break
                else:
                    i += 1
pre_process()
run_algo()
print(womenMatching.items())
for k,v in womenMatching.items():
    womK = womenValList.index(k)
    #womV = womenKeyList.index(womK)
    menK = manValList.index(v)
    #menV = menKeyList.index(menK)
    print(manKeyList[menK],womenKeyList[womK])
                    


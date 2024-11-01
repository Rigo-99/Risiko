import numpy as np

esiti = [1,2,3,4,5,6]
ndas = [1,2,3]
ndds = [1,2,3]


# se i dadi sono 3 vs 3

points=np.zeros(shape=(3,3,4))

aa = np.zeros(shape=(3,3))
dd = np.zeros(shape=(3,3))

for a1 in esiti:
    aa[0] = sorted([a1,0,0], reverse=True)
    for a2 in esiti:
        aa[1] = sorted([a1,a2,0], reverse=True)
        for a3 in esiti:
            aa[2] = sorted([a1,a2,a3], reverse=True)
            for d1 in esiti:
                dd[0] = sorted([d1,0,0], reverse=True)
                for d2 in esiti:
                    dd[1] = sorted([d1,d2,0], reverse=True)
                    for d3 in esiti:
                        dd[2] = sorted([d1,d2,d3], reverse=True)
                        
                        for i in ndas:
                            for j in ndds:
                                punti = sum([1 for a, d in zip(aa[i-1], dd[j-1]) if ((a > d) and ((a!=0) and (d!=0)))])
                                points[i-1,j-1,punti] = points[i-1,j-1,punti]+1

ntrials = 6**6

points = points/ntrials

#print("Esiti:\n\n", points)


print ("          D=1           D=2           D=3")
for i in ndas:
    print ("A=",i,sep='',end='  ')
    for j in ndds:
        print("[",end='')
        for k in range(4):
            
            val=round(100.*points[i-1,j-1,k])
            print("{:02d}".format(val),end=' ')
        print("\b] ",end='')
    print()





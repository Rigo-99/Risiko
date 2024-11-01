import numpy as np

def get_positive_integer():
    while True:
        try:
            num = int(input("[enter a positive integer]"))
            if num > 0:
                return num
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid positive integer.")








esiti = [1,2,3,4,5,6]
ndas = [1,2,3]
ndds = [1,2,3]


# se i dadi sono 3 vs 3

print("initializing...")

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

print("Ready")



print("ARMATE ATTACCO:")
armate_attacco = get_positive_integer()

print("ARMATE DIFESA:")
armate_difesa = get_positive_integer()

stato = np.zeros((armate_attacco+1,armate_difesa+1))

stato[armate_attacco,armate_difesa] = 1


nda,ndd = chiedi_dadi()

while (nda!=0):
    
    punteggi = points[nda-1,ndd-1]

    used = min(nda,ndd)
    
    nuovo = np.zeros((armate_attacco+1,armate_difesa+1))
    
    for aa in range(armate_attacco+1):
        for ad in range(armate_difesa+1):
            for i in range(used+1):
                if (aa+used-i <= armate_attacco && ad+i <= armate_difesa):
                    nuovo[aa,ad] = nuovo[aa,ad] + stato[aa+used-i,ad+i] * punteggi[i]
            
    print(nuovo)


    nda,ndd = chiedi_dadi()
    





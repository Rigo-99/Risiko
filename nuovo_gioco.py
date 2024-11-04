import numpy as np

# prima attacco, poi difesa.
class Battaglia:
    def __init__(self, n, m):
        
        # Inizializza la matrice "campo" con tutti zeri
        self.campo = np.zeros((n+1 , m+1))
        
        # Imposta l'elemento (n, m) a 1
        self.campo[n,m] = 1
        
        # Inizializza la lista "active" con la coppia
        self.active = [[n,m,1.0]]
        
        # Inizializza la lista "nds" con la coppia (min(3, n), min(3, m))
        self.nds = [[min(3, n), min(3, m)]]

        self.dadi = np.load('dadi.npy')

    def aggiorna_attivi(self):
        # Prendi tutti elementi non nulli in campo e salvali in lista (na,nd,p).
        indices = np.argwhere(self.campo != 0)
        self.active = [[idx[0], idx[1], self.campo[tuple(idx)]] for idx in indices]
        return


    def dadi_massimi(self):
        self.nds = []
        for sito in self.active:
            x,y,p = sito
            self.nds.append([min(3,x-1),min(3,y)])


    def battaglia(self):
        #aggiorna_attivi()
        #dadi_massimi()      # per ora senza personabilizzazione
        self.campo = np.zeros(self.campo.shape)
        for i,sito in enumerate(self.active):
            self.sparatoria(sito,self.nds[i])
            
    def sparatoria(self, coppia, nds):
        naa,nad,p = coppia
        if (naa<=1 or nad==0):
            self.campo[naa,nad] += p 
        else:
            nda,ndd = nds
            persi = min(nda,ndd)
            for k in range(persi+1):
                x = int(naa - (persi - k))
                y = int(nad - k)
                self.campo[x,y] += p*self.dadi[nda-1][ndd-1][k]


    def guerra_maxi(self):
        for _ in range(max(self.campo.shape)):
            self.aggiorna_attivi()
            self.dadi_massimi()
            self.battaglia()
        self.view_campo()


    def view_campo(self):
        # Usa np.array_str per formattare l'array con 2 cifre decimali
        formatted_matrix = np.array_str(self.campo, precision=5, suppress_small=True)
        print(formatted_matrix)
        p_win = np.sum(self.campo[:,0])
        p_lose = np.sum(self.campo[1,:])

        print('terrotorio conquistato con probabilita\'',p_win)
        print('battaglia persa con probabilita\'       ',p_lose)
        return

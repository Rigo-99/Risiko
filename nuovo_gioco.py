import numpy as np

# prima attacco, poi difesa.
class Battaglia:
    def __init__(self, n, m):
        
        # Inizializza la matrice "campo" con tutti zeri
        self.campo = np.zeros(n+1 , m+1)
        
        # Imposta l'elemento (n, m) a 1
        self.campo[n,m] = 1
        
        # Inizializza la lista "active" con la coppia (n, m)
        self.active = [(n, m)]
        
        # Inizializza la lista "nds" con la coppia (min(3, n), min(3, m))
        self.nds = [(min(3, n), min(3, m))]

        self.dadi = np.load('dadi.npy')
    
    def battaglia(self):
        # Prendi tutti elementi non nulli in campo e salvali in lista (na,nd,p).
        # Azzera il campo
        # Per ogni coppia in active
            # Distribuisci (elimina originale e aggiungi successivi) e aggiungi ad active
            
        #esegui unique su active



    def sparatoria(self, coppia):
        naa, nad = coppia
        





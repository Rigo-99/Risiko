import tkinter as tk
import numpy as np
import random
from matplotlib import cm
from matplotlib.colors import Normalize

# Dimensione fissa dell'area di visualizzazione della matrice
AREA_SIZE = 300  # Dimensione fissa in pixel per la matrice

# Creazione della finestra principale con dimensione iniziale fissa
root = tk.Tk()
root.title("Matrice Colorata con Tkinter")
root.geometry("400x500")  # Dimensione iniziale per ospitare matrice e pulsanti

# Funzione per ottenere un colore dalla colormap in base al valore
def get_color(value, norm, colormap):
    rgba = colormap(norm(value))
    return f'#{int(rgba[0]*255):02x}{int(rgba[1]*255):02x}{int(rgba[2]*255):02x}'

# Funzione per mostrare il valore della cella
def on_enter(event, i, j):
    label_value.config(text=f"Valore: {matr[i][j]}")

# Funzione per ripristinare il testo quando si esce dalla cella
def on_leave(event):
    label_value.config(text="Valore:")

# Funzione per gestire il clic sul pulsante "Attacco"
def on_attacco_click():
    print("Hai premuto 'Attacco'!")

# Funzione per gestire il clic sul pulsante "Destino"
def on_destino_click():
    print("Hai premuto 'Destino'!")

# Funzione per generare e visualizzare la matrice casuale
def generate_matrix():
    global matr, frame

    try:
        num1 = int(entry_num1.get())
        num2 = int(entry_num2.get())

        # Genera una matrice casuale di dimensioni num1 x num2
        matr = [[random.randint(1, 100) for _ in range(num2)] for _ in range(num1)]

        # Normalizza i valori per la colormap
        matr_np = np.array(matr)
        norm = Normalize(vmin=matr_np.min(), vmax=matr_np.max())
        colormap = cm.get_cmap("viridis")

        # Cancella la griglia esistente
        for widget in frame.winfo_children():
            widget.destroy()

        # Calcola la dimensione quadrata delle celle in base a AREA_SIZE
        cell_size = min(AREA_SIZE // num1, AREA_SIZE // num2)

        # Ricrea la griglia colorata per la nuova matrice
        for i in range(num1):
            for j in range(num2):
                color = get_color(matr[i][j], norm, colormap)
                cell = tk.Label(frame, width=cell_size//10, height=cell_size//20,
                                bg=color, borderwidth=1, relief="solid")
                cell.grid(row=i, column=j, padx=1, pady=1)
                cell.bind("<Enter>", lambda event, x=i, y=j: on_enter(event, x, y))
                cell.bind("<Leave>", on_leave)

        label_result.config(text=f"Matrice di {num1} x {num2} generata con successo.")

    except ValueError:
        label_result.config(text="Inserisci numeri validi per le dimensioni!")

# Creazione del pulsante "Attacco"
button_attacco = tk.Button(root, text="Attacco", command=on_attacco_click)
button_attacco.pack(pady=10)

# Creazione del pulsante "Destino"
button_destino = tk.Button(root, text="Destino", command=on_destino_click)
button_destino.pack(pady=10)

# Etichetta per mostrare il valore della cella
label_value = tk.Label(root, text="Valore:", font=("Arial", 12))
label_value.pack(pady=10)

# Frame per la griglia della matrice con dimensione fissa
frame = tk.Frame(root, width=AREA_SIZE, height=AREA_SIZE)
frame.pack_propagate(False)  # Mantiene il frame alla dimensione fissa
frame.pack()

# Sezione per inserire due numeri con layout compatto
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

label_num1 = tk.Label(input_frame, text="Numero 1:")
label_num1.grid(row=0, column=0, padx=5)
entry_num1 = tk.Entry(input_frame, width=5)  # Larghezza ridotta
entry_num1.grid(row=0, column=1, padx=5)

label_num2 = tk.Label(input_frame, text="Numero 2:")
label_num2.grid(row=0, column=2, padx=5)
entry_num2 = tk.Entry(input_frame, width=5)  # Larghezza ridotta
entry_num2.grid(row=0, column=3, padx=5)

# Pulsante per generare la matrice
button_read = tk.Button(input_frame, text="Inizia battaglia", command=generate_matrix)
button_read.grid(row=0, column=4, padx=10)

# Etichetta per mostrare messaggi o errori
label_result = tk.Label(root, text="Inserisci le dimensioni della matrice e premi 'Leggi Valori'", font=("Arial", 12))
label_result.pack(pady=10)

# Avvio del loop dell'interfaccia grafica
root.mainloop()


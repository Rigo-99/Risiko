import tkinter as tk
import numpy as np
import random
from matplotlib import cm
from matplotlib.colors import Normalize, LinearSegmentedColormap
import nuovo_gioco as ng

# Dimensione fissa dell'area di visualizzazione della matrice
AREA_SIZE = 300  # Dimensione fissa in pixel per la matrice

# Creazione della finestra principale con dimensione iniziale fissa
root = tk.Tk()
root.title("Matrice Colorata con Tkinter")
root.geometry("400x550")  # Dimensione iniziale per ospitare matrice e pulsanti

# Creazione di una colormap dal bianco al blu
custom_colormap = LinearSegmentedColormap.from_list("white_to_blue", ["white", "blue"])

# Funzione per ottenere un colore dalla colormap in base al valore
def get_color(value, colormap):
    rgba = colormap(value)
    return f'#{int(rgba[0]*255):02x}{int(rgba[1]*255):02x}{int(rgba[2]*255):02x}'

# Funzione per mostrare il valore della cella
def on_enter(event, i, j):
    label_value.config(text=f"A={i} | D={j} : p={war.campo[i][j]:.3f}")

# Funzione per ripristinare il testo quando si esce dalla cella
def on_leave(event):
    label_value.config(text="")





# Funzione per gestire il clic sul pulsante "Inizia battaglia"
def start_war():
    global war
    war = ng.Battaglia(int(entry_num1.get()),int(entry_num2.get()))
    draw_matrix()
    button_attacco.config(state='normal')
    button_destino.config(state='normal')


# Funzione per gestire il clic sul pulsante "Attacco"
def on_attacco_click():
    war.dadi_massimi()
    war.battaglia()
    war.aggiorna_attivi()
    draw_matrix()

# Funzione per gestire il clic sul pulsante "Destino"
def on_destino_click():
    war.decadi()
    label_result.config(text = f"A:{war.outcome[0]} | D:{war.outcome[1]}")
    war.post_decadimento()
    draw_matrix()



# Funzione per generare e visualizzare la matrice casuale
def draw_matrix():

    matr = war.campo

    num1 = matr.shape[0]
    num2 = matr.shape[1]

    # Normalizza i valori per la colormap
    matr_np = np.array(matr)

    # Cancella la griglia esistente
    for widget in frame.winfo_children():
        widget.destroy()

    # Calcola la dimensione quadrata delle celle in base a AREA_SIZE
    cell_size = min(AREA_SIZE // num1, AREA_SIZE // num2)

    # Ricrea la griglia colorata per la nuova matrice
    for i in range(num1):
        for j in range(num2):
            finto = (i==0 or (i==1 and j==0))
            if finto:
                color = '#BBBBBB'
                bw=0
            else:
                color = get_color(matr[i][j], custom_colormap)
                bw=1
            cell = tk.Label(frame, width=cell_size // 10, height=cell_size // 20,
                            bg=color, borderwidth=bw, relief="solid")
            cell.grid(row=i, column=j, padx=1, pady=1)
            if not finto:
                cell.bind("<Enter>", lambda event, x=i, y=j: on_enter(event, x, y))
                cell.bind("<Leave>", on_leave)
            #cell.bind("<Click>", print("CLICK!"))

    label_result.config(text=f"Vittoria:{war.p_winning():.2f} | Sconfitta:{war.p_losing():.2f}")



# Creazione dei pulsanti "Attacco" e "Destino" nella stessa linea
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

button_attacco = tk.Button(button_frame, text="Attacco", command=on_attacco_click, state="disabled")
button_attacco.grid(row=0, column=0, padx=5)

button_destino = tk.Button(button_frame, text="Destino", command=on_destino_click, state="disabled")
button_destino.grid(row=0, column=1, padx=5)

# Etichetta per mostrare il valore della cella
label_value = tk.Label(root, text="", font=("Arial", 12))
label_value.pack(pady=10)

# Frame per la griglia della matrice con dimensione fissa
frame = tk.Frame(root, width=AREA_SIZE, height=AREA_SIZE)
frame.pack_propagate(False)  # Mantiene il frame alla dimensione fissa
frame.pack()

# Sezione per inserire due numeri con layout compatto
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

label_num1 = tk.Label(input_frame, text="Attacco")
label_num1.grid(row=0, column=0, padx=5)
entry_num1 = tk.Entry(input_frame, width=5)
entry_num1.grid(row=0, column=1, padx=5)

label_num2 = tk.Label(input_frame, text="Difesa:")
label_num2.grid(row=0, column=2, padx=5)
entry_num2 = tk.Entry(input_frame, width=5)
entry_num2.grid(row=0, column=3, padx=5)

# Pulsante per generare la matrice
button_generate_matrix = tk.Button(input_frame, text="Nuova battaglia", command=start_war)
button_generate_matrix.grid(row=0, column=4, padx=10)

# Etichetta per mostrare messaggi o errori
label_result = tk.Label(root, text="Inserisci armate di attacco e difesa", font=("Arial", 12))
label_result.pack(pady=10)

# Avvio del loop dell'interfaccia grafica
root.mainloop()


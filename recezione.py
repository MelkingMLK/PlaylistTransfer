import tkinter as tk
from tkinter import messagebox

# Funzione per ricevere il testo dalla casella e mostrarlo
def mostra_testo():
    send_link = send_link_textbox.get("1.0", tk.END).strip()  # Ottieni il testo send
    if send_link:
        testo = send_link
        dest_link =  dest_link_textbox.get("1.0", tk.END).strip()  # Ottieni il testo send
        if dest_link:
            testo = testo + dest_link
        output_label.config(text=f"Hai scritto:\n{testo}")

    else:
        messagebox.showwarning("Avviso", "La casella di testo è vuota!")

# Creazione della finestra principale
root = tk.Tk()
root.title("Casella di Testo Grafica")
root.geometry("600x450")  # Dimensione della finestra
root.config(bg="#e1e1e1")  # Colore di sfondo

# Titolo Send
send_link_label = tk.Label(root, text="Inserisci il link della playlist originale ", font=("Arial", 16, "bold"), bg="#e1e1e1", fg="#000000")
send_link_label.pack(pady=10)

# insert link send
send_link_textbox = tk.Text(root, height=5, width=40, font=("Arial", 12), relief="solid", borderwidth=2)
send_link_textbox.pack(pady=10)

# Titolo Dest
dest_link_label = tk.Label(root, text="Inserisci il link della playlist di destinazione ", font=("Arial", 16, "bold"), bg="#e1e1e1", fg="#000000")
dest_link_label.pack(pady=10)

# insert link dest
dest_link_textbox = tk.Text(root, height=5, width=40, font=("Arial", 12), relief="solid", borderwidth=2)
dest_link_textbox.pack(pady=10)

# Pulsante di invio
send_button = tk.Button(root, text="Invia", font=("Arial", 12, "bold"), bg="#007399", fg="white", command=mostra_testo)
send_button.pack(pady=5)

# Etichetta per mostrare il testo inviato
output_label = tk.Label(root, text="", font=("Arial", 12), bg="#e1e1e1", fg="#005266", wraplength=380, justify="center")
output_label.pack(pady=10)

# Avvio del loop principale di Tkinter
root.mainloop()
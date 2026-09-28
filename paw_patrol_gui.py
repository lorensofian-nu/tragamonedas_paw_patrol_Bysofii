import random
import time
import tkinter as tk
from tkinter import messagebox

# Configuracion de simbolos de Paw Patrol, probabilidades y multiplicadores
SIMBOLOS = {
    "🐶\nChase": {"peso": 30, "multiplicador": 2},
    "🔥\nMarshall": {"peso": 30, "multiplicador": 2},
    "🚁\nSkye": {"peso": 20, "multiplicador": 4},
    "🛠️\nRubble": {"peso": 15, "multiplicador": 6},
    "🦴\nHueso Oro": {"peso": 5, "multiplicador": 15}
}

LISTA_SIMBOLOS = list(SIMBOLOS.keys())
PESOS = [SIMBOLOS[s]["peso"] for s in LISTA_SIMBOLOS]


class PawPatrolSlotsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tragamonedas Los Paw Patrol 🐾")
        self.root.geometry("460x520")
        self.root.resizable(False, False)
        self.root.configure(bg="#1E1E1E")  # Fondo oscuro

        self.saldo = 100

        self.crear_interfaz()

    def crear_interfaz(self):
        # Titulo principal
        titulo = tk.Label(
            self.root,
            text="🐾 PAW PATROL SLOTS 🐾",
            font=("Helvetica", 18, "bold"),
            bg="#1E1E1E",
            fg="#B08BBB"  # Tono lila pastel
        )
        titulo.pack(pady=10)

        # Lema / Subtitulo
        subtitulo = tk.Label(
            self.root,
            text="¡Ninguna apuesta es demasiado grande!\n¡Ningún cachorro es demasiado pequeño!",
            font=("Helvetica", 9, "italic"),
            bg="#1E1E1E",
            fg="#A0C4FF"  # Baby blue
        )
        subtitulo.pack(pady=2)

        # Contenedor de Saldo
        self.lbl_saldo = tk.Label(
            self.root,
            text=f"💰 Saldo: {self.saldo} monedas",
            font=("Helvetica", 13, "bold"),
            bg="#1E1E1E",
            fg="#FDFFB6"  # Amarillo pastel
        )
        self.lbl_saldo.pack(pady=10)

        # Marco para los carretes de la tragamonedas
        frame_carretes = tk.Frame(self.root, bg="#2D2D2D", bd=3, relief="ridge")
        frame_carretes.pack(pady=15, padx=20)

        self.lbl_carrete1 = tk.Label(
            frame_carretes,
            text="🐶\nChase",
            font=("Helvetica", 16, "bold"),
            width=7,
            height=3,
            bg="#1E1E1E",
            fg="#FFFFFF",
            bd=2,
            relief="solid"
        )
        self.lbl_carrete1.grid(row=0, column=0, padx=8, pady=10)

        self.lbl_carrete2 = tk.Label(
            frame_carretes,
            text="🔥\nMarshall",
            font=("Helvetica", 16, "bold"),
            width=7,
            height=3,
            bg="#1E1E1E",
            fg="#FFFFFF",
            bd=2,
            relief="solid"
        )
        self.lbl_carrete2.grid(row=0, column=1, padx=8, pady=10)

        self.lbl_carrete3 = tk.Label(
            frame_carretes,
            text="🚁\nSkye",
            font=("Helvetica", 16, "bold"),
            width=7,
            height=3,
            bg="#1E1E1E",
            fg="#FFFFFF",
            bd=2,
            relief="solid"
        )
        self.lbl_carrete3.grid(row=0, column=2, padx=8, pady=10)

        # Entrada de apuesta
        frame_apuesta = tk.Frame(self.root, bg="#1E1E1E")
        frame_apuesta.pack(pady=5)

        lbl_apuesta = tk.Label(
            frame_apuesta,
            text="Apuesta:",
            font=("Helvetica", 11, "bold"),
            bg="#1E1E1E",
            fg="#FFFFFF"
        )
        lbl_apuesta.pack(side="left", padx=5)

        self.txt_apuesta = tk.Entry(
            frame_apuesta,
            font=("Helvetica", 11, "bold"),
            width=8,
            justify="center"
        )
        self.txt_apuesta.insert(0, "10")
        self.txt_apuesta.pack(side="left", padx=5)

        # Boton de Girar
        self.btn_girar = tk.Button(
            self.root,
            text="🎰 ¡GIRAR!",
            font=("Helvetica", 14, "bold"),
            bg="#A0C4FF",
            fg="#1E1E1E",
            activebackground="#B08BBB",
            cursor="hand2",
            command=self.iniciar_giro
        )
        self.btn_girar.pack(pady=15, ipadx=10, ipady=3)

        # Etiqueta de Resultado / Mensaje
        self.lbl_mensaje = tk.Label(
            self.root,
            text="¡Ingresa tu apuesta y presiona GIRAR!",
            font=("Helvetica", 10, "bold"),
            bg="#1E1E1E",
            fg="#FFFFFF",
            wraplength=400
        )
        self.lbl_mensaje.pack(pady=5)

    def iniciar_giro(self):
        entrada_apuesta = self.txt_apuesta.get().strip()

        # Validaciones de entrada
        if not entrada_apuesta:
            messagebox.showerror("Error", "Por favor ingresa una apuesta.")
            return

        if not entrada_apuesta.isdigit():
            messagebox.showerror("Error", "Por favor ingresa un numero valido para la apuesta.")
            return

        apuesta = int(entrada_apuesta)

        if apuesta <= 0:
            messagebox.showwarning("Atencion", "La apuesta debe ser mayor a 0.")
            return

        if apuesta > self.saldo:
            messagebox.showwarning("Atencion", "No tienes suficiente saldo para esta apuesta.")
            return

        # Desactivar boton durante la animacion
        self.btn_girar.config(state="disabled")
        self.saldo -= apuesta
        self.lbl_saldo.config(text=f"💰 Saldo: {self.saldo} monedas")
        self.lbl_mensaje.config(text="🔄 Girando la Bahia de Aventuras...", fg="#A0C4FF")

        # Animacion del giro
        self.animar_giro(0, apuesta)

    def animar_giro(self, paso, apuesta):
        if paso < 10:
            c1 = random.choice(LISTA_SIMBOLOS)
            c2 = random.choice(LISTA_SIMBOLOS)
            c3 = random.choice(LISTA_SIMBOLOS)

            self.lbl_carrete1.config(text=c1)
            self.lbl_carrete2.config(text=c2)
            self.lbl_carrete3.config(text=c3)

            # Programar siguiente cuadro de animacion
            self.root.after(100, self.animar_giro, paso + 1, apuesta)
        else:
            self.finalizar_giro(apuesta)

    def finalizar_giro(self, apuesta):
        # Obtener resultado real basado en probabilidades
        res1, res2, res3 = random.choices(LISTA_SIMBOLOS, weights=PESOS, k=3)

        self.lbl_carrete1.config(text=res1)
        self.lbl_carrete2.config(text=res2)
        self.lbl_carrete3.config(text=res3)

        # Calcular premios
        if res1 == res2 == res3:
            mult = SIMBOLOS[res1]["multiplicador"] * 2
            ganancia = apuesta * mult
            self.saldo += ganancia
            nombre_simbolo = res1.split("\n")[1]
            self.lbl_mensaje.config(
                text=f"!!!GRAN TRABAJO, CACHORROS!!! 🐾\n3x {nombre_simbolo} -> !Ganaste {ganancia} monedas!",
                fg="#FDFFB6"
            )
        elif res1 == res2 or res2 == res3 or res1 == res3:
            # Determinar cual es el par
            if res1 == res2:
                coincidencia = res1
            elif res2 == res3:
                coincidencia = res2
            else:
                coincidencia = res1
            mult = SIMBOLOS[coincidencia]["multiplicador"]
            ganancia = apuesta * mult
            self.saldo += ganancia
            nombre_simbolo = coincidencia.split("\n")[1]
            self.lbl_mensaje.config(
                text=f"!Par de {nombre_simbolo}! 🐾\nGanaste {ganancia} monedas.",
                fg="#A0C4FF"
            )
        else:
            self.lbl_mensaje.config(
                text="!Sin suerte esta vez! Intentalo de nuevo.",
                fg="#FFADAD"
            )

        self.lbl_saldo.config(text=f"💰 Saldo: {self.saldo} monedas")
        self.btn_girar.config(state="normal")

        # Verificar bancarrota
        if self.saldo <= 0:
            messagebox.showinfo(
                "Fin del juego",
                "😭 Te has quedado sin monedas. !Ryder te espera para la proxima!"
            )
            self.btn_girar.config(state="disabled")


if __name__ == "__main__":
    root = tk.Tk()
    app = PawPatrolSlotsApp(root)
    root.mainloop()

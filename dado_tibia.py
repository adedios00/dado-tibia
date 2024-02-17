import tkinter as tk
from tkinter import ttk

class RuletaJuego:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Juego del dado")
        self.ventana.geometry("400x300")
        
        self.balance = 0
        self.apuesta_default = 0
        self.dinero_extra = 0
        
        estilo = ttk.Style()
        estilo.configure("TButton", font=("Helvetica", 12), padding=10)
        estilo.configure("TLabel", font=("Helvetica", 12))
        estilo.configure("BotonAzulClaro.TButton", background="light blue")
        estilo.configure("BotonesPequenos.TButton", font=("Helvetica", 10))
        
        self.frame_principal = tk.Frame(ventana)
        self.frame_principal.pack(pady=20)
        
        self.etiqueta_apuesta = ttk.Label(self.frame_principal, text="Introduce apuesta:")
        self.etiqueta_apuesta.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        
        self.entry_apuesta = ttk.Entry(self.frame_principal)
        self.entry_apuesta.insert(0, str(self.apuesta_default))
        self.entry_apuesta.grid(row=0, column=1, padx=10, pady=5)
        
        self.etiqueta_dinero_extra = ttk.Label(self.frame_principal, text="Introduce dinero:")
        self.etiqueta_dinero_extra.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        
        self.entry_dinero_extra = ttk.Entry(self.frame_principal)
        self.entry_dinero_extra.insert(0, str(self.dinero_extra))
        self.entry_dinero_extra.grid(row=1, column=1, padx=10, pady=5)
        
        self.frame_radio = tk.Frame(self.frame_principal)
        self.frame_radio.grid(row=2, columnspan=2, pady=5)
        
        self.resultado_var = tk.StringVar(value="Ganó")  # Valor por defecto
        self.radio_gano = ttk.Radiobutton(self.frame_radio, text="Ganó", variable=self.resultado_var, value="Ganó")
        self.radio_gano.pack(side=tk.LEFT, padx=5)
        self.radio_perdio = ttk.Radiobutton(self.frame_radio, text="Perdió", variable=self.resultado_var, value="Perdió")
        self.radio_perdio.pack(side=tk.LEFT, padx=5)
        
        self.boton_apostar_todo = ttk.Button(self.frame_principal, text="Apostar todo", command=self.apostar_todo)
        self.boton_apostar_todo.grid(row=3, column=0, padx=5, pady=10)
        
        self.boton_calcular = ttk.Button(self.frame_principal, text="Calcular", command=self.calcular, style="BotonAzulClaro.TButton")
        self.boton_calcular.grid(row=3, column=1, padx=5, pady=10)
        
        self.etiqueta_balance = ttk.Label(self.frame_principal, text="Balance:")
        self.etiqueta_balance.grid(row=4, columnspan=2, pady=5)
        
        self.actualizar_balance()  # Actualizar el balance al iniciar
        
        self.frame_botones = tk.Frame(self.frame_principal)
        self.frame_botones.grid(row=5, columnspan=2, pady=5)
        
        self.boton_reset = ttk.Button(self.frame_botones, text="Reset", command=self.reset, style="BotonesPequenos.TButton")
        self.boton_reset.pack(side=tk.LEFT, padx=5)
        
        self.boton_finalizar = ttk.Button(self.frame_botones, text="Finalizar Juego", command=self.finalizar_juego, style="BotonesPequenos.TButton")
        self.boton_finalizar.pack(side=tk.LEFT, padx=5)
        
    def apostar_todo(self):
        self.entry_apuesta.delete(0, tk.END)
        self.entry_apuesta.insert(0, str(self.balance))
        
    def calcular(self):
        try:
            apuesta = float(self.entry_apuesta.get())
            dinero_extra = float(self.entry_dinero_extra.get())
        except ValueError:
            return
        
        if apuesta <= 0:
            return
        
        self.dinero_extra = 0  # Resetear el campo "Introduce dinero"
        
        resultado = self.resultado_var.get()
        if resultado == "Ganó":
            ganancia = 0.8 * apuesta
            self.balance += ganancia + dinero_extra
        elif resultado == "Perdió":
            perdida = apuesta
            self.balance -= perdida + dinero_extra
            
        if self.balance < 0:
            self.balance = 0  # Asegurarse de que el balance nunca sea negativo
        
        self.actualizar_balance()
        self.entry_dinero_extra.delete(0, tk.END)  # Limpiar el campo "Introduce dinero"
        self.entry_dinero_extra.insert(0, str(self.dinero_extra))
        
    def actualizar_balance(self):
        self.etiqueta_balance.config(text=f"Balance: {self.balance:.2f}")
        
    def reset(self):
        self.balance = 0
        self.apuesta_default = 0
        self.dinero_extra = 0
        self.entry_apuesta.delete(0, tk.END)
        self.entry_dinero_extra.delete(0, tk.END)
        self.entry_apuesta.insert(0, str(self.apuesta_default))
        self.entry_dinero_extra.insert(0, str(self.dinero_extra))
        self.actualizar_balance()
        
    def finalizar_juego(self):
        self.ventana.destroy()

if __name__ == "__main__":
    ventana_principal = tk.Tk()
    juego = RuletaJuego(ventana_principal)
    ventana_principal.mainloop()

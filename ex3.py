import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import subprocess
import os

class VideoResizer(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title('Redimensionador de Vídeo')

        # Crear estil per als botons
        style = ttk.Style()

        # Estil per al botó "Navegar" (blau)
        style.configure('Navegar.TButton', foreground='#ffffff', background='#2196F3')  # Text blanc i fons blau

        # Estil per al botó "Redimensionar Vídeo" (lila)
        style.configure('Redimensionar.TButton', foreground='#ffffff', background='#9C27B0')  # Text blanc i fons lila

        # Crear etiques i entrades per l'arxiu d'entrada
        self.input_label = tk.Label(self, text='Vídeo d\'Entrada:')
        self.input_entry = ttk.Entry(self, state='disabled')
        self.input_button = ttk.Button(self, text='Navegar', command=self.browse_input, style='Navegar.TButton')

        # Crear etiques i entrades per l'arxiu de sortida
        self.output_label = tk.Label(self, text='Vídeo de Sortida:')
        self.output_entry = ttk.Entry(self, state='disabled')

        # Crear etiques i entrades per la nova resolució
        self.resolution_label = tk.Label(self, text='Nova Resolució:')
        self.resolution_entry = ttk.Entry(self)

        # Crear botó per redimensionar el vídeo amb color diferent
        self.resize_button = ttk.Button(self, text='Redimensionar Vídeo', command=self.resize_video, style='Redimensionar.TButton')

        # Organitzar els widgets a la graella
        self.input_label.grid(row=0, column=0, sticky='w', padx=5, pady=5)
        self.input_entry.grid(row=0, column=1, columnspan=2, sticky='we', padx=5, pady=5)
        self.input_button.grid(row=0, column=3, sticky='e', padx=5, pady=5)

        self.output_label.grid(row=1, column=0, sticky='w', padx=5, pady=5)
        self.output_entry.grid(row=1, column=1, columnspan=2, sticky='we', padx=5, pady=5)

        self.resolution_label.grid(row=2, column=0, sticky='w', padx=5, pady=5)
        self.resolution_entry.grid(row=2, column=1, sticky='we', padx=5, pady=5)

        self.resize_button.grid(row=3, column=0, columnspan=4, pady=10)

    def browse_input(self):
        # Obtenir la ruta de l'arxiu d'entrada mitjançant un diàleg de navegació
        file_path = filedialog.askopenfilename(filetypes=[('Fitxers de Vídeo', '*.mp4;*.webm'), ('Tots els fitxers', '*.*')])
        if file_path:
            # Habilitar l'entrada d'arxiu, mostrar la ruta i desactivar l'entrada
            self.input_entry.configure(state='normal')
            self.input_entry.delete(0, tk.END)
            self.input_entry.insert(0, file_path)
            self.input_entry.configure(state='disabled')

            # Generar automàticament el nom de l'arxiu de sortida
            input_directory, input_filename = os.path.split(file_path)
            output_filename = f"redimensionat_{input_filename}"
            self.output_entry.configure(state='normal')
            self.output_entry.delete(0, tk.END)
            self.output_entry.insert(0, os.path.join(input_directory, output_filename))
            self.output_entry.configure(state='disabled')

    def resize_video(self):
        # Obtenir les rutes i la resolució des de les entrades
        input_file = self.input_entry.get()
        output_file = self.output_entry.get()
        resolution = self.resolution_entry.get()

        # Comprovar que totes les entrades estan proporcionades
        if not input_file or not output_file or not resolution:
            messagebox.showerror('Error', 'Si us plau, proporciona el vídeo d\'entrada, el vídeo de sortida i la resolució.')
            return

        try:
            # Intentar obtenir l'amplada i l'altura de la resolució
            width, height = map(int, resolution.split('x'))
        except ValueError:
            messagebox.showerror('Error', 'Format de resolució no vàlid. Utilitza Amplada x Altura (p. ex., 640x480).')
            return

        # Crear la comanda ffmpeg per redimensionar el vídeo
        command = f"ffmpeg -i {input_file} -vf scale={width}:{height} -c:a copy {output_file}"
        subprocess.run(command, shell=True)
        messagebox.showinfo('Èxit', 'Redimensionament de vídeo completat amb èxit.')

if __name__ == '__main__':
    # Iniciar l'aplicació
    app = VideoResizer()
    app.mainloop()






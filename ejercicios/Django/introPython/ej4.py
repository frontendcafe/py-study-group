import tkinter as tk
from tkinter import filedialog

def file_read() -> str:
    '''
    Abro el explorador para buscar un archivo y obtener su ruta
    '''
    file_path = filedialog.askopenfilename()
    return file_path

def read_text(path: str) -> list:
#     '''
#     Leo un archivo de texto (*.txt) y devuelvo un lista con las lineas
#     '''
	lines = []
	with open(path) as f:
	    lines = f.readlines()
	return lines


root = tk.Tk()
root.withdraw()

file_dir = file_read()
lineas = read_text(file_dir)

for line in lineas:
    print(line.strip('\n'))



# Easter egg: comentá todo lo anterior y descomentá la siguiente línea:
# import this

# + info: https://www.python.org/dev/peps/pep-0020/
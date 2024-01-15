import os
import subprocess
import random

ruta = '/media/playlist/todo'
rutaMpc = 'todo/'

subprocess.run(['mpc', 'clear'])

archivos = []
for nombre_archivo in os.listdir(ruta):
    archivos.append(nombre_archivo)

listadoMpc = random.sample(archivos, 250)

for fileMpc in listadoMpc:
    subprocess.run(['mpc', 'add', rutaMpc+fileMpc])

subprocess.run(['mpc', 'play'])
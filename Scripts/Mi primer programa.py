import os # importar la librería os

cpu_num = os.cpu_count() # ~~ener~~ obtener el número de CPU en el sistema
print(f"Mi computadora tiene {cpu_num} núcleos de CPU")
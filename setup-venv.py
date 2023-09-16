import os
import subprocess
import sys

# Nome do ambiente virtual
venv_name = "meu_ambiente_virtual"

# Lista de pacotes a serem instalados
pacotes_a_instalar = ["pacote1", "pacote2", "pacote3"]

# Verifica se o ambiente virtual já existe
if not os.path.exists(venv_name):
    # Cria um novo ambiente virtual
    subprocess.run([sys.executable, "-m", "venv", venv_name])

# Ativa o ambiente virtual
if sys.platform == "win32":
    activate_script = os.path.join(venv_name, "Scripts", "activate")
else:
    activate_script = os.path.join(venv_name, "bin", "activate")

# Ativa o ambiente virtual
activate_cmd = f"source {activate_script}"
subprocess.run(activate_cmd, shell=True)

# Instala os pacotes especificados
for pacote in pacotes_a_instalar:
    subprocess.run(["pip", "install", pacote])

print(f"Ambiente virtual '{venv_name}' criado e pacotes instalados.")
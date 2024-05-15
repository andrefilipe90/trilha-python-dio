import os
import shutil
from pathlib import Path

print(Path(__file__).parent)
ROOT_PATH = Path(__file__).parent

os.rename(ROOT_PATH / 'pasta_teste22', ROOT_PATH / 'pasta_teste2')

os.remove(ROOT_PATH / 'pasta_teste2')

# os.mkdir(ROOT_PATH / 'pasta_teste')

# os.mkdir(ROOT_PATH / "novo-diretorio")

# arquivo = open(ROOT_PATH / "novo.txt", "w")
# arquivo.close()

# os.rename(ROOT_PATH / "novo.txt", ROOT_PATH / "alterado.txt")

# os.remove(ROOT_PATH / "alterado.txt")

# shutil.move(ROOT_PATH / "novo.txt", ROOT_PATH / "novo-diretorio" / "novo.txt")

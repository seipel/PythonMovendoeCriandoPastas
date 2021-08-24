'''Importando Modulos'''
from pathlib import Path
import shutil


'''Identificado os Arquivos'''
caminho = Path('/home/seipel/Documents/Python/Projetos Destacados/PythonMovendoeCriandoPastas/Arquivos_Lojas')
arquivos = caminho.iterdir()

'''Criando as Pastas para Cada Gerente'''
estados = ['RJ', 'SP', 'MG', 'GO', 'AM']
for estado in estados:
    Path('Arquivos_Lojas/{}'.format(estado)).mkdir()

'''Retirando Arquivos Selecionados da Lista e Colocando e Cada Pasta Expecifica'''

for arquivo in arquivos:
    nome_arquivo = arquivo.name
    if nome_arquivo[-3:] == 'csv':
        estado = nome_arquivo[-6:-4]
        local_final = caminho / Path('{}/{}'.format(estado, nome_arquivo))
        shutil.move(arquivo, local_final)

    

        

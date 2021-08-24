### Desafio

Você trabalha em uma empresa que tem 18 lojas espalhadas por todo o Brasil e divididas em 5 estados diferentes:
- RJ
- SP
- MG
- GO
- AM

Todo trimestre, são calculados os indicadores de cada funcionário de cada loja e esses indicadores são armazenados em um arquivo em Excel.

Cada estado tem 1 Gerente Geral responsável por todas as lojas daqueles estados.

Pediram para você enviar para cada Gerente Geral todas as bases de indicadores correspondentes às lojas que ele é responsável, porque a equipe deles precisa desses indicadores.

Obs: Não vamos enviar por e-mail porque ainda não aprendemos a fazer isso, mas vamos deixar todos os arquivos em uma pasta única para cada gerente, ou seja, para cada estado.

Então o seu desafio é separar todos os arquivos de forma que cada arquivo esteja na pasta do estado correspondente aquele arquivo.

Obs: Para pegar o nome de um arquivo como um texto no pathlib, você pode usar Path.name ou arquivo.name:<br>
caminho = Path('Pasta/Arquivo.csv')<br>
print(caminho.name) -> resposta: 'Arquivo.csv'
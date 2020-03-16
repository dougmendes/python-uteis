**Repositório** que contém alguns scripts simples em python para tratar arquivos.

- **csv_to_xlsx.py**  
    
        Lê de um diretório fixo um arquivo .csv e converte para xlsx com o nome passado na chamada.
        Exemplo:
            python csv_to_xlsx.py nome_arquivo  
            ---------------!!Alerta!!--------------
             Não é necessario passar a extensão do arquivo.
- **xlsx_to_csv.py** 
        
        Recebe na chamada o caminho absoluto do arquivo xlsx e converte para um arquivo .csv(O caminho também é passado na chamada).
        Exemplo:
            python xlsx_to_csv.py nome_arquivo.xlsx   nome_arquivo2.csv 
- **qtd_linhas_csv.py** 

        Recebe um arquivo csv como parametro e diz quantas linhas o arquivo tem.
        Exemplo:
            python qtd_linhas_csv.py arquivo.csv

- **qtd_linhas_xlsx.py** 

        Recebe um arquivo xlsx como parametro e diz quantas linhas o arquivo tem.
        Exemplo:
            python qtd_linhas_xlsx.py arquivo
            ---------------!!Alerta!!--------------
             Não é necessario passar a extensão do arquivo.

- **cpf-fill.py** 

        Recebe um arquivo xlsx como parametro, nome da coluna que tem o CPF e o nome do arquivo de saida(csv).
        Recebe uma planilha xlsx e o nome da coluna que o cpf se encontra, verifica cada elemento da coluna, se possuir menos de 11 números é preenchido com 0 a esquerda
        Exemplo:
            python arquivos_clientes.py CPF/CNPJ arquivo_saida.csv


import pandas as pd

def processar_logs_treinamento (qrquivo_log):
    try:
        leitor = pd.read_csv(arquivo_log)
        media = leitor['tempo_execucao'].mean()
        desvio_padrao = leitor['tempo_execucao'].std()
        return f"media: {media:.2f}, desvio padrão: {desvio_padrao}"
    

    except FileExistsError 

        return "Aquivo nao encontrado"
    
    arquivo = input("Digite o nome do aqruivo de log:")
    print (processar_logs_treinamento(arquivo))

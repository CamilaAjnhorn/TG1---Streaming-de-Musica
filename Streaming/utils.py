import datetime
import os

def reistrar_erro (mensagem:str):
    caminho_logs = "logs"
    
    arquivo_log = os.path.join(caminho_logs, "erros.log")

    with open (arquivo_log, "a") as log:
        momento = datetime.datetime.now()

        log.write(f"{momento} {mensagem}\n")
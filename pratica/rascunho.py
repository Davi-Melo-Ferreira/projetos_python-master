import os
from datetime import datetime, timedelta

os.system('cls')

tarefas = {
    1:{'data_vencimento': '24/03/2006'},
    2:{'data_vencimento': '24/03/2007'}
           }

for tarefa in tarefas.values():
    data_venc = datetime.strptime(tarefa['data_vencimento'], '%d/%m/%Y')
    sorted(data_venc)
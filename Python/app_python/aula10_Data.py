from datetime import date, time, datetime, timedelta #a classe datetime possui metodos relacionados as datas e horas do computador
def trabalhando_com_datetime():
    data_atual = datetime.now()
    dia = ('Segunda-Feira','Terça-Feira','Quarta-Feira','Quinta-Feira','Sexta-Feira','Sábado','Domingo')
    print(data_atual.strftime('{} - %d/%B/%y - %H:%M'.format(dia[data_atual.weekday()])))
    print(data_atual.strftime('%c'))
    print(type(data_atual))
    data_conta = data_atual - timedelta(days=365, hours=59, minutes=9999)
    print(data_conta.strftime('{} - %d/%B/%y - %H:%M'.format(dia[data_atual.weekday()])))

def trabalhando_com_date():
    data_atual = date.today() # o .today() traz a data dod ia de hoje ao programa
    print(data_atual.strftime('%A - %d/%B/%Y')) # o %? sao diretivas da classe que podem ser consultadas online
    print(type(data_atual))

def trabalhando_com_time():
    horario = time(hour=15, minute=15, second=15)
    print(horario.strftime('%H:%M:%S'))
    print(type(horario))
if __name__ == '__main__':
    trabalhando_com_date()
    print('--------------------')
    trabalhando_com_time()
    print('--------------------')
    trabalhando_com_datetime()
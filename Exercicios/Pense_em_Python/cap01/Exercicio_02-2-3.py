# Pratique o uso do interpretador do Python como uma calculadora

'''3. Se eu sair da minha casa às 6:52 e correr 1 quilômetro a um certo passo(8min15s por quilômetro)
 , então 3 quilômetros a uma passo mais rápido(7min12s por quilômetro) e 1 quilômetro no mesmo passo
 usado em primeiro lugar, que horas chego em casa para o café da manhã'''

tempo_em_segundos_1periodo =  ((8 * 60) + 15) * 2
tempo_em_segundos_2periodo = ((7 * 60) + 15) * 3
tempo_saida = ((6 * 60) + 52) * 60
tempo_total = tempo_em_segundos_1periodo + tempo_em_segundos_2periodo

hora_chegada = tempo_saida + tempo_total

segundos = hora_chegada %60
minu = hora_chegada // 60
minutos = minu % 60
horas = minu // 60

print(f'Você chegará às {horas}:{minutos} e {segundos}')




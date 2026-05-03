from colorama import Fore, Style, init

#Inicializa o colorama
init(autoreset=True) 

'''init() prepara o ambiente para que esses códigos funcionem corretamente em diferentes SO. 
O autoreset=True garante que depois da impressão o estilo volte ao padrão automaticamente'''

#Lista de mensagem para cada nível
mensagens = [
    'Nivel 1 - Muito Baixo (Crítico)',
    'Nível 2 - Baixo',
    'Nível 3 - Médio',
    'Nível 4 - Alto',
    'Nível 5 - Muito Alto (Alerta)'
]

#Função que retorna a cor conforme o nível
def cor_por_nivel(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN 
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE
    
# Simulação: percorre todos os níveis do reservatório
for nivel in range(1, 6):
    cor = cor_por_nivel(nivel)
    print(cor + mensagens[nivel - 1] + Style.RESET_ALL)
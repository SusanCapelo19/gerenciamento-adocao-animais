import json
import os
from datetime import datetime
import re

arquivo_voluntario = os.path.join(os.path.dirname(__file__), 'armazenamento', 'voluntarios.json')

def carregar_voluntarios():
    if not os.path.exists(arquivo_voluntario):
        with open(arquivo_voluntario, 'w') as f:
            json.dump([], f, indent=4)

    with open(arquivo_voluntario, 'r') as f:
        return json.load(f)
    
def verificar_disponibilidade():
    disponibilidade = []

    dias_disponiveis = input("Já pensou em ser voluntário?\nQuais dias você tem disponível de segunda a sexta?\nPode ser mais de um dia, quanto mais você puder nos AUjudar, mais rápido podemos achar um tutor consciente para os pets: ")
    dias = [dia.strip().lower() for dia in re.split(r'[, ]+', dias_disponiveis) if dia]
   
    for dia in dias:
        periodos_disponiveis = input("E qual período ou períodos do dia você tem disponível (digite manhã, tarde ou noite): ")
        periodos = [prd.strip().lower() for prd in re.split(r'[, ]+', periodos_disponiveis) if prd]
        disponibilidade.append({"Dia": dia, "Periodos": periodos})
    
    return disponibilidade


def criar_voluntarios(cpf, nome, nascimento, endereco, disponibilidade, data_cadastro):
    voluntarios = carregar_voluntarios()

    data_nascimento = datetime.strptime(nascimento, "%d/%m/%Y")
    hoje = datetime.today()
    idade = hoje.year - data_nascimento.year
    if (hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day):
        idade -= 1      

    voluntarios.append(
        {
            "CPF": cpf,
            "Nome Completo": nome,
            "Data Nascimento": nascimento,
            "Idade": idade,
            "Endereço": endereco, 
            "Disponibilidade": disponibilidade,
            "Data Cadastro": data_cadastro
        }
    )
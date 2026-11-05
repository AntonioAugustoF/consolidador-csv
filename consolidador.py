# importando os módulos que serão utilizados
import os
import csv

# variáveis globais
PASTA = os.path.dirname(os.path.abspath(__file__))
PASTA_RELATORIOS = os.path.join(PASTA, "relatorios_mensais")

# garantindo a existência da pasta de entrada
os.makedirs(PASTA_RELATORIOS, exist_ok=True)

total_p_categoria = {}
total_p_mes = {}
total_geral = 0

# 1. listando os arquivos .csv da pasta relatorios_mensais/
arquivos = os.listdir(PASTA_RELATORIOS)
for a in arquivos:
    if a.endswith(".csv"):
        prefixo, mes = a.removesuffix(".csv").split("_") # mês: janeiro, fevereiro, março
        with open(os.path.join(PASTA_RELATORIOS, a), "r", encoding="utf-8") as f:
            linhas = csv.DictReader(f)
            for linha in linhas:
                try:
                    categoria = linha["categoria"] # Eletrônicos, Periféricos, Acessórios
                    valor = float(linha.get("valor", 0)) # converte os elementos da coluna 'valor' de string pra float
                    total_geral = total_geral + valor
                    total_p_categoria[categoria] = total_p_categoria.get(categoria, 0) + valor # itera pelo valor armazenado
                    total_p_mes[mes] = total_p_mes.get(mes, 0) + valor
                except ValueError:
                    print(f"Não foi possível converter para float o item: '{linha.get("valor")}' da coluna 'valor'.")
                    continue

print(f"Total por Mês: R$ {total_p_mes}")
print(f"Total por Categoria: R$ {total_p_categoria}")
print(f"Total Geral: R$ {total_geral}")
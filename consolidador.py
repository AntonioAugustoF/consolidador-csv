# importando os módulos que serão utilizados
import os
import csv

# variáveis globais
PASTA = os.path.dirname(os.path.abspath(__file__))
PASTA_RELATORIOS = os.path.join(PASTA, "relatorios_mensais")
PASTA_CONSOLIDADOS = os.path.join(PASTA, "consolidados")
# garantindo a existência da pasta de entrada
os.makedirs(PASTA_RELATORIOS, exist_ok=True)
# pasta saída
os.makedirs(PASTA_CONSOLIDADOS, exist_ok=True)

linhas_consolidadas = [] # lista de dicionários
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
                    linha["mes"] = mes
                    linhas_consolidadas.append(linha)
                except ValueError:
                    print(f"Não foi possível converter para float o item: '{linha.get("valor")}' da coluna 'valor'.")
                    continue

def relatorio_consolidado():
    with open(os.path.join(PASTA_CONSOLIDADOS, "relatorio_consolidado.csv"), "w", encoding="utf-8") as r:
        escritor = csv.DictWriter(r, fieldnames=["produto","categoria","valor","mes"])
        escritor.writeheader()
        escritor.writerows(linhas_consolidadas)
        len(linhas_consolidadas)


def resumo_consolidado():
    with open(os.path.join(PASTA_CONSOLIDADOS, "resumo_consolidado.txt"), "w", encoding="utf-8") as r:
        r.write("Total por Mês\n")
        for mes, valor_mes in total_p_mes.items():
            r.write(f"{mes.capitalize():<12}: R$ {valor_mes:>8.2f}\n")
        r.write("\nTotal por Categoria\n")
        for categoria, valor_categoria in total_p_categoria.items():
            r.write(f"{categoria:<12}: R$ {valor_categoria:>8.2f}\n")
        r.write(f"\nTotal Geral : R$ {total_geral:>8.2f}")

resumo_consolidado()
relatorio_consolidado()
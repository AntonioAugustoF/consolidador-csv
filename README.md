# Consolidador de CSV

## Descrição
Este projeto tem como intuito ler todos os arquivos `.csv` da pasta `relatorios_mensais/` (um por mês, colunas: `produto`, `categoria`, `valor`), e consolidar em um relatório único com:
- total por **categoria** (somando todos os meses juntos)
- total por **mês** (somando cada arquivo)
- total geral (soma de tudo)

No final:
- imprimir um resumo formatado no terminal
- gravar o relatório consolidado em um novo arquivo (`.txt` ou `.csv`)

## Funcionalidades
- Lê todos os arquivos CSV de uma pasta
- Soma os valores por categoria
- Soma os valores por mês
- Calcula o total geral
- Ignora linhas com um valor inválido, sem quebrar a execução
- Gera um relatório consolidado em arquivo de texto

## Como Usar

### Pré-requisitos
- Python 3.x instalado

### Passos
1. Clone o repositório:
```bash
git clone https://github.com/AntonioAugustoF/consolidador-csv.git
cd consolidador-csv
```

2. Coloque os arquivos CSV que deseja consolidar dentro da pasta `relatorios_mensais/`.
   Cada arquivo deve seguir o formato:
   ```
   Produto,Categoria,Valor
   Mouse,Periféricos,50.00
   ```

3. Execute o script:
```bash
python consolidador.py
```

4. O resumo aparece no terminal, e o relatório consolidado é salvo automaticamente em `relatorio_consolidado.txt`, na raiz do projeto.

## Estrutura de Pastas
```
projeto_consolidador/
├── consolidador.py
├── README.md
└── relatorios_mensais/
    ├── vendas_janeiro.csv
    ├── vendas_fevereiro.csv
    └── vendas_marco.csv
```

## Exemplos de Uso
```
Total por Categoria:
   Eletrônicos   R$ 5250.00
   Periféricos   R$ 355.00
   Acessórios    R$ 40.00

Total por Mês:
   Janeiro       R$ 995.00
   Fevereiro     R$ 3595.00
   Março         R$ 1055.00

Total Geral:     R$ 5645.00
```

## Autor

**Antonio Augusto Fernandes**    
Analista de Dados em transição para Engenharia de Dados / Analytics Engineering

- GitHub: [AntonioAugustoF](https://github.com/AntonioAugustoF)
- Linkedln: [antonioafernandes](https://www.linkedin.com/in/antonioafernandes)
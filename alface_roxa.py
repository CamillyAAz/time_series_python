# -*- coding: utf-8 -*-
"""
=====================================================
Nome do Script : alface_roxa.py
Descrição      : exemplo de cabeçalho Python
Autor          : Camilly Alves
Data           : 21/08/2025
Versão         : 1.0
Licença        : MIT (ou outra que preferir)
=====================================================
"""

import sys
import os

def main():
    print("Ta funcionando!")

if __name__ == "__main__":
    main()


# Para que serve uma docstring no python?

# segue abaixo exercício inicial:

!pip -q install yfinance > /dev/null

import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#  PARÂMETROS
TICKER = "PETR4.SA"   #@param {type:"string"}
START  = "2023-01-01" #@param {type:"string"}
END    = "2025-01-01" #@param {type:"string"}

# 1) Baixar dados
# Use yf.download(TICKER, start=START, end=END) e mantenha apenas a coluna "Close".
# Dica: df = yf.download(...); df = df[["Close"]].dropna()
try:
    df = ...  # TODO
    if df.empty:
        raise ValueError("Sem dados baixados")
except Exception:
    # Fallback: gera série sintética (para o exercício rodar sem internet)
    idx = pd.bdate_range(START, END)
    np.random.seed(42)
    steps = np.random.normal(0, 0.012, len(idx))
    price = 100 * np.exp(np.cumsum(steps))
    df = pd.DataFrame({"Close": price}, index=idx)

#  2) Indicadores 
# Crie as colunas:
# - "ret"   = df["Close"].pct_change()
# - "sma20" = df["Close"].rolling(20).mean()
# - "cumret" (opcional): (1+ret).cumprod() - 1  (curva de retorno acumulado)
...
...
...

#   3) Métricas-Resumo 
# Calcule e guarde em variáveis:
# - preco_final        (float): último Close
# - retorno_acumulado  (float): (1+ret).prod() - 1
# - vol_anualizada     (float): ret.std() * sqrt(252)
preco_final = ...
retorno_acumulado = ...
vol_anualizada = ...

#   4) Plot
# Faça um único gráfico com:
# - Série de Close
# - Série de sma20
# Dicas:
#   fig, ax = plt.subplots(figsize=(10,4))
#   ax.plot(df.index, df["Close"], label="Close")
#   ax.plot(df.index, df["sma20"], label="Média móvel 20d")
#   ax.set_title(f"{TICKER} — Preço vs. MM20")
#   ax.set_xlabel("Data"); ax.set_ylabel("Preço")
#   ax.legend(); plt.show()
...
...

#  Impressão das métricas 
print(f"TICKER: {TICKER}")
print(f"Período: {START} a {END}")
print(f"Preço final: {preco_final:,.2f}")
print(f"Retorno acumulado: {retorno_acumulado*100:,.2f}%")
print(f"Volatilidade anualizada: {vol_anualizada*100:,.2f}%")

#  TESTES RÁPIDOS 
def _testes(df):
    assert "Close" in df.columns
    assert "ret" in df.columns
    assert "sma20" in df.columns
    assert df["Close"].notna().sum() > 30, "Poucos dados; verifique datas"
    # retorno acumulado plausível: > -100%
    assert retorno_acumulado > -0.99, "Retorno acumulado inválido"
    # volatilidade positiva
    assert vol_anualizada >= 0.0
    print("teste testado!")

_testes(df)

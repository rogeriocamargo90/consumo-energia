# ==========================================================
# Calculadora de Consumo Elétrico Inteligente
# ==========================================================

print("=== CALCULADORA DE CONSUMO ELÉTRICO INTERATIVA ===")
print("Preencha as informações abaixo para calcular o consumo:\n")

# Entrada de dados do usuário
nome_aparelho = input("Nome do aparelho: ")
potencia_watts = float(input("Potência do aparelho em Watts (W): "))
horas_por_dia = float(input("Tempo de uso diário (em horas): "))

# Cálculo do consumo mensal em kWh
consumo_mensal_kwh = (potencia_watts * horas_por_dia * 30) / 1000

# Cálculo de custo estimado (Tarifa média de R$ 0,75/kWh)
tarifa_kwh = 0.75
custo_estimado = consumo_mensal_kwh * tarifa_kwh

# Exibição dos resultados
print("\n" + "="*40)
print("RESUMO DO CONSUMO ENERGÉTICO")
print("="*40)
print(f"Aparelho: {nome_aparelho}")
print(f"Consumo estimado: {consumo_mensal_kwh:.2f} kWh/mês")
print(f"Custo estimado: R$ {custo_estimado:.2f}/mês (Tarifa: R$ {tarifa_kwh:.2f}/kWh)")
print("="*40)

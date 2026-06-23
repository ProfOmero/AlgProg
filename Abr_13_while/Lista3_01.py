capInicial = float(input())

print(f"Capital Inicial = R$ {capInicial:.2f}")
print()

ctMeses = 0
capFinal = capInicial

while (capFinal <= 500.00):
    capFinal = capFinal + (capFinal * 10 / 100)
    ctMeses = ctMeses + 1
    
    print(f"{ctMeses:2d}o. mes = R$ {capFinal:.2f}")

print()
print(f"Capital Final = R$ {capFinal:.2f} apos {ctMeses} meses.")

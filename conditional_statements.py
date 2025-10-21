x = int(input("Enter a number: "))
if x < 10:
    print("Smaller.")
if x > 20:
    print("Bigger.")

print("Done.")

x = 42
if x > 1:
    print("More than 1.")
    if x < 100:
        print("Less than 100.")

print("Done.")

x = 4

if x > 2:
    print("Bigger")
else:
    print("Smaller")

print("Done.")

x = int(input("Enter a number: "))
if x < 10:
    print("Smaller.")
elif x < 20:
    print("Medium.")
else:
    print("Large.")
print("Done.")

# Código "Robusto" (com rede de segurança)

numero_em_texto = input("Insira um número: ")

try:
    # --- A "Zona Perigosa" ---
    # Tenta fazer a conversão
    numero_em_int = int(numero_em_texto)
    print(f"O dobro do seu número é {numero_em_int * 2}")
    # --------------------------

except:
    # --- O "Plano B" ---
    # Isto só executa se o 'try' falhar
    print("Ups! Isso não parece ser um número. Tente de novo.")
    # -------------------

print("O programa continua...")
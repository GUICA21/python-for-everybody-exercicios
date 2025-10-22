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

hrs = input("Enter hours:")
h = float(hrs)
rate = input("Enter rate:")
r = float(rate)

# Define a taxa normal e o limite de horas
taxa_normal = r
limite_horas = 40
taxa_extra = r * 1.5

if h > limite_horas:
    # 1. Calcula o pagamento das primeiras 40 horas
    pagamento_normal = limite_horas * taxa_normal

    # 2. Calcula as horas extra e o seu pagamento
    horas_extra = h - limite_horas
    pagamento_extra = horas_extra * taxa_extra

    # 3. O total é a soma dos dois
    total_pay = pagamento_normal + pagamento_extra
else:
    # Se houver 40 horas ou menos, o cálculo é simples
    total_pay = h * taxa_normal

print(total_pay)

score_input = input("Enter Score: ")

# --- Dica 3: Usar try/except para apanhar entradas não-numéricas ---
try:
    s = float(score_input)
except:
    print("Error, please enter a numeric value")
    exit()  # O 'exit()' pára o programa imediatamente

# --- Dica 2: A ordem da lógica ---
# PRIMEIRO, testamos se está FORA do intervalo válido (0.0 a 1.0)
# (Não te esqueças dos ':' - Dica 1)
if s < 0.0 or s > 1.0:
    print("Error, the score must be between 0.0 and 1.0")
    exit()  # Pára o programa

# Se o programa chegou aqui, sABEMOS que 's' é um número VÁLIDO.
# Agora, podemos fazer a cadeia de 'elif's em segurança.
elif s >= 0.9:
    print("A")
elif s >= 0.8:
    print("B")
elif s >= 0.7:
    print("C")
elif s >= 0.6:
    print("D")
else:
    # Se não for >= 0.6, e sabemos que é >= 0.0,
    # só pode ser < 0.6
    print("F")
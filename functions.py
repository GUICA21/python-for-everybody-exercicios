def thing():
    print("Hello World")


thing()
print("Done")
thing()


def greet(lang):
    if lang == "English":
        print("Hello World")
    elif lang == "Spanish":
        print("Hola")
    else:
        print("Sorry, I don't understand that")


greet("English")
greet("Spanish")
greet("Portuguese")


def greet():
    return "Hello"


print(greet(), "Glenn")


def computepay(h, r):
    """
    Esta função calcula o pagamento, incluindo horas extra.
    Recebe horas (h) e taxa (r) como números (float).
    Retorna o pagamento total.
    """
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

    return total_pay


# --- Programa Principal (Agora "Robusto") ---

# 1. Pedir e Validar as Horas
hrs = input("Enter Hours: ")
try:
    h = float(hrs)
except:
    print("Error, please enter a numeric value for hours")
    exit()  # 'exit()' pára o programa imediatamente.

# 2. Pedir e Validar a Taxa
# O programa só chega a esta linha se o 'try' de CIMA teve sucesso.
rate = input("Enter rate: ")
try:
    r = float(rate)
except:
    print("Error, please enter a numeric value for rate")
    exit()  # Pára o programa se a taxa for inválida

# 3. Chamar a Função e Imprimir o Resultado
# O programa só chega aqui se AMBOS os 'try's tiveram sucesso.
p = computepay(h, r)
print("Pay", p)

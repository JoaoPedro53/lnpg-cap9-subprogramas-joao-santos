#monolítica

products = []
quantities = []
unit_prices = []
subtotals = []

total = 0

qtd_products = int(input("Quantos produtos deseja cadastrar? "))

for i in range(qtd_products):

    print(f"\nProduto {i + 1}")

    name = input("Nome do produto: ")
    quantity = int(input("Quantidade: "))
    unit_price = float(input("Preço unitário: R$ "))

    subtotal = quantity * unit_price

    products.append(name)
    quantities.append(quantity)
    unit_prices.append(unit_price)
    subtotals.append(subtotal)

    total += subtotal

# cálculo do desconto
if total > 500:
    discount_percent = 10
elif total > 200:
    discount_percent = 5
else:
    discount_percent = 0

discount_value = total * (discount_percent / 100)
final_total = total - discount_value

# cupom
print("\n== CUPOM ==")

for i in range(qtd_products):
    print(
        f"{products[i]} | "
        f"Qtd: {quantities[i]} | "
        f"Unit: R$ {unit_prices[i]:.2f} | "
        f"Subtotal: R$ {subtotals[i]:.2f}"
    )

print("\n-----------")
print(f"TOTAL: R$ {total:.2f}")
print(f"DESCONTO: {discount_percent}%")
print(f"VALOR DO DESCONTO: R$ {discount_value:.2f}")
print(f"TOTAL FINAL: R$ {final_total:.2f}")
print("============")

#refatorada

def read_product():
    name = input("Nome do produto: ")
    quantity = int(input("Quantidade: "))
    unit_price = float(input("Preço unitário: R$ "))

    subtotal = quantity * unit_price

    return name, quantity, unit_price, subtotal


def calculate_discount(total):

    if total > 500:
        return 10
    elif total > 200:
        return 5

    return 0


def print_coupon(products, total, discount_percent):

    discount_value = total * (discount_percent / 100)
    final_total = total - discount_value

    print("\n== CUPOM ===")

    for product in products:

        print(
            f"{product['name']} | "
            f"Qtd: {product['quantity']} | "
            f"Unit: R$ {product['unit_price']:.2f} | "
            f"Subtotal: R$ {product['subtotal']:.2f}"
        )

    print("\n--------------")
    print(f"TOTAL: R$ {total:.2f}")
    print(f"DESCONTO: {discount_percent}%")
    print(f"VALOR DO DESCONTO: R$ {discount_value:.2f}")
    print(f"TOTAL FINAL: R$ {final_total:.2f}")
    print("===============")

products = []
total = 0

qtd_products = int(input("Quantos produtos deseja cadastrar? "))

for i in range(qtd_products):

    print(f"\nProduto {i + 1}")

    name, quantity, unit_price, subtotal = read_product()

    product = {
        "name": name,
        "quantity": quantity,
        "unit_price": unit_price,
        "subtotal": subtotal
    }

    products.append(product)

    total += subtotal

discount_percent = calculate_discount(total)

print_coupon(products, total, discount_percent)
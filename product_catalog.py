# Product Catalog

catalog = []

for product_number in range(1, 4):
    name = input(f"Enter product {product_number} name: ")
    description = input(f"Enter product {product_number} description: ")
    price = float(input(f"Enter product {product_number} price: "))
    quantity = int(input(f"Enter product {product_number} quantity in stock: "))
    weight = float(input(f"Enter product {product_number} weight: "))

    product = {
        "name": name,
        "description": description,
        "price": price,
        "quantity": quantity,
        "weight": weight,
    }

    catalog.append(product)

print("\nProduct Catalog")
print("=" * 20)

for index, product in enumerate(catalog, start=1):
    print(f"\nProduct {index}: {product['name']}")
    print(f"Description: {product['description']}")
    print(f"Price: ${product['price']:.2f}")
    print(f"Quantity in Stock: {product['quantity']}")
    print(f"Weight: {product['weight']} lbs")

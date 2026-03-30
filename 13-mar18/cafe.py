class Coffee:
    def __init__(self, name: str, description: str, base_price: float):
        self.name = name
        self.description = description
        self.base_price = base_price

    def __str__(self):
     return f"{self.name} - {self.description} (${self.base_price:.2f})"
    
latte = Coffee("Latte", "Espresso with steamed milk", 4.50)
americano = Coffee("Americano", "Espresso with hot water", 3.00)
print(latte)
print(americano)
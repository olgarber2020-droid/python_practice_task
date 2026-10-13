from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 13", "+79001112233"),
    Smartphone("Samsung", "Galaxy S21", "+79004445566"),
    Smartphone("Xiaomi", "Redmi Note 10", "+79007778899"),
    Smartphone("Google", "Pixel 6", "+79002223344"),
    Smartphone("OnePlus", "9 Pro", "+79005556677"),
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")

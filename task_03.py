import re

def normalize_phone(phone_number):
    # delete wrong symbols, leave only digits
    phone_number_digits = phone_number.strip()
    pattern = r"\d"
    phone_number_digits = re.findall(pattern, phone_number_digits)
    phone_number_digits = "".join(phone_number_digits)

    #generate normilised phone number
    if phone_number_digits.startswith("380"):
        phone_number_normilised = "+" + phone_number_digits
    elif phone_number_digits.startswith("0"):
        phone_number_normilised = "+38" + phone_number_digits
    else:
        phone_number_normilised = phone_number_digits

    return phone_number_normilised

raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
import random

options = {
    "工商银行": ("6222", 19),
    "农业银行": ("6228", 19),
    "交通银行": ("6014", 17),
    "建设银行": ("6227", 19),
}


def generate_bank_code(bank_name):
    bank = options.get(bank_name)
    bank_code = bank[0]
    for _ in range(bank[1] - len(bank[0])):
        bank_code += str(random.randint(0, 9))

    return bank_code

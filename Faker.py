import json

from faker import Faker

fake_ru = Faker('ru_RU')
dict = {}
for i in range(10):
    name = fake_ru.name()
    ad = fake_ru.address()
    job = fake_ru.job()
    phone = fake_ru.phone_number()
    dict[i] = {i:[name, ad, job, phone]}
    with open('DS.txt', 'w', encoding='utf8') as f:
        json.dump(dict, f, indent=4, ensure_ascii=False)
    with open('DS2.txt',"w") as f:
        with
def argu():
    """Thise function iis ...."""
    ...
def fr():
    """Thise func...."""
    ...
email = input("Введіть вашу електронну адресу: ")

def CorrectEmail(email):
    if "@" not in email:
        return ("Некоректна кількість знаків "@"!")
    [name,domain] = email.split('@')
    if len(domain) < 3:
        return ("Доменне ім'я коротше трьох символів!")
    if domain.count('.') == 0:
        return ("Доменне ім'я не містить крапку!")
    includedomain = domain.split('.')
    j = list(includedomain)
    for n in range(len(j)):
        if len(j[n]) <= 1:
            return ("Доменне імя містить менше двох символів після крапки!")
    for k in includedomain:
        if k == '':
            return ("Доменне імя містить порожній рядок!")
    if len(name) > 128:
        return ("Імя довше 128-ми символів!")
    return ("Поштова адреса коректна!")
print(CorrectEmail(email))

"""
gmail = input("Введіть вашу електронну адресу: ")

def AuditGmail(gmail):
    if gmail.count('@') > 1 or gmail.count('@') == 0:
        return ("Некоректна кількість знаків "@"!")

    [name,domain] = gmail.split('@')
    if len(domain) < 3:
        return ("Доменне ім'я коротше трьох символів!")
    if domain.count('.') == 0:
        return ("Доменне ім'я не містить крапку!")

    j = list(domain.split('.'))
    for n in range(len(j)):
        if len(j[n]) <= 1:
            return ("Доменне імя містить менше двох символів після крапки!")
    return ("Поштова адреса коректна!")
print(AuditGmail(gmail))"""
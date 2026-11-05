previous = int(input())
current = int(input())
if current >= previous:
    used = current - previous
else:
    used = 10000 - previous + current
if used <= 300:
    payment = 21
else:
    payment = 21
    if used <= 600:
        payment = payment + (used - 300) * 0.06
    else:
        payment = payment + 300 * 0.06
        if used <= 800:
            payment = payment + (used - 600) * 0.04
        else:
            payment = payment + 200 * 0.04
            payment = payment + (used - 800) * 0.025
average_price = payment / used
print("Предыдущее:", previous)
print("Текущее:", current)
print("Использовано:", used)
print("К оплате:", format(payment, ".2f"))
print("Ср. цена m^3:", format(average_price, ".2f"))
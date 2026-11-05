import string
password = input()
length_ok = len(password) == 8
has_upper = False
has_lower = False
has_digit = False
has_special = False
has_wrong = False
allowed = string.ascii_letters + string.digits + "*-#"
for symbol in password:
    if symbol in string.ascii_uppercase:
        has_upper = True
    if symbol in string.ascii_lowercase:
        has_lower = True
    if symbol in string.digits:
        has_digit = True
    if symbol in "*-#":
        has_special = True
    if symbol not in allowed:
        has_wrong = True
if length_ok and has_upper and has_lower and has_digit and has_special and not has_wrong:
    print("Надежный пароль")
else:
    if not length_ok:
        print("Длина пароля не равна 8")
    if not has_upper:
        print("В пароле отсутствуют заглавные буквы")
    if not has_lower:
        print("В пароле отсутствуют строчные буквы")
    if not has_digit:
        print("В пароле отсутствуют цифры")
    if not has_special:
        print("В пароле отсутствуют специальные символы")
    if has_wrong:
        print("В пароле используются непредусмотренные символы")
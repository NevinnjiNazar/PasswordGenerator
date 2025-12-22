import random
Digits_ = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
"n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", 
"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
"N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
"$", "@", "&", "?", "+", "-", "*", "/", "%", "=", "!", "№", "_", "^", ",", "."]
 
HowManyDigits = int(input("Number Of Digits(6-40): "))
if HowManyDigits > 5 and HowManyDigits < 41: 
    def generate_password_from_list(HowManyDigits):
        password = ''.join(str(random.choice(Digits_)) for i in range(HowManyDigits))
        return password

    print(f"Сгенерированный пароль: {generate_password_from_list(HowManyDigits)}")
else:
    print(f"Ваша кількість: {HowManyDigits}\nМожлива Кількість: (6-40)")
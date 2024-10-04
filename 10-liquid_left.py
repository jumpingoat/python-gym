#Szef kazał napełniać pracownikowi butelki 330 ml cieczą, w taki sposób by 12% butelki
# pozostawało puste. Pracownik umówił się z szefem, że cały płyn który mu pozostanie i nie
# wystarczy do napełnienie butelek może zostawić sobie. Po starcie odbierz od użytkownika
# informację ile ml płynu dostarczyła fabryka, a wynikiem powinna być ilość cieczy, którą
# pracownik będzie mógł wziąć ze sobą


from math import floor

#zamieniamy input ze stringu na float a ew. przecinek, który user może nam wstawić, na kropkę.
liquid = float(input('Podaj ilość płynu dostarczonego w l ').replace(",","."))
b_fill = 0.33 - (0.33 * 0.12)

bottles = liquid / b_fill
filled = floor(bottles)

left = round(((bottles - filled) * b_fill), 2)

print(f'Napełniono {filled} butelek. Pracownikowi pozostało: {left} ml płynu')

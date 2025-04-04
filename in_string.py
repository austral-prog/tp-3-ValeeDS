def check_vowels():
    # Código a implementar utilizando input.

    nombre = input("Ingrese un nombre:\n").lower()

    a = "a" in nombre
    e = "e" in nombre
    i = "i" in nombre
    o = "o" in nombre
    u = "u" in nombre

    print(f"Contiene a: {a}\nContiene e: {e}\nContiene i: {i}\nContiene o: {o}\nContiene u: {u}")

# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_in_string_test.py` o `python tp3_in_string_test.py`

def slice_advanced():
    # Código a implementar utilizando input.
    texto = input("Ingrese un texto de más de 5 caracteres: ")

    slicing = texto[4::2]

    print(slicing)
    
# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_slice_advanced_test.py` o `python tp3_slice_advanced_test.py`
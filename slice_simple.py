def slice_simple():
    texto = "Awesome"
    # Código a implementar, se debe utilizar la variable 'texto' para resolver el ejercicio.
    # No se debe modificar la definición de la función, ni ingresar otro valor mediante input.

    texto = texto.lower()

    primeras3 = texto[:3]
    medio = int(len(texto)/2)+1
    medio3 = texto[ medio - 2 : medio + 1]
    primera_a_4ta = texto[:4]
    ultimas3 = texto[-3:]

    print(primeras3)
    print(medio3)
    print(primera_a_4ta+ultimas3)

# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_slice_simple_test.py` o `python tp3_slice_simple_test.py`

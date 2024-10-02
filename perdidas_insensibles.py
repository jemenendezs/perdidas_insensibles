"""
MIT License

Copyright (c) 2024 Jorge Menéndez S.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from typing import Dict, Tuple

# Constantes para los ajustes de diaforesis
AJUSTES_DIAFORESIS = {0: 0, 1: 100, 2: 200, 3: 300}

# Descripciones de los ajustes para el reporte final
AJUSTES_DESCRIPCION = {
    "ajuste_temperatura": "Ajuste por temperatura",
    "ajuste_taquipnea": "Ajuste por taquipnea",
    "ajuste_diaforesis": "Ajuste por diaforesis",
    "ajuste_hidratacion": "Ajuste por estado de hidratación",
    "ajuste_edad": "Ajuste por edad"
}

def calcular_ajustes(temperatura: float, frecuencia_respiratoria: int, diaforesis: int, estado_hidratacion: int, edad: int) -> Dict[str, float]:
    """
    Calcula los ajustes según las condiciones del paciente.
    
    :param temperatura: Temperatura corporal en °C
    :param frecuencia_respiratoria: Frecuencia respiratoria en respiraciones por minuto
    :param diaforesis: Grado de diaforesis (0-3)
    :param estado_hidratacion: Estado de hidratación (0: Normal, 1: Deshidratado)
    :param edad: Edad del paciente en años
    :return: Diccionario con los ajustes calculados
    """
    return {
        "ajuste_temperatura": max((temperatura - 37) * 100, 0),  # Ajuste por temperatura superior a 37°C
        "ajuste_taquipnea": max((frecuencia_respiratoria - 20) * 5, 0),  # Ajuste por frecuencia respiratoria superior a 20
        "ajuste_diaforesis": AJUSTES_DIAFORESIS.get(diaforesis, 0),  # Ajuste según el grado de diaforesis
        "ajuste_hidratacion": 50 if estado_hidratacion == 1 else 0,  # Ajuste si el paciente está deshidratado
        "ajuste_edad": 100 if edad < 1 else (50 if edad > 65 else 0)  # Ajuste por edad (bebés y adultos mayores)
    }

def calcular_perdidas_insensibles(peso: float, horas: int, temperatura: float, frecuencia_respiratoria: int, diaforesis: int, estado_hidratacion: int, edad: int) -> Tuple[float, Dict[str, float], float]:
    """
    Calcula las pérdidas insensibles de agua en mililitros.
    
    :param peso: Peso del paciente en kg
    :param horas: Número de horas para el cálculo
    :param temperatura: Temperatura corporal en °C
    :param frecuencia_respiratoria: Frecuencia respiratoria en respiraciones por minuto
    :param diaforesis: Grado de diaforesis (0-3)
    :param estado_hidratacion: Estado de hidratación (0: Normal, 1: Deshidratado)
    :param edad: Edad del paciente en años
    :return: Tupla con pérdidas base, ajustes y pérdidas totales
    """
    perdidas_base = 0.5 * peso * horas  # Cálculo de pérdidas base
    ajustes = calcular_ajustes(temperatura, frecuencia_respiratoria, diaforesis, estado_hidratacion, edad)
    perdidas_totales = perdidas_base + sum(ajustes.values())  # Suma de pérdidas base y todos los ajustes
    
    return perdidas_base, ajustes, perdidas_totales

def solicitar_numero(msg: str, tipo: type = float, opciones: list = None, rango: Tuple[float, float] = None) -> float:
    """
    Solicita un número al usuario con validación.
    
    :param msg: Mensaje para solicitar el input
    :param tipo: Tipo de dato esperado (int o float)
    :param opciones: Lista de opciones válidas (si aplica)
    :param rango: Tupla con el rango válido (min, max)
    :return: Valor numérico validado
    """
    while True:
        try:
            valor = tipo(input(msg))
            if rango and not (rango[0] <= valor <= rango[1]):
                raise ValueError(f"El valor debe estar entre {rango[0]} y {rango[1]}.")
            if opciones and valor not in opciones:
                raise ValueError("Opción no válida.")
            return valor
        except ValueError as e:
            print("Entrada no válida:", e)

def main():
    print("Cálculo de pérdidas insensibles")
    print("=" * 50)

    # Diccionario con los parámetros a solicitar y sus configuraciones
    parametros = {
        "horas": ("Ingrese el número de horas para el cálculo (máximo 24): ", int, None, (1, 24)),
        "edad": ("Ingrese la edad del paciente en años: ", int, None, (1, 120)),
        "peso": ("Ingrese el peso del paciente en kg: ", int, None, (1, 500)),
        "temperatura": ("Ingrese la temperatura corporal en °C: ", float, None, (34, 42)),
        "frecuencia_respiratoria": ("Ingrese la frecuencia respiratoria en respiraciones por minuto: ", int, None, (5, 50)),
        "diaforesis": ("Seleccione el grado de diaforesis (0: Ninguna, 1: Leve, 2: Moderada, 3: Profusa): ", int, [0, 1, 2, 3], None),
        "estado_hidratacion": ("Seleccione el estado de hidratación (0: Normal, 1: Deshidratado): ", int, [0, 1], None),
    }

    # Solicitar y almacenar todos los valores necesarios
    valores = {key: solicitar_numero(*value) for key, value in parametros.items()}

    # Calcular las pérdidas insensibles
    perdidas_base, ajustes, perdidas_totales = calcular_perdidas_insensibles(**valores)

    # Imprimir el resumen de resultados
    print("\n" + "*" * 50)
    print("Resumen de pérdidas insensibles:")
    print(f"Pérdidas base: {perdidas_base:.2f} ml/día")
    for variable, aporte in ajustes.items():
        print(f"{AJUSTES_DESCRIPCION.get(variable, variable)}: {aporte:.2f} ml/día")
    print(f"Total de pérdidas insensibles: {perdidas_totales:.2f} ml/día")
    print("*" * 50)

if __name__ == "__main__":
    main()

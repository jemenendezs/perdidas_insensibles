# Cálculo de Pérdidas Insensibles de Agua

Este código está diseñado para calcular las pérdidas insensibles de agua en pacientes, teniendo en cuenta varios factores clínicos, como la temperatura corporal, la frecuencia respiratoria, el grado de diaforesis, el estado de hidratación, y la edad. Las pérdidas insensibles son aquellas que ocurren sin que el paciente lo perciba, como la evaporación a través de la piel y la respiración.

## Funcionalidades principales

1. **Cálculo de pérdidas insensibles basales**: Se calcula una pérdida basal basada en el peso del paciente, multiplicando `0.5 ml/kg/hora` por el peso y el número de horas.

2. **Ajustes adicionales**:
   - **Temperatura corporal**: Si la temperatura es mayor a 37°C, se calcula un ajuste proporcional.
   - **Frecuencia respiratoria**: Si la frecuencia respiratoria es mayor a 20 respiraciones por minuto, se aplica un ajuste.
   - **Diaforesis (sudoración)**: Se selecciona un ajuste basado en el grado de sudoración, de leve a profusa.
   - **Estado de hidratación**: Si el paciente está deshidratado, se añade un ajuste.
   - **Edad**: Los pacientes menores de un año o mayores de 65 reciben ajustes especiales.

3. **Interacción con el usuario**: A través de la función `solicitar_numero`, el programa solicita datos del paciente con validación de entradas y presenta un resumen final con las pérdidas totales y los ajustes detallados.

4. **Presentación de resultados**: Al finalizar, se muestra un resumen con las pérdidas insensibles basales, los ajustes aplicados y el total final.

Este código es útil para profesionales de la salud que necesiten estimar la pérdida de líquidos insensibles en pacientes, de modo que puedan ajustar la reposición de fluidos de manera adecuada.

## Uso

Se ejecuta en un entorno interactivo donde el usuario proporciona los datos del paciente y el programa devuelve las pérdidas insensibles calculadas. 

## Licencia

Este código está licenciado bajo la [Licencia MIT](https://opensource.org/licenses/MIT), lo que permite su uso libre y modificación.

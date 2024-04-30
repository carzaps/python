"""
1.-se importa el módulo tiempo para que haya un retardo
2. el bucle  itera 10 veces.
3. Dentro del bucle, imprimimos el progreso actual utilizando cadenas f. 
4. El argumento end='\r' garantiza que el cursor vuelva al principio de la línea tras la impresión.
5. Utilizamos time.sleep(1) para pausar la ejecución durante 1 segundo, simulando un tiempo de procesamiento.
"""
import time
# simulador de progreso
for i in range(10):
    # Print progress
    print(f"Progreso: {i}/10", end='\r')
    # periodo de un segundo
    time.sleep(1)

print("\nCompleto")

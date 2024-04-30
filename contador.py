"""
1.-se importa el módulo tiempo para que haya un retardo
2. el bucle  itera 10 veces.
3. Dentro del bucle, imprimimos el progreso actual utilizando cadenas f. 
4. El argumento end='\r' garantiza que el cursor vuelva al principio de la línea tras la impresión.
5. Utilizamos time.sleep(1) para pausar la ejecución durante 1 segundo, simulando un tiempo de procesamiento.
"""
import time
# Loop to simulate progress updates
for i in range(10):
    # Print progress
    print(f"Progress: {i}/10", end='\r')
    # Simulate some processing time
    time.sleep(1)

print("\nTask complete!")

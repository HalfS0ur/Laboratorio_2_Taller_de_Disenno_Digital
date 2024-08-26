El módulo debouncer recibe como entrada la señal del botón presionado para aplicar el antirebotes. Para obtener resultados correctos simulando con icarus la señal boton_pi debe estar en 0 al inicio hasta que el 0 se propague (aproximadamente 200 us). 
A la salida del módulo se obtiene la señal sin rebotes boton_debounce_o. En este diseño es necesario que la señal se encuentre en alto por un mínimo de 7 us para que cuente como un botón presionado y no un rebote de este.

El módulo sincronizador toma la señal sin rebotes y la sincroniza para obtener un pulso con duración de 1 ciclo de reloj.

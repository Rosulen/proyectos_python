### Algoritmo de principio y fin de palabra

Este algoritmo reconoce las palabras que están en un audio conduración de 10 segundos, con una frecia de muestreo de 8000 Hz

Para empezar se normaliza la señal y se fltra la señal, la señal obtenida por la grabación es la siguiente (boton grabar de la interface).

<p align="center"> <img src=./imagenes/senal_obtenida.png> </p>
<p style="text-align: center;">En este audio se grabaron cuatro palabras.</p>


<p align="center"> <img src=./imagenes/senal_normalizada.png> </p>
<p style="text-align: center;">La señal se normaliza tomando el valor absoluto del valor máximo que alcanza la señal, y se dividen todas las muestras entre ese valor, así la señal queda entre 1 y -1, y se filtra el resultado.</p>

La señal es procesada tomando de a 500 muestras y calculando la energía de cada tramo (la energía de una señal es el resultado de sumar todos sus componentes elevados al cuadrado), una vez hecho esto en toda la señal, se imprimen en consola los datos de energía para así después procesarla correctamente (boton procesar de la interface).

<p align="center"> <img src=./imagenes/resultados.png> </p>

<p style="text-align: center;">Resultados de energía impresos en consola, los datos mayores a 0 son loa datos donde hay una palabra.</p>


Los datos se analizan, con el resultado de la enrgía resultante, y se ajusta el valor de la condicion de n para generar una señal "cuadrada".

<p align="center"> <img src=./imagenes/valor_n.png> </p>

Cuando los valores son mayores al ajuste de n, en este caso 3, se crea un vector que dependiendo del valor de n, envia a 1 o 0 los valores del vector, esta señal cuadrada ayudará a identificar mejor, donde hay una palabra.

<p align="center"> <img src=./imagenes/pre_procesamiento.png> </p>

Existen algunas palabras que generan silencios, como se observa en la señal resultante, palabras con p en la mitad "esperar, serpiente, aspero, espia...", como se muestra en la imgane anterior algunas palagras estan cortadas, por esos silencios que se generarn, entonces se diseña un algoritmo que elimine estos "erroes" y los convierta en 1, el algoritmo está diseñado, para detectar palabras que no estan en una frase, es decir que debe existir un minímo silencio entre las palabras para que puedan ser detectadas, el resultado se muestra a coninuación.

<p align="center"> <img src=./imagenes/procesamiento.png> </p>

El algoritmo guarda los audios cortados en la carpeta con el nombre "resultado.wav o resultado (#).wav" donde # es el número de palabras, finalmente en consola se imprime el número de palabras.

<p align="center"> <img src=./imagenes/palabras.png> </p>

En laparte inferior se pone el número de audio que se quiere escuchar, y el botón mostrar, sonará el audio y mostrará la gráfica de este.

<p align="center"> <img src=./imagenes/palabra.png> </p>



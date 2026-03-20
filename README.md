# Análisis espectral de la voz

## Asignatura

Procesamiento Digital de Señales

## Programa

Ingeniería Biomédica – Universidad Militar Nueva Granada

## Práctica de laboratorio

**Análisis espectral de la voz**

## Integrantes

Danna Jimena Medina Ríos – Código 5600923
María José Polo Tovar – Código 5600894

---

## Descripción

---
## Análisis de gráficos mujeres 
- Espectro sin filtro
  
<p align="center">
  <img src="1.1.jpeg" width="700">
</p>

<p align="center">
  <em>Señal de voz mujer1</em>
</p>

**mujer1.wav:** mantiene una amplitud estable de ±10000 durante los 4.5 segundos de grabación, con segmentos vocales y pausas bien diferenciados entre sí. Hay un pico pequeño al inicio que probablemente corresponde a un artefacto del micrófono, y la energía baja de forma natural hacia el final de la frase.

<p align="center">
  <img src="2.1.jpeg" width="700">
</p>

<p align="center">
  <em>Señal de voz mujer2</em>
</p>

**mujer2.wav:** es la grabación más intensa de las tres, con amplitudes que llegan a ±30000, lo que indica que habló más cerca del micrófono o con mayor volumen. Al inicio hay un pico muy pronunciado que puede ser una consonante explosiva o un golpe de inicio. Las palabras están bien separadas por pausas claras, aunque la alta amplitud podría introducir algo de error en el cálculo del shimmer si hay zonas cercanas a saturación.

<p align="center">
  <img src="3.1.jpeg" width="700">
</p>

<p align="center">
  <em>Señal de voz mujer3</em>
</p>

**mujer3.wav:** es visualmente la más limpia. Su amplitud es moderada (±12000) y la energía se concentra en el primer segundo y medio de la grabación, decayendo progresivamente después, lo que sugiere que la frase se dijo con más énfasis al comienzo. El ruido de fondo es el menos visible de las tres grabaciones.

- Espectro de magnitud
  
<p align="center">
  <img src="1.2.jpeg" width="700">
</p>

<p align="center">
  <em>Espectro de magnitud mujer1</em>
</p>

**mujer1.wav:** se distinguen dos grupos de picos: uno entre 300–400 Hz con un máximo de 2.9×10⁷, y otro entre 500–700 Hz, que corresponden a la frecuencia fundamental y sus primeros armónicos junto con los formantes vocálicos. La energía cae rápido por encima de 1000 Hz y hay muy poco contenido por debajo de 100 Hz, lo que habla de una buena calidad de grabación y un timbre relativamente grave para una voz femenina.

<p align="center">
  <img src="2.2.jpeg" width="700">
</p>

<p align="center">
  <em>Espectro de magnitud mujer2</em>
</p>

**mujer2.wav:** presenta la mayor magnitud de las tres, alcanzando 6.7×10⁷, coherente con la alta amplitud que ya se veía en su señal temporal. Sus picos principales están entre 250–350 Hz, con un segundo grupo cerca de 500 Hz y un tercero visible entre 600–700 Hz. La distribución armónica es ordenada y bien definida, lo que refleja una voz con buena proyección y periodicidad estable. Hay algo de energía por encima de 1000 Hz aunque bastante atenuada.

<p align="center">
  <img src="3.2.jpeg" width="700">
</p>

<p align="center">
  <em>Espectro de magnitud mujer3</em>
</p>

**mujer3.wav:** es la más distinta de las tres. Su energía no se concentra en uno o dos grupos sino que se distribuye desde 200 Hz hasta cerca de 1500 Hz, con el pico más alto (~1.2×10⁷) entre 400–450 Hz. Esta distribución amplia indica una voz con mayor brillo, más armónicos presentes y posiblemente más consonantes fricativas en la frase grabada que en las otras dos.

- Espectro de la magnitud de la señal filtrada

<p align="center">
  <img src="1.3.jpeg" width="700">
</p>

<p align="center">
  <em>Espectro de la magnitud de la señal filtrada mujer1</em>
</p>

**mujer1.wav:** el filtro delimitó bien la energía entre 150 y 500 Hz, dejando dos grupos de picos claramente separados: el principal entre 300–350 Hz con un máximo de 2.9×10⁷, y el secundario entre 450–500 Hz. La separación limpia entre ambos confirma una F0 bien definida cerca de 300 Hz con su primer armónico visible, sin que el filtro haya alterado la estructura original de la señal.

<p align="center">
  <img src="2.3.jpeg" width="700">
</p>

<p align="center">
  <em>Espectro de la magnitud de la señal filtrada mujer2</em>
</p>

**mujer2.wav:** quedó limitada al rango de interés, conservando sus picos principales entre 250–350 Hz (máximo 6.7×10⁷, el más alto de las tres) y un segundo grupo entre 450–500 Hz. Todo el contenido por encima de 500 Hz fue eliminado sin afectar los picos vocales, lo que confirma que el filtro fue bien aplicado. La alta magnitud es simplemente reflejo del mayor volumen con el que fue grabada.

<p align="center">
  <img src="3.3.jpeg" width="700">
</p>

<p align="center">
  <em>Espectro de la magnitud de la señal filtrada mujer3</em>
</p>

**mujer3.wav:** es la más particular de las tres después del filtrado. A diferencia de las otras dos, su pico dominante aparece en la parte alta del rango, entre 380–500 Hz, con un pico secundario cerca de 250 Hz. Esto es consistente con la F0 más alta de las tres (~430 Hz) y tiene sentido fisiológicamente: una voz más aguda concentra su energía fundamental en frecuencias más altas dentro del rango filtrado. El filtro funcionó correctamente aunque capturó menos armónicos completos que en los otros dos casos por la posición elevada de su F0.

---
## Análisis de gráficos hombres 
- Espectro sin filtro
  
<p align="center">
  <img src="4.1.jpeg" width="700">
</p>

<p align="center">
  <em>Señal de voz hombre1</em>
</p>

**hombre1.wav:** tiene una grabación de 5.2 segundos con amplitud de ±15000, donde se distinguen claramente los grupos de palabras separados por pausas en los segundos 0.7, 2.0 y 2.8. La energía no es pareja a lo largo de la señal: hay una zona más tranquila entre el segundo 1 y 2.5, y un pico notable alrededor de los 3 segundos que probablemente corresponde a una sílaba acentuada. Los picos positivos son ligeramente más grandes que los negativos, lo que puede deberse a la posición del micrófono o la forma de articular.

<p align="center">
  <img src="5.1.jpeg" width="700">
</p>

<p align="center">
  <em>Señal de voz hombre2</em>
</p>

**hombre2.wav:** es la grabación de menor volumen de los tres (±7000), posiblemente porque habló más lejos del micrófono. A diferencia de hombre1, su señal es densa y continua durante casi los 5 segundos completos, sin pausas claras entre palabras. El trazo es muy denso a lo largo de toda la grabación, lo que sugiere buena presencia de frecuencias altas, ya sea por fricativas frecuentes o por las características naturales de su voz. La energía es bastante estable con un pequeño aumento hacia el final.

<p align="center">
  <img src="6.1.jpeg" width="700">
</p>

<p align="center">
  <em>Señal de voz hombre3</em>
</p>

**hombre3.wav:** es el de mayor amplitud de los tres (±30000) y también el de menor duración, con unos 4 segundos. Se identifican entre 6 y 7 segmentos vocales bien delimitados con pausas cortas y regulares entre ellos. Lo más llamativo es que la energía se mantiene alta y constante de principio a fin, sin la caída natural que suele verse al terminar una frase. A pesar de la alta amplitud, la señal es simétrica entre positivo y negativo, lo que indica que no hay saturación.

- Espectro de magnitud

<p align="center">
  <img src="4.2.jpeg" width="700">
</p>

<p align="center">
  <em>Espectro de magnitud hombre1</em>
</p>
  
**hombre1.wav:** presenta tres grupos armónicos bien definidos: el primero entre 80–150 Hz, el segundo entre 200–300 Hz con el pico más alto del espectro (~3.4×10⁷), y un tercero entre 500–700 Hz. Esta distribución apunta a una F0 alrededor de 100–120 Hz, típica de una voz masculina adulta. Hay contenido residual hasta los 4000 Hz, lo que le da algo de brillo al timbre. De los tres, es el que tiene la distribución armónica más equilibrada.

<p align="center">
  <img src="5.2.jpeg" width="700">
</p>

<p align="center">
  <em>Espectro de magnitud hombre2</em>
</p>
  
**hombre2.wav:** concentra casi toda su energía en un rango muy estrecho entre 100–170 Hz, con un pico máximo de 4.6×10⁷ que es el más alto de los tres a pesar de ser la grabación de menor volumen. Los armónicos secundarios a 280–350 Hz y cerca de 500 Hz están presentes pero son notablemente más débiles. La energía cae rápido después de 600 Hz y prácticamente desaparece por encima de 1000 Hz, lo que resulta en un timbre oscuro y poco brillante comparado con los otros dos.

<p align="center">
  <img src="6.2.jpeg" width="700">
</p>

<p align="center">
  <em>Espectro de magnitud hombre3</em>
</p>
  
**hombre3.wav:** es el más grave y el de espectro más rico de los tres. Tiene cuatro grupos de picos entre 70 y 600 Hz, con magnitudes bastante similares entre sí (entre 4.8×10⁷ y 5.5×10⁷), sin que ninguno domine claramente sobre los demás. Esto indica una F0 baja (~85–100 Hz) con una serie armónica muy completa. La energía llega con algo de presencia hasta los 1000 Hz, confirmando una voz resonante y con cuerpo.

- Espectro de la magnitud de la señal filtrada
  
<p align="center">
  <img src="4.3.jpeg" width="700">
</p>

<p align="center">
  <em>Espectro de la magnitud de la señal filtrada hombre1</em>
</p>

**hombre1.wav:** el filtro delimitó bien la energía entre 80 y 400 Hz, conservando dos grupos de picos con un valle claro entre ellos alrededor de 170 Hz. El primero está entre 80–150 Hz y el segundo entre 200–300 Hz con el pico más alto (~3.4×10⁷). Esa separación limpia entre ambos confirma el F0 y su segundo armónico bien diferenciados, lo que hace de esta señal la más favorable de las tres para calcular jitter y shimmer con precisión.

<p align="center">
  <img src="5.3.jpeg" width="700">
</p>

<p align="center">
  <em>Espectro de la magnitud de la señal filtrada hombre2</em>
</p>

**hombre2.wav:** quedó con un pico muy dominante entre 100–170 Hz (máximo 4.6×10⁷), el más alto de los tres dentro del rango filtrado, seguido de un segundo grupo en 280–320 Hz y uno más pequeño justo en el límite del filtro cerca de 400 Hz. La diferencia de magnitud entre el primer pico y los demás es grande, lo que ratifica que esta voz concentra casi toda su energía en la frecuencia fundamental con poca presencia de armónicos, algo ya evidente en el espectro sin filtrar..

<p align="center">
  <img src="6.3.jpeg" width="700">
</p>

<p align="center">
  <em>Espectro de la magnitud de la señal filtrada hombre3</em>
</p>

**hombre3.wav:** es el más ancho y uniforme de los tres después del filtrado. La energía se reparte de forma bastante pareja en tres grupos entre 80 y 400 Hz, sin valles profundos entre ellos. El pico más alto (~5.3×10⁷) aparece entre 170–250 Hz, flanqueado por grupos de magnitud similar en 80–120 Hz y 300–400 Hz. Esto es consecuencia directa de su F0 más baja (~85–100 Hz), que hace que varios armónicos queden dentro del rango del filtro, dando esa apariencia de energía continua y distribuida.

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

*mujer1.wav:* la señal tiene buena amplitud (±10000) y se ve actividad vocal continua a lo largo de los ~4.5 segundos. Se notan claramente los segmentos sonoros (partes densas) separados por pequeñas pausas que corresponden a consonantes o silencios entre palabras. El pico inicial al inicio (~0.1s) puede ser un artefacto de inicio de grabación. La energía decae gradualmente hacia el final, lo cual es natural al terminar de hablar.

<p align="center">
  <img src="2.1.jpeg" width="700">
</p>

<p align="center">
  <em>Señal de voz mujer2</em>
</p>

mujer2.wav: esta es la señal con mayor amplitud de las tres (±30000), lo que indica que esta persona habló más cerca del micrófono o con mayor volumen. El pico al inicio (~0.1–0.2s) es muy pronunciado y podría ser una consonante explosiva o un artefacto. La señal tiene segmentos bien definidos con pausas claras entre palabras. La mayor amplitud puede afectar ligeramente el shimmer si hay zonas cercanas a saturación.

<p align="center">
  <img src="3.1.jpeg" width="700">
</p>

<p align="center">
  <em>Señal de voz mujer3</em>
</p>

mujer3.wav: es la señal más limpia visualmente de las tres. La amplitud es moderada (±12000) y se observa que la energía es mayor al inicio (~0–1.5s) y decae progresivamente, sugiriendo que la frase fue dicha con énfasis al principio. Los segmentos sonoros están bien separados y hay menos ruido de fondo visible.

- Espectro de magnitud
  
<p align="center">
  <img src="1.2.jpeg" width="700">
</p>

<p align="center">
  <em>Espectro de magnitud mujer1</em>
</p>

mujer1.wav: Se observan dos grupos de picos dominantes: el primero alrededor de 300–400 Hz (pico máximo ~2.9×10⁷) y el segundo alrededor de 500–700 Hz. Estos corresponden al F0 y sus primeros armónicos, más los formantes F1 y F2 del habla. La energía cae rápidamente por encima de 1000 Hz, lo que indica una voz con timbre más grave dentro del rango femenino. Hay poca energía por debajo de 100 Hz, lo que confirma buena calidad de grabación sin ruido de baja frecuencia importante.

<p align="center">
  <img src="2.2.jpeg" width="700">
</p>

<p align="center">
  <em>Espectro de magnitud mujer2</em>
</p>

mujer2.wav: Es el espectro con mayor magnitud absoluta (hasta 6.7×10⁷), consistente con la mayor amplitud vista en la señal temporal. Los picos principales están en 250–350 Hz y un segundo grupo bien definido cerca de 500 Hz. Destaca un tercer grupo de picos visible alrededor de 600–700 Hz. La distribución armónica está bien definida, lo que indica una voz bien proyectada y con buena periodicidad. La energía en frecuencias altas (>1000 Hz) es baja pero presente.

<p align="center">
  <img src="3.2.jpeg" width="700">
</p>

<p align="center">
  <em>Espectro de magnitud mujer3</em>
</p>

mujer3.wav: Este espectro es notablemente diferente a los otros dos. La energía está más distribuida en frecuencia, con picos relevantes desde ~200 Hz hasta más allá de 1000 Hz. El pico máximo (~1.2×10⁷) aparece alrededor de 400–450 Hz, pero hay actividad espectral significativa hasta los 1500 Hz. Esto sugiere una voz con mayor brillo (centroide espectral más alto), más armónicos presentes, y posiblemente una frase con más consonantes fricativas o sibilantes que las otras dos.

- Espectro de la magnitud de la señal filtrada

<p align="center">
  <img src="1.3.jpeg" width="700">
</p>

<p align="center">
  <em>Espectro de la magnitud de la señal filtrada mujer1</em>
</p>

mujer1.wav: El filtro funcionó correctamente: toda la energía está concentrada entre 150 y 500 Hz, con cero contenido fuera de ese rango. Se distinguen claramente dos grupos de picos: el primero alrededor de 300–350 Hz (pico máximo ~2.9×10⁷, el más alto de las tres) y el segundo alrededor de 450–500 Hz. La separación entre ambos grupos es nítida, lo que confirma una F0 bien definida cerca de 300 Hz con su primer armónico visible. El filtro no distorsionó la estructura espectral vocal.

<p align="center">
  <img src="2.3.jpeg" width="700">
</p>

<p align="center">
  <em>Espectro de la magnitud de la señal filtrada mujer2</em>
</p>

mujer2.wav: También con energía perfectamente limitada al rango 150–500 Hz. Los picos principales están en 250–350 Hz (máximo ~6.7×10⁷, la mayor magnitud de las tres) y un segundo grupo en 450–500 Hz. Comparado con el espectro sin filtrar, el filtro eliminó toda la energía por encima de 500 Hz sin afectar los picos principales. La estructura de dos formantes dentro del rango filtrado es consistente con una voz femenina de F0 moderada (~250 Hz). La alta magnitud refleja el mayor volumen de esta grabación.

<p align="center">
  <img src="3.3.jpeg" width="700">
</p>

<p align="center">
  <em>Espectro de la magnitud de la señal filtrada mujer3</em>
</p>

mujer3.wav: Este espectro es el más interesante de los tres. A diferencia de mujer1 y mujer2, aquí el pico dominante está desplazado hacia frecuencias más altas: el máximo (~1.1×10⁷) aparece entre 380–500 Hz, con un pico secundario visible cerca de 250 Hz. Esto indica una F0 más alta que las otras dos (consistente con el resultado numérico de ~430 Hz visto antes). El filtro funcionó bien pero la energía está concentrada en la parte superior del rango, lo cual es fisiológicamente coherente con una voz femenina de tono más agudo.

---
## Análisis de gráficos hombres 
- Espectro sin filtro
  
<p align="center">
  <img src="4.1.jpeg" width="700">
</p>

<p align="center">
  <em>Señal de voz hombre1</em>
</p>

hombre1.wav: La señal dura aproximadamente 5.2 segundos con una amplitud de ±15000. Se observa una estructura claramente segmentada con grupos de actividad vocal separados por pausas bien definidas, especialmente notorias alrededor de los segundos 0.7, 2.0 y 2.8. Esto refleja una articulación clara con separación natural entre palabras. La energía no es uniforme: hay una zona de menor intensidad entre 1.0–2.5s y un pico de energía prominente alrededor de 3.0–3.2s, que podría corresponder a una vocal acentuada o sílaba tónica. Los picos positivos son ligeramente mayores que los negativos, lo que sugiere una leve asimetría en la grabación.

<p align="center">
  <img src="5.1.jpeg" width="700">
</p>

<p align="center">
  <em>Señal de voz hombre2</em>
</p>

hombre2.wav: Con una amplitud de apenas ±7000, esta es la grabación de menor intensidad de los tres hombres, indicando que se habló con menor volumen o mayor distancia al micrófono. A diferencia de hombre1, la señal es densa y continua durante casi todos los 5 segundos, con muy pocas pausas visibles. Esto sugiere una elocución más fluida y encadenada. La densidad del trazo a lo largo de toda la señal indica presencia importante de frecuencias altas, posiblemente por fricativas o una voz naturalmente más brillante. La energía se mantiene relativamente estable con un leve incremento hacia los 3.0–3.5s.

<p align="center">
  <img src="6.1.jpeg" width="700">
</p>

<p align="center">
  <em>Señal de voz hombre3</em>
</p>

hombre3.wav: Esta es la grabación de mayor amplitud de los tres (±30000), lo que indica una voz muy proyectada o grabada muy cerca del micrófono. La señal dura ~4 segundos y presenta 6 a 7 segmentos vocales bien delimitados con pausas cortas entre ellos, visibles alrededor de 0.7s, 1.3s, 1.8s, 2.3s y 3.0s. La energía se mantiene alta y sostenida a lo largo de toda la grabación, lo cual es notable porque no decae hacia el final como suele ocurrir naturalmente. Los picos de amplitud son simétricos entre positivo y negativo, lo que indica una buena calidad de captura sin saturación evidente pese a la alta amplitud.

- Espectro de magnitud

<p align="center">
  <img src="4.2.jpeg" width="700">
</p>

<p align="center">
  <em>Espectro de magnitud hombre1</em>
</p>
  
hombre1.wav: El espectro muestra tres grupos de picos bien definidos: el primero entre 80–150 Hz (picos ~3.1×10⁷), el segundo alrededor de 200–300 Hz (pico máximo ~3.4×10⁷, el más alto del espectro) y un tercer grupo entre 500–700 Hz (~2.1×10⁷). Esta estructura de múltiples grupos armónicos bien separados indica una voz con F0 alrededor de 100–120 Hz, lo cual es típico de una voz masculina adulta. La energía decae progresivamente después de 700 Hz pero hay contenido residual visible hasta los 4000 Hz, lo que sugiere una voz con cierto brillo y presencia de formantes superiores. La distribución armónica es la más equilibrada y rica de los tres hombres.

<p align="center">
  <img src="5.2.jpeg" width="700">
</p>

<p align="center">
  <em>Espectro de magnitud hombre2</em>
</p>
  
hombre2.wav: Este espectro está claramente dominado por un único grupo de picos concentrado entre 100–170 Hz con magnitud máxima de ~4.6×10⁷, siendo el pico más alto de los tres hombres a pesar de tener la menor amplitud temporal. Hay un segundo grupo visible alrededor de 280–350 Hz (~1.9×10⁷) y un tercero más pequeño cerca de 500 Hz (~1.1×10⁷). La energía cae rápidamente después de 600 Hz y es casi nula por encima de 1000 Hz. Esto indica una voz con F0 cercana a 120–130 Hz y bajo brillo espectral, es decir, una voz más oscura y grave en timbre, con pocos armónicos de alta frecuencia. La concentración de energía en el primer pico es la característica más distintiva de esta voz.

<p align="center">
  <img src="6.2.jpeg" width="700">
</p>

<p align="center">
  <em>Espectro de magnitud hombre3</em>
</p>
  
hombre3.wav: Es el espectro más complejo y rico en contenido frecuencial de los tres. Se observan cuatro grupos de picos claramente diferenciados: el primero entre 70–100 Hz (inicio visible desde ~60 Hz), el segundo entre 130–200 Hz (pico máximo ~5.5×10⁷), el tercero entre 250–350 Hz (~5.2×10⁷) y un cuarto grupo muy notable entre 450–600 Hz (~4.8×10⁷). Lo más llamativo es que los cuatro grupos tienen magnitudes comparables entre sí, sin que uno domine claramente sobre los demás. Esto indica una voz con F0 más baja (~85–100 Hz), que es la más grave de los tres, con una serie armónica muy completa y bien distribuida. La energía se extiende con cierta presencia hasta los 1000 Hz, confirmando un timbre rico y resonante.

- Espectro de la magnitud de la señal filtrada
  
<p align="center">
  <img src="4.3.jpeg" width="700">
</p>

<p align="center">
  <em>Espectro de la magnitud de la señal filtrada hombre1</em>
</p>

hombre1.wav: El filtro actuó correctamente limitando la energía al rango 80–400 Hz, con energía nula fuera de ese rango. Se conservan dos grupos de picos principales: el primero entre 80–150 Hz (picos ~3.1×10⁷) y el segundo entre 200–300 Hz (pico máximo ~3.4×10⁷). Entre ambos grupos hay un valle bien definido alrededor de 170 Hz, lo que confirma que son el F0 y su segundo armónico claramente diferenciados. El tercer grupo que se veía en el espectro sin filtrar (~500–700 Hz) fue correctamente eliminado por el filtro. La estructura de dos picos simétricos y bien separados indica una F0 muy estable y periódica, ideal para el cálculo preciso de jitter y shimmer.

<p align="center">
  <img src="5.3.jpeg" width="700">
</p>

<p align="center">
  <em>Espectro de la magnitud de la señal filtrada hombre2</em>
</p>

hombre2.wav: El filtro conservó la energía entre 80–400 Hz con muy buena selectividad. El espectro muestra un pico dominante muy concentrado entre 100–170 Hz (máximo ~4.6×10⁷), que es el más alto de los tres hombres dentro del rango filtrado. Un segundo grupo aparece alrededor de 280–320 Hz (~1.7×10⁷) y un tercero más pequeño cerca de 380–400 Hz (~0.8×10⁷), este último justo en el límite del filtro. La relación entre el primer pico y los demás es muy alta, lo que confirma una voz con energía muy concentrada en la F0 fundamental y poca distribución armónica. Esto es coherente con el timbre oscuro y concentrado observado en el espectro sin filtrar.

<p align="center">
  <img src="6.3.jpeg" width="700">
</p>

<p align="center">
  <em>Espectro de la magnitud de la señal filtrada hombre3</em>
</p>

hombre3.wav: Este es el espectro filtrado más ancho y complejo de los tres. La energía está distribuida de forma más uniforme a lo largo de todo el rango 80–400 Hz, con tres grupos de picos de magnitudes similares: el primero entre 80–120 Hz (~3.8×10⁷), el segundo entre 170–250 Hz (pico máximo ~5.3×10⁷) y un tercer grupo muy notable entre 300–400 Hz (~3.8×10⁷). A diferencia de hombre1 y hombre2, aquí no hay valles profundos entre los grupos, sino una distribución más continua de energía. Esto confirma la F0 más baja de los tres (~85–100 Hz) con múltiples armónicos dentro del rango filtrado, lo que hace que el filtro capture más ciclos glotales completos y sus primeras resonancias.

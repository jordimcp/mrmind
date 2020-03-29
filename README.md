# mrmind
Juego Master Mind en python 

https://es.wikipedia.org/wiki/Mastermind

El ordenador crea una secuencia de 4 colores aleatoria. El jugador tiene 10 intentos para averiguar la secuencia,
empezando por la fila de mas abajo hasta la de más arriba.

Presionando sobre uno de los colores se selecciona el color, y presionando sobre las casillas de la fila pertinente
se coloca el color. Cuando el jugador quiere checkear si la secuencia es correcta se debe presionar en la casilla
más a la derecha de la fila en la que se está jugando.

Después de checkeado la secuencia pueden aparecer unos colores entre la secuencia y la casilla del extremo.
  - Blanco: Una casilla tiene el color correcto pero no la posicion
  - Lima (verde): Una casilla tiene el color y la posición correcta

Se acaba el juego cuando el jugador tiene 4 casillas verdes o lo ha intentado ya 10 veces.

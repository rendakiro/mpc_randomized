# mpc_randomized
Pequeño script para cargar aleatoriamente carpetas y procesarlas en MPC

## Introducción
Tengo una pequeña radio online _http://icecast.rendakiro.es:8000/play_ debido a lo que suelo escuchar no lo encuentro mucho en las radios comunes, así que aproveche hace tiempo y monte mi propia radio online que da servicio a poca gente.

Pero luego surgió un problema, tenía más canciones que la soportada por la playlist, y claro, algunas se quedaban fuera por nombre.
La solución es simplona, un script en Python que recorre todas mis carpetas, selecciona 250, limpia la playlist actual y genera uno nuevo, así puede sonar cualquier canción y no tengo que ir vigilando la playlist.

Nada más, así que aquí está público para quien sea. 
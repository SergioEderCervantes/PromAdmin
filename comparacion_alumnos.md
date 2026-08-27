# Comparación: Base de Datos vs Lista Nueva

- **Registros en BD (`db.sqlite3`, tabla `Alumno`):** 67
- **Registros en la lista nueva que enviaste:** 62
- **Emparejados (mismo alumno en ambos lados):** 52
- **Faltan en la BD (están en tu lista, no existen como alumno en la BD):** 10 (9 si contamos el caso "Reyli", ver nota)
- **Sobran en la BD (existen en la BD, no aparecen en tu lista nueva):** 15

> Nota de matching: los nombres no siempre coinciden letra por letra entre la lista y la BD (acentos, apellidos de más/menos, mayúsculas, typos). Emparejé por similitud de nombre; los casos dudosos están marcados con ⚠️.

## 1. Alumnos que SÍ están en ambos — diferencias de min/max

`diff_min` y `diff_max` = (valor de tu lista nueva) − (valor actual en BD). Positivo = tu lista tiene más que la BD.

| Nombre (BD) | Min BD | Max BD | Min Lista | Max Lista | Diff Min | Diff Max |
|---|---|---|---|---|---|---|
| Rene Rosendo De Anda Medina | 12 | 10 | 22 | 26 | +10 | +16 |
| Alfredo Chinchillas ⚠️ (lista: "...Duardo") | 3 | 7 | 13 | 22 | +10 | +15 |
| Osmar Alvarez Barranco | 0 | 0 | 10 | 20 | +10 | +20 |
| Juan Carlos Uriarte Padilla | 0 | 0 | 8 | 20 | +8 | +20 |
| Emiliano Jahir Espinoza Herrera | 0 | 0 | 8 | 12 | +8 | +12 |
| Jose Luis Espinoza Sanchez | 0 | 0 | 4 | 16 | +4 | +16 |
| Yahir Eduardo Tostado Nieto | 10 | 15 | 18 | 22 | +8 | +7 |
| Diego Saldaña Centeno | 0 | 0 | 6 | 10 | +6 | +10 |
| Brandon Ruiz Morales | 0 | 0 | 8 | 8 | +8 | +8 |
| Daniel Omar Flores Ibarra | 5 | 7 | 11 | 16 | +6 | +9 |
| Nadia Guadalupe Ramirez Solis | 0 | 0 | 5 | 10 | +5 | +10 |
| Rafael Márquez Macías | 6 | 20 | 17 | 23 | +11 | +3 |
| Angel Ramses Martinez Herrera ⚠️ (lista: "Ramses") | 0 | 0 | 5 | 15 | +5 | +15 |
| Camila Jaasiel Mendoza Martínez | 16 | 8 | 7 | 15 | -9 | +7 |
| Angel Daniel López Rodríguez | 16 | 8 | 8 | 16 | -8 | +8 |
| Valeria Michelle Saucedo Díaz | 15 | 5 | 10 | 15 | -5 | +10 |
| Gustavo Andrés Mojica Lamas | 12 | 5 | 5 | 12 | -7 | +7 |
| Paola Becerra Rodriguez ⚠️ (lista: "...Guadalupe...") | 0 | 0 | 4 | 6 | +4 | +6 |
| Hector Oswaldo Villegas Pérez | 15 | 10 | 10 | 15 | -5 | +5 |
| Diego Adriel Segura Ramírez | 10 | 5 | 6 | 10 | -4 | +5 |
| Sergio Eder Cervantes Rincon | 8 | 28 | 8 | 20 | 0 | -8 |
| Elias Lopez Fematt | 10 | 22 | 8 | 17 | -2 | -5 |
| Juan Osbaldo Escalera Valenciano | 7 | 10 | 4 | 6 | -3 | -4 |
| Diana Esmeralda González Rivera | 7 | 12 | 10 | 8 | +3 | -4 |
| Saul Alvarez Gaspar | 4 | 20 | 6 | 15 | +2 | -5 |
| Daan Jostin Carabez García | 6 | 15 | 5 | 10 | -1 | -5 |
| Cindy Fabiola Hernandez Muñoz | 0 | 0 | 2 | 4 | +2 | +4 |
| Cristian Emmanuel Aguilar Nuñez | 4 | 8 | 5 | 12 | +1 | +4 |
| Luis Alberto Hernández Velasco | 17 | 22 | 19 | 19 | +2 | -3 |
| Jesus David Montero Ayala | 5 | 6 | 6 | 10 | +1 | +4 |
| Jaime Iván López Gutiérrez | 3 | 7 | 6 | 8 | +3 | +1 |
| Ricardo Ramírez Torres | 4 | 4 | 5 | 7 | +1 | +3 |
| Uriel Rodrigues Guadarrama ⚠️ (typo "Rodrigues") | 7 | 7 | 8 | 10 | +1 | +3 |
| Christian Isaac Martinez Sánchez | 6 | 8 | 4 | 6 | -2 | -2 |
| Laura Jaretzi Dominguez Gallardo | 11 | 16 | 10 | 13 | -1 | -3 |
| Luis David Flores Martínez | 8 | 14 | 6 | 12 | -2 | -2 |
| Judith Yahaira Ortega Ortega | 6 | 12 | 8 | 11 | +2 | -1 |
| Jesús Eduardo Tapia Ávalos | 10 | 13 | 13 | 13 | +3 | 0 |
| Martha Melinna Flores Hernández | 9 | 12 | 9 | 10 | 0 | -2 |
| Oswaldo De La Cruz García | 5 | 10 | 4 | 9 | -1 | -1 |
| Cinthia Edith García de Luna | 5 | 5 | 4 | 6 | -1 | +1 |
| Joshua Dávila Rodríguez | 5 | 9 | 5 | 7 | 0 | -2 |
| Diego Ivan Salas Pedroza | 3 | 5 | 4 | 6 | +1 | +1 |
| Alondra Ibarra Chavez ⚠️ (lista: "Alondra Ibarra", max "Aprox 9") | 5 | 8 | 6 | 9 | +1 | +1 |
| Ilse Jacqueline Martínez Espinosa | 9 | 7 | 7 | 7 | -2 | 0 |
| Adal Yahir De Luna Nieves | 5 | 10 | 5 | 8 | 0 | -2 |
| Ian Alejandro Hernandez Aranda | 5 | 4 | 5 | 5 | 0 | +1 |
| Alondra Joceline Quezada Alfaro | 5 | 8 | 5 | 9 | 0 | +1 |
| Jaime López Martinez | 4 | 4 | 4 | 5 | 0 | +1 |
| Kimberly Marmolejo García | 5 | 8 | 6 | 8 | +1 | 0 |
| Marco Antonio Olivares Guzman | 6 | 12 | 7 | 12 | +1 | 0 |
| Oscar Manuel Garcia Rodriguez | 4 | 4 | 4 | 4 | 0 | 0 |

**52 coinciden por nombre; de esos, 46 tienen algún valor de min y/o max distinto y solo 1 (Oscar Manuel Garcia Rodriguez) coincide exacto en min y max.**

## 2. Faltan en la BD (10 nombres de tu lista sin alumno correspondiente)

| Nombre | Min | Max |
|---|---|---|
| Bruno Muñoz | 5 | 15 |
| Abraham Barrientos Esquivel | 1 | 5 |
| Diana Cristina Dávila Martínez | 8 | 12 |
| Ricardo Almada Diaz | 6 | 12 |
| YAHIR GUEVARA CARDONA | 3 | 5 |
| Edgar Alejandro Cedeño Suárez | 16 | 22 |
| Erik Omar Alba Dávila | 13 | 15 |
| Reyli Uvaldo Martínez Hernández ⚠️ | 6 | 14 |
| Josimar Maldonado Rosales | 6 | 10 |
| Enrique Amador Macías | 5 | 10 |

⚠️ **"Reyli Uvaldo Martínez Hernández"** probablemente sea la misma persona que **"Reyli Ubaldo"** en la BD (min/max 0/0) — el algoritmo de emparejamiento no los unió por la diferencia de apellidos/typo ("Uvaldo" vs "Ubaldo"). Si es la misma persona, serían **9 faltantes reales**, no 10.

## 3. Sobran en la BD (15 alumnos que no aparecen en tu lista nueva)

| Nombre | Min | Max |
|---|---|---|
| Aaron Ruiz Fonseca | 4 | 6 |
| Angel Esteban Esparza Muñoz | 9 | 12 |
| Angel Garza Flores | 10 | 6 |
| Burno Santiago Muñoz Lopez | 0 | 0 |
| Carlos Vicente Muñoz | 2 | 8 |
| Eric Daniel Salas Martinez | 0 | 0 |
| Ernesto Alonso Morquecho Canales | 0 | 0 |
| Jaime Alberto Cruz Rodriguez | 3 | 10 |
| Juan Mauricio Montoya Martínez | 2 | 6 |
| Luís Fernando Navarro Lozano | 8 | 11 |
| Miguel Angel Torres Esparza | 0 | 0 |
| Reyli Ubaldo ⚠️ | 0 | 0 |
| Ricardo Padilla Hernández | 6 | 10 |
| Tomás Alberto Alegría Martínez | 6 | 15 |
| Vicente Barrios Mariscal | 3 | 6 |

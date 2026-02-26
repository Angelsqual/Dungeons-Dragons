# Mazmorras y Dragones 2D (terminal)

Juego sencillo estilo roguelike hecho desde cero en Python (sin dependencias externas).

---

## Quiero jugar pero no sé programar (guía desde cero)

Perfecto. Sigue estos pasos **en orden**.

## 1) Instalar lo mínimo

### En Windows
1. Instala **Python** desde: https://www.python.org/downloads/
2. Durante la instalación, marca la casilla **"Add Python to PATH"**.
3. (Opcional, recomendado) Instala **Git** desde: https://git-scm.com/download/win

### En macOS
1. Instala Python 3 (por ejemplo desde python.org o con Homebrew):
   - `brew install python`
2. (Opcional, recomendado) Instala Git:
   - `brew install git`

### En Ubuntu / Debian (Linux)
```bash
sudo apt update
sudo apt install -y python3 git
```

---

## 2) Tener el juego en tu ordenador

Tienes dos formas:

### Opción A (fácil): Descargar ZIP desde GitHub
1. En tu repositorio de GitHub, pulsa botón verde **Code**.
2. Pulsa **Download ZIP**.
3. Descomprime el ZIP en una carpeta que recuerdes (por ejemplo Escritorio).

### Opción B (con Git)
1. Copia la URL del repo (`https://github.com/usuario/repositorio.git`).
2. Abre terminal y ejecuta:
```bash
git clone URL_DE_TU_REPO
```
3. Entra en la carpeta descargada:
```bash
cd NOMBRE_DEL_REPO
```

---

## 3) Ejecutar el juego

1. Abre terminal (CMD/PowerShell en Windows, Terminal en macOS/Linux).
2. Ve a la carpeta del juego:
```bash
cd dnd_2d_terminal
```
3. Ejecuta:
```bash
python3 game.py
```

> En algunos Windows puede ser:
```bash
python game.py
```

Si se abre el mapa con símbolos (`@`, `#`, `E`, etc.), ya estás jugando 🎮

---

## 4) Controles del juego

- `w`, `a`, `s`, `d`: moverte
- `p`: beber poción
- `i`: ver enemigos
- `q`: salir

---

## 5) Objetivo

- Avanza por 3 niveles de mazmorra.
- Mejora tu personaje.
- Derrota al Dragón final.

---

## 6) Si no te aparece en GitHub (muy importante)

Si en tu GitHub no ves la carpeta `dnd_2d_terminal`, significa que tus cambios locales no se han subido al remoto.

Desde la raíz del repo, ejecuta:
```bash
git status
git log --oneline -n 5
git push
```

Si `git push` da error por no tener remoto configurado, añade tu repo:
```bash
git remote add origin URL_DE_TU_REPO
git branch -M main
git push -u origin main
```

---

## 7) Símbolos del mapa

- `@` héroe
- `E` enemigo normal
- `D` dragón
- `#` muro
- `>` escaleras al siguiente piso
- `$` oro
- `!` poción

---

## Requisitos técnicos

- Python 3.10 o superior.

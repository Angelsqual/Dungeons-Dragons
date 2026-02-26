#!/usr/bin/env python3
"""Mazmorras y Dragones 2D - juego de terminal sencillo e interactivo."""

from __future__ import annotations

import random
from dataclasses import dataclass, field

WIDTH = 30
HEIGHT = 15
FLOORS_TO_WIN = 3


@dataclass
class Hero:
    x: int
    y: int
    hp: int = 25
    max_hp: int = 25
    attack: int = 5
    defense: int = 2
    level: int = 1
    xp: int = 0
    potions: int = 1
    gold: int = 0


@dataclass
class Enemy:
    x: int
    y: int
    hp: int
    attack: int
    defense: int
    name: str
    xp: int


@dataclass
class GameState:
    floor: int = 1
    map_grid: list[list[str]] = field(default_factory=list)
    hero: Hero | None = None
    enemies: list[Enemy] = field(default_factory=list)
    message: str = "Bienvenido a Mazmorras y Dragones 2D"
    game_over: bool = False
    victory: bool = False


def new_floor(state: GameState) -> None:
    """Genera una nueva mazmorra y coloca entidades."""
    grid = [["#" for _ in range(WIDTH)] for _ in range(HEIGHT)]

    # Cava un área central con algunos muros internos aleatorios.
    for y in range(1, HEIGHT - 1):
        for x in range(1, WIDTH - 1):
            grid[y][x] = "."
            if random.random() < 0.1:
                grid[y][x] = "#"

    # Garantiza algunas celdas limpias alrededor del spawn.
    spawn_x, spawn_y = 2, 2
    for oy in range(-1, 2):
        for ox in range(-1, 2):
            grid[spawn_y + oy][spawn_x + ox] = "."

    # Escaleras de salida.
    stairs_x, stairs_y = WIDTH - 3, HEIGHT - 3
    grid[stairs_y][stairs_x] = ">"

    # Tesoros y pociones.
    for _ in range(8):
        x, y = random_empty_cell(grid)
        grid[y][x] = "$"

    for _ in range(4):
        x, y = random_empty_cell(grid)
        grid[y][x] = "!"

    # Enemigos.
    enemies = []
    for _ in range(4 + state.floor):
        x, y = random_empty_cell(grid)
        enemy = build_enemy_for_floor(state.floor, x, y)
        enemies.append(enemy)

    hero = state.hero or Hero(spawn_x, spawn_y)
    hero.x, hero.y = spawn_x, spawn_y

    state.map_grid = grid
    state.enemies = enemies
    state.hero = hero
    state.message = f"Has entrado en la mazmorra nivel {state.floor}."


def build_enemy_for_floor(floor: int, x: int, y: int) -> Enemy:
    if floor < FLOORS_TO_WIN:
        name = random.choice(["Goblin", "Esqueleto", "Orco"])
        hp = random.randint(7, 12) + floor
        attack = random.randint(3, 5) + floor
        defense = random.randint(1, 3)
        xp = random.randint(5, 9)
    else:
        name = "Dragón"
        hp = random.randint(15, 22)
        attack = random.randint(6, 9)
        defense = random.randint(2, 4)
        xp = random.randint(12, 16)
    return Enemy(x=x, y=y, hp=hp, attack=attack, defense=defense, name=name, xp=xp)


def random_empty_cell(grid: list[list[str]]) -> tuple[int, int]:
    while True:
        x = random.randint(1, WIDTH - 2)
        y = random.randint(1, HEIGHT - 2)
        if grid[y][x] == ".":
            return x, y


def draw(state: GameState) -> None:
    hero = state.hero
    if hero is None:
        return

    print("\n" * 2)
    print(f"=== MAZMORRAS Y DRAGONES 2D | Piso {state.floor}/{FLOORS_TO_WIN} ===")
    print(
        f"Vida {hero.hp}/{hero.max_hp} | Atk {hero.attack} | Def {hero.defense} | "
        f"Lvl {hero.level} XP {hero.xp} | Oro {hero.gold} | Pociones {hero.potions}"
    )

    enemy_positions = {(e.x, e.y): e for e in state.enemies if e.hp > 0}

    for y in range(HEIGHT):
        row = []
        for x in range(WIDTH):
            if x == hero.x and y == hero.y:
                row.append("@")
            elif (x, y) in enemy_positions:
                row.append("D" if enemy_positions[(x, y)].name == "Dragón" else "E")
            else:
                row.append(state.map_grid[y][x])
        print("".join(row))

    print("\nLeyenda: @ tú, E enemigo, D dragón, # muro, > salida, $ oro, ! poción")
    print("Comandos: w/a/s/d mover | p usar poción | i info enemigos | q salir")
    print(f"\n{state.message}")


def process_command(state: GameState, command: str) -> None:
    hero = state.hero
    if hero is None:
        return

    command = command.strip().lower()

    if command == "q":
        state.game_over = True
        state.message = "Has abandonado la aventura."
        return

    if command == "p":
        if hero.potions <= 0:
            state.message = "No te quedan pociones."
        elif hero.hp >= hero.max_hp:
            state.message = "Ya tienes la vida al máximo."
        else:
            heal = random.randint(8, 12)
            hero.hp = min(hero.max_hp, hero.hp + heal)
            hero.potions -= 1
            state.message = f"Bebes una poción y recuperas {heal} de vida."
            enemies_turn(state)
        return

    if command == "i":
        living = [e for e in state.enemies if e.hp > 0]
        if not living:
            state.message = "No hay enemigos vivos en esta planta."
        else:
            preview = ", ".join(f"{e.name}({e.hp}HP)" for e in living[:6])
            state.message = f"Enemigos: {preview}"
        return

    moves = {"w": (0, -1), "s": (0, 1), "a": (-1, 0), "d": (1, 0)}
    if command not in moves:
        state.message = "Comando no válido."
        return

    dx, dy = moves[command]
    nx, ny = hero.x + dx, hero.y + dy

    if not (0 <= nx < WIDTH and 0 <= ny < HEIGHT):
        state.message = "No puedes salir del mapa."
        return

    target = state.map_grid[ny][nx]
    if target == "#":
        state.message = "Un muro bloquea tu paso."
        return

    # ¿Hay enemigo en la casilla?
    enemy = get_enemy_at(state, nx, ny)
    if enemy is not None:
        hit = max(1, hero.attack + random.randint(-1, 2) - enemy.defense)
        enemy.hp -= hit
        if enemy.hp <= 0:
            hero.x, hero.y = nx, ny
            hero.xp += enemy.xp
            reward = random.randint(4, 10)
            hero.gold += reward
            state.message = f"Has derrotado a {enemy.name}. +{enemy.xp}XP y {reward} oro."
            maybe_level_up(state)
            if enemy.name == "Dragón" and state.floor == FLOORS_TO_WIN:
                state.victory = True
                state.game_over = True
                state.message = "¡Derrotaste al Dragón final! El reino está a salvo."
                return
        else:
            state.message = f"Golpeas a {enemy.name} por {hit} de daño."
        enemies_turn(state)
        return

    # Mover y resolver casilla.
    hero.x, hero.y = nx, ny

    if target == "$":
        gain = random.randint(6, 15)
        hero.gold += gain
        state.map_grid[ny][nx] = "."
        state.message = f"Encuentras un cofre con {gain} monedas de oro."
    elif target == "!":
        hero.potions += 1
        state.map_grid[ny][nx] = "."
        state.message = "Has recogido una poción."
    elif target == ">":
        if state.floor >= FLOORS_TO_WIN:
            state.message = "Necesitas derrotar al Dragón para ganar."
        else:
            state.floor += 1
            new_floor(state)
            return
    else:
        state.message = "Te mueves en silencio por la mazmorra..."

    enemies_turn(state)


def get_enemy_at(state: GameState, x: int, y: int) -> Enemy | None:
    for enemy in state.enemies:
        if enemy.hp > 0 and enemy.x == x and enemy.y == y:
            return enemy
    return None


def enemies_turn(state: GameState) -> None:
    hero = state.hero
    if hero is None:
        return

    for enemy in state.enemies:
        if enemy.hp <= 0:
            continue

        dx = hero.x - enemy.x
        dy = hero.y - enemy.y
        distance = abs(dx) + abs(dy)

        if distance == 1:
            dmg = max(1, enemy.attack + random.randint(-1, 1) - hero.defense)
            hero.hp -= dmg
            state.message += f" | {enemy.name} te golpea por {dmg}."
            if hero.hp <= 0:
                state.game_over = True
                state.message = "Has muerto en la mazmorra... Fin de la partida."
                return
            continue

        # Movimiento simple hacia el jugador.
        step_x = 0 if dx == 0 else (1 if dx > 0 else -1)
        step_y = 0 if dy == 0 else (1 if dy > 0 else -1)

        candidates = []
        if abs(dx) > abs(dy):
            candidates = [(enemy.x + step_x, enemy.y), (enemy.x, enemy.y + step_y)]
        else:
            candidates = [(enemy.x, enemy.y + step_y), (enemy.x + step_x, enemy.y)]

        for nx, ny in candidates:
            if can_enemy_move_to(state, nx, ny):
                enemy.x, enemy.y = nx, ny
                break


def can_enemy_move_to(state: GameState, x: int, y: int) -> bool:
    hero = state.hero
    if hero is None:
        return False
    if not (0 <= x < WIDTH and 0 <= y < HEIGHT):
        return False
    if state.map_grid[y][x] == "#":
        return False
    if x == hero.x and y == hero.y:
        return False
    if get_enemy_at(state, x, y) is not None:
        return False
    return True


def maybe_level_up(state: GameState) -> None:
    hero = state.hero
    if hero is None:
        return

    threshold = hero.level * 12
    while hero.xp >= threshold:
        hero.xp -= threshold
        hero.level += 1
        hero.max_hp += 4
        hero.hp = hero.max_hp
        hero.attack += 1
        hero.defense += 1
        state.message += f" ¡Subes a nivel {hero.level}!"
        threshold = hero.level * 12


def main() -> None:
    random.seed()
    state = GameState()
    new_floor(state)

    while not state.game_over:
        draw(state)
        cmd = input("\nTu acción: ")
        process_command(state, cmd)

    draw(state)
    if state.victory:
        print("\n🏆 Victoria total. Gracias por jugar.")
    else:
        print("\n💀 Juego terminado.")


if __name__ == "__main__":
    main()

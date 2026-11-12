import pydirectinput
import pygetwindow as gw
import time
import keyboard
import functools
import os

TOGGLE_BUTTON = 'f8'
EXIT_BUTTON = 'f9'
is_paused = False

def toggle_macro():
    global is_paused
    is_paused = not is_paused
    if is_paused:
        print(f"\n[ПАУЗА] Ждем снятия... (Кнопка выхода: {EXIT_BUTTON})")
    else:
        print("\n[АКТИВНО] Продолжаем работу!")

def exit_macro():
    print(f"\n[ВЫХОД] Нажата {EXIT_BUTTON}. Скрипт полностью остановлен.")
    os._exit(0)

keyboard.add_hotkey(TOGGLE_BUTTON, toggle_macro)
keyboard.add_hotkey(EXIT_BUTTON, exit_macro)

def delay_with_pause(seconds):
    time.sleep(seconds)
    while is_paused:
        time.sleep(0.1)

def activate_window_first(func):
    @functools.wraps(func)
    def wrapper(target_title):
        windows = gw.getWindowsWithTitle(target_title)
        if not windows:
            print(f"Окно '{target_title}' не найдено.")
            return

        print(f"Окно '{target_title}' найдено. Активируем...")
        try:
            windows[0].activate()
        except Exception:
            pass
    
        time.sleep(3)
        return func()
    return wrapper

@activate_window_first
def jump_plus_lcm():
    while True:
        delay_with_pause(0.1)
        
        pydirectinput.keyDown('space')
        pydirectinput.click()
        pydirectinput.keyUp('space')


@activate_window_first
def antiafk_w():
    minutes = 18
    while True:
        for i in range(minutes):
            delay_with_pause(60)
            print(f'minute of afk:{i}')
        pydirectinput.keyDown('w')
        pydirectinput.keyUp('w')


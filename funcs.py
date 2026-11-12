import pydirectinput
import pygetwindow as gw
import time
import keyboard

def jump_plus_lcm(target_title):
    windows = gw.getWindowsWithTitle(target_title)
    if not windows:
        print(f"Окно '{target_title}' не найдено.")
        return
    
    win = windows[0]
    print(f"Окно '{target_title}' найдено. Активируем...")
    

    try:
        win.activate()
    except Exception:
        print("Внимание: Нажмите на окно Roblox мышкой, чтобы сделать его активным!")

    print("Анти-АФК начнется через 3 секунды.")
    print("Для экстренной остановки нажмите и удерживайте клавишу F8.")
    time.sleep(3)
    pydirectinput.keyDown('space')
    while True:
        # Надежная проверка аппаратного прерывания
        if keyboard.is_pressed('f8'):
            pydirectinput.keyUp('space')
            break

        pydirectinput.click()
        
        
        for _ in range(10):
            if keyboard.is_pressed('f8'):
                print("Нажат F8. Выход из программы.")
                pydirectinput.keyUp('space')
                return
            time.sleep(0.1)


def anti_afk(target_title):
        windows = gw.getWindowsWithTitle(target_title)
        if not windows:
            print(f"Окно '{target_title}' не найдено.")
            return
        
        win = windows[0]
        print(f"Окно '{target_title}' найдено. Активируем...")
        

        try:
            win.activate()
        except Exception:
            print("Внимание: Нажмите на окно Roblox мышкой, чтобы сделать его активным!")

        print("Анти-АФК начнется через 3 секунды.")
        print("Для экстренной остановки нажмите и удерживайте клавишу F8.")
        time.sleep(3)
        while True:
            if keyboard.is_pressed('f8'):
                pydirectinput.keyUp('space')
                break

            

            for _ in range(10):
                if keyboard.is_pressed('f8'):
                    print("Нажат F8. Выход из программы.")
                    pydirectinput.keyUp('space')
                    return
                time.sleep(0.1)

from ahk import AHK

ahk = AHK()

def show_window_titles():
    print("Собираю список окон...\n")
    
    # Получаем все окна, которые видит система
    windows = ahk.list_windows()
    count = 0
    
    for win in windows:
        try:
            title = win.title
            # Выводим только те окна, у которых заголовок не пустой
            if title.strip():
                print(f"ID: {win.id:<10} | Заголовок: '{title}'")
                count += 1
        except Exception:
            # Игнорируем окна, которые закрылись в момент опроса или к которым нет доступа
            continue
            
    print(f"\nВсего найдено окон с заголовками: {count}")
    print("Найдите в списке нужное окно (например, игру) и скопируйте текст внутри одинарных кавычек.")

if __name__ == "__main__":
    show_window_titles()
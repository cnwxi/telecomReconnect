from pynput import mouse

def on_move(x, y):
    # print(f"Pointer moved to ({x}, {y})")
    pass

def on_click(x, y, button, pressed):
    if pressed:
        print(f"Mouse clicked at ({x}, {y}) with {button}")
    else:
        print(f"Mouse released at ({x}, {y}) with {button}")

def on_scroll(x, y, dx, dy):
    # print(f"Mouse scrolled at ({x}, {y})({dx}, {dy})")
    listener.stop()
    print("stop listener")

# 创建一个监听器对象
with mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
    listener.join()
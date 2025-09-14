import pyautogui
import time

print("Mova o mouse para a posição desejada. Aguarde 5 segundos...")
time.sleep(5)
x, y = pyautogui.position()
print(f"Posição atual do mouse: x={x}, y={y}")
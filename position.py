import pyautogui
import time

print("Mova o mouse para a posição desejada. Aguarde 6 segundos...")
time.sleep(6)
x, y = pyautogui.position()
print(f"Posição atual do mouse: x={x}, y={y}")
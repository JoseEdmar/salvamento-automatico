# Salvador de arquivos automático
# Aperte CTRL + ALT + N para rodar
import pyautogui as pa
import time
import pyperclip
from ids_e_comentario import ids, comentario_fixo

pa.PAUSE = 4

# lista de IDs para processar (Vem do arquivo ids_e_cometario.py)
# ---------------------------------------------------
# 1) Navegação inicial até chegar na tela de busca
# ---------------------------------------------------
pa.click(x=1915, y=1050)
pa.click(x=37, y=536)
pa.press('ENTER')

#pa.hotkey('win', 'up')
pa.press('win')
pa.write('firefox')
pa.press('ENTER')
#pa.hotkey('win', 'up')
pa.write('SEU SITE AQUI')
pa.press('ENTER')
pa.click(x=1219, y=568)
pa.click(x=519, y=325)

# ---------------------------------------------------
# 2) Loop: para cada ID, repete tudo abaixo
# ---------------------------------------------------
for id_atual in ids:

    # clicar em "Localizar cadastros" e digitar o ID
    pa.click(x=804, y=425)
    pa.write(id_atual)
    pa.click(x=1091, y=560)
    pa.press('ENTER')

    # clicar em Anexo
    localizacao_imagem3 = pa.locateOnScreen("anexo.png"
    , confidence=0.8)
    if  localizacao_imagem3:
      x,y = pa.center(localizacao_imagem3)
      pa.moveTo(x,y)
      pa.click(x,y)

    # escrever comentário
    pa.click(x=523, y=390)
    pyperclip.copy(comentario_fixo)
    pa.hotkey('ctrl', 'v')  # selecionar tudo
    
    # selecionar documento do cadastro
    pa.click(x=423, y=480)
    pa.click(x=236, y=211)
    pa.press('ENTER')

    # clicar em salvar
    pa.press('pagedown')  # descer a tela
    time.sleep(2)  # esperar a imagem carregar na tela
    localizacao_imagem = pa.locateOnScreen("salvar.png"
    , confidence=0.8)
    if  localizacao_imagem:
      x,y = pa.center(localizacao_imagem)
      pa.moveTo(x,y)
      pa.click(x,y)
    
    # excluir o anexo já salvo
    pa.click(x=566, y=1052)
    pa.click(x=618, y=444)
    pa.press('DELETE')

    # voltar para a tela de Cadastros
    pa.click(x=830, y=1054)
    localizacao_imagem2 = pa.locateOnScreen("cadastro.png"
    , confidence=0.8)
    if  localizacao_imagem2:
      x,y = pa.center(localizacao_imagem2)
      pa.moveTo(x,y)
      pa.click(x,y)
    

# fim do loop
import pyautogui
import time



pyautogui.alert('O código vai começar. Não mexa em NADA enquanto o código tiver rodando. Quando finalizar, eu te aviso')

pyautogui.PAUSE = 1
# apertar o windows do teclado
pyautogui.press('win')
# digitar chrome
pyautogui.write("chrome")
# apertar enter
pyautogui.press('enter')

# entrar no Gmail
pyautogui.write('gmail')
pyautogui.press('enter')

#esperar carregar o google
while not pyautogui.locateOnScreen('imagem.png'):
    time.sleep(1)

# localizar a imagem -> vai te dar 4 informações: posicao x, posicao y, largura e altura
x, y, largura, altura = pyautogui.locateOnScreen('imagem.png')
# clicar no meio da imagem
pyautogui.click(x + largura/2, y + altura/2)


#esperar o gmail
while not pyautogui.locateOnScreen('imagem.png'):
    time.sleep(1)

# entrar em contatos
x, y, largura, altura = pyautogui.locateOnScreen('imagem.png')
pyautogui.click(x + largura/2, y + altura/2)

time.sleep(1)
x, y, largura, altura = pyautogui.locateOnScreen('imagem.png')
pyautogui.click(x + largura/2, y + altura/2)

#esperar o contatos
while not pyautogui.locateOnScreen('imagem.png'):
    time.sleep(1)

# exportar os contatos
x, y, largura, altura = pyautogui.locateOnScreen('imagem.png')
pyautogui.click(x + largura/2, y + altura/2)
x, y, largura, altura = pyautogui.locateOnScreen('imagem.png')
pyautogui.click(x + largura/2, y + altura/2)


#Escrevendo E-mail


import pandas as pd
import pyperclip

time.sleep(2)
df = pd.read_csv(r'o caminho do arquivo')
df = df.dropna(axis=1)


pyautogui.hotkey('ctrl', 'pgup')

for email in df['coluna do df']:
    # clicar no botão escrever
    time.sleep(1)
    x, y, largura, altura = pyautogui.locateOnScreen('imagem.png')
    pyautogui.click(x + largura / 2, y + altura / 2)
    time.sleep(1)
    # escrever o email
    pyautogui.write(email)
    # enter
    pyautogui.press('enter')
    # tab para o assunto do email
    pyautogui.press('tab')
    pyautogui.write('cabeçallho')
    # tab para o corpo do email
    pyautogui.press('tab')
    texto = """
    Mensagem """
    pyperclip.copy(texto)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.hotkey('ctrl', 'enter')

pyautogui.alert('O código terminou, pode pegar o seu computador de volta')
import mysql.connector
from PyQt5 import uic, QtWidgets

banco = mysql.connector.connect(
    host="localhost",
    user = 'root',
    password = '',
    database='db_led'    
)

app = QtWidgets.QApplication([])
leds = uic.loadUi('untitled.ui')

def corLed():
    cor = ""
    if(leds.LedAzul.isChecked()):
        cor = "Azul"
        return cor
    elif(leds.LedVermelho.isChecked()):
        cor = "Vermelho"
        return cor
    cor = "Verde" 
    return cor


def submit():
    cursor = banco.cursor()
    try:
        cursor.execute(f"Insert into tbl_led (nome) values('{corLed()}')")
        banco.commit()
        print("Cadastro realizado com sucesso")
    except Exception as e:
        print(f"Deu merda ai filhao, ve ai: {e}")
    return    

leds.BtnEnviar.clicked.connect(submit)
leds.show()
app.exec()
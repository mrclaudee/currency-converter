from PySide2 import QtWidgets
import currency_converter

# Définition de l'app
class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.c = currency_converter.CurrencyConverter()
        self.setWindowTitle("Convertisseur de devises")
        self.setup_ui()
        self.set_default_values()
        
    def setup_ui(self):
        #Orientation horizontale du layout
        self.layout = QtWidgets.QHBoxLayout(self)
        
        #Eléments du layout
        self.cbb_devisesFrom = QtWidgets.QComboBox() 
        self.spn_montant = QtWidgets.QSpinBox()
        self.cbb_devisesTo = QtWidgets.QComboBox()
        self.spn_montantConverti = QtWidgets.QSpinBox()
        self.btn_inverser = QtWidgets.QPushButton("Inverser devises")
        
        #Ajout des éléments aux layout
        self.layout.addWidget(self.cbb_devisesFrom)
        self.layout.addWidget(self.spn_montant)
        self.layout.addWidget(self.cbb_devisesTo)
        self.layout.addWidget(self.spn_montantConverti)
        self.layout.addWidget(self.btn_inverser)
    
    def set_default_values(self):
        #ComboBox
        self.cbb_devisesFrom.addItems(sorted(list(self.c.currencies)))
        self.cbb_devisesTo.addItems(sorted(list(self.c.currencies)))
        self.cbb_devisesFrom.setCurrentText("EUR")
        self.cbb_devisesTo.setCurrentText("EUR")
       
        #SpinBox
        self.spn_montant.setRange(1, 1000000)
        self.spn_montantConverti.setRange(1, 1000000)
        self.spn_montant.setValue(100)
        self.spn_montantConverti.setValue(100)
       
    
    

# création d'une application. Toujours passer une liste vide, si non on a une erreur*
app = QtWidgets.QApplication([])

# Création de la fenêtre || Instancier l'app
win = App()

# Affichage de la fenêtre
win.show()

# Exécution de l'application
app.exec_()
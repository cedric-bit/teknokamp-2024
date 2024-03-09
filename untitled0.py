import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class PieChartApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Graphiques en camembert interactifs")
        self.setGeometry(100, 100, 1200, 400)  # Ajustez la taille pour mieux voir les camemberts

        widget = QWidget(self)
        self.setCentralWidget(widget)
        layout = QVBoxLayout(widget)

        canvas = FigureCanvas(Figure(figsize=(12, 4)))
        layout.addWidget(canvas)

        self.figure = canvas.figure
        self.ax1 = self.figure.add_subplot(131)  # Premier camembert à gauche
        self.ax2 = self.figure.add_subplot(132)  # Deuxième camembert au milieu
        self.ax3 = self.figure.add_subplot(133)  # Troisième camembert à droite

        # Ajout des nouvelles catégories et leurs prix initiaux
        self.sizes1 = [25, 25, 20, 15, 15]
        self.sizes2 = [40, 60, 50, 30, 20]
        self.sizes3 = [40, 60]
        
        self.labels1 = ['Soleil', 'éoliennes', 'thermique', 'nucléaire', 'hydrogène']
        self.labels2 = ['PRIX SOL', 'PRIX EOL', 'PRIX THER', 'PRIX NUC', 'PRIX HYD']
        self.labels3 = ['HYDR VERT', 'THERMAL']
        self.colors3 = ['green', 'black']

        self.pie1 = None
        self.pie2 = None
        self.pie3 = None
        self.update_pie_charts()

        canvas.mpl_connect('button_press_event', self.on_click)

    def update_pie_charts(self):
        self.ax1.clear()
        self.ax2.clear()
        self.ax3.clear()

        wedges1, texts1, autotexts1 = self.ax1.pie(self.sizes1, labels=self.labels1, autopct='%1.1f%%', startangle=90)
        self.pie1 = wedges1

        wedges2, texts2, autotexts2 = self.ax2.pie(self.sizes2, labels=self.labels2, autopct='%1.1f%%', startangle=90)
        self.pie2 = wedges2
        
        wedges3, texts3, autotexts3 = self.ax3.pie(self.sizes3, labels=self.labels3, autopct='%1.1f%%', colors=self.colors3)
        self.pie3 = wedges3

        self.ax1.axis('equal')
        self.ax2.axis('equal')
        self.ax3.axis('equal')

        self.figure.canvas.draw_idle()

 
    def on_click(self, event):
        for i, pie_slice in enumerate(self.pie1):
            if pie_slice.contains_point((event.x, event.y)):
                self.sizes1[i] += 1  # Augmenter la consommation

                # Augmenter le prix de manière différente selon la source d'énergie
                if i == 0:  # Soleil
                    self.sizes2[0] += 2
                elif i == 1:  # éoliennes
                    self.sizes2[1] += 1.5
                elif i == 2:  # thermique
                    self.sizes2[2] += 1.2
                elif i == 3:  # nucléaire
                    self.sizes2[3] += 1.1
                elif i == 4:  # hydrogène
                    self.sizes2[4] += 1

                self.update_pie_charts()
                return
            
            
            for i, pie_slice in enumerate(self.pie2):
                if pie_slice.contains_point((event.x, event.y)):
                    self.sizes1[i] += 1  # Augmenter la consommation

                    
                    if i == 0:  # Soleil
                        self.sizes2[0] += 2
                    elif i == 1:  # éoliennes
                        self.sizes2[1] += 1.5
                    elif i == 2:  # thermique
                        self.sizes2[2] += 1.2
                    elif i == 3:  # nucléaire
                        self.sizes2[3] += 1.1
                    elif i == 4:  # hydrogène
                        self.sizes2[4] += 1

                    self.update_pie_charts()
                    return         

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainApp = PieChartApp()
    mainApp.show()
    sys.exit(app.exec_())

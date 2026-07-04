# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)        


    #Block of functions to determine player stats without
    #needing manual calculation, for convenience
    def determine_intrigue_defense(self):
        #Awareness + Cunning + Status
        awareness_value = int(self.ui.awareness_rating_text.toPlainText());
        cunning_value = int(self.ui.cunning_rating_text.toPlainText());
        status_value = int(self.ui.status_rating_text.toPlainText());
        intrigue_defense = awareness_value + cunning_value + status_value;
        self.ui.intrigue_defense_value_text.setText(str(intrigue_defense));

    def determine_maximum_health(self):
        #Endurance * 3
        endurance_value = int(self.ui.endurance_rating_text.toPlainText());
        max_health_value = endurance_value * 3;
        self.ui.max_health_value_text.setText(str(max_health_value));

    def determine_combat_defense(self):
        #Agility + Athletics + Awareness + Defense Bonus - Armor Penalty
        agility_value = int(self.ui.agility_rating_text.toPlainText());
        athletics_value = int(self.ui.athletics_rating_text.toPlainText());
        awareness_value = int(self.ui.awareness_rating_text.toPlainText());
        defense_value = int(self.ui.armor_rating_final_value.toPlainText());
        armor_penalty_value = int(self.ui.armor_penalty_final_value.toPlainText());

        combat_defense = agility_value + athletics_value + awareness_value + defense_value - armor_penalty_value;
        self.ui.combat_defense_value_text.setText(str(combat_defense));

    def determine_composure(self):
        #Will * 3
        will_value = int(self.ui.will_rating_text.toPlainText());
        composure_value = will_value * 3;
        self.ui.composure_value_text.setText(str(composure_value));




if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
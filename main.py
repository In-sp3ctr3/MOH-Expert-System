# BY: Jadan Jones, Shahine Porter, Rolando Alberts

# IMPORT / GUI AND MODULES AND WIDGETS

import sys
import os
import platform
import fileinput
from modules import *
from widgets import *
from PySide6 import *
os.environ["QT_FONT_DPI"] = "96"
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QProgressBar, QSizePolicy, QVBoxLayout, QWidget)
from ui_splash_screen import Ui_SplashScreen
from ui_main import Ui_MainWindow
from pyswip import Prolog
prolog = Prolog()
prolog.consult("prolog.pl")

#Global
widgets = None
counter = 0
list_of_sym = []
list_of_con = []

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        #Instanciate Window
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        #Hide all extra widgets and popups
        widgets.hypertension.hide()
        widgets.clear_button.hide()
        widgets.error_message.hide()
        widgets.clear_conditions_button.hide()
        widgets.error_message_2.hide()
        widgets.success_message.hide()
        widgets.widget_4.hide()
        widgets.popout_box.hide()

        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # APP NAME
        title = "COVIDEX"
        description = "COVIDEX"

        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        # TOGGLE MENU
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        UIFunctions.uiDefinitions(self)

        # BUTTONS CLICK SECTION

        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_widgets.clicked.connect(self.buttonClick)
        widgets.btn_new.clicked.connect(self.buttonClick)
        widgets.symptom_dropdown.activated.connect(self.buttonClick)
        widgets.diagnosis_submit.clicked.connect(self.buttonClick)
        widgets.clear_button.clicked.connect(self.buttonClick)
        widgets.no_Bp.clicked.connect(self.buttonClick)
        widgets.clear_conditions_button.clicked.connect(self.buttonClick)
        widgets.conditions_dropdown.activated.connect(self.buttonClick)
        widgets.add_button_covid.clicked.connect(self.buttonClick)
        widgets.add_button_delta.clicked.connect(self.buttonClick)
        widgets.add_button_omicron.clicked.connect(self.buttonClick)
        widgets.add_button_conditions.clicked.connect(self.buttonClick)
        widgets.dialog_button.clicked.connect(self.buttonClick)

        
        self.progressBarValue()
        self.setHomePageStats()
        self.setSymptoms()

        # EXTRA RIGHT BOX
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        # SHOW APP
        self.show()

        # SET HOME PAGE AND SELECT MENU
        widgets.stackedWidget.setCurrentWidget(widgets.home)
        p = list(prolog.query("cases(X,Y)"))
        check_surge = p[0]['Y']/p[0]['X']
        if check_surge > 0.40:
            widgets.popout_box.show()

        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))

        #Progress Bar for Pie Charts
    def progressBarValue(self):

        x = list(prolog.query("cases(X,Y)"))
        progress = 1-(x[0]['Y']/x[0]['X'])
        stop1 = str(progress - 0.001)
        stop2 = str(progress)
        styleSheet = """QFrame{
                                background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{stop1} rgba(129, 61, 156, 0), stop:{stop2} rgba(53, 132, 228, 255));
                                } """
        newStylesheet = styleSheet.replace("{stop1}", stop1).replace("{stop2}", stop2)
        self.ui.frame_14.setStyleSheet(newStylesheet)
        widgets.label_31.setText(f'{round((1-progress)*100)}%')

        x = list(prolog.query("tot_omicron(X)"))
        y = list(prolog.query("omicron_underlying(X)"))
        progress = 1-(y[0]['X']/x[0]['X'])
        stop1 = str(progress - 0.001)
        stop2 = str(progress)
        styleSheet = """QFrame{
                                background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{stop1} rgba(129, 61, 156, 0), stop:{stop2} rgb(129, 61, 156));
                                } """
        newStylesheet = styleSheet.replace("{stop1}", stop1).replace("{stop2}", stop2)
        self.ui.frame_17.setStyleSheet(newStylesheet)
        widgets.label_33.setText(f'{round((1-progress)*100)}%')

    def setHomePageStats(self):
        y = list(prolog.query("cases(Y,_)"))

        widgets.total_diagnosed.setText(f"<html><head/><body><p>{y[0]['Y']}</p></body></html>")
        x = list(prolog.query("tot_covid(X)"))
        widgets.label_52.setText(f"<html><head/><body><p>{round((x[0]['X']/y[0]['Y'])*100)}%</p></body></html>")
        x = list(prolog.query("tot_delta(X)"))
        widgets.label_53.setText(f"<html><head/><body><p>{round((x[0]['X']/y[0]['Y'])*100)}%</p></body></html>")
        x = list(prolog.query("tot_omicron(X)"))
        widgets.label_54.setText(f"<html><head/><body><p>{round((x[0]['X']/y[0]['Y'])*100)}%</p></body></html>")

        x = list(prolog.query("mild(X)"))
        widgets.progressBar_mild.setValue(round((x[0]['X']/y[0]['Y'])*100))
        widgets.percentage_mild.setText(f"<html><head/><body><p>{round((x[0]['X']/y[0]['Y'])*100)}%</p></body></html>")

        x = list(prolog.query("severe(X)"))
        widgets.progressBar_severe.setValue(round((x[0]['X']/y[0]['Y'])*100))
        widgets.percentage_severe.setText(f"<html><head/><body><p>{round((x[0]['X']/y[0]['Y'])*100)}%</p></body></html>")

        x = list(prolog.query("male_positives(X)"))
        widgets.progressBar_male_positives.setValue(round((x[0]['X']/y[0]['Y'])*100))
        widgets.percentage_male_positives.setText(f"<html><head/><body><p>{round((x[0]['X']/y[0]['Y'])*100)}%</p></body></html>")

        x = list(prolog.query("female_positives(X)"))
        widgets.progressBar_female_positives.setValue(round((x[0]['X']/y[0]['Y'])*100))
        widgets.percentage_female_positives.setText(f"<html><head/><body><p>{round((x[0]['X']/y[0]['Y'])*100)}%</p></body></html>")

        x = list(prolog.query("blood_pressure(X)"))
        widgets.progressBar_blood_pressure.setValue(round((x[0]['X']/y[0]['Y'])*100))
        widgets.percentage_blood_pressure.setText(f"<html><head/><body><p>{round((x[0]['X']/y[0]['Y'])*100)}%</p></body></html>")
        
    def setSymptoms(self):

        symptoms = list(prolog.query("covid_symptoms(X)"))
        symptoms.extend((list(prolog.query("delta_symptoms(X)"))))
        symptoms.extend((list(prolog.query("omicron_symptoms(X)"))))
        widgets.symptom_dropdown.clear()

        for s in range(len(symptoms)):
            for k in symptoms[s]['X']:
                widgets.symptom_dropdown.addItem(k)

        con = list(prolog.query("underlying_conditions(X)"))
        widgets.conditions_dropdown.clear()

        for l in con[0]['X']:
            widgets.conditions_dropdown.addItem(l)

    def checkEmpty(self):
        fields =  [widgets.form_age,widgets.form_height_inches,widgets.form_height_feet,widgets.form_temperature,widgets.form_weight]
        
        if widgets.form_name.text() == '':
            widgets.error_message.show()
            QtCore.QTimer.singleShot(1800, lambda: widgets.error_message.hide())
            return True

        if not widgets.hypertension.isHidden():
            fields.extend((widgets.form_systolic,widgets.form_diastolic))

        for t in fields:
            if t.value() == 0:
                widgets.error_message.show()
                QtCore.QTimer.singleShot(1800, lambda: widgets.error_message.hide())
                return True

    def resetFields(self):
        form =  [widgets.form_diastolic,widgets.form_systolic,widgets.form_height_inches,widgets.form_height_feet,widgets.form_temperature,widgets.form_weight]
        widgets.form_name.clear()
        widgets.symptom_display.clear()
        widgets.conditions_display.clear()
        widgets.clear_conditions_button.hide()
        widgets.clear_button.hide()
        widgets.form_age.setValue(1)
        list_of_sym.clear()
        list_of_con.clear()

        for f in form:
            f.setValue(0)

        

    # BUTTONS CLICK
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        diagnosis = "You Do Not Have COVID-19"
        suggestion = "Symptoms usually manifest between 4 - 12 days. If you have been exposed symptoms may take a while to show"

        # SHOW HOME PAGE
        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
            self.progressBarValue()
            self.setHomePageStats()
            b = list(prolog.query("cases(X,Y)"))
            check_surge = b[0]['Y']/b[0]['X']
            if check_surge > 0.40:
                widgets.popout_box.show()
            

        # SHOW DIAGNOSIS PAGE
        if btnName == "btn_widgets":
            widgets.stackedWidget.setCurrentWidget(widgets.widgets)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
            self.resetFields()

        # SHOW ADD FACTS PAGE
        if btnName == "btn_new":
            widgets.stackedWidget.setCurrentWidget(widgets.new_page) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU

        if btnName == "clear_button":
            widgets.symptom_display.setText('')
            list_of_sym.clear()
            widgets.widget_4.hide()
            

        if btnName == "clear_conditions_button":
            widgets.conditions_display.setText('')
            list_of_con.clear()

        if btnName == "dialog_button":
            widgets.popout_box.hide()
            

        if btnName == "no_Bp":
            widgets.hypertension.hide()
        
        # SET EACH SYMPTOM FROM DROPDOWN LIST
        if btnName == "symptom_dropdown":
            print("SSomething BTN clicked!")

            selected = widgets.symptom_dropdown.currentText()

            if selected not in list_of_sym:
                list_of_sym.append(selected)
                widgets.widget_4.show()

            if not list_of_sym:
                widgets.clear_button.hide()
            else:
                widgets.clear_button.show()

            items = ' '.join(repr(x) for x in list_of_sym)
            widgets.symptom_display.setText(f'{items}')
            widgets.symptom_display.setWordWrap(True)

            z = list(prolog.query("blood_pressure_check_required(X)"))
            check_required = []
            for g in z[0]['X']:
                check_required.append(g)

            if (widgets.symptom_dropdown.currentText() in check_required):
                widgets.hypertension.show()

        # SET EACH SYMPTOM FROM DROPDOWN LIST
        if btnName == "conditions_dropdown":
            selected_condition = widgets.conditions_dropdown.currentText()

            if selected_condition not in list_of_con:
                list_of_con.append(selected_condition)

            if not list_of_con:
                widgets.clear_conditions_button.hide()
            else:
                widgets.clear_conditions_button.show()

            condit = ' '.join(repr(x) for x in list_of_con)
            widgets.conditions_display.setText(f'{condit}')
            widgets.conditions_display.setWordWrap(True)

            u = list(prolog.query("blood_pressure_check_required(X)"))
            check_required = []
            for r in u[0]['X']:
                check_required.append(r)

            if widgets.conditions_dropdown.currentText() in check_required:
                widgets.hypertension.show()

        if btnName == "add_button_covid":
            if not widgets.add_covid.text().strip():
                widgets.error_message_2.show()
                QtCore.QTimer.singleShot(1800, lambda: widgets.error_message_2.hide())
                return

            list(prolog.query(f"update_covid_symptoms('{widgets.add_covid.text().strip()}')"))

            x = list(prolog.query("covid_symptoms(X)"))
            q = x[0]['X']
            q.append(widgets.add_covid.text().strip())
            changed = False
            with fileinput.input("prolog.pl", inplace=True) as file:
                    for line in file:
                        if "covid_symptoms(" in line and not changed:
                            new_line = line.replace(line, f"covid_symptoms({q}).")
                            print(new_line, end='\n')
                            changed = True
                        else:
                            print(line, end='')

            if(widgets.bp_check_covid.isChecked()):
                list(prolog.query(f"update_bp_required('{widgets.add_covid.text().strip()}')"))
            self.setSymptoms()

            x = list(prolog.query("blood_pressure_check_required(X)"))
            q = x[0]['X']
            q.append(widgets.add_covid.text().strip())
            changed = False
            with fileinput.input("prolog.pl", inplace=True) as file:
                    for line in file:
                        if "blood_pressure_check_required(" in line and not changed:
                            new_line = line.replace(line, f"blood_pressure_check_required({q}).")
                            print(new_line, end='\n')
                            changed = True
                        else:
                            print(line, end='')

            widgets.add_covid.clear()
            widgets.success_message.show()
            QtCore.QTimer.singleShot(1800, lambda: widgets.success_message.hide())

        if btnName == "add_button_delta":
            if not widgets.add_delta.text().strip():
                widgets.error_message_2.show()
                QtCore.QTimer.singleShot(1800, lambda: widgets.error_message_2.hide())
                return

            list(prolog.query(f"update_delta_symptoms('{widgets.add_delta.text().strip()}')"))
            
            x = list(prolog.query("delta_symptoms(X)"))
            q = x[0]['X']
            q.append(widgets.add_delta.text().strip())
            changed = False
            with fileinput.input("prolog.pl", inplace=True) as file:
                    for line in file:
                        if "delta_symptoms(" in line and not changed:
                            new_line = line.replace(line, f"delta_symptoms({q}).")
                            print(new_line, end='\n')
                            changed = True
                        else:
                            print(line, end='')

            if(widgets.bp_check_delta.isChecked()):
                list(prolog.query(f"update_bp_required('{widgets.add_delta.text().strip()}')"))
            self.setSymptoms()

            x = list(prolog.query("blood_pressure_check_required(X)"))
            q = x[0]['X']
            q.append(widgets.add_delta.text().strip())
            changed = False
            with fileinput.input("prolog.pl", inplace=True) as file:
                    for line in file:
                        if "blood_pressure_check_required(" in line and not changed:
                            new_line = line.replace(line, f"blood_pressure_check_required({q}).")
                            print(new_line, end='\n')
                            changed = True
                        else:
                            print(line, end='')

            widgets.add_delta.clear()
            widgets.success_message.show()
            QtCore.QTimer.singleShot(1800, lambda: widgets.success_message.hide())

        if btnName == "add_button_omicron":
            if not widgets.add_omicron.text().strip():
                widgets.error_message_2.show()
                QtCore.QTimer.singleShot(1800, lambda: widgets.error_message_2.hide())
                return

            list(prolog.query(f"update_omicron_symptoms('{widgets.add_omicron.text().strip()}')"))
            x = list(prolog.query("omicron_symptoms(X)"))
            q = x[0]['X']
            q.append(widgets.add_omicron.text().strip())
            changed = False
            with fileinput.input("prolog.pl", inplace=True) as file:
                    for line in file:
                        if "omicron_symptoms(" in line and not changed:
                            new_line = line.replace(line, f"omicron_symptoms({q}).")
                            print(new_line, end='\n')
                            changed = True
                        else:
                            print(line, end='')
            if(widgets.bp_check_omicron.isChecked()):
                list(prolog.query(f"update_bp_required('{widgets.add_omicron.text().strip()}')"))
            self.setSymptoms()

            x = list(prolog.query("blood_pressure_check_required(X)"))
            q = x[0]['X']
            q.append(widgets.add_omicron.text().strip())
            changed = False
            with fileinput.input("prolog.pl", inplace=True) as file:
                    for line in file:
                        if "blood_pressure_check_required(" in line and not changed:
                            new_line = line.replace(line, f"blood_pressure_check_required({q}).")
                            print(new_line, end='\n')
                            changed = True
                        else:
                            print(line, end='')

            widgets.add_omicron.clear()
            widgets.success_message.show()
            QtCore.QTimer.singleShot(1800, lambda: widgets.success_message.hide())

        if btnName == "add_button_conditions":
            if not widgets.add_conditions.text().strip():
                widgets.error_message_2.show()
                QtCore.QTimer.singleShot(1800, lambda: widgets.error_message_2.hide())
                return

            list(prolog.query(f"update_conditions('{widgets.add_conditions.text().strip()}')"))

            x = list(prolog.query("underlying_conditions(X)"))
            q = x[0]['X']
            q.append(widgets.add_conditions.text().strip())
            changed = False
            with fileinput.input("prolog.pl", inplace=True) as file:
                    for line in file:
                        if "underlying_conditions(" in line and not changed:
                            new_line = line.replace(line, f"underlying_conditions({q}).")
                            print(new_line, end='\n')
                            changed = True
                        else:
                            print(line, end='')

            if(widgets.bp_check_conditions.isChecked()):
                list(prolog.query(f"update_bp_required('{widgets.add_conditions.text().strip()}')"))
            self.setSymptoms()

            x = list(prolog.query("blood_pressure_check_required(X)"))
            q = x[0]['X']
            q.append(widgets.add_conditions.text().strip())
            changed = False
            with fileinput.input("prolog.pl", inplace=True) as file:
                    for line in file:
                        if "blood_pressure_check_required(" in line and not changed:
                            new_line = line.replace(line, f"blood_pressure_check_required({q}).")
                            print(new_line, end='\n')
                            changed = True
                        else:
                            print(line, end='')

            widgets.add_conditions.clear()
            widgets.success_message.show()
            QtCore.QTimer.singleShot(1800, lambda: widgets.success_message.hide())

        #SUBMIT BUTTON FOR DIAGNOSIS FORM
        if btnName == "diagnosis_submit":

            risk = 0

            if(self.checkEmpty()):
                return
            #convert temperature
            temperature = (( int(widgets.form_temperature.value()) *  9/5) + 32)
            if temperature > 100.4:
                risk+=1
                print('temp high')
            #convert height to metres
            height = (int(widgets.form_height_inches.value())* 0.0254)+(int(widgets.form_height_feet.value())* 0.305 )
            #convert weight
            body_max_index = (int(widgets.form_weight.value())/height*height)
            if body_max_index >= 40:
                risk +=1
                print('too fat')
            #high or low blood pressure
            if not widgets.hypertension.isHidden():
                if widgets.form_systolic.value() < 90 or widgets.form_diastolic.value < 60:
                    risk += 1
                    b = list(prolog.query("blood_pressure(X)"))
                    bp = b[0]['X']
                    prolog.retractall("blood_pressure(_)")
                    prolog.asserta(f"blood_pressure({bp+1})")
                    changed = False
                    with fileinput.input("prolog.pl", inplace=True) as file:
                        for line in file:
                            if "blood_pressure(" in line and not changed:
                                new_line = line.replace(line, f"blood_pressure({bp+1}).")
                                print(new_line, end='\n')
                                changed = True
                            else:
                                print(line, end='')


            #age check
            if widgets.form_age.value() > 65:
                risk +=1
                print('too old')

            if len(list_of_sym) > 2:
                risk += 1

            if not widgets.widget_4.isHidden():
                if widgets.mild_symptoms.isChecked():
                    m = list(prolog.query("mild(X)"))
                    mld = m[0]['X']
                    prolog.retractall("mild(_)")
                    prolog.asserta(f"mild({mld+1})")
                    changed = False
                    with fileinput.input("prolog.pl", inplace=True) as file:
                        for line in file:
                            if "mild(" in line and not changed:
                                new_line = line.replace(line, f"mild({mld+1}).")
                                print(new_line, end='\n')
                                changed = True
                            else:
                                print(line, end='')
                elif widgets.severe_symptoms.isChecked():
                    s = list(prolog.query("severe(X)"))
                    svr = s[0]['X']
                    prolog.retractall("severe(_)")
                    prolog.asserta(f"severe({svr+1})")
                    changed = False
                    with fileinput.input("prolog.pl", inplace=True) as file:
                        for line in file:
                            if "severe(" in line and not changed:
                                new_line = line.replace(line, f"severe({svr+1}).")
                                print(new_line, end='\n')
                                changed = True
                            else:
                                print(line, end='')
                

            c = list(prolog.query("covid_symptoms(X)"))
            covid = []
            for i in c[0]['X']:
                covid.append(i)

            d = list(prolog.query("delta_symptoms(X)"))
            delta = []
            for i in d[0]['X']:
                delta.append(i)

            o = list(prolog.query("omicron_symptoms(X)"))
            omicron = []
            for i in o[0]['X']:
                omicron.append(i)

            covid.sort()
            delta.sort()
            omicron.sort()
            list_of_sym.sort()


            x = list(prolog.query("cases(X,Y)"))
            diagnosed = x[0]['X']
            positive = x[0]['Y']

            x = list(prolog.query("tot_covid(X)"))
            tot_covid = x[0]['X']

            x = list(prolog.query("tot_delta(X)"))
            tot_delta = x[0]['X']

            x = list(prolog.query("tot_omicron(X)"))
            tot_omicron = x[0]['X']

            x = list(prolog.query("omicron_underlying(X)"))
            omicron_underlying = x[0]['X']

            print(omicron)
            print(list_of_sym)


            flag = False
            if(all(a in list_of_sym for a in omicron)):
                positive += 1
                diagnosis = "This patient may have COVID-19. Variant: Omicron"
                prolog.retractall("tot_omicron(_)")
                prolog.asserta(f"tot_omicron({tot_omicron+1})")
                changed = False
                with fileinput.input("prolog.pl", inplace=True) as file:
                    for line in file:
                        if "tot_delta(" in line and not changed:
                            new_line = line.replace(line, f"tot_omicron({tot_omicron+1}).")
                            print(new_line, end='\n')
                            changed = True
                        else:
                            print(line, end='')
                if not list_of_con:
                    prolog.retractall("omicron_underlying(_)")
                    prolog.asserta(f"omicron_underlying({omicron_underlying+1})")
                    changed = False
                    with fileinput.input("prolog.pl", inplace=True) as file:
                        for line in file:
                            if "tot_delta(" in line and not changed:
                                new_line = line.replace(line, f"omicron_underlying({omicron_underlying+1}).")
                                print(new_line, end='\n')
                                changed = True
                            else:
                                print(line, end='')
                    flag = True

            if(all(b in list_of_sym for b in delta)):
                if not flag:
                    positive += 1
                    diagnosis = "This patient may have COVID-19. Variant: Delta"
                    prolog.retractall("tot_delta(_)")
                    prolog.asserta(f"tot_delta({tot_delta+1})")
                    changed = False
                    with fileinput.input("prolog.pl", inplace=True) as file:
                        for line in file:
                            if "tot_delta(" in line and not changed:
                                new_line = line.replace(line, f"tot_delta({tot_delta+1}).")
                                print(new_line, end='\n')
                                changed = True
                            else:
                                print(line, end='')
                    flag = True

            if(all(c in list_of_sym for c in covid) or risk >= 3):
                if not flag:
                    positive += 1
                    diagnosis = "This patient may have COVID-19"
                    prolog.retractall("tot_covid(_)")
                    prolog.asserta(f"tot_covid({tot_covid+1})")
                    changed = False
                    with fileinput.input("prolog.pl", inplace=True) as file:
                        for line in file:
                            if "tot_covid(" in line:
                                new_line = line.replace(line, f"tot_covid({tot_covid+1}).")
                                print(new_line, end='\n')
                                changed = True
                            else:
                                print(line, end='')
                    flag = True

            if widgets.male_radio.isChecked() and flag:
                m = list(prolog.query("male_positives(X)"))
                mle = m[0]['X']
                prolog.retractall("male_positives(_)")
                prolog.asserta(f"male_positives({mle+1})")
                changed = False
                with fileinput.input("prolog.pl", inplace=True) as file:
                    for line in file:
                        if "male_positives(" in line and not changed:
                            new_line = line.replace(line, f"male_positives({mle+1}).")
                            print(new_line, end='\n')
                            changed = True
                        else:
                            print(line, end='')
            elif widgets.female_radio.isChecked() and flag:
                f = list(prolog.query("female_positives(X)"))
                fmle = f[0]['X']
                prolog.retractall("female_positives(_)")
                prolog.asserta(f"female_positives({fmle+1})")
                changed = False
                with fileinput.input("prolog.pl", inplace=True) as file:
                    for line in file:
                        if "female_positives(" in line and not changed:
                            new_line = line.replace(line, f"female_positives({fmle+1}).")
                            print(new_line, end='\n')
                            changed = True
                        else:
                            print(line, end='')


                
            diagnosed += 1

            prolog.retractall("cases(_,_)")
            prolog.assertz(f"cases({diagnosed},{positive})")
            changed = False
            with fileinput.input("prolog.pl", inplace=True) as file:
                for line in file:
                    if "cases(" in line and not changed:
                        new_line = line.replace(line, f"cases({diagnosed},{positive}).")
                        print(new_line, end='\n')
                        changed = True
                    else:
                        print(line, end='')
                    
                    
            print(list(prolog.query("cases(X,Y)")))

            widgets.stackedWidget.setCurrentWidget(widgets.page)
            widgets.diagnosis_main.setText(f'<html><head/><body><p align="center"><span style="font-size:26pt;"> {diagnosis} </span></p></body></html>')
            widgets.diagnosis_main.setWordWrap(True)
            widgets.diagnosis_suggestion.setText(f'<html><head/><body><p><span style=" font-size:12pt;">{suggestion}</span></p></body></html>')
            widgets.diagnosis_suggestion.setWordWrap(True)

        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')


    # RESIZE EVENTS
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

# SPLASH SCREEN
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        # UI

        # REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)


        # DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        # QTIMER START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(30)

        # CHANGE DESCRIPTION SSECTION 

        # Initial Text
        self.ui.label_description.setText("<strong>SETTING</strong> UP THINGS")

        # Change Texts
        QtCore.QTimer.singleShot(1500, lambda: self.ui.label_description.setText("<strong>LOADING</strong> DATABASE"))
        QtCore.QTimer.singleShot(3000, lambda: self.ui.label_description.setText("<strong>LOADING</strong> USER INTERFACE"))


        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

    ## ==> APP FUNCTIONS
    ########################################################################
    def progress(self):

        global counter

        # SET VALUE TO PROGRESS BAR
        self.ui.progressBar.setValue(counter)

        # CLOSE SPLASH SCREEN AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW
            self.main = MainWindow()
            self.main.show()

            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        counter += 1



if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = SplashScreen()
    sys.exit(app.exec())

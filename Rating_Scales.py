#!/usr/bin/env python3
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QWidget,
    QPushButton,
    QGridLayout,
    QMessageBox,
    QComboBox,
    QLineEdit,
)
from PyQt6.QtGui import QIcon
import os
import json

### Variables ###
source_type = ""  # Used for the source rating system (Mine, School, Linear)
source_selection = ""  # Used to store to type of selection
source_rating = ""  # Used to store the current rating
# Directories
directory_path = os.path.dirname(os.path.realpath(__file__))
path_to_mine = directory_path + "/Data/Mine_Scale.json"
path_to_school = directory_path + "/Data/School_Scale.json"
path_to_linear = directory_path + "/Data/Linear_Scale.json"
path_to_icon = directory_path + "/Data/icon.ico"
# Data
loaded_data = {}
### Application ####
# Test value
def Get_Information():
    global source_type
    global source_selection
    global source_rating
    Current_System = ""
    Current_Selection = ""
    Current_Rating = ""
    Current_System = System_Box.currentText()
    Current_Selection = Selection_Box.currentText()
    Current_Rating = Rating_Box.currentText()
    # Checking the numbers
    if Current_System != "" and Current_Selection != "" and Current_Rating != "":
        source_type = Current_System
        source_selection = Current_Selection
        source_rating = Current_Rating
        Load_Json()
        Get_Rating()
    else:
        Show_Error("Not all inputs are selected")


# Loading JSON
def Load_Json():
    global loaded_data
    use_path = ""
    if source_type == "Mine":
        use_path = path_to_mine
    elif source_type == "School":
        use_path = path_to_school
    elif source_type == "Linear":
        use_path = path_to_linear
    else:
        use_path = "Error"
    if use_path != "Error":
        with open(use_path) as temp_file:
            loaded_data = json.load(temp_file)
    else:
        Show_Error("Error loading data")


# Get Ratings
def Get_Rating():
    # Fixed Variables
    output = {"Rating": "", "100": "", "10": "", "5": ""}
    output["Rating"] = source_rating
    output["100"] = loaded_data[source_rating][source_selection]
    # Calculations
    if source_selection != "Range":
        temp_100 = float(output["100"])
        temp_10 = temp_100 / 10
        temp_5 = temp_100 / 20
    else:  # Converting to range info
        temp_100 = output["100"]
        temp_100_split = temp_100.split("-")
        temp_100_min = float(temp_100_split[0])
        temp_100_max = float(temp_100_split[1])
        temp_10 = str(temp_100_min / 10) + "-" + str(temp_100_max / 10)
        temp_5 = str(temp_100_min / 20) + "-" + str(temp_100_max / 20)
    # Getting the output {Dictionary}
    output["10"] = str(temp_10)
    output["5"] = str(temp_5)
    # Output
    Output_Rating.setText(output["Rating"])
    Output_100.setText(output["100"])
    Output_10.setText(output["10"])
    Output_5.setText(output["5"])


# Shows an error message
def Show_Error(warning):
    dialog = QMessageBox(text=warning, parent=window)
    dialog.setWindowTitle("Issue")
    dialog.setIcon(QMessageBox.Icon.Warning)
    dialog.exec()


### GUI ###
# Basic window
app = QApplication([])
window = QWidget()
window.setWindowTitle("Rating Scales")
window.setWindowIcon(QIcon(path_to_icon))
# Making objects
Input_Label = QLabel("<h1>Inputs</h1>", parent=window)  # Static
System_Label = QLabel("System: ", parent=window)  # Static
System_Box = QComboBox(parent=window)  # User
System_Box.setPlaceholderText("System")
System_Box.addItems(["Mine", "School", "Linear"])
Rating_Label = QLabel("Rating: ", parent=window)  # Static
Rating_Box = QComboBox(parent=window)  # User
Rating_Box.setPlaceholderText("Scale")
Rating_Box.addItems(["Trash", "Bad", "Meh", "Ok", "Good", "Great", "God"])
Selection_Label = QLabel("Selection: ", parent=window)  # Static
Selection_Box = QComboBox(parent=window)  # User
Selection_Box.setPlaceholderText("Scale")
Selection_Box.addItems(["Minimum", "Average", "Maximum", "Range", "Length"])
Output_Label = QLabel("<h1>Outputs</h1>", parent=window)  # Static
Output_Rating_Label = QLabel("Rating: ", parent=window)  # Static
Output_100_Label = QLabel("100 Point: ", parent=window)  # Static
Output_10_Label = QLabel("10 Point: ", parent=window)  # Static
Output_5_Label = QLabel("5 Point: ", parent=window)  # Static
Output_Rating = QLineEdit(parent=window)  # Dynamic
Output_Rating.setReadOnly(True)
Output_100 = QLineEdit(parent=window)  # Dynamic
Output_100.setReadOnly(True)
Output_10 = QLineEdit(parent=window)  # Dynamic
Output_10.setReadOnly(True)
Output_5 = QLineEdit(parent=window)  # Dynamic
Output_5.setReadOnly(True)
Information_Button = QPushButton("Information", parent=window)
# Making Layout
layout = QGridLayout()
layout.addWidget(Input_Label, 0, 0, alignment=Qt.AlignmentFlag.AlignCenter)
layout.addWidget(System_Label, 1, 0, alignment=Qt.AlignmentFlag.AlignCenter)
layout.addWidget(System_Box, 1, 1, alignment=Qt.AlignmentFlag.AlignCenter)
layout.addWidget(Rating_Label, 2, 0, alignment=Qt.AlignmentFlag.AlignCenter)
layout.addWidget(Rating_Box, 2, 1, alignment=Qt.AlignmentFlag.AlignCenter)
layout.addWidget(Selection_Label, 3, 0, alignment=Qt.AlignmentFlag.AlignCenter)
layout.addWidget(Selection_Box, 3, 1, alignment=Qt.AlignmentFlag.AlignCenter)
layout.addWidget(Output_Label, 4, 0, alignment=Qt.AlignmentFlag.AlignCenter)
layout.addWidget(Output_Rating_Label, 5, 0, alignment=Qt.AlignmentFlag.AlignCenter)
layout.addWidget(Output_Rating, 5, 1, alignment=Qt.AlignmentFlag.AlignCenter)
layout.addWidget(Output_100_Label, 6, 0, alignment=Qt.AlignmentFlag.AlignCenter)
layout.addWidget(Output_100, 6, 1, alignment=Qt.AlignmentFlag.AlignCenter)
layout.addWidget(Output_10_Label, 7, 0, alignment=Qt.AlignmentFlag.AlignCenter)
layout.addWidget(Output_10, 7, 1, alignment=Qt.AlignmentFlag.AlignCenter)
layout.addWidget(Output_5_Label, 8, 0, alignment=Qt.AlignmentFlag.AlignCenter)
layout.addWidget(Output_5, 8, 1, alignment=Qt.AlignmentFlag.AlignCenter)
layout.addWidget(Information_Button, 9, 0, alignment=Qt.AlignmentFlag.AlignCenter)
# Testing Values
Information_Button.pressed.connect(Get_Information)
### Showing the application and window ###
window.setLayout(layout)
window.setMinimumSize(window.minimumSizeHint())
window.setMaximumSize(window.sizeHint())
window.show()
sys.exit(app.exec())

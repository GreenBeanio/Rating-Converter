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
from PyQt6.QtGui import QIcon, QDoubleValidator
import os
import json

### Variables ###
source_type = ""  # Used for the source rating system (Mine, School, Linear)
source_scale = ""  # Used for the source rating scale (100 point, 10 point, 5 points)
source_rating = ""  # Used to store the current rating
output_scale = ""  # Used to set which scale to output at
# Directories
directory_path = os.path.dirname(os.path.realpath(__file__))
path_to_mine = directory_path + "/Data/Mine.json"
path_to_school = directory_path + "/Data/School.json"
path_to_linear = directory_path + "/Data/Linear.json"
path_to_icon = directory_path + "/Data/icon.ico"
# Data
loaded_data = {}
### Application ####
# Test value
def Get_Values():
    global source_type
    global source_scale
    global source_rating
    global output_scale
    global rating_mask
    Current_System = ""
    Current_Scale = ""
    Current_Rating = ""
    Current_System = Select_System_Box.currentText()
    Current_Scale = Select_Scale_Box.currentText()
    Current_Output_Scale = Output_Scale_Box.currentText()
    Current_Rating = Select_Rating_Text.text()
    # Setting the right mask to check
    if Current_Scale == "100":
        rating_mask.setRange(0.00, 100.00, 2)
    elif Current_Scale == "10":
        rating_mask.setRange(0.00, 10.00, 2)
    elif Current_Scale == "5":
        rating_mask.setRange(0.00, 5.00, 2)
    else:
        Show_Error("Number doesn't fit with your selected scale")
    # Checking the numbers
    Input_Check = QDoubleValidator.validate(rating_mask, Current_Rating, 0)
    if (
        Current_System != ""
        and Current_Scale != ""
        and Current_Output_Scale != ""
        and Current_Rating != ""
        and str(Input_Check[0]) == "State.Acceptable"
    ):
        source_type = Current_System
        source_scale = Current_Scale
        source_rating = Current_Rating
        output_scale = Current_Output_Scale
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
    test_rating = ""
    out_rating = ""
    out_mine = ""
    out_school = ""
    out_linear = ""
    # Convert to rating
    if source_scale == "100":
        test_rating = round(float(source_rating))
    elif source_scale == "10":
        test_rating = round(float(source_rating) * 10)
    elif source_scale == "5":
        test_rating = round(float(source_rating) * 20)
    else:
        Show_Error("Error converting data")
    test_rating = str(test_rating)
    out_rating = loaded_data[test_rating]["My System"]
    temp_mine = float(loaded_data[test_rating]["Mine"])
    temp_school = float(loaded_data[test_rating]["School"])
    temp_linear = float(loaded_data[test_rating]["Linear"])
    # Math for the output scale
    if output_scale == "100":
        out_mine = temp_mine
        out_school = temp_school
        out_linear = temp_linear
    elif output_scale == "10":
        out_mine = temp_mine / 10
        out_school = temp_school / 10
        out_linear = temp_linear / 10
    elif output_scale == "5":
        out_mine = temp_mine / 20
        out_school = temp_school / 20
        out_linear = temp_linear / 20
    else:
        Show_Error("Error outputting data")
    # Getting the output {Dictionary}
    output = {"Rating": "", "Mine": "", "School": "", "Linear": ""}
    output["Rating"] = str(out_rating)
    output["Mine"] = str(out_mine)
    output["School"] = str(out_school)
    output["Linear"] = str(out_linear)
    # Output
    Output_Category.setText(output["Rating"])
    Output_Mine.setText(output["Mine"])
    Output_School.setText(output["School"])
    Output_Linear.setText(output["Linear"])


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
window.setWindowTitle("Rating Converter")
window.setWindowIcon(QIcon(path_to_icon))
# Making objects
Input_Label = QLabel("<h1>Inputs</h1>", parent=window)  # Static
Source_System_Label = QLabel("Source System: ", parent=window)  # Static
Select_System_Box = QComboBox(parent=window)  # User
Select_System_Box.setPlaceholderText("System")
Select_System_Box.addItems(["Mine", "School", "Linear"])
Source_Scale_Label = QLabel("Source Scale: ", parent=window)  # Static
Select_Scale_Box = QComboBox(parent=window)  # User
Select_Scale_Box.setPlaceholderText("Scale")
Select_Scale_Box.addItems(["100", "10", "5"])
Source_Rating_Label = QLabel("Source Rating: ", parent=window)  # Static
Select_Rating_Text = QLineEdit(parent=window)  # User
Output_Scale_Label = QLabel("Output Scale: ", parent=window)  # Static
Output_Scale_Box = QComboBox(parent=window)  # User
Output_Scale_Box.setPlaceholderText("Scale")
Output_Scale_Box.addItems(["100", "10", "5"])
rating_mask = QDoubleValidator(parent=window)
rating_mask.setNotation(QDoubleValidator.Notation.StandardNotation)
rating_mask.setRange(0.00, 100.00, 2)
Select_Rating_Text.setPlaceholderText("Rating")
Select_Rating_Text.setValidator(rating_mask)
Output_Label = QLabel("<h1>Outputs</h1>", parent=window)  # Static
Output_Category_Label = QLabel("Rating: ", parent=window)  # Static
Output_Mine_Label = QLabel("Mine: ", parent=window)  # Static
Output_School_Label = QLabel("School: ", parent=window)  # Static
Output_Linear_Label = QLabel("Linear: ", parent=window)  # Static
Output_Category = QLineEdit(parent=window)  # Dynamic
Output_Category.setReadOnly(True)
Output_Mine = QLineEdit(parent=window)  # Dynamic
Output_Mine.setReadOnly(True)
Output_School = QLineEdit(parent=window)  # Dynamic
Output_School.setReadOnly(True)
Output_Linear = QLineEdit(parent=window)  # Dynamic
Output_Linear.setReadOnly(True)
Convert_Button = QPushButton("Convert", parent=window)
# Making Layout
layout = QGridLayout()
layout.addWidget(Input_Label, 0, 0, alignment=Qt.AlignmentFlag.AlignCenter)
layout.addWidget(Source_System_Label, 1, 0, alignment=Qt.AlignmentFlag.AlignCenter)
layout.addWidget(Select_System_Box, 1, 1, alignment=Qt.AlignmentFlag.AlignCenter)
layout.addWidget(Source_Scale_Label, 2, 0, alignment=Qt.AlignmentFlag.AlignCenter)
layout.addWidget(Select_Scale_Box, 2, 1, alignment=Qt.AlignmentFlag.AlignCenter)
layout.addWidget(Source_Rating_Label, 3, 0, alignment=Qt.AlignmentFlag.AlignCenter)
layout.addWidget(Select_Rating_Text, 3, 1, alignment=Qt.AlignmentFlag.AlignCenter)
layout.addWidget(Output_Scale_Label, 4, 0, alignment=Qt.AlignmentFlag.AlignCenter)
layout.addWidget(Output_Scale_Box, 4, 1, alignment=Qt.AlignmentFlag.AlignCenter)
layout.addWidget(Output_Label, 5, 0, alignment=Qt.AlignmentFlag.AlignCenter)
layout.addWidget(Output_Category_Label, 6, 0, alignment=Qt.AlignmentFlag.AlignCenter)
layout.addWidget(Output_Category, 6, 1, alignment=Qt.AlignmentFlag.AlignCenter)
layout.addWidget(Output_Mine_Label, 7, 0, alignment=Qt.AlignmentFlag.AlignCenter)
layout.addWidget(Output_Mine, 7, 1, alignment=Qt.AlignmentFlag.AlignCenter)
layout.addWidget(Output_School_Label, 8, 0, alignment=Qt.AlignmentFlag.AlignCenter)
layout.addWidget(Output_School, 8, 1, alignment=Qt.AlignmentFlag.AlignCenter)
layout.addWidget(Output_Linear_Label, 9, 0, alignment=Qt.AlignmentFlag.AlignCenter)
layout.addWidget(Output_Linear, 9, 1, alignment=Qt.AlignmentFlag.AlignCenter)
layout.addWidget(Convert_Button, 10, 0, alignment=Qt.AlignmentFlag.AlignCenter)
# Testing Values
Convert_Button.pressed.connect(Get_Values)
### Showing the application and window ###
window.setLayout(layout)
window.setMinimumSize(window.minimumSizeHint())
window.setMaximumSize(window.sizeHint())
window.show()
sys.exit(app.exec())

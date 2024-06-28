from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QScrollArea
import json
from functools import partial
# Sample JSON data
json_data = '''
{
    "friends":[
        {
            "id":12,
            "unid":"wassq1",
            "name":"wajih"
        },{
            "id":13,
            "unid":"asfq1",
            "name":"amin"
        },{
            "id":14,
            "unid":"asasfq1",
            "name":"samer"
        },{
            "id":12,
            "unid":"wassq1",
            "name":"wajih"
        },{
            "id":13,
            "unid":"asfq1",
            "name":"amin"
        },{
            "id":14,
            "unid":"asasfq1",
            "name":"samer"
        },{
            "id":12,
            "unid":"wassq1",
            "name":"wajih"
        },{
            "id":13,
            "unid":"asfq1",
            "name":"amin"
        },{
            "id":14,
            "unid":"asasfq1",
            "name":"samer"
        },{
            "id":12,
            "unid":"wassq1",
            "name":"wajih"
        },{
            "id":13,
            "unid":"asfq1",
            "name":"amin"
        },{
            "id":14,
            "unid":"asasfq1",
            "name":"samer"
        }
    ]
}
'''

def mssf(uis):
    print("Button clicked",uis)
data = json.loads(json_data)
app = QApplication([])
ff = loadUi("interfaces/wajhsa.ui")


layout = QVBoxLayout()

scroll_area = ff.findChild(QScrollArea, "scrollArea")
scroll_content = QWidget()
scroll_layout = QVBoxLayout(scroll_content)
for friend in data['friends']:
    label = QLabel(friend['name'])
    button = QPushButton(friend['name'])
    button.setObjectName(friend['unid'])
    button.clicked.connect(partial(mssf, friend['unid']))
    scroll_layout.addWidget(label)
    scroll_layout.addWidget(button)

# Set the layout to the scroll area widget
scroll_area.setWidget(scroll_content)
scroll_area.setWidgetResizable(False)

# Show the main window
ff.show()
app.exec_()

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, 
    QPushButton, QLabel, 
    QListWidget, QLineEdit, 
    QTextEdit, QInputDialog, 
    QHBoxLayout, QVBoxLayout, 
    QFormLayout)

import json

app =QApplication([])

notes = {
    'Это первая заметка!' : {
        'текст': 'Тут ничего интересного!',
        'теги' : ['алгоритмика','супер', 'номер 1']
    }
}


with open('notes1.json', 'w', encoding = 'utf-8') as file:
    json.dump(notes,file)

window =QWidget()
window.setWindowTitle('Умные заметки')
window.resize(900,900)

window_list = QListWidget()
window_List_label = QLabel('Список твоих заметок')

text =QTextEdit()
#кнопки для заметок
button1 =QPushButton('Создать заметку')
button2 =QPushButton('Удалить заметку')
button3 =QPushButton('Сохранить заметку')


#теги

tag = QLineEdit()
tag.setPlaceholderText('Тег')
text = QTextEdit()
button1_tag=QPushButton('Добавь к заметке')
button2_tag=QPushButton('Открепить от заметки')
button3_tag=QPushButton('Искать заметки по тегу')
tags = QListWidget()
tags_label = QLabel('Теги')

layout_notes =QHBoxLayout()
c1 = QVBoxLayout()
c1.addWidget(text)







c2 =QVBoxLayout()
c2.addWidget(window_List_label)
c2.addWidget(window_list)
r_1 = QHBoxLayout()
r_1.addWidget(button1)
r_1.addWidget(button2)
r_2 = QHBoxLayout()
r_2.addWidget(button3)
c2.addLayout(r_1)
c2.addLayout(r_2)


c2.addWidget(tags_label)
c2.addWidget(tags)
c2.addWidget(tag)
r_3 =QHBoxLayout()
r_3.addWidget(button1_tag)
r_3.addWidget(button2_tag)
r_4 =QHBoxLayout()
r_4.addWidget(button3_tag)
c2.addLayout(r_3)
c2.addLayout(r_4)

layout_notes.addLayout(c1, stretch =2 )
layout_notes.addLayout(c2, stretch =1 )
window.setLayout(layout_notes)


#функции
def show():
    key = window_list.selectedItems()[0].text()
    text.setText(notes[key]['текст'])
    tags.clear()
    tags.addItems(notes[key]['теги'])
def add_note():
    note_name, ok = QInputDialog.getText(window,'Добавь свою заметку','Назови свою заметку: ')
    if ok and note_name != '':
        notes[note_name]={'текст': '', 'теги' : []}
        window_list.clear()
        window_list.addItems(notes)    
        tags.addItems(notes[note_name]['теги'])
        with open('notes1.json', 'w') as file:
            json.dump(notes, file, sort_keys=True)

def del_note():
    if window_list.selectedItems():
        key = window_list.selectedItems()[0].text()  
        del notes[key] 
        window_list.clear()
        tags.clear()
        text.clear()
        window_list.addItems(notes)
        with open('notes1.json', 'w') as file:
            json.dump(notes, file, sort_keys=True)

def save_note():
    if window_list.selectedItems():
        key = window_list.selectedItems()[0].text()    
        notes[key]['текст']=text.toPlainText()
        with open('notes1.json', 'w') as file:
            json.dump(notes, file, sort_keys=True)
def add_tags():
    if window_list.selectedItems():
        key = window_list.selectedItems()[0].text()
        time_tag  = tag.text()
        if not time_tag in notes[key]['теги']:
            notes[key]['теги'].append(time_tag)
            tags.addItem(time_tag)
            tag.clear()
        with open('notes1.json', 'w') as file:
            json.dump(notes, file, sort_keys=True)
def del_tag():
    if window_list.selectedItems():
        key = window_list.selectedItems()[0].text()
        time_tag  = tags.selectedItems()[0].text()
        notes[key]['теги'].remove(time_tag)
        tags.clear()
        tags.addItems(notes[key]['теги'])
        with open('notes1.json', 'w') as file:
            json.dump(notes, file, sort_keys=True)



def search_tag():
    tags1 = tag.text()
    if button3_tag.text() == "Искать заметки по тегу" and tags1:
        notes_filtered = {} #тут будут заметки с выделенным тегом
        for note in notes:
            if tags1 in notes[note]["теги"]: 
                notes_filtered[note]=notes[note]
        button3_tag.setText("Сбросить поиск")
        notes.clear()
        tag.clear()
        window_list.addItems(notes_filtered)
    elif button3_tag.text() == "Сбросить поиск":
        tags.clear()
        notes.clear()
        window_list.addItems(notes)
        button3_tag.setText("Искать заметки по тегу")
    else:
        pass
    with open('notes1.json', 'w', encoding = 'utf-8') as file:
            json.dump(notes, file, sort_keys=True)




#кнопки
window_list.itemClicked.connect(show)
button1.clicked.connect(add_note)
button2.clicked.connect(del_note)
button3.clicked.connect(save_note)
button1_tag.clicked.connect(add_tags)
button2_tag.clicked.connect(del_tag)
button3_tag.clicked.connect(search_tag)
window.show()

with open('notes1.json', 'r') as file:
    notes = json.load(file)

window_list.addItems(notes)

app.exec()


#notes[key]['теги'].append(То что ввел)
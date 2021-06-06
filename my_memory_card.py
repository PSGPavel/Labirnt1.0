#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QButtonGroup, QRadioButton, QPushButton, QLabel, QMessageBox)
from random import shuffle
 
app = QApplication([])
btn_OK = QPushButton('Ответить') 
lb_Question = QLabel('Самый сложный вопрос в мире!')
 
RadioGroupBox = QGroupBox("Варианты ответов") 
rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')
 
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout() 
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) 
layout_ans3.addWidget(rbtn_4)
 
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3) 
 
RadioGroupBox.setLayout(layout_ans1) 
 
AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('прав ты или нет?')
lb_Correct = QLabel('ответ будет тут!')
 
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
 
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
 
layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide() 
layout_line3.addWidget(btn_OK, stretch=2) 
 
layout_card = QVBoxLayout()
 
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addLayout(layout_line3, stretch=1)

class Gerund():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
question_list = []   
question_list.append(Gerund('Куда на курортных пляжах просят не заплывать отдыхающих?', 'За буйки', 'За горизонт', 'В камыши', 'За границу'))
question_list.append(Gerund("При падении чего принято загадывать желание?", "Звезды", "Температуры", "Курса рубля", "Дисциплины" ))
question_list.append(Gerund("Что показывает судья футболисту, делая предупреждение?", "Желтую карточку", "Бюллетень", "Язык", "Паспорт" ))
question_list.append(Gerund("Какой рубрики в разделе объявлений не существует?", "Обую", "Продам", "Куплю", "Сниму" ))
question_list.append(Gerund("Какой запрет реже всего нарушают российские граждане?", "Не влезай, убьет!", "Не курить!", "Соблюдайте очередь!", "Вход - по пропускам!" ))


def show_question():
    ''' показать панель вопросов '''
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False) 
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True) 

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
 
def ask(q: Gerund):
    ''' функция записывает значения вопроса и ответов в соответствующие виджеты, 
    при этом варианты ответов распределяются случайным образом'''
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer) 
    show_question() 

 
def check_answer():
    ''' если выбран какой-то вариант ответа, то надо проверить и показать панель ответов'''
    if answers[0].isChecked():
        window.count1 = window.count1 + 1
        lb_Result.setText("Правильно")
        RadioGroupBox.hide()
        AnsGroupBox.show()
        btn_OK.setText('Следующий вопрос')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            lb_Result.setText("Неверно")
            RadioGroupBox.hide()
            AnsGroupBox.show()
            btn_OK.setText('Следующий вопрос')

def next_question():
    window.count = window.count + 1
    if window.count >= len(question_list):
        victory_win = QMessageBox()
        victory_win.setText("Ты прошёл тест на " + str(window.count1) + " баллов")
        victory_win.exec_()
    q = question_list[window.count]
    ask(q)

def click_Ok():
    if btn_OK.text() == "Ответить":
        check_answer()
    else:
        next_question()

window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memo Card')

window.count = -1
window.count1 = 0
btn_OK.clicked.connect(click_Ok) 
next_question()
window.show()
app.exec()




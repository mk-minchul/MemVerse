#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from functools import partial

VERSENAME = [u'고후5:17',u'갈2:20',u'롬12:1',u'요14:21',u'딤후3:16',u'수1:8',
             u'요15:7',u'빌4:6,7',u'마18:20',u'히10:24,25',u'마4:19',u'롬1:16',
             u'롬3:23',u'사53:6',u'롬6:23',u'히9:27',u'롬5:8',u'벧전3:18',
             u'엡2:8,9',u'딛3:5',u'요1:12',u'계3:20',u'요일5:13',u'요5:24',
             u'고전3:16',u'고전2:12',u'사41:10',u'빌4:13',u'애3:22,23',u'민23:19',
             u'사26:3',u'벧전5:7',u'롬8:32',u'빌4:19',u'히2:18',u'시119:9,11',
             u'마6:33',u'눅9:23',u'요일2:15,16',u'롬12:2',u'고전15:58',u'히12:3',
             u'막10:45',u'고후4:5',u'잠3:9,10',u'고후9:6,7',u'행1:8',u'마28:19,20',
             u'요13:34,35',u'요일3:18',u'빌2:3,4',u'벧전5:5,6',u'엡5:3',u'벧전2:11',
             u'레19:11',u'행24:16',u'히11:6',u'롬4:20,21',u'갈6:9,10',u'마5:16']

VERSE = [u'그런즉 누구든지 그리스도 안에 있으면 새로운 피조물이라 이전 것은 지나갔으니 보라 새 것이 되었도다',
         u'내가 그리스도와 함께 십자가에 못 박혔나니 그런즉 이제는 내가 산 것이 아니요 오직 내 안에 그리스도께서 사신 것이라 이제 내가 육체 가운데 사는 것은 나를 사랑하사 나를 위하여 자기 몸을 버리신 하나님의 아들을 믿는 믿음 안에서 사는 것이라',
         u'그러므로 형제들아 내가 하나님의 모든 자비하심으로 너희를 권하노니 너희 몸을 하나님이 기뻐하시는 거룩한 산 제사로 드리라 이는 너희의 드릴 영적 예배니라',
         u'나의 계명을 가지고 지키는 자라야 나를 사랑하는 자니 나를 사랑하는 자는 내 아버지께 사랑을 받을 것이요 나도 그를 사랑하여 그에게 나를 나타내리라',
         u'모든 성경은 하나님의 감동으로 된 것으로 교훈과 책망과 바르게 함과 의로 교육하기에 유익하니',
         u'이 율법책을 네 입에서 떠나지 말게 하며 주야로 그것을 묵상하여 그 가운데 기록한대로 다 지켜 행하라 그리하면 네 길이 평탄하게 될 것이라 네가 형통하리라',
         u'너희가 내 안에 거하고 내 말이 너희 안에 거하면 무엇이든지 원하는대로 구하라 그리하면 이루리라',
         u'아무 것도 염려하지 말고 오직 모든 일에 기도와 간구로 너희 구할 것을 감사함으로 하나님께 아뢰라 그리하면 모든 지각에 뛰어난 하나님의 평강이 그리스도 예수 안에서 너희 마음과 생각을 지키시리라',
         u'두 세 사람이 내 이름으로 모인 곳에는 나도 그들 중에 있느니라',
         u'서로 돌아보아 사랑과 선행을 격려하며 모이기를 폐하는 어떤 사람들의 습관과 같이 하지 말고 오직 권하여 그날이 가까움을 볼수록 더욱 그리하자',
         u'말씀하시되 나를 따라 오너라 내가 너희로 사람을 낚는 어부가 되게 하리라 하시니',
         u'내가 복음을 부끄러워하지 아니하노니 이 복음은 모든 믿는 자에게 구원을 주시는 하나님의 능력이 됨이라 첫째는 유대인에게요 또한 헬라인에게로다',
         u'모든 사람이 죄를 범하였으매 하나님의 영광에 이르지 못하더니',
         u'우리는 다 양 같아서 그릇 행하여 각기 제 길로 갔거늘 여호와께서는 우리 무리의 죄악을 그에게 담당시키셨도다',
         u'죄의 삯은 사망이요 하나님의 은사는 그리스도 예수 우리 주 안에 있는 영생이니라',
         u'한번 죽는 것은 사람에게 정하신 것이요 그 후에는 심판이 있으리니',
         u'우리가 아직 죄인 되었을 때에 그리스도께서 우리를 위하여 죽으심으로 하나님께서 우리에게 대한 자기의 사랑을 확증하셨느니라',
         u'그리스도께서도 한번 죄를 위하여 죽으사 의인으로서 불의한 자를 대신하셨으니 이는 우리를 하나님 앞으로 인도하려 하심이라 육체로는 죽임을 당하시고 영으로는 살리심을 받으셨으니',
         u'너희가 그 은혜를 인하여 믿음으로 말미암아 구원을 얻었나니 이것이 너희에게서 난 것이 아니요 하나님의 선물이라 행위에서 난 것이 아니니 이는 누구든지 자랑치 못하게 함이니라',
         u'우리를 구원하시되 우리의 행한바 의로운 행위로 말미암지 아니하고 오직 그의 긍휼하심을 좇아 중생의 씻음과 성령의 새롭게 하심으로 하셨나니',
         u'영접하는 자 곧 그 이름을 믿는 자들에게는 하나님의 자녀가 되는 권세를 주셨으니',
         u'볼지어다 내가 문밖에 서서 두드리노니 누구든지 내 음성을 듣고 문을 열면 내가 그에게로 들어가 그로 더불어 먹고 그는 나로 더불어 먹으리라',
         u'내가 하나님의 아들의 이름을 믿는 너희에게 이것을 쓴 것은 너희로 하여금 너희에게 영생이 있음을 알게 하려 함이라',
         u'내가 진실로 진실로 너희에게 이르노니 내 말을 듣고 또 나 보내신 이를 믿는 자는 영생을 얻었고 심판에 이르지 아니하나니 사망에서 생명으로 옮겼느니라',
         u'너희가 하나님의 성전인 것과 하나님의 성령이 너희 안에 거하시는 것을 알지 못하느뇨',
         u'우리가 세상의 영을 받지 아니하고 오직 하나님께로 온 영을 받았으니 이는 우리로 하여금 하나님께서 우리에게 은혜로 주신 것들을 알게 하려 하심이라',
         u'두려워 말라 내가 너와 함께 함이니라 놀라지 말라 나는 네 하나님이 됨이니라 내가 너를 굳세게 하리라 참으로 너를 도와 주리라 참으로 나의 의로운 오른손으로 너를 붙들리라',
         u'내게 능력 주시는 자 안에서 내가 모든 것을 할 수 있느니라',
         u'여호와의 자비와 긍휼이 무궁하시므로 우리가 진멸되지 아니함이니이다 이것이 아침마다 새로우니 주의 성실이 크도소이다',
         u'하나님은 인생이 아니시니 식언치 않으시고 인자가 아니시니 후회가 없으시도다 어찌 그 말씀하신 바를 행치 않으시며 하신 말씀을 실행치 않으시랴',
         u'주께서 심지가 견고한 자를 평강에 평강으로 지키시리니 이는 그가 주를 의뢰함이니이다',
         u'너희 염려를 다 주께 맡겨 버리라 이는 저가 너희를 권고하심이니라',
         u'자기 아들을 아끼지 아니하시고 우리 모든 사람을 위하여 내어 주신 이가 어찌 그 아들과 함께 모든 것을 우리에게 은사로 주지 아니 하시겠느뇨',
         u'나의 하나님이 그리스도 예수 안에서 영광 가운데 그 풍성한 대로 너희 모든 쓸 것을 채우시리라',
         u'자기가 시험을 받아 고난을 당하셨은즉 시험받는 자들을 능히 도우시느니라',
         u'청년이 무엇으로 그 행실을 깨끗케 하리이까 주의 말씀을 따라 삼갈 것이니이다 내가 주께 범죄치 아니하려 하여 주의 말씀을 내 마음에 두었나이다',
         u'너희는 먼저 그의 나라와 그의 의를 구하라 그리하면 이 모든 것을 너희에게 더하시리라',
         u'또 무리에게 이르시되 아무든지 나를 따라 오려거든 자기를 부인하고 날마다 제 십자가를 지고 나를 좇을 것이니라',
         u'이 세상이나 세상에 있는 것들을 사랑치 말라 누구든지 세상을 사랑하면 아버지의 사랑이 그 속에 있지 아니하니 이는 세상에 있는 모든 것이 육신의 정욕과 안목의 정욕과 이생의 자랑이니 다 아버지께로 좇아 온 것이 아니요 세상으로 좇아 온 것이라',
         u'너희는 이 세대를 본받지 말고 오직 마음을 새롭게 함으로 변화를 받아 하나님의 선하시고 기뻐하시고 온전하신 뜻이 무엇인지 분별하도록 하라',
         u'그러므로 내 사랑하는 형제들아 견고하며 흔들리지 말며 항상 주의 일에 더욱 힘쓰는 자들이 되라 이는 너희 수고가 주 안에서 헛되지 않은 줄을 앎이니라',
         u'너희가 피곤하여 낙심치 않기 위하여 죄인들의 이같이 자기에게 거역한 일을 참으신 자를 생각하라',
         u'인자의 온 것은 섬김을 받으려 함이 아니라 도리어 섬기려 하고 자기 목숨을 많은 사람의 대속물로 주려 함이니라',
         u'우리가 우리를 전파하는 것이 아니라 오직 그리스도 예수의 주 되신 것과 또 예수를 위하여 우리가 너희의 종 된 것을 전파함이라',
         u'네 재물과 네 소산물의 처음 익은 열매로 여호와를 공경하라 그리하면 네 창고가 가득히 차고 네 즙틀에 새 포도즙이 넘치리라',
         u'이것이 곧 적게 심는 자는 적게 거두고 많이 심는 자는 많이 거둔다 하는 말이로다 각각 그 마음에 정한대로 할 것이요 인색함으로나 억지로 하지 말지니 하나님은 즐겨 내는 자를 사랑하시느니라',
         u'오직 성령이 너희에게 임하시면 너희가 권능을 받고 예루살렘과 온 유대와 사마리아와 땅끝까지 이르러 내 증인이 되리라 하시니라',
         u'그러므로 너희는 가서 모든 족속으로 제자를 삼아 아버지와 아들과 성령의 이름으로 세례를 주고 내가 너희에게 분부한 모든 것을 가르쳐 지키게 하라 볼지어다 내가 세상 끝날까지 너희와 항상 함께 있으리라 하시니라',
         u'새 계명을 너희에게 주노니 서로 사랑하라 내가 너희를 사랑한 것 같이 너희도 서로 사랑하라 너희가 서로 사랑하면 이로써 모든 사람이 너희가 내 제자인 줄 알리라',
         u'자녀들아 우리가 말과 혀로만 사랑하지 말고 오직 행함과 진실함으로 하자',
         u'아무 일에든지 다툼이나 허영으로 하지 말고 오직 겸손한 마음으로 각각 자기보다 남을 낫게 여기고 각각 자기 일을 돌아볼 뿐더러 또한 각각 다른 사람들의 일을 돌아보아 나의 기쁨을 충만케 하라',
         u'젊은 자들아 이와 같이 장로들에게 순복하고 다 서로 겸손으로 허리를 동이라 하나님이 교만한 자를 대적하시되 겸손한 자들에게는 은혜를 주시느니라 그러므로 하나님의 능하신 손 아래서 겸손하라 때가 되면 너희를 높이시리라',
         u'음행과 온갖 더러운 것과 탐욕은 너희 중에서 그 이름이라도 부르지 말라 이는 성도의 마땅한 바니라',
         u'사랑하는 자들아 나그네와 행인 같은 너희를 권하노니 영혼을 거스려 싸우는 육체의 정욕을 제어하라',
         u'너희는 도적질하지 말며 속이지 말며 서로 거짓말하지 말며',
         u'이것을 인하여 나도 하나님과 사람을 대하여 항상 양심에 거리낌이 없기를 힘쓰노라',
         u'믿음이 없이는 기쁘시게 못하나니 하나님께 나아가는 자는 반드시 그가 계신 것과 또한 그가 자기를 찾는 자들에게 상 주시는 이심을 믿어야 할지니라',
         u'믿음이 없어 하나님의 약속을 의심치 않고 믿음에 견고하여져서 하나님께 영광을 돌리며 약속하신 그것을 또한 능히 이루실 줄을 확신하였으니',
         u'우리가 선을 행하되 낙심하지 말지니 피곤하지 아니하면 때가 이르매 거두리라 그러므로 우리는 기회 있는대로 모든 이에게 착한 일을 하되 더욱 믿음의 가정들에게 할지니라',
         u'이같이 너희 빛을 사람 앞에 비취게 하여 저희로 너희 착한 행실을 보고 하늘에 계신 너희 아버지께 영광을 돌리게 하라']

print len(VERSE)



class MainWindow(QtGui.QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()

    def initUI(self):


        grid = QtGui.QGridLayout()

        positions = [(i, j) for i in range(10) for j in range(6)]
        self.checkbox_state = []
        k = 0
        for i, j in positions:
            cb = QtGui.QCheckBox(VERSENAME[k], self)
            #cb.toggle()
            cb.stateChanged.connect(partial( self.check_pressed, cb))
            grid.addWidget(cb, i,j)
            k += 1

        self.verseSelector = 0
        self.verseAddress = QtGui.QLabel(u"요한복음 3장 18절")
        self.currentAddress = QtGui.QLabel(u"")
        self.verseAddress.setWordWrap(True)
        self.verseAnswer = u"자녀들아, 우리가 말과 혀로만 사랑하지 말고 행함과 진실함으로 하자."
        self.hintLabel = QtGui.QLabel(u"")
        self.hintLabel.setWordWrap(True)
        self.copiedVerse = QtGui.QLabel(u'성경구절')
        self.copiedVerse.setWordWrap(True)
        self.writeVerse = QtGui.QTextEdit()
        QtCore.QObject.connect(self.writeVerse, QtCore.SIGNAL("textChanged()"), self.text_changed)

        vbox = QtGui.QVBoxLayout()
        vbox.addLayout(grid)
        vbox.addWidget(self.verseAddress)
        vbox.addWidget(self.currentAddress)
        vbox.addWidget(self.hintLabel)
        vbox.addWidget(self.copiedVerse)
        vbox.addWidget(self.writeVerse)

        hbox = QtGui.QHBoxLayout()
        self.nextBt = QtGui.QPushButton("next")
        self.nextBt.clicked.connect(self.nextBtClicked)
        self.hintBt = QtGui.QPushButton("hint")
        self.hintBt.clicked.connect(self.hintClicked)
        hbox.addWidget(self.nextBt)
        hbox.addWidget(self.hintBt)
        vbox.addLayout(hbox)

        self.setLayout(vbox)


        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle("MemVerse")
        self.show()

    def text_changed(self):
        text = unicode(self.writeVerse.toPlainText() )
        compare_text = text.replace(" ", "")
        compare_answer = self.verseAnswer
        compare_answer = compare_answer.replace(" ", "")
        if compare_text == compare_answer[:len(compare_text)]:
            right = text
            wrong = ""
        else:
            i = 0
            if len(compare_text) > len(compare_answer):
                i = len(compare_answer)
            else:
                while compare_text[i] == compare_answer[i]:
                    i += 1
            #calculate empty spaces. This is necessary because we don't
            #take empty space into account when we are comparing right and wrong
            space = sum( c.isspace() for c in text[:len(compare_text)] )
            space = sum(c.isspace() for c in text[:len(compare_text)+space])
            if i + space > len(text):
                space = len(text) - i
            right = text[0:i+space]
            wrong = text[i+space:]
        self.copiedVerse.setText(right + "<font style='color: red;'>" + wrong +"</font>")

    def check_pressed(self,cb, state):
        if state == QtCore.Qt.Checked:
            self.checkbox_state.append( unicode(cb.text()) )
            address_list = ', '.join(self.checkbox_state)
            self.verseAddress.setText(unicode(address_list))

            if len(self.checkbox_state) > 0:
                self.currentAddress.setText(u'현재구절: ' + self.checkbox_state[self.verseSelector])
                self.verseAnswer = VERSE[VERSENAME.index(self.checkbox_state[self.verseSelector])]
                self.hintLabel.setText(self.verseAnswer)
            else:
                self.currentAddress.setText( u"")
        else:
            try:
                self.checkbox_state.remove(unicode(cb.text()))
                address_list = ', '.join(self.checkbox_state)
                self.verseAddress.setText(unicode(address_list))

                if len(self.checkbox_state) > 0:
                    self.currentAddress.setText(u'현재구절: '+  self.checkbox_state[self.verseSelector])
                    self.verseAnswer = VERSE[VERSENAME.index(self.checkbox_state[self.verseSelector])]
                    self.hintLabel.setText(self.verseAnswer)
                else:
                    self.currentAddress.setText( u"")
            except:
                print ""

    def nextBtClicked(self):
        if len(self.checkbox_state) == 0:
            return
        if self.verseSelector +1 >= len(self.checkbox_state):
            self.verseSelector = 0
        else:
            self.verseSelector += 1
        self.currentAddress.setText(u'현재구절: ' + self.checkbox_state[self.verseSelector])
        self.verseAnswer = VERSE[VERSENAME.index(self.checkbox_state[self.verseSelector])]
        self.writeVerse.setText(u"")
        self.hintLabel.setText(self.verseAnswer)


    def hintClicked(self):
        if self.hintLabel.isHidden() == False:
            self.hintLabel.hide()
        else:
            self.hintLabel.show()
if __name__ == "__main__":

    app = QtGui.QApplication(sys.argv)
    myWindow = MainWindow()
    myWindow.show()
    app.exec_()
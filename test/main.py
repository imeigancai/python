# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtCore import QSize

from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout,QVBoxLayout

import sys

from PyQt5.QtWidgets import QPushButton

from PyQt5.QtWidgets import QFormLayout,QLineEdit,QLabel,QListWidget,QListWidgetItem

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.setGeometry(300, 300, 600, 620)

        # 列表
        self.listWidget = QListWidget(self)

        item1 = QListWidgetItem()  # 创建QListWidgetItem对象
        item1.setSizeHint(QSize(300, 150))  # 设置QListWidgetItem大小

        self.tab1 = QWidget()
        self.tab1UI()

        self.listWidget.addItem(item1)  # 添加item
        self.listWidget.setItemWidget(item1, self.tab1)  # 为item设置widget

        item2 = QListWidgetItem()  # 创建QListWidgetItem对象
        item2.setSizeHint(QSize(300, 150))  # 设置QListWidgetItem大小

        self.tab2 = QWidget()
        self.tab2UI()

        self.listWidget.addItem(item2)  # 添加item
        self.listWidget.setItemWidget(item2, self.tab2)  # 为item设置widget

        item3 = QListWidgetItem()
        item3.setSizeHint(QSize(300, 150))  # 设置QListWidgetItem大小
        widget = QWidget()

        layoutA = QHBoxLayout()
        label1 = QLabel("AAA")
        label2 = QLabel("BBB")
        layoutA.addWidget(label1)
        layoutA.addWidget(label2)

        widget.setLayout(layoutA)

        self.listWidget.addItem(item3)
        self.listWidget.setItemWidget(item3, widget)

        # 清空按钮
        self.clearBtn = QPushButton('清空', self)
        self.clearBtn.clicked.connect(self.clear_button)

        layout = QVBoxLayout(self)

        layout.addWidget(self.listWidget)

        layout.addWidget(self.clearBtn)

    def clear_button(self):
        pass
        windows = self.listWidget.currentItem()

        print('aaa')
        print(type(windows))

        widget = self.listWidget.itemWidget(windows)

        print(type(widget))
        print('bbb')
        print('111')
        print(type(str))
        print('ccc')

    def tab1UI(self):
        layout = QFormLayout()
        layout.addRow("姓名", QLineEdit())
        layout.addRow("地址", QLineEdit())
        self.tab1.setLayout(layout)

    def tab2UI(self):
        layout = QFormLayout()
        layout.addRow("年龄", QLineEdit())
        layout.addRow("性别", QLineEdit())
        self.tab2.setLayout(layout)

    def initUI(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())


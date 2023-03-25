#include "widget.h"
#include <qpushbutton.h>
#include <qapplication.h>

MyProWidget::MyProWidget(QWidget *parent)
    : QWidget(parent)
{   /*setMinimumSize(300,150);
    setMaximumSize(300,150);*/

    //在窗口创建一个命令按钮Pushbutton
    QPushButton *quit=new QPushButton("Quit",this);
    quit->setGeometry(600,40,700,280);

}

MyProWidget::~MyProWidget()
{

}


//Widget::~Widget()
//{

//}

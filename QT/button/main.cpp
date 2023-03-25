#include "widget.h"
#include <QApplication>
#include <stdio.h>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    MyProWidget w;

    w.setGeometry(500,999,1200,720);

    w.show();


    return a.exec();
}


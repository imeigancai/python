#ifndef WIDGET_H
#define WIDGET_H

#include <QWidget>

class MyProWidget : public QWidget
{
    Q_OBJECT

public:
    MyProWidget(QWidget *parent = 0);
    ~MyProWidget();
};

#endif // WIDGET_H

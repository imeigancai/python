#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "QDebug"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}


void MainWindow::on_pushButton_clicked()
{
    qDebug()<<"on_pushButton2_clicked";
}

void MainWindow::on_pushButton_2_destroyed()
{

}



void MainWindow::on_textBrowser_anchorClicked(const QUrl &arg1)
{

}





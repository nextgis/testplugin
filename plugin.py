# -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *

# инициализируем ресурсы Qt из файла resouces.py
import resources

class TestPlugin:

  def __init__(self, iface):
    """Иннициализируем класс"""
    # сохраним ссылку на интерфейс QGIS
    self.iface = iface
  
  def initGui(self):
    """Иннициализируем графический интерфейс пользователя"""
    # создадим действие, которое будет запускать конфигурацию расширения
    self.action = QAction(QIcon(":/plugins/testplugingl/icon.png"), "Test plugin", self.iface.mainWindow())
    self.action.setWhatsThis("Configuration for test plugin")
    self.action.setStatusTip("This is status tip")
    
    # connect the action to the run method
    QObject.connect(self.action, SIGNAL("triggered()"), self.run)
    
    # добавим кнопку на панель инструментов
    self.iface.addToolBarIcon(self.action)
    
    # добавим строку вызова в новое подменю
    self.iface.addPluginToMenu("&Test plugin", self.action)
      
  def unload(self):
    """Действия при отключении расширения"""
    # удалить меню расширения и иконку
    self.iface.removePluginMenu("&Test plugin",self.action)
    self.iface.removeToolBarIcon(self.action)

  def run(self):
    """Действия при запуске расширения"""
    # создать и показать сообщение
    infoString = QString("This is a test")
    QMessageBox.information(self.iface.mainWindow(),"About",infoString)

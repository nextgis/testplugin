# -*- coding: utf-8 -*-
#******************************************************************************
#
# TestPlugin
# ---------------------------------------------------------
# This plugin is for testing and templating purposes
#
# Copyright (C) 2013 NextGIS (info@nextgis.org)
#
# This source is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 2 of the License, or (at your option)
# any later version.
#
# This code is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.
#
# A copy of the GNU General Public License is available on the World Wide Web
# at <http://www.gnu.org/licenses/>. You can also obtain it by writing
# to the Free Software Foundation, 51 Franklin Street, Suite 500 Boston,
# MA 02110-1335 USA.
#
#******************************************************************************

import os
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *

# initialize resources (icons) from resouces.py
import resources


class TestPlugin:
    def __init__(self, iface):
        """Initialize class"""
        # save reference to QGIS interface
        self.iface = iface
        self.qgsVersion = unicode(QGis.QGIS_VERSION_INT)
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'TestPlugin_{}.qm'.format(locale))
        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

    def tr(self, message):
        return QCoreApplication.translate("TestPlugin", message)

    def initGui(self):
        """Initialize graphic user interface"""
        # check if the plugin is ran below 2.0
        if int(self.qgsVersion) < 10900:
            qgisVersion = self.qgsVersion[0] + "." + self.qgsVersion[2] + "." + self.qgsVersion[3]
            QMessageBox.warning(self.iface.mainWindow(),
                                "TestPlugin", "Error",
                                "TestPlugin", "QGIS %s detected.\n" % (qgisVersion) +
                                "TestPlugin", "This version of TestPlugin requires at least QGIS version 2.0.\nPlugin will not be enabled.")
            return None

        # create action that will be run by the plugin
        self.action = QAction("Test plugin", self.iface.mainWindow())
        self.action.setIcon(QIcon(":/icons/icon.png"))
        self.action.setWhatsThis("Configuration for test plugin")
        self.action.setStatusTip("This is status tip")

        # add plugin menu to Vector toolbar
        self.iface.addPluginToVectorMenu("TestPlugin", self.action)

        # add icon to new menu item in Vector toolbar
        self.iface.addVectorToolBarIcon(self.action)

        # connect action to the run method
        self.action.triggered.connect(self.run)

    def unload(self):
        """Actions to run when the plugin is unloaded"""
        # remove menu and icon from the menu
        self.iface.removeVectorToolBarIcon(self.action)
        self.iface.removePluginVectorMenu("TestPlugin", self.action)

    def run(self):
        """Action to run"""
        # create a string and show it
        infoString = self.tr("This is a test")
        QMessageBox.information(self.iface.mainWindow(), self.tr("About"), infoString)

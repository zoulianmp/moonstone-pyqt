# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/igor/Desenvolvimento/neppo/moonstone/src/resources/ui/qt/importwindow.ui'
#
# Created: Fri Sep 20 14:20:28 2013
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ImportWindow(object):
    def setupUi(self, ImportWindow):
        ImportWindow.setObjectName("ImportWindow")
        ImportWindow.setWindowModality(QtCore.Qt.WindowModal)
        ImportWindow.resize(657, 539)
        ImportWindow.setCursor(QtCore.Qt.ArrowCursor)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/static/default/icon/22x22/moonstone.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ImportWindow.setWindowIcon(icon)
        self.verticalLayout_3 = QtGui.QVBoxLayout(ImportWindow)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.mainWidget = QtGui.QWidget(ImportWindow)
        self.mainWidget.setObjectName("mainWidget")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.mainWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.splitter = QtGui.QSplitter(self.mainWidget)
        self.splitter.setMidLineWidth(0)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.treeWidgetContainer = QtGui.QWidget(self.splitter)
        self.treeWidgetContainer.setObjectName("treeWidgetContainer")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.treeWidgetContainer)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.splitter_2 = QtGui.QSplitter(self.treeWidgetContainer)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.widget = QtGui.QWidget(self.splitter_2)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtGui.QFrame(self.widget)
        self.frame.setMinimumSize(QtCore.QSize(0, 40))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.searchText = QtGui.QLineEdit(self.frame)
        self.searchText.setObjectName("searchText")
        self.horizontalLayout.addWidget(self.searchText)
        self.searchButton = QtGui.QPushButton(self.frame)
        self.searchButton.setEnabled(True)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/static/default/icon/22x22/page-region.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.searchButton.setIcon(icon1)
        self.searchButton.setCheckable(False)
        self.searchButton.setChecked(False)
        self.searchButton.setFlat(False)
        self.searchButton.setObjectName("searchButton")
        self.horizontalLayout.addWidget(self.searchButton)
        self.resetButton = QtGui.QPushButton(self.frame)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/static/default/icon/22x22/view-refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.resetButton.setIcon(icon2)
        self.resetButton.setObjectName("resetButton")
        self.horizontalLayout.addWidget(self.resetButton)
        self.verticalLayout.addWidget(self.frame)
        self.treeWidget = QtGui.QTreeWidget(self.widget)
        self.treeWidget.setAlternatingRowColors(True)
        self.treeWidget.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.treeWidget.setAnimated(False)
        self.treeWidget.setWordWrap(True)
        self.treeWidget.setHeaderHidden(False)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.header().setCascadingSectionResizes(False)
        self.treeWidget.header().setHighlightSections(False)
        self.treeWidget.header().setSortIndicatorShown(True)
        self.verticalLayout.addWidget(self.treeWidget)
        self.importContainer = QtGui.QWidget(self.splitter_2)
        self.importContainer.setObjectName("importContainer")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.importContainer)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_2.addWidget(self.splitter_2)
        self.imageGroupBox = QtGui.QGroupBox(self.splitter)
        self.imageGroupBox.setTitle("")
        self.imageGroupBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.imageGroupBox.setObjectName("imageGroupBox")
        self.gridLayout = QtGui.QGridLayout(self.imageGroupBox)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtGui.QSpacerItem(27, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.label = QtGui.QLabel(self.imageGroupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.spinBox = QtGui.QSpinBox(self.imageGroupBox)
        self.spinBox.setMinimumSize(QtCore.QSize(0, 0))
        self.spinBox.setMaximumSize(QtCore.QSize(40, 16777215))
        self.spinBox.setObjectName("spinBox")
        self.gridLayout.addWidget(self.spinBox, 0, 2, 1, 1)
        self.imageViewWidget = QtGui.QFrame(self.imageGroupBox)
        self.imageViewWidget.setFrameShape(QtGui.QFrame.StyledPanel)
        self.imageViewWidget.setObjectName("imageViewWidget")
        self.gridLayout.addWidget(self.imageViewWidget, 1, 0, 1, 3)
        self.horizontalSlider = QtGui.QSlider(self.imageGroupBox)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.gridLayout.addWidget(self.horizontalSlider, 2, 0, 1, 2)
        spacerItem1 = QtGui.QSpacerItem(69, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 3, 0, 1, 1)
        self.importButton = QtGui.QPushButton(self.imageGroupBox)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/static/default/icon/22x22/dialog-ok-apply.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.importButton.setIcon(icon3)
        self.importButton.setDefault(True)
        self.importButton.setObjectName("importButton")
        self.gridLayout.addWidget(self.importButton, 3, 1, 1, 2)
        self.horizontalLayout_2.addWidget(self.splitter)
        self.verticalLayout_3.addWidget(self.mainWidget)

        self.retranslateUi(ImportWindow)
        QtCore.QMetaObject.connectSlotsByName(ImportWindow)

    def retranslateUi(self, ImportWindow):
        ImportWindow.setWindowTitle(QtGui.QApplication.translate("ImportWindow", "Moonstone :: Dicom Importing", None, QtGui.QApplication.UnicodeUTF8))
        self.searchButton.setText(QtGui.QApplication.translate("ImportWindow", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.resetButton.setText(QtGui.QApplication.translate("ImportWindow", "Reset", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.setSortingEnabled(True)
        self.treeWidget.headerItem().setText(0, QtGui.QApplication.translate("ImportWindow", "Status", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(1, QtGui.QApplication.translate("ImportWindow", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(2, QtGui.QApplication.translate("ImportWindow", "Sex", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(3, QtGui.QApplication.translate("ImportWindow", "Age", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(4, QtGui.QApplication.translate("ImportWindow", "Modality", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(5, QtGui.QApplication.translate("ImportWindow", "#Images", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(6, QtGui.QApplication.translate("ImportWindow", "Institution", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(7, QtGui.QApplication.translate("ImportWindow", "Date of Birth", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ImportWindow", "Serie:", None, QtGui.QApplication.UnicodeUTF8))
        self.importButton.setText(QtGui.QApplication.translate("ImportWindow", "&Load", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ImportWindow = QtGui.QWidget()
    ui = Ui_ImportWindow()
    ui.setupUi(ImportWindow)
    ImportWindow.show()
    sys.exit(app.exec_())

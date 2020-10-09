import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import csv


class MainWidgets(QTableWidget):
	def __init__(self,r,c):
		super().__init__(r,c)
		self.check_change = True
		self.init_ui()
	def init_ui(self):
		self.cellChanged.connect(self.c_current)
	def c_current(self):
		if self.check_change:
			row = self.currentRow()
			col = self.currentColumn()
			value = self.item(row,col)
			value = value.text()
			print("the current cell is", row, ", ", col)
			print("In this cell we have: ", value)
	def open_sheet(self):
		self.check_change = False
		path = QFileDialog.getOpenFileName(self, os.getenv('HOME'),"", 'CSV(*.csv)')
		if path[0] != "":
			with open(path[0], newline="") as csv_file:
				self.setRowCount(0)
				self.setColumnCount(4)
				my_file = csv.reader(csv_file, dialect='excel')
				for row_data in my_file:
					row = self.rowCount()
					self.insertRow(row)
					if len(row_data) > 10:
						self.setColumnCount(len(row_data))
					for column, stuff in enumerate(row_data):
						item = QTableWidgetItem(stuff)
						self.setItem(row, column, item)
		self.check_change = True
	def save_sheet(self):
		path = QFileDialog.getSaveFileName(self, "Save CSV", os.getenv('HOME'),"", 'CSV(*.csv)')
		if path [0] != "":
			with open(path[0], 'w') as csv_file:
				writer = csv.writer(csv_file, dialect='excel')
				for row in range(self.rowCount()):
					row_data=[]
					for column in range(self.columnCount()):
						item = self.item(row, column)
						if item is not None:
							row_data.append(item.text())
						else:
							row_data.append('')
					writer.writerow(row_data)

	def contextMenuEvent(self, event):
		contextMenu = QMenu(self)
		newAct = contextMenu.addAction("Add Row")
		newAct1 = contextMenu.addAction("Delete Last Row")
		newAct2 = contextMenu.addAction("Copy Last Row")
		action = contextMenu.exec_(self.mapToGlobal(event.pos()))
		if action == newAct:
			rowCount = self.rowCount()
			self.insertRow(rowCount)
		if action == newAct1:
			if self.rowCount() > 0:
				self.removeRow(self.rowCount()-1)
		if action == newAct2:
			self.insertRow(self.rowCount())
			rowCount = self.rowCount()
			columnCount = self.columnCount()

			for j in range(columnCount):
				if not self.item(rowCount-2, j) is None:
					self.setItem(rowCount-1, j, QTableWidgetItem(self.item(rowCount-2, j).text()))

			

class Window(QMainWindow):
	def __init__(self):
		super().__init__()

		self.form_widget = MainWidgets(10, 4)
		self.setCentralWidget(self.form_widget)
		col_headers = ['A', 'B', 'C', 'D']
		self.form_widget.setHorizontalHeaderLabels(col_headers)

		openMenu = QAction('Open File', self)
		openMenu.triggered.connect(self.form_widget.open_sheet)

		saveMenu = QAction('Save File', self)
		saveMenu.triggered.connect(self.form_widget.save_sheet)

		self.statusBar()

		mainMenu = self.menuBar()
		fileMenu = mainMenu.addMenu('&File')
		fileMenu.addAction(openMenu)
		fileMenu.addAction(saveMenu)

		closeMenu = QAction('Quit App', self)
		closeMenu.triggered.connect(qApp.quit)
		fileMenu.addAction(closeMenu)

		fileMenu = mainMenu.addMenu('&Edit')
		fileMenu = mainMenu.addMenu('&View')

		self.setStyleSheet("QMainWindow{background:lightgray;}")

		self.home()


			# tableWidget = QTableWidget()
			# currentRowCount = tableWidget.rowCount() #necessary even when there are no rows in the table
			# tableWidget.setItem(currentRowCount, 0, QTableWidgetItem("Some text"))
				

	def home(self):
		self.setGeometry(0,0, 1200, 500)
		self.setWindowTitle("Main title")
		self.show()

if __name__ == '__main__':
	app=QApplication(sys.argv)
	w = Window()
	w.show()
	sys.exit(app.exec_())


		
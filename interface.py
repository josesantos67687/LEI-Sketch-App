# coding: utf-8

from javax.swing import JFrame, JButton, JOptionPane

class Mywindow(JFrame):
	def __init__(self):
		super(Mywindow, self).__init__(windowClosing=self.on_close)
		self.setDefaultCloseOperation(JFrame.DO_NOTHING_ON_CLOSE)

		self.setSize(300,200)
		self.setLocationRelativeTo(None)
		self.setTitle('Title')

		self.button = JButton('Click me', actionPerformed=self.on_click)
		self.add(self.button)

	def on_click(self, widget):
		print 'clicked'

	def on_close(self, widget):
		self.dispose()


if __name__ == '__main__':
	win = Mywindow()
	win.setVisible(1)


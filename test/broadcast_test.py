import unittest
import sys
import os
from PyQt5 import QtWidgets

class TestBrowser(unittest.TestCase):
    
    def setUp(self):
        global ui, home
        BASEDIR, BASEFILE = os.path.split(os.path.abspath(__file__))
        parent_basedir, __ = os.path.split(BASEDIR)
        print(parent_basedir)
        home = os.path.join(os.path.expanduser('~'), '.config', 'kawaii_player_test')
        if not os.path.exists(home):
            os.makedirs(home)
        sys.path.insert(0, parent_basedir)
        k_dir = os.path.join(parent_basedir, 'kawaii_player')
        sys.path.insert(0, k_dir)

    def test_browser(self):
        from kawaii_player import Ui_MainWindow, MainWindowWidget
        from kawaii_player import send_notification, BroadcastServer, get_lan_ip
        # app = QtWidgets.QApplication(sys.argv)
        # MainWindow = MainWindowWidget()
        # ui = Ui_MainWindow()
        # ui.setupUi(MainWindow, home_val=home, scr_width=800, scr_height=600)
        # ui.set_parameters_value(siteval='MyServer', op='Login')
        # ui.widget_style.apply_stylesheet()
        # ui.local_port_stream = 9001
        # ui.local_ip_stream = get_lan_ip()
        # bser = BroadcastServer(ui, True)
        # bser.start()
        # MainWindow.show()
        # app.exec_()
        
        
if __name__ == '__main__':
    unittest.main()

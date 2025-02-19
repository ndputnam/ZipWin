from os.path import join
from zipfile import ZipFile
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMainWindow, QPushButton, QHBoxLayout, QWidget, QFileDialog
from resources.stylesheets import button
from resources.utility import resource_path, get_all_file_paths


class Zippy(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ZIPPY")
        self.setToolTip('Select ZIP Files to Extract or Select Files to Compress to ZIP')
        self.setWindowIcon(QIcon(resource_path('../resources/images/gear.ico')))
        self.setFixedSize(250, 50)
        self.base_dir = 'C:\\'

        self.extract_file = QPushButton('Extract Files')
        self.extract_file.setMinimumWidth(120)
        self.extract_file.setStyleSheet(button)
        self.extract_file.clicked.connect(lambda checked: self.extract())
        self.extract_file.setToolTip('Decompress ZIP files')

        self.compress_file = QPushButton('Compress Files')
        self.compress_file.setMinimumWidth(120)
        self.compress_file.setStyleSheet(button)
        self.compress_file.clicked.connect(lambda checked: self.compress())
        self.compress_file.setToolTip('Compress to ZIP')

        body = QWidget()
        layout = QHBoxLayout()
        layout.addWidget(self.extract_file)
        layout.addWidget(self.compress_file)
        body.setLayout(layout)
        self.setCentralWidget(body)

    def get_file(self):
        file_name, ok = QFileDialog.getOpenFileName(self, 'Select File to UnZip', self.base_dir, 'ZIP (*.zip)')
        if file_name:
            self.base_dir = file_name[:file_name.rfind('/')]
            return file_name
        return ''

    def get_dir(self, title):
        directory = QFileDialog.getExistingDirectory(self, title, self.base_dir)
        if directory:
            self.base_dir = directory
            return directory
        return ''

    def extract(self):
        file_name = None
        directory = None
        while file_name is None: file_name = self.get_file()
        if file_name and file_name is not None:
            while directory is None: directory = self.get_dir('Select Directory to Extract to')
        if directory and directory is not None:
            with ZipFile(file_name, 'r') as z: z.extractall(directory)

    def compress(self):
        directory = self.get_dir('Select Directory to compress')
        if directory:
            file_paths = get_all_file_paths(directory)
            name = directory.split('/')[-1]
            with ZipFile('%s.zip' % join(self.base_dir[:self.base_dir.rfind('/')], name), 'w') as z:
                for file in file_paths:
                    z.write(file)
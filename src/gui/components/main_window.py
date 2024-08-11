from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QFileDialog
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
import sys,os
from gui.components.image_widget import ImageDisplay
from PIL import Image, ImageEnhance

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.image_display = ImageDisplay(self)
        self.open_button = QPushButton("选择图片", self)
        self.test_button = QPushButton("测试按钮", self)

        layout = QVBoxLayout()
        
        self.save_button = QPushButton("保存图片", self)

        self.open_button.clicked.connect(self.open_image)
        self.test_button.clicked.connect(self.test_change_image)
        self.save_button.clicked.connect(self.save_image)

        layout.addWidget(self.image_display)
        layout.addWidget(self.open_button)
        layout.addWidget(self.test_button)
        layout.addWidget(self.save_button)
        self.setLayout(layout)
        
        self.current_image_path = None
        self.temp_image_path = None
        
    def open_image(self):
        file_dialog = QFileDialog(self)
        file_path, _ = file_dialog.getOpenFileName(self, "选择图片", "", "Images (*.png *.xpm *.jpg)")
        if file_path:
            self.current_image_path = file_path
            self.image_display.set_image(file_path)

    def test_change_image(self):
        if self.current_image_path:
            # 使用 PIL 加载图片
            image = Image.open(self.current_image_path)
            
            # 调整图片颜色（例如增加亮度）
            enhancer = ImageEnhance.Color(image)
            image_enhanced = enhancer.enhance(2.0)  # 增加颜色饱和度

            # 保存调整后的图片到临时文件
            self.temp_image_path = os.path.join(os.path.dirname(self.current_image_path), "temp_image.jpg")
            image_enhanced.save(self.temp_image_path)

            # 更新 ImageDisplay 显示
            self.image_display.set_image(self.temp_image_path)
            
    def save_image(self):
        if self.temp_image_path:
            save_path, _ = QFileDialog.getSaveFileName(self, "保存图片", "", "Images (*.png *.xpm *.jpg)")
            if save_path:
                Image.open(self.temp_image_path).save(save_path)
import sys
import json
import re
import os
import random
from datetime import datetime
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QComboBox, QTextEdit,
    QFrame, QDialog, QSpinBox, QMessageBox,
    QDialogButtonBox, QFormLayout, QCompleter,
    QListWidget, QListWidgetItem, QGroupBox, QAbstractItemView
)
from PySide6.QtGui import (
    QFont, QPixmap, QKeySequence, QIcon, QShortcut, QFontDatabase
)
from PySide6.QtCore import Qt, QSize, QStringListModel
from PIL import Image

# 导入 STM32H7 数据
import STM32H7
from STM32H7 import (
    ALL_STM32H7_DATA, ALL_STM32H7_DATA_H, WW_DATA,
    DEFINE_DATA, DEFINE_DATA_DefineX, WAISHE_DATA
)
from F_Data import (
    TMode1_STM32F103C8T6, TMode1_STM32H7, TMode2_STM32F103C8T6,
    TMode2_STM32H7, TMode3_STM32F103C8T6, TMode3_STM32H7, TMode3_STM32H7X,
    TMode4_STM32F103C8T6, DATA, DATA0, DATA1, DATA2
)
from color_set import THEMES

MAX_HISTORY = 20

# -------------------- 日志功能 --------------------
def clear_log():
    """每次启动时清空日志文件"""
    try:
        with open("operation_log.txt", "w", encoding="utf-8") as f:
            f.write("")
    except Exception as e:
        print(f"清空日志失败: {e}")

def log_operation(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {message}"
    print(log_entry)
    try:
        with open("operation_log.txt", "a", encoding="utf-8") as f:
            f.write(log_entry + "\n")
    except Exception as e:
        print(f"写入日志失败: {e}")

# -------------------- 全局数据加载 --------------------
with open('MODE_DATA.json', 'r', encoding='utf-8') as f:
    settings_data = json.load(f)

with open('wen.json', 'r', encoding='utf-8') as f:
    wen_s = json.load(f)

file_path = "stm32f103c8t6_@V4.0.txt"
try:
    with open(file_path, encoding="utf-8") as DU:
        read = DU.read()
except FileNotFoundError:
    QMessageBox.critical(None, "错误", f"没有找到 {file_path} 文件")
    sys.exit()

ALL_STM32H7_NAMES = list(ALL_STM32H7_DATA_H.keys())

# -------------------- 历史记录管理对话框 --------------------
class HistoryDialog(QDialog):
    def __init__(self, main_window):
        super().__init__(main_window)
        self.main_window = main_window
        self.setWindowTitle("搜索历史管理")
        self.setFixedSize(500, 450)

        layout = QVBoxLayout(self)

        chip_layout = QHBoxLayout()
        chip_layout.addWidget(QLabel("芯片型号："))
        self.chip_combo = QComboBox()
        self.chip_combo.addItems(["STM32F103C8T6", "STM32H7"])
        current_chip = main_window.settings.get('STM', 'STM32F103C8T6')
        self.chip_combo.setCurrentText(current_chip)
        self.chip_combo.currentTextChanged.connect(self.on_chip_changed)
        chip_layout.addWidget(self.chip_combo)
        layout.addLayout(chip_layout)

        self.list_widget = QListWidget()
        self.list_widget.setAlternatingRowColors(True)
        self.list_widget.itemDoubleClicked.connect(self.on_item_double_clicked)
        layout.addWidget(self.list_widget)

        btn_layout = QHBoxLayout()
        self.btn_delete_one = QPushButton("删除选中")
        self.btn_delete_one.clicked.connect(self.delete_one)
        self.btn_clear_all = QPushButton("清除全部")
        self.btn_clear_all.clicked.connect(self.clear_all)
        btn_layout.addWidget(self.btn_delete_one)
        btn_layout.addWidget(self.btn_clear_all)
        layout.addLayout(btn_layout)

        close_btn = QPushButton("关闭")
        close_btn.clicked.connect(self.close)
        layout.addWidget(close_btn)

        self.current_history = []
        self.load_history_for_chip(self.chip_combo.currentText())
        log_operation("打开历史记录管理窗口")

    def load_history_for_chip(self, chip):
        filename = f"search_history_{chip}.json"
        if os.path.exists(filename):
            try:
                with open(filename, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                if data and isinstance(data[0], str):
                    self.current_history = [{"text": s, "time": "未知时间"} for s in data]
                else:
                    self.current_history = data
            except:
                self.current_history = []
        else:
            self.current_history = []
        self.refresh_list()
        log_operation(f"历史管理窗口切换芯片至: {chip}")

    def save_current_history(self):
        chip = self.chip_combo.currentText()
        filename = f"search_history_{chip}.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.current_history, f, ensure_ascii=False, indent=2)
        log_operation(f"保存{chip}的搜索历史")

    def refresh_list(self):
        self.list_widget.clear()
        for item in self.current_history:
            display = f"{item['time']}  {item['text']}"
            list_item = QListWidgetItem(display)
            list_item.setData(Qt.UserRole, item['text'])
            self.list_widget.addItem(list_item)

    def on_chip_changed(self, chip):
        self.load_history_for_chip(chip)

    def delete_one(self):
        current_row = self.list_widget.currentRow()
        if current_row >= 0:
            deleted_item = self.current_history.pop(current_row)
            self.save_current_history()
            if self.chip_combo.currentText() == self.main_window.settings.get('STM'):
                self.main_window.refresh_history()
            self.refresh_list()
            log_operation(f"删除历史记录: {deleted_item['text']}")

    def clear_all(self):
        reply = QMessageBox.question(self, "确认", "确定要清除所有搜索历史吗？",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.current_history.clear()
            self.save_current_history()
            if self.chip_combo.currentText() == self.main_window.settings.get('STM'):
                self.main_window.refresh_history()
            self.refresh_list()
            log_operation("清除所有搜索历史")

    def on_item_double_clicked(self, item):
        keyword = item.data(Qt.UserRole)
        if keyword:
            self.main_window.search_entry.setText(keyword)
            log_operation(f"从历史记录双击关键词: {keyword}")
            self.main_window.mod0(chip=self.chip_combo.currentText())

# -------------------- 设置对话框 --------------------
class SettingsDialog(QDialog):
    def __init__(self, main_window):
        super().__init__(main_window)
        self.main_window = main_window
        self.setWindowTitle("设置界面")
        self.setFixedSize(600, 400)

        layout = QFormLayout(self)

        # 动态加载系统可用字体
        system_fonts = QFontDatabase.families()
        preferred = ["Microsoft YaHei", "宋体", "黑体", "楷体", "仿宋",
                     "Arial", "Helvetica", "Times New Roman", "Consolas", "Courier New"]
        available_preferred = [f for f in preferred if f in system_fonts]
        other_fonts = sorted([f for f in system_fonts if f not in preferred])
        all_fonts = available_preferred + other_fonts

        self.font_combo = QComboBox()
        self.font_combo.addItems(all_fonts)
        current_font = self.main_window.settings.get('ziti', 'Microsoft YaHei')
        if current_font in all_fonts:
            self.font_combo.setCurrentText(current_font)
        else:
            self.font_combo.setCurrentIndex(0)
        layout.addRow("输出字体选择：", self.font_combo)

        self.font_size_spin = QSpinBox()
        self.font_size_spin.setRange(5, 50)
        self.font_size_spin.setValue(self.main_window.settings.get('ziti_size', 12))
        layout.addRow("输出字体大小：", self.font_size_spin)

        self.chip_combo = QComboBox()
        self.chip_combo.addItems(["STM32H7", "STM32F103C8T6"])
        self.chip_combo.setCurrentText(self.main_window.settings.get('STM', 'STM32F103C8T6'))
        layout.addRow("芯片型号：", self.chip_combo)

        self.theme_combo = QComboBox()
        self.theme_combo.addItems(list(THEMES.keys()))
        self.theme_combo.setCurrentText(self.main_window.settings.get('theme', '灰白'))
        layout.addRow("主题风格：", self.theme_combo)

        history_btn = QPushButton("打开历史记录管理")
        history_btn.setFixedSize(450, 20)
        history_btn.clicked.connect(self.open_history_dialog)
        layout.addRow("搜索历史：", history_btn)

        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        button_box.accepted.connect(self.save_settings)
        button_box.rejected.connect(self.reject)
        layout.addRow(button_box)

        log_operation("打开设置界面")

    def open_history_dialog(self):
        dlg = HistoryDialog(self.main_window)
        dlg.exec()

    def save_settings(self):
        old_chip = self.main_window.settings.get('STM')
        new_chip = self.chip_combo.currentText()
        new_font = self.font_combo.currentText()
        new_font_size = self.font_size_spin.value()
        new_theme = self.theme_combo.currentText()

        self.main_window.settings['ziti'] = new_font
        self.main_window.settings['ziti_size'] = new_font_size
        self.main_window.settings['STM'] = new_chip
        self.main_window.settings['theme'] = new_theme

        with open('MODE_DATA.json', 'w', encoding='utf-8') as f:
            json.dump(self.main_window.settings, f, ensure_ascii=False, indent=4)

        log_operation(f"保存设置: 字体={new_font}, 大小={new_font_size}, 芯片={new_chip}, 主题={new_theme}")
        QMessageBox.information(self, "提示", "设置已保存，程序将自动退出。")
        self.accept()
        QApplication.instance().quit()
        sys.exit(0)

# -------------------- 结果显示对话框 --------------------
class ResultDialog(QDialog):
    def __init__(self, main_window, title, text, output_font):
        super().__init__(main_window)
        self.main_window = main_window
        self.setWindowTitle(title)
        self.resize(700, 400)
        self.setMinimumSize(700, 400)
        self.text_edit = QTextEdit()
        self.text_edit.setFont(output_font)
        self.text_edit.setReadOnly(True)
        self.text_edit.setPlainText(text)
        layout = QVBoxLayout(self)
        layout.addWidget(self.text_edit)

        QShortcut(QKeySequence("Ctrl+F"), self, activated=self.main_window.search_shortcut)
        QShortcut(QKeySequence("Ctrl+Q"), self, activated=self.main_window.close)
        QShortcut(QKeySequence("F1"), self, activated=self.main_window.open_settings)

# -------------------- 主窗口 --------------------
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.settings = settings_data
        self.output_font = QFont(
            self.settings.get('ziti', 'Microsoft YaHei'),
            self.settings.get('ziti_size', 12)
        )
        # 界面控件统一 13pt 字体
        self.ui_font = QFont(self.settings.get('ziti', 'Microsoft YaHei'), 13)
        # 设置全局默认字体，所有控件自动继承
        QApplication.instance().setFont(self.ui_font)

        stm = self.settings.get('STM', 'STM32F103C8T6')
        self.history_file = f"search_history_{stm}.json"

        self.history_data = self.load_history()
        self.history_texts = [item['text'] for item in self.history_data]
        self.history_model = QStringListModel(self.history_texts)

        self._search_locked = False

        self.apply_theme()
        self.init_ui()

        log_operation("程序启动")

    def load_history(self):
        if os.path.exists(self.history_file):
            try:
                with open(self.history_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                if data and isinstance(data[0], str):
                    return [{"text": s, "time": "未知时间"} for s in data]
                return data
            except:
                return []
        return []

    def save_history(self):
        with open(self.history_file, 'w', encoding='utf-8') as f:
            json.dump(self.history_data, f, ensure_ascii=False, indent=2)

    def update_history_model(self):
        self.history_texts = [item['text'] for item in self.history_data]
        self.history_model.setStringList(self.history_texts)

    def add_to_history_for_chip(self, text, chip):
        if not text:
            return
        filename = f"search_history_{chip}.json"
        if os.path.exists(filename):
            try:
                with open(filename, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                if data and isinstance(data[0], str):
                    data = [{"text": s, "time": "未知时间"} for s in data]
            except:
                data = []
        else:
            data = []
        data = [item for item in data if item['text'] != text]
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data.insert(0, {"text": text, "time": now})
        if len(data) > MAX_HISTORY:
            data = data[:MAX_HISTORY]
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        if chip == self.settings.get('STM'):
            self.history_data = data
            self.update_history_model()
        log_operation(f"添加搜索历史 [{chip}]：{text}")

    def add_to_history(self, text):
        self.add_to_history_for_chip(text, self.settings.get('STM'))

    def refresh_history(self):
        self.history_data = self.load_history()
        self.update_history_model()

    def apply_theme(self):
        theme = self.settings.get('theme', '灰白')
        QApplication.instance().setStyleSheet(THEMES.get(theme, ""))

    def init_ui(self):
        stm_type = self.settings.get('STM', 'STM32F103C8T6')
        self.init_small_window_min(stm_type)

    def init_small_window_min(self, stm_type):
        self.setWindowTitle("STM32 工具箱 V3.0 @一岁 作")
        self.setFixedSize(340, 240)
        self.move(600, 300)

        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)
        layout.setContentsMargins(10, 15, 10, 10)
        layout.setSpacing(10)

        self.search_entry = QLineEdit()
        self.search_entry.setPlaceholderText("请输入要查询的信息后按回车查询")
        self.search_entry.setMinimumHeight(30)
        self.search_entry.returnPressed.connect(self.mod0)

        completer = QCompleter(self.history_model, self)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        completer.setCompletionMode(QCompleter.CompletionMode.UnfilteredPopupCompletion)
        completer.setMaxVisibleItems(10)
        self.search_entry.setCompleter(completer)
        completer.activated.connect(self.on_history_selected)

        layout.addWidget(self.search_entry)

        if stm_type == "STM32H7":
            btn_row1 = QHBoxLayout()
            self.btn1 = QPushButton("函数列表")
            self.btn2 = QPushButton("功能介绍")
            self.btn1.setFixedSize(150, 90)
            self.btn2.setFixedSize(150, 90)
            self.btn1.clicked.connect(self.mod1)
            self.btn2.clicked.connect(self.mod3)
            btn_row1.addWidget(self.btn1)
            btn_row1.addWidget(self.btn2)
            layout.addLayout(btn_row1)

        if stm_type == "STM32F103C8T6":
            btn_row1 = QHBoxLayout()
            self.btn1 = QPushButton("函数列表")
            self.btn2 = QPushButton("引脚定义")
            self.btn1.setMinimumHeight(40)
            self.btn2.setMinimumHeight(40)
            self.btn1.clicked.connect(self.mod1)
            self.btn2.clicked.connect(self.mod2)
            btn_row1.addWidget(self.btn1)
            btn_row1.addWidget(self.btn2)
            layout.addLayout(btn_row1)

            btn_row2 = QHBoxLayout()
            self.btn3 = QPushButton("外设开启和运用")
            self.btn4 = QPushButton("其他")
            self.btn3.setMinimumHeight(40)
            self.btn4.setMinimumHeight(40)
            self.btn3.clicked.connect(self.mod3)
            self.btn4.clicked.connect(self.mod4)
            btn_row2.addWidget(self.btn3)
            btn_row2.addWidget(self.btn4)
            layout.addLayout(btn_row2)

        self.settings_btn = QPushButton("设置")
        self.settings_btn.setMinimumHeight(40)
        self.settings_btn.clicked.connect(self.open_settings)
        layout.addWidget(self.settings_btn)

        QShortcut(QKeySequence("Ctrl+Q"), self, activated=self.close)
        QShortcut(QKeySequence("F1"), self, activated=self.open_settings)
        QShortcut(QKeySequence("Ctrl+F"), self, activated=self.search_shortcut)
        QShortcut(QKeySequence("Ctrl+D"), self, activated=self.show_shortcuts)
        QShortcut(QKeySequence("Ctrl+H"), self, activated=self.open_history_dialog)

    def on_history_selected(self, text):
        self.search_entry.setText(text)
        self.mod0()

    def _lock_search(self):
        self._search_locked = True
        try:
            self.search_entry.returnPressed.disconnect(self.mod0)
        except:
            pass

    def _unlock_search(self):
        self._search_locked = False
        self.search_entry.returnPressed.connect(self.mod0)

    def mod0(self, chip=None):
        if self._search_locked:
            return
        text = self.search_entry.text().strip()
        if not text:
            return
        self._lock_search()
        stm = chip if chip else self.settings.get('STM', 'STM32F103C8T6')
        log_operation(f"搜索 [{stm}]：{text}")
        try:
            if stm == "STM32F103C8T6":
                result = TMode1_STM32F103C8T6(text)
            else:
                result = TMode1_STM32H7(text)
            self.show_result(f"{text} 查询结果", result)
            self.add_to_history_for_chip(text, stm)
        finally:
            self._unlock_search()

    def open_history_dialog(self):
        dlg = HistoryDialog(self)
        dlg.exec()

    def mod1(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("查看函数")
        dialog.resize(750, 450)
        dialog.setMinimumSize(700, 400)
        layout = QVBoxLayout(dialog)

        stm = self.settings.get('STM', 'STM32F103C8T6')
        combo = QComboBox()
        if stm == "STM32F103C8T6":
            items = ["全部","ADC","GPIO","USART","BKP","CAN","DMA","EXTI","FLASH","I2C","IWDG","NVIC","PWR","RCC","RTC","SPI","SysTick","TIM","WWDG"]
        else:
            items = ["全部","ADC","CEC","COMP","CORTEX","CRC","CRYP","DAC","DCMI","DFSDM","DMA","DMA2D","ETH","EXTI","FDCAN","FLASH","GPIO","HAL","HASH","HCD","HRTIM","HSEM","I2C","I2S","IRDA","IWDG","JPEG","LPTIM","LTDC","MDIOS","MDMA","MMC","NAND","NOR","OPAMP","PCD","PWR","QSPI","RAMECC","RCC","RNG","RTC","SAI","SD","SDIO","SDRAM","SMARTCARD","SMBUS","SPDIFRX","SPI","SRAM","SWPMI","TIM","UART","USART","WWDG"]
        combo.addItems(items)
        combo.setCurrentText(settings_data.get('mod1data', '全部'))
        layout.addWidget(combo)

        text_edit = QTextEdit()
        text_edit.setFont(self.output_font)
        text_edit.setReadOnly(True)
        layout.addWidget(text_edit)

        def update_list():
            sel = combo.currentText()
            log_operation(f"查看函数列表 [{stm}]：{sel}")
            if stm == "STM32F103C8T6":
                text_edit.setPlainText(TMode2_STM32F103C8T6(sel))
            else:
                text_edit.setPlainText(TMode2_STM32H7(sel))

        combo.currentTextChanged.connect(update_list)
        update_list()

        QShortcut(QKeySequence("Ctrl+F"), dialog, activated=self.search_shortcut)
        QShortcut(QKeySequence("Ctrl+Q"), dialog, activated=self.close)
        QShortcut(QKeySequence("F1"), dialog, activated=self.open_settings)
        dialog.exec()

    def mod2(self):
        stm = self.settings.get('STM', 'STM32F103C8T6')
        if stm == "STM32F103C8T6":
            try:
                img = Image.open('STM32F103C8T6引脚定义.png')
                img.show()
                log_operation("查看引脚定义图片")
            except Exception as e:
                QMessageBox.warning(self, "错误", f"无法打开图片：{e}")
        else:
            self.mod3()

    def mod3(self):
        dialog = QDialog(self)
        stm = self.settings.get('STM', 'STM32F103C8T6')
        dialog.setWindowTitle("外设开启和应用" if stm == "STM32F103C8T6" else "功能查找")
        dialog.resize(750, 450)
        dialog.setMinimumSize(700, 400)
        layout = QVBoxLayout(dialog)

        if stm == "STM32F103C8T6":
            combo = QComboBox()
            combo.addItems(["ADC","GPIO","USART","BKP","CAN","DMA","EXTI","FLASH","I2C","IWDG","NVIC","PWR","RCC","RTC","SPI","SysTick","TIM","WWDG","USB"])
            combo.setCurrentText(settings_data.get('mod3data', '请选择'))
            layout.addWidget(combo)
            text_edit = QTextEdit()
            text_edit.setFont(self.output_font)
            text_edit.setReadOnly(True)
            layout.addWidget(text_edit)

            def update():
                sel = combo.currentText()
                log_operation(f"外设查看 [{stm}]：{sel}")
                text_edit.setPlainText(TMode3_STM32F103C8T6(sel))
            combo.currentTextChanged.connect(update)
            update()
        else:
            h_layout = QHBoxLayout()
            combo1 = QComboBox()
            combo1.addItems(["ADC","CEC","COMP","CORTEX","CRC","CRYP","DAC","DCMI","DFSDM","DMA","DMA2D","ETH","EXTI","FDCAN","FLASH","GPIO","HAL","HASH","HCD","HRTIM","HSEM","I2C","I2S","IRDA","IWDG","JPEG","LPTIM","LTDC","MDIOS","MDMA","MMC","NAND","NOR","OPAMP","PCD","PWR","QSPI","RAMECC","RCC","RNG","RTC","SAI","SD","SDIO","SDRAM","SMARTCARD","SMBUS","SPDIFRX","SPI","SRAM","SWPMI","TIM","UART","USART","WWDG"])
            combo1.setCurrentText(settings_data.get('mod3data', '请选择'))
            combo2 = QComboBox()
            h_layout.addWidget(combo1, 1)
            h_layout.addWidget(combo2, 2)
            layout.addLayout(h_layout)

            text_edit = QTextEdit()
            text_edit.setFont(self.output_font)
            text_edit.setReadOnly(True)
            layout.addWidget(text_edit)

            def update_main():
                sel = combo1.currentText()
                log_operation(f"功能查找 [{stm}] 主类：{sel}")
                text_edit.setPlainText(TMode3_STM32H7(sel))
                base_key = sel + "_W"
                if base_key in WAISHE_DATA:
                    items = list(WAISHE_DATA[base_key].keys())
                else:
                    items = []
                combo2.clear()
                combo2.addItems(items)
                combo2.setCurrentText("")

            def update_detail():
                sel_main = combo1.currentText()
                sel_sub = combo2.currentText()
                if sel_main != "请选择" and sel_sub:
                    log_operation(f"功能查找 [{stm}] 详细：{sel_main} -> {sel_sub}")
                    base_key = sel_main + "_W"
                    text_edit.setPlainText(TMode3_STM32H7X(sel_sub, base_key))

            combo1.currentTextChanged.connect(update_main)
            combo2.currentTextChanged.connect(update_detail)
            update_main()

        QShortcut(QKeySequence("Ctrl+F"), dialog, activated=self.search_shortcut)
        QShortcut(QKeySequence("Ctrl+Q"), dialog, activated=self.close)
        QShortcut(QKeySequence("F1"), dialog, activated=self.open_settings)
        dialog.exec()

    def mod4(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("其他功能")
        dialog.resize(750, 450)
        dialog.setMinimumSize(700, 400)
        layout = QVBoxLayout(dialog)

        combo = QComboBox()
        combo.addItems(["I2C介绍和软件I2C的编写","中断服务函数的介绍和使用","中断服务函数列表","__WFI()和__WFE()的使用"])
        combo.setCurrentText("请选择功能")
        layout.addWidget(combo)

        text_edit = QTextEdit()
        text_edit.setFont(self.output_font)
        text_edit.setReadOnly(True)
        layout.addWidget(text_edit)

        def update():
            sel = combo.currentText()
            log_operation(f"其他功能：{sel}")
            text_edit.setPlainText(TMode4_STM32F103C8T6(sel))
        combo.currentTextChanged.connect(update)
        update()

        QShortcut(QKeySequence("Ctrl+F"), dialog, activated=self.search_shortcut)
        QShortcut(QKeySequence("Ctrl+Q"), dialog, activated=self.close)
        QShortcut(QKeySequence("F1"), dialog, activated=self.open_settings)
        dialog.exec()

    def show_result(self, title, text):
        dlg = ResultDialog(self, title, text, self.output_font)
        dlg.exec()

    def search_shortcut(self):
        dlg = QDialog(self)
        dlg.setWindowTitle("搜索界面")
        dlg.resize(700, 400)
        dlg.setMinimumSize(600, 300)
        layout = QVBoxLayout(dlg)

        search_edit = QLineEdit()
        search_edit.setPlaceholderText("请输入要查询的内容后按回车查询")
        layout.addWidget(search_edit)

        text_edit = QTextEdit()
        text_edit.setFont(self.output_font)
        text_edit.setReadOnly(True)
        random_text = random.choice(wen_s) if wen_s else ""
        text_edit.setPlainText(random_text)
        layout.addWidget(text_edit)

        def do_search():
            stm = self.settings.get('STM', 'STM32F103C8T6')
            query = search_edit.text().strip()
            if query:
                log_operation(f"快捷搜索 [{stm}]：{query}")
                if stm == "STM32F103C8T6":
                    text_edit.setPlainText(TMode1_STM32F103C8T6(query))
                else:
                    text_edit.setPlainText(TMode1_STM32H7(query))

        search_edit.returnPressed.connect(do_search)

        QShortcut(QKeySequence("Ctrl+Q"), dlg, activated=self.close)
        QShortcut(QKeySequence("F1"), dlg, activated=self.open_settings)
        dlg.exec()

    def show_shortcuts(self):
        QMessageBox.information(self, "快捷键使用说明",
            "【快捷键列表】\n\nCtrl+Q：退出程序\nF1：打开设置界面\nCtrl+F：快捷打开函数搜索界面\nCtrl+D：打开快捷键使用说明\nCtrl+H：打开历史记录管理")
        log_operation("显示快捷键说明")

    def open_settings(self):
        dlg = SettingsDialog(self)
        dlg.exec()

    def closeEvent(self, event):
        log_operation("程序退出")
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    clear_log()  # 每次启动清空旧日志
    init_theme = settings_data.get('theme', '灰白')
    app.setStyleSheet(THEMES.get(init_theme, ""))
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
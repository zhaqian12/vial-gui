# SPDX-License-Identifier: GPL-2.0-or-later
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QSizePolicy, QGridLayout, QLabel, QSlider, \
    QComboBox, QColorDialog, QCheckBox, QSpacerItem

from basic_editor import BasicEditor
from clickable_label import ClickableLabel
from util import tr
from vial_device import VialKeyboard


class QmkRgblightEffect:

    def __init__(self, idx, name, color_picker):
        self.idx = idx
        self.name = name
        self.color_picker = color_picker


QMK_RGBLIGHT_EFFECTS = [
    QmkRgblightEffect(0, "关闭", False),
    QmkRgblightEffect(1, "静态单色", True),
    QmkRgblightEffect(2, "单色呼吸 1", True),
    QmkRgblightEffect(3, "单色呼吸 2", True),
    QmkRgblightEffect(4, "单色呼吸 3", True),
    QmkRgblightEffect(5, "单色呼吸 4", True),
    QmkRgblightEffect(6, "彩虹循环 1", False),
    QmkRgblightEffect(7, "彩虹循环 2", False),
    QmkRgblightEffect(8, "彩虹循环 3", False),
    QmkRgblightEffect(9, "彩虹漩涡 1", False),
    QmkRgblightEffect(10, "彩虹漩涡 2", False),
    QmkRgblightEffect(11, "彩虹漩涡 3", False),
    QmkRgblightEffect(12, "彩虹漩涡 4", False),
    QmkRgblightEffect(13, "彩虹漩涡 5", False),
    QmkRgblightEffect(14, "彩虹漩涡 6", False),
    QmkRgblightEffect(15, "蛇形灯效 1", True),
    QmkRgblightEffect(16, "蛇形灯效 2", True),
    QmkRgblightEffect(17, "蛇形灯效 3", True),
    QmkRgblightEffect(18, "蛇形灯效 4", True),
    QmkRgblightEffect(19, "蛇形灯效 5", True),
    QmkRgblightEffect(20, "蛇形灯效 6", True),
    QmkRgblightEffect(21, "霹雳游侠 1", True),
    QmkRgblightEffect(22, "霹雳游侠 2", True),
    QmkRgblightEffect(23, "霹雳游侠 3", True),
    QmkRgblightEffect(24, "圣诞灯效", True),
    QmkRgblightEffect(25, "静态渐变 1", True),
    QmkRgblightEffect(26, "静态渐变 2", True),
    QmkRgblightEffect(27, "静态渐变 3", True),
    QmkRgblightEffect(28, "静态渐变 4", True),
    QmkRgblightEffect(29, "静态渐变 5", True),
    QmkRgblightEffect(30, "静态渐变 6", True),
    QmkRgblightEffect(31, "静态渐变 7", True),
    QmkRgblightEffect(32, "静态渐变 8", True),
    QmkRgblightEffect(33, "静态渐变 9", True),
    QmkRgblightEffect(34, "静态渐变 10", True),
    QmkRgblightEffect(35, "灯光测试", True),
    QmkRgblightEffect(36, "交替灯效", True),
]


class VialRGBEffect:

    def __init__(self, idx, name):
        self.idx = idx
        self.name = name


VIALRGB_EFFECTS = [
    VialRGBEffect(0, "关闭"),
    VialRGBEffect(1, "Vial控制"),
    VialRGBEffect(2, "静态单色"),
    VialRGBEffect(3, "静态双色"),
    VialRGBEffect(4, "静态纵向渐变"),
    VialRGBEffect(5, "静态横向渐变"),
    VialRGBEffect(6, "单色呼吸"),
    VialRGBEffect(7, "背光横向滚动"),
    VialRGBEffect(8, "单色横向滚动"),
    VialRGBEffect(9, "背光风车"),
    VialRGBEffect(10, "单色风车"),
    VialRGBEffect(11, "背光螺旋"),
    VialRGBEffect(12, "单色螺旋"),
    VialRGBEffect(13, "彩虹循环"),
    VialRGBEffect(14, "横向彩虹"),
    VialRGBEffect(15, "纵向彩虹"),
    VialRGBEffect(16, "V型彩虹"),
    VialRGBEffect(17, "彩虹漩涡"),
    VialRGBEffect(18, "双重彩虹漩涡"),
    VialRGBEffect(19, "彩虹风车"),
    VialRGBEffect(20, "彩虹螺旋"),
    VialRGBEffect(21, "彩虹旋转 1"),
    VialRGBEffect(22, "彩虹旋转 2"),
    VialRGBEffect(23, "双重彩虹风车"),
    VialRGBEffect(24, "雨滴 1"),
    VialRGBEffect(25, "雨滴 2"),
    VialRGBEffect(26, "色相呼吸"),
    VialRGBEffect(27, "色相摇摆"),
    VialRGBEffect(28, "色相波浪"),
    VialRGBEffect(29, "按键热图"),
    VialRGBEffect(30, "雨滴下坠"),
    VialRGBEffect(31, "单色按键响应"),
    VialRGBEffect(32, "背光单色按键响应"),
    VialRGBEffect(33, "单色范围响应 1"),
    VialRGBEffect(34, "单色范围响应 2"),
    VialRGBEffect(35, "单色交叉响应 1"),
    VialRGBEffect(36, "单色交叉响应 2"),
    VialRGBEffect(37, "单色十字响应 1"),
    VialRGBEffect(38, "单色十字响应 2"),
    VialRGBEffect(39, "单色涟漪响应 1"),
    VialRGBEffect(40, "单色涟漪响应 2"),
    VialRGBEffect(41, "彩虹涟漪响应 1"),
    VialRGBEffect(42, "彩虹涟漪响应 2"),
    VialRGBEffect(43, "像素雨"),
    VialRGBEffect(44, "像素随机"),
    VialRGBEffect(45, "像素流"),
    VialRGBEffect(46, "彩虹按键响应"),
    VialRGBEffect(47, "循环背光风车"),
    VialRGBEffect(48, "循环风车"),
    VialRGBEffect(49, "循环背光螺旋"),
    VialRGBEffect(50, "循环螺旋"),
    VialRGBEffect(51, "循环横向滚动"),
    VialRGBEffect(52, "循环呼吸"),
    VialRGBEffect(53, "反向横向彩虹"),
    VialRGBEffect(54, "反向纵向彩虹"),
    VialRGBEffect(55, "彩虹涟漪"),
    VialRGBEffect(56, "双重彩虹涟漪"),
    VialRGBEffect(57, "循环涟漪响应"),
    VialRGBEffect(58, "循环交叉响应"),
    VialRGBEffect(59, "循环十字响应"),
    VialRGBEffect(60, "循环范围响应"),
    VialRGBEffect(61, "彩虹交叉响应"),
    VialRGBEffect(62, "彩虹十字响应"),
    VialRGBEffect(63, "彩虹范围响应"),
    VialRGBEffect(64, "彩虹像素随机"),
    VialRGBEffect(65, "循环蛇形灯效"),
    VialRGBEffect(66, "循环波形"),
    VialRGBEffect(67, "彩虹波形"),
    VialRGBEffect(68, "反向彩虹波形"),
]


class UnderglowRGBEffect:

    def __init__(self, idx, name):
        self.idx = idx
        self.name = name


UNDERGLOWRGB_EFFECTS = [
    UnderglowRGBEffect(0, "关闭"),
    UnderglowRGBEffect(1, "同步轴灯"),
    UnderglowRGBEffect(2, "单色呼吸"),
    UnderglowRGBEffect(3, "循环呼吸"),
    UnderglowRGBEffect(4, "循环横向滚动"),
    UnderglowRGBEffect(5, "循环风车"),
    UnderglowRGBEffect(6, "彩虹循环"),
    UnderglowRGBEffect(7, "横向彩虹"),
    UnderglowRGBEffect(8, "纵向彩虹"),
    UnderglowRGBEffect(9, "彩虹漩涡"),
    UnderglowRGBEffect(10, "彩虹涟漪"),
    UnderglowRGBEffect(11, "彩虹风车"),
    UnderglowRGBEffect(12, "彩虹螺旋"),
    UnderglowRGBEffect(13, "变速横向彩虹"),
    UnderglowRGBEffect(14, "变速彩虹风车"),
    UnderglowRGBEffect(15, "变速循环呼吸"),
    UnderglowRGBEffect(16, "变速彩虹螺旋"),
    UnderglowRGBEffect(17, "变速彩虹涟漪"),
]


class IndicatorRGBEffect:
    
    def __init__(self, idx, name):
        self.idx = idx
        self.name = name


INDICATORS_EFFECT = [
    IndicatorRGBEffect(0, "关闭"),
    IndicatorRGBEffect(1, "静态单色"),
    IndicatorRGBEffect(2, "单色呼吸"),
    IndicatorRGBEffect(3, "循环呼吸"),
    IndicatorRGBEffect(4, "彩虹循环"),
]


class BasicHandler(QObject):

    update = pyqtSignal()

    def __init__(self, container):
        super().__init__()
        self.device = self.keyboard = None
        self.widgets = []

    def set_device(self, device):
        self.device = device
        if self.valid():
            self.keyboard = self.device.keyboard
            self.show()
        else:
            self.hide()

    def show(self):
        for w in self.widgets:
            w.show()

    def hide(self):
        for w in self.widgets:
            w.hide()

    def block_signals(self):
        for w in self.widgets:
            w.blockSignals(True)

    def unblock_signals(self):
        for w in self.widgets:
            w.blockSignals(False)

    def update_from_keyboard(self):
        raise NotImplementedError

    def valid(self):
        raise NotImplementedError


class QmkRgblightHandler(BasicHandler):

    def __init__(self, container):
        super().__init__(container)

        row = container.rowCount()
        
        self.lbl_underglow_effect = QLabel(tr("RGBConfigurator", "底灯灯效"))
        container.addWidget(self.lbl_underglow_effect, row, 0)
        self.underglow_effect = QComboBox()
        for ef in QMK_RGBLIGHT_EFFECTS:
            self.underglow_effect.addItem(ef.name)
        container.addWidget(self.underglow_effect, row, 1)

        self.lbl_underglow_brightness = QLabel(tr("RGBConfigurator", "底灯亮度"))
        container.addWidget(self.lbl_underglow_brightness, row + 1, 0)
        self.underglow_brightness = QSlider(QtCore.Qt.Horizontal)
        self.underglow_brightness.setMinimum(0)
        self.underglow_brightness.setMaximum(255)
        self.underglow_brightness.valueChanged.connect(self.on_underglow_brightness_changed)
        container.addWidget(self.underglow_brightness, row + 1, 1)

        self.lbl_underglow_color = QLabel(tr("RGBConfigurator", "底灯颜色"))
        container.addWidget(self.lbl_underglow_color, row + 2, 0)
        self.underglow_color = ClickableLabel(" ")
        self.underglow_color.clicked.connect(self.on_underglow_color)
        container.addWidget(self.underglow_color, row + 2, 1)

        self.underglow_effect.currentIndexChanged.connect(self.on_underglow_effect_changed)

        self.widgets = [self.lbl_underglow_effect, self.underglow_effect, self.lbl_underglow_brightness,
                        self.underglow_brightness, self.lbl_underglow_color, self.underglow_color]

    def update_from_keyboard(self):
        if not self.valid():
            return

        self.underglow_brightness.setValue(self.device.keyboard.underglow_brightness)
        self.underglow_effect.setCurrentIndex(self.device.keyboard.underglow_effect)
        self.underglow_color.setStyleSheet("QWidget { background-color: %s}" % self.current_color().name())

    def valid(self):
        return isinstance(self.device, VialKeyboard) and self.device.keyboard.lighting_qmk_rgblight

    def on_underglow_brightness_changed(self, value):
        self.device.keyboard.set_qmk_rgblight_brightness(value)
        self.update.emit()

    def on_underglow_effect_changed(self, index):
        self.lbl_underglow_color.setVisible(QMK_RGBLIGHT_EFFECTS[index].color_picker)
        self.underglow_color.setVisible(QMK_RGBLIGHT_EFFECTS[index].color_picker)

        self.device.keyboard.set_qmk_rgblight_effect(index)

    def on_underglow_color(self):
        color = QColorDialog.getColor(self.current_color())
        if not color.isValid():
            return
        self.underglow_color.setStyleSheet("QWidget { background-color: %s}" % color.name())
        h, s, v, a = color.getHsvF()
        if h < 0:
            h = 0
        self.device.keyboard.set_qmk_rgblight_color(int(255 * h), int(255 * s), int(255 * v))
        self.update.emit()

    def current_color(self):
        return QColor.fromHsvF(self.device.keyboard.underglow_color[0] / 255.0,
                               self.device.keyboard.underglow_color[1] / 255.0,
                               self.device.keyboard.underglow_brightness / 255.0)


class QmkBacklightHandler(BasicHandler):

    def __init__(self, container):
        super().__init__(container)

        row = container.rowCount()

        self.lbl_backlight_brightness = QLabel(tr("RGBConfigurator", "背光亮度"))
        container.addWidget(self.lbl_backlight_brightness, row, 0)
        self.backlight_brightness = QSlider(QtCore.Qt.Horizontal)
        self.backlight_brightness.setMinimum(0)
        self.backlight_brightness.setMaximum(255)
        self.backlight_brightness.valueChanged.connect(self.on_backlight_brightness_changed)
        container.addWidget(self.backlight_brightness, row, 1)

        self.lbl_backlight_breathing = QLabel(tr("RGBConfigurator", "背光呼吸"))
        container.addWidget(self.lbl_backlight_breathing, row + 1, 0)
        self.backlight_breathing = QCheckBox()
        self.backlight_breathing.stateChanged.connect(self.on_backlight_breathing_changed)
        container.addWidget(self.backlight_breathing, row + 1, 1)

        self.widgets = [self.lbl_backlight_brightness, self.backlight_brightness, self.lbl_backlight_breathing,
                        self.backlight_breathing]

    def update_from_keyboard(self):
        if not self.valid():
            return

        self.backlight_brightness.setValue(self.device.keyboard.backlight_brightness)
        self.backlight_breathing.setChecked(self.device.keyboard.backlight_effect == 1)

    def valid(self):
        return isinstance(self.device, VialKeyboard) and self.device.keyboard.lighting_qmk_backlight

    def on_backlight_brightness_changed(self, value):
        self.device.keyboard.set_qmk_backlight_brightness(value)

    def on_backlight_breathing_changed(self, checked):
        self.device.keyboard.set_qmk_backlight_effect(int(checked))


class VialRGBHandler(BasicHandler):

    def __init__(self, container):
        super().__init__(container)

        row = container.rowCount()

        self.lbl_rgb_title = QLabel(tr("RGBConfigurator", "全局灯光设置"))
        container.addWidget(self.lbl_rgb_title, row, 0)

        self.lbl_rgb_effect = QLabel(tr("RGBConfigurator", "灯光效果"))
        container.addWidget(self.lbl_rgb_effect, row + 1, 0)
        self.rgb_effect = QComboBox()
        self.rgb_effect.addItem("0")
        self.rgb_effect.addItem("1")
        self.rgb_effect.addItem("2")
        self.rgb_effect.addItem("3")
        self.rgb_effect.currentIndexChanged.connect(self.on_rgb_effect_changed)
        container.addWidget(self.rgb_effect, row + 1, 1)

        self.lbl_rgb_color = QLabel(tr("RGBConfigurator", "灯光颜色"))
        container.addWidget(self.lbl_rgb_color, row + 2, 0)
        self.rgb_color = ClickableLabel(" ")
        self.rgb_color.clicked.connect(self.on_rgb_color)
        container.addWidget(self.rgb_color, row + 2, 1)

        self.lbl_rgb_brightness = QLabel(tr("RGBConfigurator", "灯光亮度"))
        container.addWidget(self.lbl_rgb_brightness, row + 3, 0)
        self.rgb_brightness = QSlider(QtCore.Qt.Horizontal)
        self.rgb_brightness.setMinimum(0)
        self.rgb_brightness.setMaximum(255)
        self.rgb_brightness.valueChanged.connect(self.on_rgb_brightness_changed)
        container.addWidget(self.rgb_brightness, row + 3, 1)

        self.lbl_rgb_speed = QLabel(tr("RGBConfigurator", "灯光速度"))
        container.addWidget(self.lbl_rgb_speed, row + 4, 0)
        self.rgb_speed = QSlider(QtCore.Qt.Horizontal)
        self.rgb_speed.setMinimum(0)
        self.rgb_speed.setMaximum(255)
        self.rgb_speed.valueChanged.connect(self.on_rgb_speed_changed)
        container.addWidget(self.rgb_speed, row + 4, 1)

        self.widgets = [self.lbl_rgb_title, self.lbl_rgb_effect, self.rgb_effect, self.lbl_rgb_brightness, self.rgb_brightness,
                        self.lbl_rgb_color, self.rgb_color, self.lbl_rgb_speed, self.rgb_speed]

        self.effects = []

    def on_rgb_brightness_changed(self, value):
        self.keyboard.set_vialrgb_brightness(value)

    def on_rgb_speed_changed(self, value):
        self.keyboard.set_vialrgb_speed(value)

    def on_rgb_effect_changed(self, index):
        self.keyboard.set_vialrgb_mode(self.effects[index].idx)

    def on_rgb_color(self):
        color = QColorDialog.getColor(self.current_color())
        if not color.isValid():
            return
        self.rgb_color.setStyleSheet("QWidget { background-color: %s}" % color.name())
        h, s, v, a = color.getHsvF()
        if h < 0:
            h = 0
        self.keyboard.set_vialrgb_color(int(255 * h), int(255 * s), self.keyboard.rgb_hsv[2])
        self.update.emit()

    def current_color(self):
        return QColor.fromHsvF(self.keyboard.rgb_hsv[0] / 255.0,
                               self.keyboard.rgb_hsv[1] / 255.0,
                               1.0)

    def rebuild_effects(self):
        self.effects = []
        for effect in VIALRGB_EFFECTS:
            if effect.idx in self.keyboard.rgb_supported_effects:
                self.effects.append(effect)

        self.rgb_effect.clear()
        for effect in self.effects:
            self.rgb_effect.addItem(effect.name)

    def update_from_keyboard(self):
        if not self.valid():
            return

        self.rebuild_effects()
        for x, effect in enumerate(self.effects):
            if effect.idx == self.keyboard.rgb_mode:
                self.rgb_effect.setCurrentIndex(x)
                break
        self.rgb_brightness.setMaximum(self.keyboard.rgb_maximum_brightness)
        self.rgb_brightness.setValue(self.keyboard.rgb_hsv[2])
        self.rgb_speed.setValue(self.keyboard.rgb_speed)
        self.rgb_color.setStyleSheet("QWidget { background-color: %s}" % self.current_color().name())

    def valid(self):
        return isinstance(self.device, VialKeyboard) and self.device.keyboard.lighting_vialrgb


class ControllerRGBHandler(BasicHandler):

    def __init__(self, container):
        super().__init__(container)

        row = container.rowCount()
        self.lbl_blank =  QLabel(tr("RGBConfigurator", "  "))
        container.addWidget(self.lbl_blank, row, 0)

        self.lbl_ctrl_rgb_title = QLabel(tr("RGBConfigurator", "灯光开关设置"))
        container.addWidget(self.lbl_ctrl_rgb_title, row + 1, 0)

        self.lbl_ctrl_rgb_key = QLabel(tr("RGBConfigurator", "轴灯开关"))
        container.addWidget(self.lbl_ctrl_rgb_key, row + 2, 0)
        self.cb_key_rgb_enable = QCheckBox()
        self.cb_key_rgb_enable.stateChanged.connect(self.on_key_rgb_changed)
        container.addWidget(self.cb_key_rgb_enable, row + 2, 1, QtCore.Qt.AlignHCenter)

        self.lbl_ctrl_rgb_underglow = QLabel(tr("RGBConfigurator", "底灯开关"))
        container.addWidget(self.lbl_ctrl_rgb_underglow, row + 3, 0)
        self.cb_ug_rgb_enable = QCheckBox()
        self.cb_ug_rgb_enable.stateChanged.connect(self.on_ug_rgb_changed)
        container.addWidget(self.cb_ug_rgb_enable, row + 3, 1, QtCore.Qt.AlignHCenter)

        self.widgets = [self.lbl_blank, self.lbl_ctrl_rgb_title, self.lbl_ctrl_rgb_key, self.cb_key_rgb_enable,
                        self.lbl_ctrl_rgb_underglow, self.cb_ug_rgb_enable]

    def on_key_rgb_changed(self, checked):
        if (checked):
            self.device.keyboard.set_key_rgb(1) 
        else:
            self.device.keyboard.set_key_rgb(0) 

    def on_ug_rgb_changed(self, checked):
        if (checked):
            self.device.keyboard.set_underglow_rgb(1) 
        else:
            self.device.keyboard.set_underglow_rgb(0) 


    def update_from_keyboard(self):
        if not self.valid():
            return

        self.cb_key_rgb_enable.setChecked(self.device.keyboard.key_rgb_enable == 1)
        self.cb_ug_rgb_enable.setChecked(self.device.keyboard.underglow_rgb_enable == 1)

    def valid(self):
        return isinstance(self.device, VialKeyboard) and self.device.keyboard.rgb_matrix_control == "advanced"


class LogoRGBHandler(BasicHandler):
    
    def __init__(self, container):
        super().__init__(container)

        row = container.rowCount()

        self.lbl_ctrl_rgb_logo = QLabel(tr("RGBConfigurator", "LOGO灯开关"))
        container.addWidget(self.lbl_ctrl_rgb_logo, row, 0)
        self.logo_rgb_enable = QCheckBox()
        self.logo_rgb_enable.stateChanged.connect(self.on_logo_rgb_changed)
        container.addWidget(self.logo_rgb_enable, row, 1, QtCore.Qt.AlignHCenter)
        self.widgets = [self.lbl_ctrl_rgb_logo, self.logo_rgb_enable]

    def on_logo_rgb_changed(self, checked):
        if (checked):
            self.device.keyboard.set_logo_rgb(1) 
        else:
            self.device.keyboard.set_logo_rgb(0) 

    def update_from_keyboard(self):
        if not self.valid():
            return

        self.logo_rgb_enable.setChecked(self.device.keyboard.logo_rgb_enable == 1)

    def valid(self):
        return isinstance(self.device, VialKeyboard) and self.device.keyboard.rgb_matrix_control == "advanced" and self.device.keyboard.logo_rgb == True

class UnderglowRGBHandler(BasicHandler):

    def __init__(self, container):
        super().__init__(container)

        row = container.rowCount()
        self.lbl_blank =  QLabel(tr("RGBConfigurator", "  "))
        container.addWidget(self.lbl_blank, row, 0)

        self.lbl_ug_rgb_title = QLabel(tr("RGBConfigurator", "底灯灯光设置"))
        container.addWidget(self.lbl_ug_rgb_title, row + 1, 0)

        self.lbl_ug_rgb_effect = QLabel(tr("RGBConfigurator", "底灯效果"))
        container.addWidget(self.lbl_ug_rgb_effect, row + 2, 0)
        self.ug_rgb_effect = QComboBox()
        self.ug_rgb_effect.addItem("0")
        self.ug_rgb_effect.addItem("1")
        self.ug_rgb_effect.addItem("2")
        self.ug_rgb_effect.addItem("3")
        self.ug_rgb_effect.currentIndexChanged.connect(self.on_ug_rgb_effect_changed)
        container.addWidget(self.ug_rgb_effect, row + 2, 1)

        self.lbl_ug_rgb_color = QLabel(tr("RGBConfigurator", "底灯颜色"))
        container.addWidget(self.lbl_ug_rgb_color, row + 3, 0)
        self.ug_rgb_color = ClickableLabel(" ")
        self.ug_rgb_color.clicked.connect(self.on_ug_rgb_color)
        container.addWidget(self.ug_rgb_color, row + 3, 1)

        self.lbl_ug_rgb_brightness = QLabel(tr("RGBConfigurator", "底灯亮度"))
        container.addWidget(self.lbl_ug_rgb_brightness, row + 4, 0)
        self.ug_rgb_brightness = QSlider(QtCore.Qt.Horizontal)
        self.ug_rgb_brightness.setMinimum(0)
        self.ug_rgb_brightness.setMaximum(255)
        self.ug_rgb_brightness.valueChanged.connect(self.on_ug_rgb_brightness_changed)
        container.addWidget(self.ug_rgb_brightness, row + 4, 1)

        self.lbl_ug_rgb_speed = QLabel(tr("RGBConfigurator", "底灯速度"))
        container.addWidget(self.lbl_ug_rgb_speed, row + 5, 0)
        self.ug_rgb_speed = QSlider(QtCore.Qt.Horizontal)
        self.ug_rgb_speed.setMinimum(0)
        self.ug_rgb_speed.setMaximum(255)
        self.ug_rgb_speed.valueChanged.connect(self.on_ug_rgb_speed_changed)
        container.addWidget(self.ug_rgb_speed, row + 5, 1)

        self.widgets = [self.lbl_blank, self.lbl_ug_rgb_title, self.lbl_ug_rgb_effect, self.ug_rgb_effect, 
                        self.lbl_ug_rgb_brightness, self.ug_rgb_brightness,
                        self.lbl_ug_rgb_color, self.ug_rgb_color, self.lbl_ug_rgb_speed, self.ug_rgb_speed]

        self.ug_effects = []

    def on_ug_rgb_brightness_changed(self, value):
        self.keyboard.set_ugrgb_brightness(value)

    def on_ug_rgb_speed_changed(self, value):
        self.keyboard.set_ugrgb_speed(value)

    def on_ug_rgb_effect_changed(self, index):
        self.keyboard.set_ugrgb_mode(self.ug_effects[index].idx)

    def on_ug_rgb_color(self):
        color = QColorDialog.getColor(self.current_color())
        if not color.isValid():
            return
        self.ug_rgb_color.setStyleSheet("QWidget { background-color: %s}" % color.name())
        h, s, v, a = color.getHsvF()
        if h < 0:
            h = 0
        self.keyboard.set_ugrgb_color(int(255 * h), int(255 * s), self.keyboard.ug_rgb_hsv[2])
        self.update.emit()

    def current_color(self):
        return QColor.fromHsvF(self.keyboard.ug_rgb_hsv[0] / 255.0,
                               self.keyboard.ug_rgb_hsv[1] / 255.0,
                               1.0)

    def rebuild_effects(self):
        self.ug_effects = []
        for effect in UNDERGLOWRGB_EFFECTS:
            if effect.idx in self.keyboard.ug_rgb_supported_effects:
                self.ug_effects.append(effect)

        self.ug_rgb_effect.clear()
        for effect in self.ug_effects:
            self.ug_rgb_effect.addItem(effect.name)

    def update_from_keyboard(self):
        if not self.valid():
            return

        self.rebuild_effects()
        for x, effect in enumerate(self.ug_effects):
            if effect.idx == self.keyboard.ug_rgb_mode:
                self.ug_rgb_effect.setCurrentIndex(x)
                break
        self.ug_rgb_brightness.setMaximum(self.keyboard.ug_rgb_maximum_brightness)
        self.ug_rgb_brightness.setValue(self.keyboard.ug_rgb_hsv[2])
        self.ug_rgb_speed.setValue(self.keyboard.ug_rgb_speed)
        self.ug_rgb_color.setStyleSheet("QWidget { background-color: %s}" % self.current_color().name())

    def valid(self):
        return isinstance(self.device, VialKeyboard) and self.device.keyboard.underglow_rgb_matrix == "advanced"


class IndicatorsRGBHandler(BasicHandler):

    def __init__(self, container, row):
        super().__init__(container)

        self.lbl_blank = QLabel(tr("RGBConfigurator", "      "))
        # container.addWidget(self.lbl_blank, row, 2)
        spacerItem = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Fixed)
        container.addWidget(spacerItem, row, 2)

        self.lbl_ind_rgb_title = QLabel(tr("RGBConfigurator", "指示灯灯光设置"))
        container.addWidget(self.lbl_ind_rgb_title, row, 3)

        self.lbl_caps_lock = QLabel(tr("RGBConfigurator", "Caps Lock 指示灯"))
        container.addWidget(self.lbl_caps_lock, row + 1, 3)

        self.lbl_caps_led = QLabel(tr("RGBConfigurator", "Caps Lock LED"))
        container.addWidget(self.lbl_caps_led, row + 2, 3)
        self.caps_led = QComboBox()
        self.caps_led.addItem("LED0")
        self.caps_led.addItem("LED1")
        self.caps_led.addItem("LED2")
        self.caps_led.addItem("LED3")
        # self.caps_led.currentIndexChanged.connect(self.on_caps_led_changed)
        container.addWidget(self.caps_led, row + 2, 4)

        self.lbl_caps_color = QLabel(tr("RGBConfigurator", "Caps Lock 颜色"))
        container.addWidget(self.lbl_caps_color, row + 3, 3)
        self.caps_color = ClickableLabel(" ")
        # self.caps_color.clicked.connect(self.on_caps_color)
        container.addWidget(self.caps_color, row + 3, 4)

        self.lbl_caps_effect = QLabel(tr("RGBConfigurator", "Caps Lock 灯效"))
        container.addWidget(self.lbl_caps_effect, row + 4, 3)
        self.caps_effect = QComboBox()
        self.caps_effect.addItem("0")
        self.caps_effect.addItem("1")
        self.caps_effect.addItem("2")
        self.caps_effect.addItem("3")
        # self.caps_effect.currentIndexChanged.connect(self.on_caps_effect_changed)
        container.addWidget(self.caps_effect, row + 4, 4)

        container.addWidget(self.lbl_blank, row + 5, 3)

        self.lbl_num_lock = QLabel(tr("RGBConfigurator", "Num Lock 指示灯"))
        container.addWidget(self.lbl_num_lock, row + 6, 3)

        self.lbl_num_led = QLabel(tr("RGBConfigurator", "Num Lock LED"))
        container.addWidget(self.lbl_num_led, row + 7, 3)
        self.num_led = QComboBox()
        self.num_led.addItem("LED0")
        self.num_led.addItem("LED1")
        self.num_led.addItem("LED2")
        self.num_led.addItem("LED3")
        # self.num_led.currentIndexChanged.connect(self.on_num_led_changed)
        container.addWidget(self.num_led, row + 7, 4)

        self.lbl_num_color = QLabel(tr("RGBConfigurator", "Num Lock 颜色"))
        container.addWidget(self.lbl_num_color, row + 8, 3)
        self.num_color = ClickableLabel(" ")
        # self.num_color.clicked.connect(self.on_num_color)
        container.addWidget(self.num_color, row + 8, 4)

        self.lbl_num_effect = QLabel(tr("RGBConfigurator", "Num Lock 灯效"))
        container.addWidget(self.lbl_num_effect, row + 9, 3)
        self.num_effect = QComboBox()
        self.num_effect.addItem("0")
        self.num_effect.addItem("1")
        self.num_effect.addItem("2")
        self.num_effect.addItem("3")
        # self.num_effect.currentIndexChanged.connect(self.on_num_effect_changed)
        container.addWidget(self.num_effect, row + 9, 4)

        container.addWidget(self.lbl_blank, row + 10, 3)
        self.lbl_scroll_lock = QLabel(tr("RGBConfigurator", "Scroll Lock 指示灯"))
        container.addWidget(self.lbl_scroll_lock, row + 11, 3)
        
        self.lbl_scroll_led = QLabel(tr("RGBConfigurator", "Scroll Lock LED"))
        container.addWidget(self.lbl_scroll_led, row + 12, 3)
        self.scroll_led = QComboBox()
        self.scroll_led.addItem("LED0")
        self.scroll_led.addItem("LED1")
        self.scroll_led.addItem("LED2")
        self.scroll_led.addItem("LED3")
        # self.scroll_led.currentIndexChanged.connect(self.on_scroll_led_changed)
        container.addWidget(self.scroll_led, row + 12, 4)

        self.lbl_scroll_color = QLabel(tr("RGBConfigurator", "Scroll Lock 颜色"))
        container.addWidget(self.lbl_scroll_color, row + 13, 3)
        self.scroll_color = ClickableLabel(" ")
        # self.scroll_color.clicked.connect(self.on_scroll_color)
        container.addWidget(self.scroll_color, row + 13, 4)

        self.lbl_scroll_effect = QLabel(tr("RGBConfigurator", "Scroll Lock 灯效"))
        container.addWidget(self.lbl_scroll_effect, row + 14, 3)
        self.scroll_effect = QComboBox()
        self.scroll_effect.addItem("0")
        self.scroll_effect.addItem("1")
        self.scroll_effect.addItem("2")
        self.scroll_effect.addItem("3")
        # self.scroll_effect.currentIndexChanged.connect(self.on_scroll_effect_changed)
        container.addWidget(self.scroll_effect, row + 14, 4)

        self.widgets = [self.lbl_blank, self.lbl_ind_rgb_title, self.lbl_caps_lock, self.lbl_caps_led, self.caps_led, 
                        self.lbl_caps_color, self.caps_color, self.lbl_caps_effect, self.caps_effect, self.lbl_num_lock, 
                        self.lbl_num_led, self.num_led, self.lbl_num_color, self.num_color, self.lbl_num_effect, 
                        self.num_effect, self.lbl_scroll_lock, self.lbl_scroll_led, self.scroll_led, self.lbl_scroll_color, 
                        self.scroll_color, self.lbl_scroll_effect, self.scroll_effect]

        self.ug_effects = []



    def current_color(self):
        return QColor.fromHsvF(self.keyboard.ug_rgb_hsv[0] / 255.0,
                               self.keyboard.ug_rgb_hsv[1] / 255.0,
                               1.0)


    def update_from_keyboard(self):
        if not self.valid():
            return


    def valid(self):
        return isinstance(self.device, VialKeyboard) and self.device.keyboard.rgb_indicators


class RGBConfigurator(BasicEditor):

    def __init__(self):
        super().__init__()

        self.addStretch()

        w = QWidget()
        w.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        self.container = QGridLayout()
        w.setLayout(self.container)
        self.addWidget(w)
        self.setAlignment(w, QtCore.Qt.AlignHCenter)
        self.handler_backlight = QmkBacklightHandler(self.container)
        self.handler_backlight.update.connect(self.update_from_keyboard)
        self.handler_rgblight = QmkRgblightHandler(self.container)
        self.handler_rgblight.update.connect(self.update_from_keyboard)
        row = self.container.rowCount()
        self.handler_vialrgb = VialRGBHandler(self.container)
        self.handler_vialrgb.update.connect(self.update_from_keyboard)
        self.handler_rgb_controller = ControllerRGBHandler(self.container)
        self.handler_rgb_controller.update.connect(self.update_from_keyboard)
        self.handler_logo_rgb = LogoRGBHandler(self.container)
        self.handler_logo_rgb.update.connect(self.update_from_keyboard)
        self.handler_underglowlrgb = UnderglowRGBHandler(self.container)
        self.handler_underglowlrgb.update.connect(self.update_from_keyboard)
        self.handler_rgb_indicator = IndicatorsRGBHandler(self.container, row)
        self.handler_rgb_indicator.update.connect(self.update_from_keyboard)
        self.handlers = [self.handler_backlight, self.handler_rgblight, self.handler_vialrgb, self.handler_rgb_controller, self.handler_logo_rgb, self.handler_underglowlrgb, self.handler_rgb_indicator]

        self.addStretch()
        buttons = QHBoxLayout()
        buttons.addStretch()
        save_btn = QPushButton(tr("RGBConfigurator", "保存"))
        buttons.addWidget(save_btn)
        save_btn.clicked.connect(self.on_save)
        self.addLayout(buttons)

    def on_save(self):
        self.device.keyboard.save_rgb()

    def valid(self):
        return isinstance(self.device, VialKeyboard) and \
               (self.device.keyboard.lighting_qmk_rgblight or self.device.keyboard.lighting_qmk_backlight
                or self.device.keyboard.lighting_vialrgb or self.device.keyboard.underglow_rgb_matrix == "advanced"
                or self.device.keyboard.rgb_matrix_control == "advanced")

    def block_signals(self):
        for h in self.handlers:
            h.block_signals()

    def unblock_signals(self):
        for h in self.handlers:
            h.unblock_signals()

    def update_from_keyboard(self):
        self.device.keyboard.reload_rgb()

        self.block_signals()

        for h in self.handlers:
            h.update_from_keyboard()

        self.unblock_signals()

    def rebuild(self, device):
        super().rebuild(device)

        for h in self.handlers:
            h.set_device(device)

        if not self.valid():
            return

        self.update_from_keyboard()

# SPDX-License-Identifier: GPL-2.0-or-later
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QSizePolicy, QGridLayout, QLabel, QSlider, \
    QComboBox, QColorDialog, QCheckBox

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
    VialRGBEffect(39, "单色涟漪 1"),
    VialRGBEffect(40, "单色涟漪 2"),
    VialRGBEffect(41, "彩虹涟漪 1"),
    VialRGBEffect(42, "彩虹涟漪 2"),
    VialRGBEffect(43, "像素雨"),
    VialRGBEffect(44, "像素随机"),
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

        self.lbl_rgb_effect = QLabel(tr("RGBConfigurator", "灯光效果"))
        container.addWidget(self.lbl_rgb_effect, row, 0)
        self.rgb_effect = QComboBox()
        self.rgb_effect.addItem("0")
        self.rgb_effect.addItem("1")
        self.rgb_effect.addItem("2")
        self.rgb_effect.addItem("3")
        self.rgb_effect.currentIndexChanged.connect(self.on_rgb_effect_changed)
        container.addWidget(self.rgb_effect, row, 1)

        self.lbl_rgb_color = QLabel(tr("RGBConfigurator", "灯光颜色"))
        container.addWidget(self.lbl_rgb_color, row + 1, 0)
        self.rgb_color = ClickableLabel(" ")
        self.rgb_color.clicked.connect(self.on_rgb_color)
        container.addWidget(self.rgb_color, row + 1, 1)

        self.lbl_rgb_brightness = QLabel(tr("RGBConfigurator", "灯光亮度"))
        container.addWidget(self.lbl_rgb_brightness, row + 2, 0)
        self.rgb_brightness = QSlider(QtCore.Qt.Horizontal)
        self.rgb_brightness.setMinimum(0)
        self.rgb_brightness.setMaximum(255)
        self.rgb_brightness.valueChanged.connect(self.on_rgb_brightness_changed)
        container.addWidget(self.rgb_brightness, row + 2, 1)

        self.lbl_rgb_speed = QLabel(tr("RGBConfigurator", "灯光速度"))
        container.addWidget(self.lbl_rgb_speed, row + 3, 0)
        self.rgb_speed = QSlider(QtCore.Qt.Horizontal)
        self.rgb_speed.setMinimum(0)
        self.rgb_speed.setMaximum(255)
        self.rgb_speed.valueChanged.connect(self.on_rgb_speed_changed)
        container.addWidget(self.rgb_speed, row + 3, 1)

        self.widgets = [self.lbl_rgb_effect, self.rgb_effect, self.lbl_rgb_brightness, self.rgb_brightness,
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


class UnderglowRGBHandler(BasicHandler):

    def __init__(self, container):
        super().__init__(container)

        row = container.rowCount()

        self.lbl_ug_rgb_effect = QLabel(tr("RGBConfigurator", "底灯效果"))
        container.addWidget(self.lbl_ug_rgb_effect, row + 1, 0)
        self.ug_rgb_effect = QComboBox()
        self.ug_rgb_effect.addItem("0")
        self.ug_rgb_effect.addItem("1")
        self.ug_rgb_effect.addItem("2")
        self.ug_rgb_effect.addItem("3")
        self.ug_rgb_effect.currentIndexChanged.connect(self.on_rgb_effect_changed)
        container.addWidget(self.ug_rgb_effect, row + 1, 1)

        self.lbl_ug_rgb_color = QLabel(tr("RGBConfigurator", "底灯颜色"))
        container.addWidget(self.lbl_ug_rgb_color, row + 2, 0)
        self.ug_rgb_color = ClickableLabel(" ")
        self.ug_rgb_color.clicked.connect(self.on_rgb_color)
        container.addWidget(self.ug_rgb_color, row + 2, 1)

        self.lbl_ug_rgb_brightness = QLabel(tr("RGBConfigurator", "底灯亮度"))
        container.addWidget(self.lbl_ug_rgb_brightness, row + 3, 0)
        self.ug_rgb_brightness = QSlider(QtCore.Qt.Horizontal)
        self.ug_rgb_brightness.setMinimum(0)
        self.ug_rgb_brightness.setMaximum(255)
        self.ug_rgb_brightness.valueChanged.connect(self.on_rgb_brightness_changed)
        container.addWidget(self.ug_rgb_brightness, row + 3, 1)

        self.lbl_ug_rgb_speed = QLabel(tr("RGBConfigurator", "底灯速度"))
        container.addWidget(self.lbl_ug_rgb_speed, row + 4, 0)
        self.ug_rgb_speed = QSlider(QtCore.Qt.Horizontal)
        self.ug_rgb_speed.setMinimum(0)
        self.ug_rgb_speed.setMaximum(255)
        self.ug_rgb_speed.valueChanged.connect(self.on_rgb_speed_changed)
        container.addWidget(self.ug_rgb_speed, row + 4, 1)


        self.widgets = [self.lbl_ug_rgb_effect, self.ug_rgb_effect, self.lbl_ug_rgb_brightness, self.ug_rgb_brightness,
                        self.lbl_ug_rgb_color, self.ug_rgb_color, self.lbl_ug_rgb_speed, self.ug_rgb_speed]

        self.ug_effects = []

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
        self.ug_rgb_color.setStyleSheet("QWidget { background-color: %s}" % color.name())
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
        self.ug_effects = []
        for effect in VIALRGB_EFFECTS:
            if effect.idx in self.keyboard.rgb_supported_effects:
                self.ug_effects.append(effect)

        self.ug_rgb_effect.clear()
        for effect in self.ug_effects:
            self.ug_rgb_effect.addItem(effect.name)

    def update_from_keyboard(self):
        if not self.valid():
            return

        self.rebuild_effects()
        for x, effect in enumerate(self.ug_effects):
            if effect.idx == self.keyboard.rgb_mode:
                self.ug_rgb_effect.setCurrentIndex(x)
                break
        self.ug_rgb_brightness.setMaximum(self.keyboard.rgb_maximum_brightness)
        self.ug_rgb_brightness.setValue(self.keyboard.rgb_hsv[2])
        self.ug_rgb_speed.setValue(self.keyboard.rgb_speed)
        self.ug_rgb_color.setStyleSheet("QWidget { background-color: %s}" % self.current_color().name())

    def valid(self):
        return isinstance(self.device, VialKeyboard) and self.device.keyboard.underglow_rgb_matrix == "advanced"


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
        self.handler_vialrgb = VialRGBHandler(self.container)
        self.handler_vialrgb.update.connect(self.update_from_keyboard)
        self.handler_underglowlrgb = UnderglowRGBHandler(self.container)
        self.handler_underglowlrgb.update.connect(self.update_from_keyboard)
        self.handlers = [self.handler_backlight, self.handler_rgblight, self.handler_vialrgb, self.handler_underglowlrgb]

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
                or self.device.keyboard.lighting_vialrgb or self.device.keyboard.underglow_rgb_matrix == "advanced")

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

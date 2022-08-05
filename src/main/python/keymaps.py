from keycodes import Keycode
from keymap import danish, eurkey, french, german, hebrew, hungarian, latam, norwegian, russian, slovak, spanish, swedish, swiss

KEYMAPS = [
    ("QWERTY", dict()),
    ("丹麦(QWERTY)", danish.keymap),
    ("欧盟(QWERTY)", eurkey.keymap),
    ("法国(AZERTY)", french.keymap),
    ("德国(QWERTZ)", german.keymap),
    ("以色列(Standard)", hebrew.keymap),
    ("匈牙利(QWERTZ)", hungarian.keymap),
    ("拉丁美洲(QWERTY)", latam.keymap),
    ("挪威(QWERTY)", norwegian.keymap),
    ("俄罗斯(ЙЦУКЕН)", russian.keymap),
    ("斯洛伐克(QWERTY)", slovak.keymap),
    ("西班牙(QWERTY)", spanish.keymap),
    ("瑞典(QWERTY)", swedish.keymap),
    ("瑞士(QWERTZ)", swiss.keymap)
]

# make sure that qmk IDs we used are all correct
for name, keymap in KEYMAPS:
    for qmk_id in keymap.keys():
        if Keycode.find_by_qmk_id(qmk_id) is None:
            raise RuntimeError("Misconfigured - cannot find QMK keycode {}".format(qmk_id))

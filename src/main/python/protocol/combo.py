# SPDX-License-Identifier: GPL-2.0-or-later
import struct

from keycodes.keycodes import Keycode, RESET_KEYCODE
from protocol.base_protocol import BaseProtocol
from protocol.constants import CMD_VIA_VIAL_PREFIX, CMD_VIAL_DYNAMIC_ENTRY_OP, DYNAMIC_VIAL_COMBO_GET, \
    DYNAMIC_VIAL_COMBO_SET
from unlocker import Unlocker


class ProtocolCombo(BaseProtocol):

    def reload_combo(self):
        self.combo_entries = self._retrieve_dynamic_entries(DYNAMIC_VIAL_COMBO_GET,
                                                            self.combo_count, "<HHHHH")
        for x, entry in enumerate(self.combo_entries):
            self.combo_entries[x] = (Keycode.serialize(entry[0]), Keycode.serialize(entry[1]),
                                     Keycode.serialize(entry[2]), Keycode.serialize(entry[3]),
                                     Keycode.serialize(entry[4]))

    def combo_get(self, idx):
        return self.combo_entries[idx]

    def combo_set(self, idx, entry):
        if self.combo_entries[idx] == entry:
            return
        # for the replacement key
        if entry[-1] == RESET_KEYCODE:
            Unlocker.unlock(self)
        self.combo_entries[idx] = entry
        entry = [Keycode.deserialize(entry[0]), Keycode.deserialize(entry[1]), Keycode.deserialize(entry[2]),
                 Keycode.deserialize(entry[3]), Keycode.deserialize(entry[4])]
        serialized = struct.pack("<HHHHH", *entry)
        self.usb_send(self.dev, struct.pack("BBBB", CMD_VIA_VIAL_PREFIX, CMD_VIAL_DYNAMIC_ENTRY_OP,
                                            DYNAMIC_VIAL_COMBO_SET, idx) + serialized, retries=20)

    def save_combo(self):
        combo = []
        for entry in self.combo_entries:
            combo.append((entry[0], entry[1], entry[2], entry[3], entry[4]))
        return combo

    def restore_combo(self, data):
        for x, e in enumerate(data):
            if x < self.combo_count:
                self.combo_set(x, e)

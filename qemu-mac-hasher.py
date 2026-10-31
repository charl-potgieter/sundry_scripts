#!/usr/bin/env python
# usage: qemu-mac-hasher.py <VMName>

# Below script assists in assigning QEMU virtual machine with a unique
# link-levl adddress
# https://wiki.archlinux.org/title/QEMU#Link-level_address_caveat

import sys
import zlib

crc = str(hex(zlib.crc32(sys.argv[1].encode("utf-8")))).replace("x", "")[-8:]
print("52:54:%s%s:%s%s:%s%s:%s%s" % tuple(crc))

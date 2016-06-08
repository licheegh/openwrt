#!/usr/bin/python
import binascii

offset = 4
f = open('/lib/firmware/mt7628.eeprom','rb')
f.seek(offset)
d = f.read(6)
print "Original mac address:" + binascii.hexlify(d)
f.close()

indata = raw_input("input mac last two digit address: ")
indatahex = binascii.unhexlify(indata)
print "your input: " + binascii.hexlify(indatahex)
print len(indata)

f = open('/lib/firmware/mt7628.eeprom','rb+')
f.seek(offset + 4)
f.write(indatahex)
f.close()

print "done, a restart is required"

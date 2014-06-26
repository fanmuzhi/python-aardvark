import pyaardvark

a = pyaardvark.open()
data = a.i2c_master_read(0x53, 256)
print(' '.join('%02x' % ord(c) for c in data))
# data = '\x00\x01\x02\x03\x04'
a.close()
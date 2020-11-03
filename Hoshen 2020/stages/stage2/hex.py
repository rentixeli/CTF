hex_string = "0x666c61677b4d6f6164696d204c6573696d6368617d"[2:]
bytes_object = bytes.fromhex(hex_string)
ascii_string = bytes_object.decode("ASCII")
print("Flag is: ", ascii_string)

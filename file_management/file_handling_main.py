sai = open("file_handaling.py", "r")
kiran = sai.read()
print(kiran)
sai.close()

print("\n now write")

sai_w = open("file_handaling.py", "w")
sai_w.write("sai is awosome")
sai_w.close()

sai_w = open("file_handaling.py", "r")
print(sai_w.read())
""" this will print:
sai is beautiful

 now write
sai is beautiful
"""

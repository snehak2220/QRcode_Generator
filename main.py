import qrcode

qr=qrcode.make("Follow @sneha")
qr.save("my_qrcode.png")
print("QR code generated and saved as png")
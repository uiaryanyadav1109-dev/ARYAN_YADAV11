import qrcode
url=input("Enter Your URL Here:").strip()
file_path="C:\\Users\\DIPAK PC\\DESKTOP\\YOUR_NAME.png"

qr = qrcode.QRCode(version=1,box_size=10,border=5) #qrcode code size

qr.add_data(url)
qr.make(fit=True)
img = qr.make_image(fill_color="RED", back_color="BLACK")
img.save(file_path)
print("QR_CODE GENERATED SUCCESSFULLY")
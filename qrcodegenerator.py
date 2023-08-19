import qrcode
import image
qr=qrcode.QRCode(
    version = 15,
    box_size = 10,
    border = 5
)

data = "https://www.youtube.com/channel/UCBLke_hG2PP6vrlJl5bMQOg"

qr.add_data(data)
qr.make(fit = True)
image = qr.make_image(fill = "black", back_color ="white")
image.save("test.png")
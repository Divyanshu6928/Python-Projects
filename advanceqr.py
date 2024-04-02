import qrcode
import PIL
from PIL import Image

qr = qrcode.QRCode(version = 1, error_connection = qrcode.constants.ERROR_CORRECT_H,box_size =10,border=4)
qr.add_data("https://zebronics.vercel.app/")
qr.make(fit=True)
img = qrcode.make_image(fill_color="yellow",back_color="black")
img.save("Clone.png")
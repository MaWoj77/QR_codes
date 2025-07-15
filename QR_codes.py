import os
import qrcode

img = qrcode.make("https://www.linkedin.com/in/maria-wojewoda/")

img.save("LinkedIn_qr.png", "PNG")
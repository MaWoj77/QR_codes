import os
import qrcode

img_linkedin = qrcode.make("https://www.linkedin.com/in/maria-wojewoda/")
img_github = qrcode.make("https://github.com/MaWoj77")

img_linkedin.save("LinkedIn_qr.png", "PNG")
img_github.save("GitHub_qr.png", "PNG")
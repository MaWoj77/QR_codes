import os
import qrcode

folder_name = "qr_images"

folder_path = os.path.join(os.getcwd(), folder_name)

if not os.path.exists(folder_path):
    os.makedirs(folder_path)

img_linkedin = qrcode.make("https://www.linkedin.com/in/maria-wojewoda/")
img_github = qrcode.make("https://github.com/MaWoj77")

img_linkedin.save(os.path.join(folder_name, "LinkedIn_qr.png"), "PNG")
img_github.save(os.path.join(folder_name, "GitHub_qr.png"), "PNG")

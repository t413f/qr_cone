import base64
import qrcode
from typing import Optional

class QR_manager():

    @classmethod
    async def create_code(cls, content: str, colored: str):
        QR_manager.create_simple_qr(content=content, colored=colored)
        pass

    @classmethod
    def create_simple_qr(cls, content: str, colored: str) -> None:
        qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
        qr.add_data(content)
        img = qrcode.QRCode.make_image(qr, fill_color=colored, back_color="White").convert("RGB")
        img.save('test.png')

    @classmethod
    async def base64_from_img(cls) -> bytes:
        with open('test.png', 'rb') as i:
            return base64.encodebytes(i.read())

    @classmethod
    async def image_from_base64(cls, inp: bytes) -> None:
        with open('output.png', 'wb') as f:
            f.write(base64.decodebytes(inp))

QR_manager.create_simple_qr('google.com', '#ffffff')
import io
from Histogram import Histogram
from Bit_Counter import BitCounter
import base64
from PIL import Image


class Converter:
    jpg_file_byte = str
    jpg_file_str_byte = str
    jpg_file = Image
    bytes = io.BytesIO()

    def __init__(self, track):
        with open(track, 'rb') as f:
            self.jpg_file_byte = self.bytes.read()
            self.jpg_file_str_byte = base64.b64encode(f.read())
        f.closed

    def convert2image(self, byte, track):
        with open(track, 'wb') as f:
            f.write(byte)
        f.closed

    def print_image(self, track):
        self.jpg_file = Image.open(track)
        self.jpg_file.show()
        self.jpg_file.close()

    def print_bytes(self):
        print(self.jpg_file_str_byte)

    def get_n_byte(self, track, n):
        with open(track, 'rb') as f:
            try:
                f.seek(n)
                return f.read(1)
            finally:
                f.closed


img = Converter("image.jpg")
#img.convert2image(img.jpg_file_str_byte, "picture.jpg")
#img.print_image("image.jpg")
#img.print_bytes()
#print(img.get_n_byte("image.jpg", 2))
his_bit = BitCounter(img.jpg_file_byte)
his = Histogram(his_bit.list_of_zeros, '0')
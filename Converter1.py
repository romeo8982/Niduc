import io
from Histogram import  Histogram
from Bit_Counter import BitCounter
from PIL import Image


class Converter:

    jpg_file_str_byte = str
    jpg_file = Image
    bytes = io.BytesIO()

    def __init__(self, track):
        self.bytes = open(track, "rb")
        self.jpg_file_str_byte = self.bytes.read()
        self.bytes.close()

    def convert2image(self, byte, track):
        self.bytes = open(track, 'wb')
        self.bytes.write(byte)
        self.bytes.close()

    def print_image(self, track):
        self.jpg_file = Image.open(track)
        self.jpg_file.show()
        self.jpg_file.close()

    def print_bytes(self):
        print(self.jpg_file_str_byte)

    def get_n_byte(self, track, n):
        self.bytes = open(track, "rb")
        try:
            self.bytes.seek(n)
            return self.bytes.read(1)
        finally:
            self.bytes.close()


img = Converter("image.jpg")
#img.convert2image(img.jpg_file_str_byte, "picture.jpg")
#img.print_image("image.jpg")
#img.print_bytes()
#print(img.jpg_file)
#print(img.get_n_byte("image.jpg", 2))
#his_bit = BitCounter(img.jpg_file_str_byte)
#his = Histogram(his_bit.list_of_zeros, '0')
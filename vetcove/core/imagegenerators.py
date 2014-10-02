'''
lenghtgsa
'''

from imagekit import ImageSpec, register
from imagekit.processors import ResizeToFill

class PocketImage(ImageSpec):
    processors = [ResizeToFill(100, 50)]
    format = 'JPEG'
    options = {'quality': 60}

register.generator('vetcove:pocketimage', PocketImage)
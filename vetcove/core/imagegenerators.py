from imagekit import ImageSpec, register
from imagekit.processors import ResizeToFit

''' 
We are generating different image sizes for use across
our website. We stick to these image sizes to improve performance.
To call an image within a template, use the following code:
% generateimage 'vetcove:mediumthumbnail' source=image -- alt="alt text" class="class names" %
'''

class SmallThumbnail(ImageSpec):
    processors = [ResizeToFit(50, 50)]
    format = 'PNG'

register.generator('vetcove:smallthumbnail', SmallThumbnail)

class MediumThumbnail(ImageSpec):
    processors = [ResizeToFit(100, 100)]
    format = 'PNG'

register.generator('vetcove:mediumthumbnail', MediumThumbnail)

class LargeThumbnail(ImageSpec):
    processors = [ResizeToFit(200, 200)]
    format = 'PNG'

register.generator('vetcove:largethumbnail', LargeThumbnail)

class SmallImage(ImageSpec):
    processors = [ResizeToFit(300, 300)]
    format = 'PNG'

register.generator('vetcove:smallimage', SmallImage)

class MediumImage(ImageSpec):
    processors = [ResizeToFit(700, 700)]
    format = 'PNG'

register.generator('vetcove:mediumimage', MediumImage)

class LargeImage(ImageSpec):
    processors = [ResizeToFit(1200, 1200)]
    format = 'PNG'

register.generator('vetcove:largeimage', LargeImage)
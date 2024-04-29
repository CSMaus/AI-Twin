import mss
import cv2
import pytesseract
from PIL import Image


def capture_screen(region=None, monitor_index=1):
    """
    :param region: Optional. A dict specifying the 'top', 'left', 'width', and 'height' to capture.
    :param monitor_index: Optional. The index of the monitor to capture.
    """
    with mss.mss() as sct:
        if region:
            monitor = {**sct.monitors[monitor_index], **region}
        else:
            # whole monitor
            monitor = sct.monitors[monitor_index]

        sct_img = sct.grab(monitor)
        return Image.frombytes('RGB', (sct_img.width, sct_img.height), sct_img.rgb)


region = {'top': 250, 'left': 100, 'width': 200, 'height': 200}
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

with mss.mss() as sct:
    monitor_dims = sct.monitors[1:]
    top = monitor_dims[0]['top']
    left = monitor_dims[0]['left']
    width = monitor_dims[0]['width']
    height = monitor_dims[0]['height']

    # to read only description
    region['left'] = left
    region['top'] = top + height // 10
    region['width'] = width // 3
    region['height'] = height - height // 5

    region['left'] -= monitor_dims[0]['width']

# now take the image of the screen and define rect contours
current_img = capture_screen(region)
current_img.show()

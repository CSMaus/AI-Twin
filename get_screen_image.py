import mss
import numpy as np
from PIL import Image
import time
import pytesseract


def capture_screen(region=None, monitor_index=1):
    """
    :param region: Optional. A dict specifying the 'top', 'left', 'width', and 'height' to capture. if None - whole
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


def are_images_equal(img1, img2):
    if img1.size != img2.size:
        return False
    return np.array(img1).tobytes() == np.array(img2).tobytes()


def find_overlap(prev_text, new_text):
    """Find the longest overlapping substring between the end of prev_text and the start of new_text."""
    # Start from the full length of the shortest string and reduce until a match is found.
    max_overlap_len = min(len(prev_text), len(new_text))
    for i in range(max_overlap_len, 0, -1):
        # Check if the end of prev_text overlaps with the start of new_text.
        if prev_text[-i:] == new_text[:i]:
            return new_text[i:]
    return new_text


def filter_description_text(text):
    # if character '/n' is one - remove it
    # if character '/n' is more than one - remove all except one
    new_text = ''
    for i in range(len(text)):
        if text[i] == '\n':
            if i == 0 or i == len(text) - 1:
                continue
            if text[i - 1] != '\n' and text[i + 1] != '\n':
                new_text += ' '
                continue

            if text[i + 1] == '\n' and new_text[-1] != '\n':
                new_text += text[i]
                continue
        else:
            new_text += text[i]

    description_key = new_text.split('\n')[0]
    filtered_text = new_text[len(description_key):]
    return description_key, new_text


def save_description_text(text, key):

    # first, need to save previous text
    # if the key of the previous text is the same as current, then need to add new text to the previous text
    # if there is common part between end of prev text and start of the new one, then remove it in new text
    # if description key is different, then write previous text into file with the name of the key

    with open(f'{key}.txt', 'w') as file:
        file.write(text)


def main(isMultipleMonitors=True, timeout=1, dsOption=0):
    """
    isMultipleMonitors parameter for my personal settings, so adjust or use one monitor
    :param isMultipleMonitors: if there is 2 monitors, then we will take the lef one (which should be second)
    :param timeout: time between screen captures
    :param dsOption: option to define region: 0 - about character, 1 - archived dialogue, 2 - new dialogue
    :return:
    """
    previous_img = None
    region = {'top': 250, 'left': 100, 'width': 200, 'height': 200}

    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    # img_path = 'details1_1_en.jpg'
    # mg = Image.open(img_path)

    with mss.mss() as sct:
        monitor_dims = sct.monitors[1:]
        top = monitor_dims[0]['top']
        left = monitor_dims[0]['left']
        width = monitor_dims[0]['width']
        height = monitor_dims[0]['height']

        # to read only description
        region['left'] = width - width//3
        region['top'] = top + height//10
        region['width'] = width//3
        region['height'] = height - height//5

        # TODO: define region where will be dialog part: for archived and new dialogs

        # for key, value in monitor_dims[0].items():
        #     region[key] = value

        # if isMultipleMonitors:
        # region['left'] -= monitor_dims[0]['width']
    prev_text = ''
    prev_chapter = '_'
    while True:
        current_img = capture_screen(region)

        if previous_img is not None and are_images_equal(current_img, previous_img):
            print("No change detected.")
        else:
            # print("Change detected, process the image.")
            # display the image
            current_img.show()
            previous_img = current_img
            text = pytesseract.image_to_string(current_img, lang='rus')  # lang="jpn" "rus" "eng"
            chapter, filtered_text = filter_description_text(text)

            # first, need to save previous text
            # if the key of the previous text is the same as current, then need to add new text to the previous text
            # if there is common part between end of prev text and start of the new one, then remove it in new text
            # if description key is different, then write previous text into file with the name of the key

            # this idea with key is bad. Need to define it based on the selected section in the right side of the screen

            if len(prev_text) < 1:
                prev_text = filtered_text
                prev_chapter = chapter
            else:
                if prev_chapter == chapter:
                    # define the common text in the end of prev text and in the start of the new one and remove it in
                    # new current filtered_text
                    filtered_text = find_overlap(prev_text, filtered_text)
                    prev_text += filtered_text

                else:
                    save_description_text(prev_text, prev_chapter)
                    prev_text = filtered_text
                    prev_chapter = chapter

        # break
        time.sleep(timeout)


main(timeout=2)


# to create dataset need to define region where we take the image and recognize text
# if the image same, we will not make text recon and update recognized text

# 2. need to define time, after which we will start taking images
# 3. for each option define region: (0 - about character, 1 - archived dialogue, 2 - new dialogue)
# 4. Filter the text. Need to take parts of the text which are not repeated ( i e if we moved image, and part of the
# old text was also captured)
# 5.



# %%
# utils.py
import cv2
import numpy as np
from PIL import Image

def crop_and_resize(image, xyxy, size=(160,160)):
    # xyxy: (x1,y1,x2,y2)
    x1, y1, x2, y2 = [int(x) for x in xyxy]
    h, w = image.shape[:2]
    x1 = max(0, x1)
    y1 = max(0, y1)
    x2 = min(w-1, x2)
    y2 = min(h-1, y2)
    crop = image[y1:y2, x1:x2]
    if crop.size == 0:
        return None
    crop = cv2.resize(crop, size, interpolation=cv2.INTER_AREA)
    crop = cv2.cvtColor(crop, cv2.COLOR_BGR2RGB)
    return crop

def cv2_to_pil(image_bgr):
    image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
    return Image.fromarray(image_rgb)


# %%




import json
from datetime import datetime
from typing import Dict

import cv2
import numpy as np


def image_rotate(image: np.ndarray, degree: int):
    """
    * 이미지를 각도 별로 회전시킵니다.

    Args:
        * image (np.ndarray): 회전시킬 이미지
        * degree (int): 회전시킬 각도 (0, 90, 180, 270)

    Returns:
        * image (np.ndarray): degree에 맞춰 회전한 이미지
    """
    
    if degree == 0:
        return image
    elif degree == 90:
        return cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
    elif degree == 180:
        return cv2.rotate(image, cv2.ROTATE_180)
    elif degree == 270:
        return cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)

def get_now_time(form: str="%Y%m%dT%H%M%S") -> str:
    """
    * 현재 시간을 form 형식으로 반환합니다.

    Args:
        form (str, optional): 반환하려는 . Defaults to "%Y%m%dT%H%M%S".

    Returns:
        str: 현재 시간
    """  
    
    now = datetime.now()
    now_time = now.strftime(form)
    return now_time


def get_cam(cam_no: int=0, cam_width: int=1920, cam_height: int=1080) -> cv2.VideoCapture:
    """
    * cam 설정 후 반환합니다.

    Args:
        * cam_no (int, optional): OS에 등록된 Cam 번호. Defaults to 0.
            * common/find_cam.sh를 통해 cam 번호 확인 가능
        * cam_width (int, optional): 캠에 출력되는 화면 길이. Defaults to 1920.
        * cam_height (int, optional): 캠에 출력되는 화면 높이. Defaults to 1080.

    Returns:
        * cv2.VideoCapture
    """
    cam = cv2.VideoCapture(cam_no)
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, cam_width)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, cam_height)
    return cam

def read_json(src: str) -> Dict:
    """json 파일을 읽어 Dict 형태로 반환합니다.

    Args:
        src (str): json 파일 경로

    Returns:
        Dict
    """
    
    with open(src, "r", encoding="utf-8") as json_file:
        return json.load(json_file)

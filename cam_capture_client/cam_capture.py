import os

import cv2
import numpy as np
from fvcore.common.config import CfgNode as CN

from cam_capture_client.common import get_now_time, image_rotate, get_cam, Logger

class CamCapture:
    def __init__(self, cfg: CN):
        self.__save_width = cfg.CAPTURE.SAVE_WIDTH
        self.__save_height = cfg.CAPTURE.SAVE_HEIGHT
        
        self.__cam_width = cfg.CAPTURE.CAM_WIDTH
        self.__cam_height = cfg.CAPTURE.CAM_HEIGHT
        self.__cam_no = cfg.CAPTURE.CAM_NO
        self.__cam_rotate = cfg.CAPTURE.CAM_ROTATE
        self.__cam_name = cfg.CAPTURE.CAM_NAME
        self.__output_path = cfg.CAPTURE.OUTPUT_PATH
        self.__now = get_now_time()
        
        self.__image_path = os.path.join(self.__output_path, self.__now)
        os.makedirs(self.__image_path, exist_ok=True)
        
        self.__iter = 0

        self.__cap = get_cam(self.__cam_no, self.__save_width, self.__save_height)
        self.__logger = Logger(cfg)
        
        
    def __save_image(self, image: np.ndarray):
        path_save = os.path.join(self.__image_path, f"capture_{self.__now}_{self.__iter:06d}.png")
        cv2.imwrite(path_save, image)
        self.__logger.info(f"save image: {path_save}")
    
    
    def run(self):
        self.__logger.info("start capture")
        
        while True:
            ret, cam = self.__cap.read()
            
            if ret:
                cam_show = cv2.resize(cam, (self.__cam_width, self.__cam_height))
                cam_show = image_rotate(cam_show, self.__cam_rotate)
                cv2.imshow(self.__cam_name, cam_show)
                
                if cv2.waitKey(1) & 0xFF == ord("c"):
                    cam = image_rotate(cam, self.__cam_rotate)
                    self.__save_image(cam)
                    self.__iter += 1

                elif cv2.waitKey(1) & 0xFF == 27:
                    print("closed wait...")
                    break
            
        self.__cap.release()
        cv2.destroyAllWindows()
        
        self.__logger.info("end capture")
        
    def __call__(self):
        self.run()
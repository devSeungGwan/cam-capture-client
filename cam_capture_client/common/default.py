from fvcore.common.config import CfgNode as CN

_C = CN()
_C.CAPTURE = CN()
_C.CAPTURE.SAVE_WIDTH = 3264
_C.CAPTURE.SAVE_HEIGHT = 2448
_C.CAPTURE.CAM_WIDTH = 816
_C.CAPTURE.CAM_HEIGHT = 612
_C.CAPTURE.CAM_NO = 0
_C.CAPTURE.CAM_ROTATE = 0
_C.CAPTURE.CAM_NAME = "cam"
_C.CAPTURE.OUTPUT_PATH = "./outputs"

_C.CONTROL = CN()
_C.CONTROL.CAPTURE = "c"
_C.CONTROL.CLOSE = "esc"

_C.LOGGER = CN()
_C.LOGGER.NAME = "cam-capture"
_C.LOGGER.CONF_PATH = "./cam_capture_client/config/logger.json"

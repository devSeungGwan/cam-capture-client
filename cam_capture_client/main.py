from argparse import ArgumentParser

from cam_capture_client import CamCapture
from cam_capture_client.common import cfg

if __name__ == "__main__":
    parser = ArgumentParser()
    
    parser.add_argument("--config", type=str, default="./cam_capture_client/config/config.yaml", help="config file path")
    args = parser.parse_args()
    
    cfg.merge_from_file(args.config)
    client = CamCapture(cfg)
    client.run()
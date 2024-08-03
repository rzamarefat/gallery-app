from ultralytics import YOLO
import gdown
import os
import torch

class FaceDetector:
    def __init__(self):
        self._face_det_ckpt_path = os.path.join(os.getcwd(), "back", ".ckpts", "yolov8n-face.pt")

        if not(os.path.isfile(self._face_det_ckpt_path)):
            print("Downloading Face Detection Checkpoint ...")
            gdown.download(
                "https://drive.google.com/uc?id=10-iUQGoAkTaeahs-jC0W05G4qaspTF3N",
                self._sam2_model_path,
                quiet=False
            )

        try:
            self._face_det_model = YOLO(self._face_det_ckpt_path)
        except Exception as e:
            print(e)
            exit()


        self._device = torch.cuda.is_available()
    
    def __call__(self, img):
        res = self._face_det_model.predict(img, conf=0.3, verbose=False, device=self._device)
        boxes = res[0].boxes.xyxy.to("cpu").numpy().astype(int)
        return boxes
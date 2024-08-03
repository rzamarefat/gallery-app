from .FaceDetector import FaceDetector
from .TasksNames import TasksNames
from .adaface import AdaFace
import torch
import os

class Analyzer:
    def __init__(self) -> None:
        self._device = "cuda" if torch.cuda.is_available() else "cpu"
        os.makedirs(os.path.join(os.getcwd(), ".ckpts"), exist_ok=True)
        self._face_detector = FaceDetector(self._device)        
        self._generator_name = "ir_101_webface_12m"
        self._face_emb_gen = AdaFace(self._generator_name, self._device)

        """
        1. face detection and face alignement module
        2. face embedding generator
        3. image captioning module
        4. Text embedder model
        4. embedding database
        5. image database
        """

    def _add_to_gallery(self, image, description):
        face_detection_result = self._face_detector(image)
        face_data = self._face_emb_gen(face_detection_result)

        print(face_data)

        

    def __call__(self, data, task_name):
        image = data["image"]
        description = data["description"]

        if task_name == TasksNames.ADD_TO_GALLERY:
            self._add_to_gallery(image, description)
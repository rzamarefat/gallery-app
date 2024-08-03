from .FaceDetector import FaceDetector
from .TasksNames import TasksNames
from .Adaface import AdaFace
from .ImageCaptioner import ImageCaptioner
from .TextEmbedder import TextEmbedder
import torch
import os



class Analyzer:
    def __init__(self) -> None:
        self._device = "cuda" if torch.cuda.is_available() else "cpu"
        os.makedirs(os.path.join(os.getcwd(), ".ckpts"), exist_ok=True)
        self._face_detector = FaceDetector(self._device)        
        self._generator_name = "ir_101_webface_12m"
        self._face_emb_gen = AdaFace(self._generator_name, self._device)
        self._img_captioner = ImageCaptioner()
        self._text_embedder = TextEmbedder()

        

    def _add_to_gallery(self, image, description):
        face_detection_result = self._face_detector(image)
        face_data = self._face_emb_gen(face_detection_result)
        caption = self._img_captioner(image)
        caption_embedding = self._text_embedder(caption)
        print(caption_embedding)

        # print(face_data)
        # print(caption)

        

    def __call__(self, data, task_name):
        image = data["image"]
        description = data["description"]

        if task_name == TasksNames.ADD_TO_GALLERY:
            self._add_to_gallery(image, description)
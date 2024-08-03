from .FaceDetector import FaceDetector
from .TasksNames import TasksNames
from .Adaface import AdaFace
from .ImageCaptioner import ImageCaptioner
from .TextEmbedder import TextEmbedder
from .ElasticHandler import ElasticHandler
import torch
import os


class Analyzer:
    def __init__(self) -> None:
        self._device = "cuda" if torch.cuda.is_available() else "cpu"
        os.makedirs(os.path.join(os.getcwd(), ".ckpts"), exist_ok=True)
        self._face_detector = FaceDetector(self._device)        
        self._face_emb_gen = AdaFace(self._device)
        self._img_captioner = ImageCaptioner()
        self._text_embedder = TextEmbedder()
        self._elastic_handler = ElasticHandler()

        

    def _add_to_gallery(self, image, description):
        face_detection_result = self._face_detector(image)
        face_data = self._face_emb_gen(face_detection_result)
        caption = self._img_captioner(image)
        caption_embedding = self._text_embedder(caption)
        description_embedding = self._text_embedder(description)
        from uuid import uuid1
        random_name = str(uuid1)[0: 8]
        random_name = "sadasdasdasdassdasdad"
        self._elastic_handler.push_index(index_name=random_name, index_id=f"{random_name}", embedding=caption_embedding)
        print("Success")
        

    def __call__(self, data, task_name):
        image = data["image"]
        description = data["description"]

        if task_name == TasksNames.ADD_TO_GALLERY:
            self._add_to_gallery(image, description)
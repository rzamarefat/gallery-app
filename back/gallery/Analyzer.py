from .FaceDetector import FaceDetector
from .TasksNames import TasksNames
from .Adaface import AdaFace
from .ImageCaptioner import ImageCaptioner
from .TextEmbedder import TextEmbedder
from .ElasticHandler import ElasticHandler
import torch
import os
from uuid import uuid1
import base64
from PIL import Image
from io import BytesIO
import cv2
class Analyzer:
    def __init__(self) -> None:
        self._device = "cuda" if torch.cuda.is_available() else "cpu"
        os.makedirs(os.path.join(os.getcwd(), ".ckpts"), exist_ok=True)
        self._face_detector = FaceDetector(self._device)        
        self._face_emb_gen = AdaFace(self._device)
        self._img_captioner = ImageCaptioner()
        self._text_embedder = TextEmbedder()
        self._elastic_handler = ElasticHandler()
        

    @staticmethod
    def _encode_image(image):
        image = Image.fromarray(image)
        buffer = BytesIO()
        image.save(buffer, format='PNG')  
        image_data = buffer.getvalue()
        encoded_image = base64.b64encode(image_data)
        encoded_image_str = encoded_image.decode('utf-8')
        
        return encoded_image_str

        

    def _do_preprocessing(self, image, description):
        face_detection_result = self._face_detector(image)
        face_data = self._face_emb_gen(face_detection_result)
        
        
        caption = self._img_captioner(image)
        # caption_description_embedding = self._text_embedder(f"{caption} {description}")
        caption_description_embedding = [1, 2, 3]

        
        index_id = str(uuid1())[0: 8]
        data = {
                "id": index_id,
                "faces": [self._encode_image(f) for f in face_data["faces"]],
                "face_embs": [face_emb.detach().to("cpu").numpy().tolist() for face_emb in face_data["embs"]],
                "description_emb": caption_description_embedding
            }
        
        return data
        
        # self._elastic_handler.push_index(index_id=face_index_id, embedding=face_emb, mode="face")

        # self._elastic_handler.push_index(index_id=index_id, embedding=caption_description_embedding, mode="text")
        
        

    def __call__(self, data, task_name):
        image = data["image"]
        description = data["description"]

        if task_name == TasksNames.DO_PREPROCESSING:
            return self._do_preprocessing(image, description)
from .FaceDetector import FaceDetector
from .TasksNames import TasksNames

class Analyzer:
    def __init__(self) -> None:
        self._face_detector = FaceDetector()

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
        

    def __call__(self, data, task_name):
        image = data["image"]
        description = data["description"]

        if task_name == TasksNames.ADD_TO_GALLERY:
            self._add_to_gallery(image, description)
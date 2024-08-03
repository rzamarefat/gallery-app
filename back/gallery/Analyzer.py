from .FaceDetector import FaceDetector

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

    def __call__(self, task_name):
        pass
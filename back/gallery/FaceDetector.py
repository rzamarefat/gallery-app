from ultralytics import YOLO
import gdown
import os
from .face_alignment.mtcnn_pytorch.src.align_trans import warp_and_crop_face, get_reference_facial_points

class FaceDetector:
    def __init__(self, device):
        self._face_det_ckpt_path = os.path.join(os.getcwd(), ".ckpts", "yolov8n-face.pt")

        if not(os.path.isfile(self._face_det_ckpt_path)):
            print("Downloading Face Detection Checkpoint ...")
            gdown.download(
                "https://drive.google.com/uc?id=10-iUQGoAkTaeahs-jC0W05G4qaspTF3N",
                self._face_det_ckpt_path,
                quiet=False
            )

        try:
            self._face_det_model = YOLO(self._face_det_ckpt_path)
        except Exception as e:
            print(e)
            exit()


        self._device = device
    
    def _get_faces(sel, image, box, landmark):
        
        converted_landmarks = []
        for key in landmark:
            if len(key.xy.tolist()[0]) == 0:
                continue

            converted_landmarks.append([
                [int(key.xy.tolist()[0][0][0]), int(key.xy.tolist()[0][0][1])],
                [int(key.xy.tolist()[0][1][0]), int(key.xy.tolist()[0][1][1])],
                [int(key.xy.tolist()[0][2][0]), int(key.xy.tolist()[0][2][1])],
                [int(key.xy.tolist()[0][3][0]), int(key.xy.tolist()[0][3][1])],
                [int(key.xy.tolist()[0][4][0]), int(key.xy.tolist()[0][4][1])]
            ])
        

        reference_pts = get_reference_facial_points(default_square=True)
        try:
            face = warp_and_crop_face(image, converted_landmarks[0], reference_pts=reference_pts, align_type='smilarity')
        except:
            print("Error happend in YOLOLandmark")
            return None

        return face

    def _process_bboxes_n_landmakes(self, image, bounding_boxes, landmarks, find_largest_box=False):
        largest_area = 0
        largest_box = None
        result = {
            "xyxy_boxes": [],
            "faces": [],
            "landmarks":[]
        }
        for box, landmark in zip(bounding_boxes, landmarks):
                landmark_1 = (int(landmark.xy.tolist()[0][0][0]), int(landmark.xy.tolist()[0][0][1]))
                landmark_2 = (int(landmark.xy.tolist()[0][1][0]), int(landmark.xy.tolist()[0][1][1]))
                landmark_3 = (int(landmark.xy.tolist()[0][2][0]), int(landmark.xy.tolist()[0][2][1]))
                landmark_4 = (int(landmark.xy.tolist()[0][3][0]), int(landmark.xy.tolist()[0][3][1]))
                landmark_5 = (int(landmark.xy.tolist()[0][4][0]), int(landmark.xy.tolist()[0][4][1]))

                top_left_x = int(box.xyxy.tolist()[0][0])
                top_left_y = int(box.xyxy.tolist()[0][1])
                bottom_right_x = int(box.xyxy.tolist()[0][2])
                bottom_right_y = int(box.xyxy.tolist()[0][3])

                face = self._get_faces(image, box, landmark)


                if find_largest_box:
                    area = (bottom_right_x - top_left_x) * (bottom_right_y - top_left_y)

                    if area > largest_area:
                        largest_area = area
                    
                        result.__setitem__("biggest_xyxy", [top_left_x, top_left_y, bottom_right_x, bottom_right_y])
                        result.__setitem__("biggest_landmarks", [landmark_1, landmark_2, landmark_3, landmark_4, landmark_5])
                        result.__setitem__("biggest_face", face)

                result["xyxy_boxes"].append([top_left_x, top_left_y, bottom_right_x, bottom_right_y])
                result["landmarks"].append([top_left_x, top_left_y, bottom_right_x, bottom_right_y])
                result["faces"].append(face)

        return result
    
    def __call__(self, img):
        results = self._face_det_model.predict(img, device=self._device, verbose=False)
        boxes = results[0].boxes
        landmarks = results[0].keypoints

        if len(boxes) == 0:
            return None
        else:
            result = self._process_bboxes_n_landmakes(img, boxes, landmarks, find_largest_box=False)
            return result
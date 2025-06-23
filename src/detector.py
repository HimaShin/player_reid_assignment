# detector.py

from ultralytics import YOLO
import cv2

class PlayerDetector:
    def __init__(self, model_path='models/best.pt', confidence_threshold=0.4):
        self.model = YOLO(model_path)
        self.conf_threshold = confidence_threshold

    def detect_players(self, frame):
        """
        Runs detection on the given frame using YOLOv11.
        Returns list of detections: [x1, y1, x2, y2, confidence, class_id]
        """
        results = self.model(frame)[0]
        detections = []

        for box in results.boxes:
            cls_id = int(box.cls)
            if cls_id != 0:  # Skip if it's not a player class (assume class 0 = player)
                continue

            conf = float(box.conf)
            if conf < self.conf_threshold:
                continue

            x1, y1, x2, y2 = map(int, box.xyxy[0])
            detections.append([x1, y1, x2, y2, conf, cls_id])

        return detections

# tracker.py

import numpy as np
from scipy.spatial import distance

class PlayerTracker:
    def __init__(self, max_distance=50, max_frames_lost=30):
        self.next_id = 0
        self.players = {}  # id: {bbox, centroid, lost_frames}
        self.max_distance = max_distance
        self.max_frames_lost = max_frames_lost

    def _get_centroid(self, bbox):
        x1, y1, x2, y2 = bbox
        return ((x1 + x2) // 2, (y1 + y2) // 2)

    def update(self, detections):
        """
        detections: list of [x1, y1, x2, y2, conf, class_id]
        returns: list of (id, bbox)
        """
        new_centroids = [self._get_centroid(d[:4]) for d in detections]
        updated_players = {}
        assigned = set()

        # Match existing players to new detections
        for pid, pdata in self.players.items():
            prev_centroid = pdata["centroid"]
            distances = [distance.euclidean(prev_centroid, c) for c in new_centroids]
            
            if distances and min(distances) < self.max_distance:
                idx = distances.index(min(distances))
                if idx not in assigned:
                    assigned.add(idx)
                    updated_players[pid] = {
                        "bbox": detections[idx][:4],
                        "centroid": new_centroids[idx],
                        "lost_frames": 0
                    }

        # Add new players
        for i, det in enumerate(detections):
            if i in assigned:
                continue
            pid = self.next_id
            self.next_id += 1
            updated_players[pid] = {
                "bbox": det[:4],
                "centroid": new_centroids[i],
                "lost_frames": 0
            }

        # Increment lost_frames for unmatched
        for pid in self.players:
            if pid not in updated_players:
                pdata = self.players[pid]
                pdata["lost_frames"] += 1
                if pdata["lost_frames"] <= self.max_frames_lost:
                    updated_players[pid] = pdata  # keep tracking

        self.players = updated_players

        # Output list of (id, bbox)
        return [(pid, pdata["bbox"]) for pid, pdata in self.players.items()]

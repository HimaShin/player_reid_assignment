# main.py

import cv2
from detector import PlayerDetector
from tracker import PlayerTracker
import os
import pickle  # For saving tracking results

# Paths
VIDEO_PATH = "input/15sec_input_720p.mp4"
MODEL_PATH = "models/best.pt"
OUTPUT_VIDEO_PATH = "output/reid_output.mp4"
OUTPUT_DATA_PATH = "output/results.pkl"

# Initialize detector and tracker
detector = PlayerDetector(model_path=MODEL_PATH, confidence_threshold=0.4)
tracker = PlayerTracker(max_distance=50, max_frames_lost=30)

# Load video
cap = cv2.VideoCapture(VIDEO_PATH)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# Output video writer
os.makedirs("output", exist_ok=True)
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter(OUTPUT_VIDEO_PATH, fourcc, fps, (width, height))

frame_count = 0
tracking_data = {}  # For saving ID and bbox info per frame

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Detect players
    detections = detector.detect_players(frame)

    # Track players
    tracked_players = tracker.update(detections)

    # Store results for .pkl
    tracking_data[frame_count] = [
        {"id": pid, "bbox": bbox} for pid, bbox in tracked_players
    ]

    # Draw bounding boxes and IDs
    for pid, bbox in tracked_players:
        x1, y1, x2, y2 = bbox
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, f"Player {pid}", (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    out.write(frame)

    frame_count += 1
    print(f"Processed frame: {frame_count}", end="\r")

# Save tracking data to .pkl
with open(OUTPUT_DATA_PATH, "wb") as f:
    pickle.dump(tracking_data, f)

# Cleanup
cap.release()
out.release()
print(f"\n✅ Video and tracking data saved to:\n- {OUTPUT_VIDEO_PATH}\n- {OUTPUT_DATA_PATH}")

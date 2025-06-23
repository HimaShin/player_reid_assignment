# Player Re-Identification – List.ai Assignment

This project solves **player re-identification** in a 15-second soccer video using YOLOv11 and centroid-based tracking.

## ✅ Task Chosen: Option 2 – Re-Identification in a Single Feed

> Detect each player and ensure that players who go out of frame and reappear are assigned the **same identity** throughout the video.

---

## 📁 Folder Structure

player_reid_assignment/
├── models/ # best.pt (YOLOv11 model)
├── input/ # 15sec_input_720p.mp4
├── output/ # Final output
│ ├── reid_output.mp4
│ └── results.pkl
├── src/
│ ├── detector.py
│ ├── tracker.py
│ └── main.py
├── README.md
└── requirements.txt

yaml
Copy
Edit

---

## ⚙️ Installation

```bash
pip install -r requirements.txt
If you're using a virtual environment:

bash
Copy
Edit
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
🚀 Running the Project
bash
Copy
Edit
python src/main.py
Ensure:

models/best.pt is present

input/15sec_input_720p.mp4 exists

📽️ Output
🎥 output/reid_output.mp4 → video with player ID tracking

📦 output/results.pkl → frame-wise ID and bounding box data

👨‍💻 Developer Info
Name: Pendlimarri Himakar
Role Applied: AI Intern at List.ai

📧 Submit to:

archana@list.ai

rahul@list.ai

🔍 Notes
Detection: YOLOv11 (Ultralytics)

Tracking: Custom centroid-based method

Fully modular code, ready for extension (e.g., Deep SORT)

✅ Done!
Thanks for the opportunity!









# 🏃‍♂️ Player Re-Identification in Sports Footage

This project is a solution for the **Player Re-Identification** assignment given by **List.ai** as part of the AI Intern role selection.

## 🎯 Task: Re-Identification in a Single Feed

Given a 15-second football video (`15sec_input_720p.mp4`), the goal is to:
- Detect players and assign consistent IDs
- Ensure players who exit and re-enter the frame retain the same identity
- Generate a final output video with tracking overlays
- Save tracking metadata in `.pkl` format

## 🗂️ Folder Structure

```
player_reid_assignment/
├── models/
│   └── best.pt               # [Download separately – see below]
├── output/
│   ├── reid_output.mp4       # [Generated output – see Drive link]
│   └── results.pkl           # [Tracking data]
├── src/
│   ├── main.py               # Main execution script
│   ├── detector.py           # Player detection (YOLOv11)
│   └── tracker.py            # ID tracking logic
├── requirements.txt
├── README.md
└── .gitignore
```

## 📦 Model & Output Files

Due to GitHub's 100MB file size limit, the model and output files are hosted on Google Drive.

🔗 [Download Model & Output Files](https://drive.google.com/drive/folders/1OHQSONJHMNd-0aJY_aZP6FZGLAWytpBf?usp=sharing)

Includes:
- `models/best.pt` – YOLOv11 model for player detection
- `output/reid_output.mp4` – Final video with tracked player IDs
- `output/results.pkl` – Pickle file with player tracking metadata

## 🚀 How to Run

1. **Clone the repo**:
   ```bash
   git clone https://github.com/HimaShin/player_reid_assignment.git
   cd player_reid_assignment
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Place files**:
   - Download `best.pt` and place it in the `models/` folder
   - Make sure `15sec_input_720p.mp4` is available in `sample_videos/`

4. **Run the main script**:
   ```bash
   python src/main.py --input sample_videos/15sec_input_720p.mp4 --output output/reid_output.mp4 --model models/best.pt --save-results output/results.pkl
   ```

## 🧠 Technologies Used

- Python 3.10+
- YOLOv11 (fine-tuned) for detection
- OpenCV for video I/O
- Custom tracker for player re-identification
- Pickle for result serialization

## 📬 Submission

Submitted to:  
- `archana@list.ai`  
- `rahul@list.ai`  

By:  
**Himakar Pendlimarri**

## 📌 Note

- This repo only contains code.
- Large files are excluded as per GitHub file size policies.

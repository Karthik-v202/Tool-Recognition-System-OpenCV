# 🛠️ Geometric Tool Recognition System

A real-time Computer Vision pipeline developed to identify and classify mechanical tools through deterministic geometric analysis. This project demonstrates a lightweight approach to object recognition, optimized for low-compute environments by utilizing traditional image processing instead of heavy neural networks.

## 🚀 Overview
This system processes a live video feed—streamed from a **mobile device configured as an IP Camera**—to isolate and classify tools based on their physical signatures. By focusing on **Contour Analysis**, the system achieves high-speed, real-time processing suitable for edge computing and basic industrial automation prototypes.



## 🛠️ Technical Pipeline
1.  **Acquisition:** Captures real-time frames over a local network via an RTSP/HTTP mobile stream.
2.  **Preprocessing:** Converts BGR frames to **Grayscale** and applies a **7x7 Gaussian Blur** to reduce high-frequency sensor noise.
3.  **Segmentation:** Employs **Otsu’s Binarization** to automatically calculate the optimal threshold value, allowing the system to adapt to varying ambient light levels frame-by-frame.
4.  **Morphology:** Uses a **5x5 NumPy kernel** for **Morphological Closing**, bridging internal gaps caused by metallic reflections on the tools.
5.  **Heuristic Classification:** Extracts **Spatial Invariants** to label tools based on predefined geometric ranges:
    * **Area:** Total pixel count of the object silhouette.
    * **Aspect Ratio:** Width-to-height ratio used to distinguish thin tools (Screwdrivers) from squarer tools (Pliers).

## ⚠️ Engineering Limitations & Accuracy
As this is a **Deterministic Logic-based system** (non-Deep Learning), it operates on shape math:
* **Geometric Overlap:** Any object (e.g., a rectangular piece of cardboard) sharing the same area and aspect ratio as a tool may trigger a false positive.
* **Orientation Dependency:** The current logic is optimized for tools placed relatively parallel or perpendicular to the camera's axis.
* **Background Contrast:** Detection accuracy is highest when there is a clear visual contrast between the tool and the workspace surface.

## 📂 Project Structure
```text
├── src/
│   └── Tool-detector.py           # Core detection script
├── requirements.txt      # Dependency list (OpenCV, NumPy)
└── README.md             # Project documentation
```

![Project Demo](assets/Demo)

# 🐾 How Computer Sees Us: A Feline Guide to Computer Vision

An interactive, 2-hour educational project designed for high school graduates to demystify **Computer Vision** through the lens of biological evolution (cats) and mathematical architecture (CNNs).

## 📖 Project Overview
This repository contains the full curriculum, speaker notes, and image-generation scripts for a presentation that bridges the gap between how a cat's brain works and how modern AI processes images.

### Key Learning Objectives:
- **Digital Foundations:** Understanding images as RGB numerical matrices ($0-255$).
- **Biological Inspiration:** The Hubel & Wiesel experiment and "Edge Detection."
- **AI Mechanism:** How Convolutional Neural Networks (CNNs) learn their own filters.
- **Hands-On Lab:** Training a real-time model using Google Teachable Machine.
- **Ethics & Bias:** Real-world implications using Samsung's categorization and social media.

---

## 🛠️ Repository Structure

- **`presentation_plan.md`**: The complete script, slide-by-side breakdown, and speaker notes.
- **`scripts/utils.py`**: A utility library containing Python functions to generate the technical visuals (Edges, Pixel Grids, RGB Splitting) using `OpenCV` and `Matplotlib`.
- **`images/`**: Organized folders containing all visual assets needed for the PowerPoint, categorized by presentation phase.

---

## 🚀 Getting Started

### 1. Prerequisites
You will need Python 3.8+ installed. Install the necessary libraries for the image generation scripts:
```bash
pip install opencv-python matplotlib numpy pillow pillow-heif
```

**Note:** ```pillow-heif``` is only needed when input images are in HEIC format
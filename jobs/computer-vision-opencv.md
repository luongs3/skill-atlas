# Job: Computer Vision (OpenCV)

**You're about to:** process images and video — classical CV with OpenCV, deep CV with torchvision.
Related: [machine-learning-pytorch](machine-learning-pytorch.md).

> Reputation pulled live **2026-06-04** via `gh api`.

---

## Tier A 🟢 — Canonical

### OpenCV + official docs
The canonical computer-vision library — I/O, filtering, transforms, feature detection, calibration,
classical detection/tracking. The docs/tutorials are the reference.
- **source:** https://github.com/opencv/opencv (docs: https://docs.opencv.org)
- **reputation:** OpenCV · **87,776★** · pushed 2026-06-04
- **last_validated:** 2026-06-04
- **assumes:** Python or C++; `opencv-python` for Python
- **adapt:** none — reference. Reach here first for classical pipelines before pulling in a deep model.

### torchvision (PyTorch)
The deep-CV companion — datasets, transforms, and pretrained detection/segmentation/classification
models. Lives in the PyTorch project.
- **source:** https://github.com/pytorch/pytorch (docs: https://pytorch.org/vision/stable)
- **reputation:** PyTorch Foundation · **100,381★** · pushed 2026-06-04
- **last_validated:** 2026-06-04
- **assumes:** PyTorch installed; see [machine-learning-pytorch](machine-learning-pytorch.md)
- **adapt:** pin versions; pretrained-weight APIs shift between releases.

---

## Tier B 🔵 — Community-proven

*No community substitute listed — for classical CV, OpenCV is the standard; for deep CV, torchvision
plus task-specific model repos. Verify any third-party model repo (license, maintenance) yourself.*

---

*Substitution-resistant private skill: your imaging domain — camera/sensor quirks, annotation schema,
augmentation policy, and accuracy/latency targets. An LLM calls `cv2` fine; it doesn't know your data
or what "correct" looks like for your task.*

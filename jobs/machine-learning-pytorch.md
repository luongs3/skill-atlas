# Job: Machine Learning (PyTorch)

**You're about to:** train and ship ML models — tensors, autograd, classical ML, transformers.
Related: [llm-app-development](llm-app-development.md), [data-analysis](data-analysis.md).

> Reputation pulled live **2026-06-04** via `gh api`.

ML moves fast — **last_validated matters here.** Re-check versions before trusting any snippet.

---

## Tier A 🟢 — Canonical

### PyTorch + official docs
The deep-learning framework — tensors, autograd, `nn`, training loops, the docs/tutorials.
- **source:** https://github.com/pytorch/pytorch (docs: https://pytorch.org/docs)
- **reputation:** PyTorch Foundation · **100,381★** · pushed 2026-06-04
- **last_validated:** 2026-06-04
- **assumes:** Python + (optionally) a CUDA GPU
- **adapt:** none — reference.

### scikit-learn
The canonical classical-ML library — pipelines, preprocessing, model selection, metrics.
- **source:** https://github.com/scikit-learn/scikit-learn (docs: https://scikit-learn.org)
- **reputation:** scikit-learn · **66,242★** · pushed 2026-06-03
- **last_validated:** 2026-06-03
- **assumes:** Python + NumPy
- **adapt:** none — reference. Reach here before PyTorch for tabular problems.

### Hugging Face Transformers
The standard library for pretrained models — load, fine-tune, run NLP/vision/audio transformers.
- **source:** https://github.com/huggingface/transformers (docs: https://huggingface.co/docs/transformers)
- **reputation:** Hugging Face · **161,278★** · pushed 2026-06-04
- **last_validated:** 2026-06-04
- **assumes:** PyTorch (or JAX/TF) installed
- **adapt:** pin model + library versions; APIs shift release-to-release.

---

*Substitution-resistant private skill: your data pipeline, training infra, and eval harness — dataset
splits, feature engineering, experiment tracking, and what "good" means for your metric. An LLM writes
a training loop fine; it doesn't know your data or how you measure success.*

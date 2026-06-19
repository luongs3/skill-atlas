# Job: Model Serving (non-LLM)

**You're about to:** deploy ML models behind low-latency APIs — batching, versioning, GPU sharing.

> Reputation pulled live **2026-06-19** via `gh api`.

LLM-specific serving is [llm-serving-inference](llm-serving-inference.md).

---

## Tier A 🟢 — Canonical

### NVIDIA Triton
Production inference server — multi-framework, dynamic batching, GPU sharing, model ensembles.
- **source:** https://github.com/triton-inference-server/server
- **reputation:** **10,765★** · pushed 2026-06-19
- **last_validated:** 2026-06-19
- **assumes:** models + (ideally) GPU
- **adapt:** fork your model repo layout + batching config.

### BentoML
Python-first model serving + packaging (Bentos) with adaptive batching — ML to API fast.
- **source:** https://github.com/bentoml/BentoML
- **reputation:** **8,675★** · pushed 2026-06-03
- **last_validated:** 2026-06-19
- **assumes:** Python
- **adapt:** fork your service definition + runners.

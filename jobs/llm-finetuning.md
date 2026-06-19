# Job: Fine-Tuning LLMs

**You're about to:** adapt open LLMs to your task with LoRA/QLoRA/full fine-tuning — efficiently, on modest hardware.

> Reputation pulled live **2026-06-19** via `gh api`.

Serve the result via [llm-serving-inference](llm-serving-inference.md).

---

## Tier A 🟢 — Canonical

### LLaMA-Factory
Unified fine-tuning for 100+ LLMs — LoRA/QLoRA/full, a UI, sane defaults. The fastest path to a custom model.
- **source:** https://github.com/hiyouga/LLaMA-Factory
- **reputation:** **72,296★** · pushed 2026-06-17
- **last_validated:** 2026-06-19
- **assumes:** Python + GPU
- **adapt:** fork your dataset format + training config.

### Unsloth
2x-faster, low-VRAM fine-tuning with patched kernels — fine-tune on a single consumer GPU.
- **source:** https://github.com/unslothai/unsloth
- **reputation:** **66,819★** · pushed 2026-06-19
- **last_validated:** 2026-06-19
- **assumes:** Python + NVIDIA GPU
- **adapt:** fork the notebook for your base model + data.

### PEFT
Hugging Face's parameter-efficient fine-tuning library — LoRA/adapters/prompt-tuning primitives.
- **source:** https://github.com/huggingface/peft
- **reputation:** **21,288★** · pushed 2026-06-19
- **last_validated:** 2026-06-19
- **assumes:** Python + transformers
- **adapt:** fork your PEFT config; compose with TRL.

### TRL
Transformer RL + SFT/DPO trainers — the alignment/post-training toolkit from Hugging Face.
- **source:** https://github.com/huggingface/trl
- **reputation:** **18,667★** · pushed 2026-06-19
- **last_validated:** 2026-06-19
- **assumes:** Python + transformers
- **adapt:** fork the trainer for your SFT/DPO recipe.

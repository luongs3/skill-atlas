# Job: Distributed & Large-Model Training

**You're about to:** train models too big for one GPU — data/model/pipeline parallelism, ZeRO, sharding.

> Reputation pulled live **2026-06-19** via `gh api`.

Single-GPU tuning is [llm-finetuning](llm-finetuning.md).

---

## Tier A 🟢 — Canonical

### DeepSpeed
ZeRO sharding + offload for training huge models on limited hardware. The memory-efficiency workhorse.
- **source:** https://github.com/microsoft/DeepSpeed
- **reputation:** **42,542★** · pushed 2026-06-18
- **last_validated:** 2026-06-19
- **assumes:** Python + multi-GPU
- **adapt:** fork your ZeRO stage + offload config.

### Megatron-LM
Reference tensor/pipeline parallelism for large transformer training — the techniques most frameworks copy.
- **source:** https://github.com/NVIDIA/Megatron-LM
- **reputation:** **16,753★** · pushed 2026-06-18
- **last_validated:** 2026-06-19
- **assumes:** Python + multi-GPU cluster
- **adapt:** study the parallelism; adapt to your stack.

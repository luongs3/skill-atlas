# Job: LLM Serving & Inference

**You're about to:** run/serve LLMs yourself — local inference, self-hosted endpoints, or
high-throughput serving. Distinct from [llm-app-development](llm-app-development.md) (the
app layer); this is the ops/hosting layer.

> Reputation pulled live **2026-06-03** via `gh api`.

---

## Tier A 🟢 — Canonical (the de-facto serving stacks)

### Ollama — easiest local serving
Run open models locally with one command; OpenAI-compatible API. The fastest path to a
local LLM endpoint.
- **source:** https://github.com/ollama/ollama (docs: https://docs.ollama.com)
- **reputation:** Official Ollama · **172,989★** · pushed 2026-06-03
- **last_validated:** 2026-06-03
- **assumes:** a machine with enough RAM/VRAM
- **adapt:** fork your model list + Modelfile conventions.

### llama.cpp — the inference engine
The C/C++ engine under much of local inference (GGUF quantization, CPU/GPU). What Ollama
and many others build on.
- **source:** https://github.com/ggerganov/llama.cpp
- **reputation:** **114,396★** · pushed 2026-06-03 (the foundational local-inference engine)
- **last_validated:** 2026-06-03
- **assumes:** build toolchain; a GGUF model
- **adapt:** none — reference for quantization + server flags.

### vLLM — high-throughput production serving
The standard for serving LLMs at scale (PagedAttention, batching, OpenAI-compatible API).
What you reach for beyond a single-user local setup.
- **source:** https://github.com/vllm-project/vllm (docs: https://docs.vllm.ai)
- **reputation:** Official vLLM · **81,794★** · pushed 2026-06-03
- **last_validated:** 2026-06-03
- **assumes:** GPU(s)
- **adapt:** fork your serving config (model, tensor-parallel, quant, max-batch).

---

## How to choose

- **One user / local dev / a tool on your machine →** Ollama (wraps llama.cpp).
- **Need to understand/tune the engine, CPU inference, exotic quant →** llama.cpp directly.
- **Serving many concurrent users in prod on GPUs →** vLLM.

*The private skill: your deployment's actual config (which model, which quant, the hardware
it runs on, the throughput target). The atlas names the live engines; your skill pins the
choice so you don't re-benchmark every time.*

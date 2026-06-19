# Job: Speech — STT & TTS

**You're about to:** transcribe audio and synthesize speech with open models — streaming, diarization, voices.

> Reputation pulled live **2026-06-19** via `gh api`.

---

## Tier A 🟢 — Canonical

### Whisper
The reference open speech-to-text model + code — robust multilingual transcription. The STT baseline.
- **source:** https://github.com/openai/whisper
- **reputation:** **103,046★** · pushed 2026-04-15
- **last_validated:** 2026-06-19
- **assumes:** Python + (GPU helps)
- **adapt:** pick model size by latency/accuracy; verify on your audio.

### faster-whisper
CTranslate2 reimplementation of Whisper — up to 4x faster, lower memory. The production STT default.
- **source:** https://github.com/SYSTRAN/faster-whisper
- **reputation:** **23,727★** · pushed 2025-11-19
- **last_validated:** 2026-06-19
- **assumes:** Python
- **adapt:** swap in for whisper; fork your batching.

---

## Tier B 🔵 — Community-proven

### Coqui TTS
Open text-to-speech with many models + voice cloning. Verify maintenance + license for your use.
- **source:** https://github.com/coqui-ai/TTS
- **reputation:** **45,584★** · pushed 2024-08-16
- **last_validated:** 2026-06-19
- **assumes:** Python
- **adapt:** pick a model; fork your voice config.

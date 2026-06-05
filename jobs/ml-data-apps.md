# Job: ML Data Apps (Streamlit/Gradio)

**You're about to:** ship a quick web UI for a model or data tool without frontend work.

> Reputation pulled live **2026-06-05** via `gh api`.

---

## Tier A 🟢 — Canonical

### Streamlit
Turn a Python script into a shareable data/ML web app in minutes.
- **source:** https://github.com/streamlit/streamlit (docs: https://docs.streamlit.io)
- **reputation:** **44,828★** · pushed 2026-06-05
- **last_validated:** 2026-06-05
- **assumes:** Python
- **adapt:** fork your app-layout conventions.

### Gradio
Fast UIs for ML models — inputs/outputs, sharing, Hugging Face integration.
- **source:** https://github.com/gradio-app/gradio (docs: https://www.gradio.app/docs)
- **reputation:** **42,811★** · pushed 2026-06-05
- **last_validated:** 2026-06-05
- **assumes:** Python
- **adapt:** pick Streamlit (data apps) or Gradio (model demos).

---

## How to use this job

Use **Streamlit** for data/dashboard apps — multi-widget layouts, charts, tables, and exploratory tools where you control the page structure. Use **Gradio** for model demos — its `Interface`/`Blocks` map inputs→outputs cleanly and it integrates natively with Hugging Face Spaces for one-click sharing. The decision hinges on whether you're presenting *data you arrange* (Streamlit) or wrapping a *function/model with typed I/O* (Gradio); for a quick public model demo, Gradio + Spaces is the shortest path.

## Pitfalls

- **Streamlit re-runs the entire script top-to-bottom on every interaction** — expensive loads (models, big files) re-execute and freeze the UI unless wrapped in `@st.cache_resource`/`@st.cache_data`. New users routinely reload a model on every click.
- **State doesn't persist across reruns without `st.session_state`** — plain Python variables reset each interaction, so counters, multi-step forms, and chat history vanish unless stored in session state.
- **Gradio's `share=True` opens a public tunnel** — convenient for demos but exposes your app (and any local data/model) to anyone with the link for the session's lifetime. Don't leave it on for anything sensitive; deploy properly instead.

---

*These let a backend/ML person skip frontend entirely. See [machine-learning-pytorch](machine-learning-pytorch.md). Private skill = your app template.*

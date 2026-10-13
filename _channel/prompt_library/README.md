# Prompt library

Base prompts per model. A recreation prompt = **lens fragment** (`../lenses/`) + **shot content** (from `shot.yaml`) + **model base** (below) + **negatives**.

| File | Use |
|---|---|
| `stills_base.md` | Keyframes from reference images (Pass A) |
| `i2v_base.md` | Image-to-video from approved stills (Pass B) |
| `negatives.md` | Channel-wide negatives appended to every prompt |
| `model_notes.md` | What each model is good at; update after the pilot |

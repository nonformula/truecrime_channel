# Image-to-video base (Pass B)

Models: Kling, Veo, Runway Gen-4.5. Route per `model_notes.md`.

Template:
> Animate this frame as {LENS_NAME}: {MOTION}. Duration {DURATION_S}s. Keep camera behaviour consistent with the lens: {LENS_MOTION}. No new people, no faces, no text. {NEGATIVES}

Generate at spec duration + 1s handles. Save takes as `C###_R###_T##.mp4` in `media:/…/recreations/R###/takes/` and log each in the repo's `takes_log.csv`.

# Graphics templates

After Effects / Premiere templates live on Drive at `media:/_channel/gfx_templates/`. This folder records what exists and the data each one takes.

| Template | Driven by | Fields |
|---|---|---|
| Knowledge Ledger | `cases/<case>/07_visuals/ledger.csv` | line_id, column, text, source |
| Exhibit card | `visual_index.csv` rows of type `exhibit_card` | number, object, descriptor, source |
| Lens HUD (per lens) | `recreations/R###/shot.yaml` | clock, location, telemetry, source citation |
| Map | `04_locations.csv` + map specs | pins, labels, routes |
| Lower third / source tag | asset index | asset source, date |

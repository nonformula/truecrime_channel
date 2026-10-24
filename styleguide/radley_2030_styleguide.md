# Radley 2030 — Style Guide
**Updated March 2026**

Reference document for all design and development decisions on the Radley 2030 project.
For verbatim copy and section structure, see `Readme.md`.

---

## 01 — Identity

### Logo
The Radley identity is a custom R mark (`R_logo2.png`) paired with the wordmark **Radley 2030** set in Inter 500.

| Context | Mark height | Wordmark |
|---|---|---|
| Navigation | 30px | Inter 500 · 15px · `#777` |
| Footer / standalone | 40px | — (mark only) |
| Standard lockup | 40px | Inter 500 · 17px · `#777` |

**Clear space:** Minimum 1× mark height on all sides.  
**Backgrounds:** The mark is red on both dark (`#0a0a0a`) and white/light backgrounds — it does not invert or change color. Never place on mid-tones, color fills, or over imagery without sufficient contrast.

---

## 02 — Color

### Foundation

| Token | Hex | Use |
|---|---|---|
| `--bg-dark` | `#0a0a0a` | Page background — all sections |
| `--bg-light` | `#e7e7e7` | Light backgrounds (not used in dark site) |
| `--text-light` | `#f0f0f0` | Primary text on dark |
| `--text-dark` | `#1a1a1a` | Text on light |
| `--text-muted` | `#888888` | Card body text |
| `--text-muted-dk` | `#666666` | Labels, metadata, muted chrome |
| Body copy | `#aaaaaa` | `.body-text` paragraphs |

### Accent Colors

| Token | Hex | Role |
|---|---|---|
| `--red` | `#d32127` | **Primary accent** — inline emphasis, callout borders |
| `--green` | `#2a7a4b` | Continuity section callout |
| `--amber` | `#c8820a` | AI Strategy section callout · Technology pills |
| `--purple` | `#7b5ea7` | Craft pill category |
| `--teal` | `#2a7a6e` | Experience pill category |
| `--coral` | `#c85a3a` | Voice pill category |

### Surface Tones (UI)

| Hex | Use |
|---|---|
| `#111111` | Card backgrounds |
| `#161616` | Dark text card backgrounds |
| `#1a1a1a` | Borders, row dividers, nav border |
| `#222222` | Card borders (text cards) |

### Color Rules
- **Red is punctuation only.** Use in `<em>` tags for inline emphasis and as callout left-border color. Never use red for buttons, backgrounds, headings, or structural elements.
- **Category colors** (purple, teal, coral, amber) appear exclusively in pill tags and their group labels. Do not repurpose them elsewhere.
- The entire site runs on a dark background. Do not introduce light-mode sections.

---

## 03 — Typography

### Typefaces
- **Inter** — 300 (body/light), 400 (headings), 500 (UI labels, card titles, captions)
- **Roboto Mono 700** — section labels, nav links, pill category labels, footer text

Both loaded from Google Fonts. Apply `-webkit-font-smoothing: antialiased` globally.

### Type Scale

**Display Heading** — `.display-heading`
- Inter 400 · `clamp(56px, 7.5vw, 116px)` · leading 1.03 · tracking −0.03em
- Color: `#ffffff` on dark · `#1a1a1a` on light

**Mantra / Hero** — `.mantra`
- Inter 300 · `clamp(64px, 9vw, 148px)` · leading 1.0 · tracking −0.035em
- Color: `#ffffff`

**Subheading** — `.subheading`
- Inter 400 · `clamp(24px, 2.8vw, 38px)` · leading 1.1 · tracking −0.02em
- Color: `#f0f0f0` · red `<em>` for key phrases

**Body Text** — `.body-text`
- Inter 300 · 22px · leading 1.58 · tracking −0.022em · color `#aaaaaa`

**Body Small** — `.body-text--small`
- Inter 300 · 17px · leading 1.58 · tracking −0.018em · color `#888`

**Section Label** — `.section-label`
- Roboto Mono 700 · 10px · tracking 0.18em · uppercase
- Color: `#666` on sections · `rgba(255,255,255,0.5)` over imagery · `rgba(255,255,255,0.45)` in intro

**Card Title** — `.card-title`
- Inter 500 · 16px (20px in AI section) · leading 1.3 · color `#f0f0f0`

**Card Body** — `.card-body`
- Inter 300 · 15px · leading 1.58 · tracking −0.018em · color `#888`

**Card Caption** — `.card-caption`
- Inter 500 · 13px · tracking 0.01em · color `#fff` (over gradient overlay)

**Callout Text** — default
- Inter 300 · `clamp(18px, 1.7vw, 23px)` · leading 1.55 · tracking −0.02em · color `#ccc`
- Green callout variant: matches subheading size · weight 400

**Nav Links** (dropdown)
- Roboto Mono 700 · 11px · tracking 0.16em · uppercase · color `#666` → `#f0f0f0` hover

### Tracking Convention
- **Headings:** Negative tracking (−0.02em to −0.035em). Required at large sizes for a sharp editorial feel.
- **Labels/mono:** Positive tracking (0.14–0.22em). Identifies structural/organizational text.
- **Body:** Slight negative tracking (−0.018em to −0.022em). Improves readability.

---

## 04 — Spacing

All layout spacing uses CSS custom properties defined in `:root`.

| Token | Value | Use |
|---|---|---|
| `--nav-h` | `56px` | Nav height · `scroll-margin-top` on all sections |
| `--section-py` | `clamp(80px, 10vw, 140px)` | Vertical section padding |
| `--section-px` | `clamp(40px, 6vw, 100px)` | Horizontal section padding |
| `--max-width` | `1400px` | Container max-width |
| `--label-mb` | `44px` | Margin below section labels |
| `--heading-mb` | `32px` | Margin below subheadings |
| `--body-gap` | `24px` | Margin below body paragraphs |
| `--callout-mb` | `40px` | Callout left padding |
| `--card-gap` | `3px` | Gap between card grid cells |

**Narrow container:** `max-width: 860px` — used for all long-form text sections (Mission, Brand Position).

**Mobile overrides** at `≤768px`:
- `--section-px: clamp(24px, 6vw, 48px)`
- `--section-py: clamp(60px, 10vw, 100px)`

> The 3px card gap is a deliberate design signature — tight gutters create the editorial film-strip feel. Do not increase it.

---

## 05 — Layout

### Grid Patterns

**Split Layout — `.split-layout`**
- `grid-template-columns: 1fr 1fr · min-height: 100vh · align-items: stretch`
- Image/media grid always on the **left**; copy always on the **right**
- Collapses to single column at `≤1024px`
- `.split-layout--contained` removes `min-height: 100vh` (used in AI Strategy)

**2×2 Card Grid — `.card-grid-2x2`**
- `grid-template-columns: 1fr 1fr · grid-template-rows: 1fr 1fr`
- Fills full split panel height · gap `3px`
- Single column at `≤480px`

**1×3 Card Grid — `.card-grid-1x3`**
- `grid-template-columns: 1fr 1fr 1fr`
- Image height: `clamp(240px, 28vw, 400px)`
- Collapses to single column at `≤768px`

**Three-Column Text — `.three-col`**
- `grid-template-columns: 1fr 1fr 1fr · gap: clamp(24px, 4vw, 60px)`
- Separated below by `1px solid #1a1a1a` border from the card grid
- Collapses to single column at `≤768px`

### Breakpoints

| Breakpoint | Changes |
|---|---|
| `≤1024px` | Split layouts → single column. Card grids min-height 80vw. |
| `≤768px` | Section padding recalculates. Three-col, 1×3, shift table all stack. Parallax hero 70vh, band 38vh. |
| `≤480px` | Display heading clamps to `clamp(36px, 10vw, 56px)`. 2×2 grid single column. |

### Parallax Wraps

| Variant | Height | Use |
|---|---|---|
| `.parallax-wrap--hero` | `100vh` (70vh mobile) | Full-height video backgrounds |
| `.parallax-wrap--band` | `52vh · min 340px` (38vh mobile) | Image/video bands between content |

Parallax image oversized to `height: 122%` · animates `yPercent: -8 → +8` via GSAP scrub.

---

## 06 — Components

### Navigation
- Fixed top · `56px` height · `#0a0a0a` background · `1px solid #1a1a1a` bottom border
- Dropdown triggers on `#nav:hover` via CSS transition (no JS)
- Dropdown: `max-height 0.55s cubic-bezier(0.16,1,0.3,1) · opacity 0.4s ease · translateY -6px → 0`
- Smooth scroll via Lenis: `duration 1.6s · offset -56px` on nav anchor clicks

### Callout Block — `.callout`
- `border-left: 2px solid var(--red)` (or accent color for variants)
- `padding-left: 40px` · margin `clamp(28px, 3.5vw, 44px)` top and bottom
- Default text: Inter 300 · `clamp(18px, 1.7vw, 23px)` · `#ccc`
- Green variant (`.callout--green`): matches subheading scale and weight
- Animation: slides in from `translateX(-32px)` · scroll trigger `top 86%`

### From / To Shift Table — `.shift-table`
- `grid-template-columns: 1fr 1fr` · gap `clamp(32px, 5vw, 80px)`
- Row borders: `1px solid #1a1a1a` · row padding `14px 0`
- Strikethrough: CSS `del::after` pseudo-element, width `0 → 100%` on `.struck` class
- Animation sequence: FROM header → FROM rows → strikethroughs (0.14s stagger) → pause → TO header → TO rows
- Stacks to single column at `≤768px`

### Pill Tags — `.pill`
- `border-radius: 100px · padding: 10px 22px`
- Transparent background · 1px solid border · color matches border
- Hover: 12% opacity fill of accent color · `transition: 0.25s ease`
- Category color map: Craft → purple · Experience → teal · Voice → coral · Technology → amber
- Group label: Roboto Mono 700 · 10px · tracking 0.18em · uppercase · category color
- Animation: scale `0.88 → 1` · `back.out(1.5)` · 0.08s stagger

### Image Cards — `.card-img`
- `overflow: hidden · object-fit: cover`
- Hover: image `scale(1.04)` · `transition: 0.8s ease`
- Caption: absolute bottom · gradient `rgba(0,0,0,0.88) → transparent` · Inter 500 · 13px · `#fff`

### Dark Text Cards — `.card-text`
- Background `#161616` · border `1px solid #222` · padding `clamp(20px, 2.5vw, 32px)`
- Title: Inter 500 · 16px · `#f0f0f0`
- Body: Inter 300 · 15px · leading 1.58 · `#888`

---

## 07 — Animation

**Libraries:** GSAP 3.12.5 + ScrollTrigger · Lenis 1.0.42 (smooth scroll)

All scroll animations fire **once** — no replay on reverse scroll. Lenis drives GSAP's ticker to keep ScrollTrigger in sync.

### Reveal Classes (initial state → animated state)

| Class | Initial State | Animation |
|---|---|---|
| `.reveal` | `opacity:0 · translateY(32px)` | → `opacity:1 · y:0` · 0.95s · power2.out · trigger `top 88%` |
| `.reveal-callout` | `opacity:0 · translateX(-32px)` | → `opacity:1 · x:0` · 0.9s · power2.out · trigger `top 86%` |
| `.reveal-card` | `opacity:0 · translateY(48px)` | → `opacity:1 · y:0` · 0.85s · power2.out · stagger 0.1s |
| `.reveal-pill` | `opacity:0 · scale(0.88)` | → `opacity:1 · scale:1` · 0.6s · back.out(1.5) · stagger 0.08s |
| `.reveal-mantra` | `opacity:0 · translateY(24px)` | → `opacity:1 · y:0` · 1.3s · power3.out — then scale pulse 1.0↔1.005 · 2.8s · sine.inOut · yoyo infinite |

### Parallax
- Image moves `yPercent: -8 → +8` as section scrolls through viewport
- `scrub: 1.2` — slightly laggy for cinematic weight
- Trigger: `start: 'top bottom' · end: 'bottom top'`

### Smooth Scroll (Lenis)
- `duration: 1.4 · easing: exponential deceleration`
- Touch smoothing disabled (respects native mobile scroll)
- Nav anchor clicks: `offset: -56px · duration: 1.6s`

---

## 08 — Imagery & Video

### Overlay System
- **Standard overlay:** `rgba(0,0,0,0.50)` — hero videos, intro section
- **Light overlay:** `rgba(0,0,0,0.35)` — image bands where texture should show through

### Video Requirements
- Always include `autoplay muted loop playsinline` attributes
- Always include a `poster` attribute with a static fallback image
- Format: `.mov` (QuickTime) for Safari · JS catches load and play errors and hides broken video on Android
- Video is oversized to `height: 122%` within its parallax wrap to allow movement without gaps

### Aesthetic Direction
- **Reference:** Polestar.com — cinematic, design-led, high contrast, minimal UI chrome
- **Subjects:** Aerial landscape, documentary, production BTS, motion graphics renders, code/tech environments
- **Color grading:** Dark and desaturated with strong directional light. Avoid bright, saturated, or stock-looking images.
- **Cropping:** Always `object-fit: cover` — never letterbox

### Card Image Dimensions
- 2×2 grid (split panel): fills full panel height, min `100vh`
- 1×3 grid: `clamp(240px, 28vw, 400px)` tall

---

## 09 — Brand Voice (Design Tone)

These rules govern visual decisions the same way copy tone governs writing.

| Do | Don't |
|---|---|
| Dark backgrounds exclusively (`#0a0a0a`) | Light-mode sections or mid-tone backgrounds |
| Red for inline emphasis and callout borders only | Red for buttons, backgrounds, or structural elements |
| Negative letter-spacing on all large headings | Default or positive tracking at display sizes |
| 3px card gaps — the signature editorial tightness | Increasing gaps to "add breathing room" |
| `clamp()` for all type and spacing | Fixed pixel values for responsive properties |
| Roboto Mono for labels and metadata only (short strings) | Roboto Mono for body copy or multi-line text |
| Image grids on the left in split layouts | Reversing split layout without strong reason |
| Poster fallback on every video element | Video elements without a `poster` attribute |
| Animations that decelerate and arrive confidently | Bounce, overshoot, or attention-seeking easing |

---

## Quick Reference — CSS Variables

```css
:root {
  /* Color */
  --bg-light:       #e7e7e7;
  --bg-dark:        #0a0a0a;
  --text-dark:      #1a1a1a;
  --text-light:     #f0f0f0;
  --text-muted:     #888888;
  --text-muted-dk:  #666666;
  --red:            #d32127;
  --green:          #2a7a4b;
  --amber:          #c8820a;
  --purple:         #7b5ea7;
  --teal:           #2a7a6e;
  --coral:          #c85a3a;

  /* Layout */
  --nav-h:          56px;
  --section-py:     clamp(80px, 10vw, 140px);
  --section-px:     clamp(40px, 6vw, 100px);
  --label-mb:       44px;
  --heading-mb:     32px;
  --body-gap:       24px;
  --callout-mb:     40px;
  --card-gap:       3px;
  --max-width:      1400px;
}
```

## Quick Reference — Dependencies

All loaded from CDN, no npm required.

```html
<!-- Google Fonts -->
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500&family=Roboto+Mono:wght@700&display=swap" rel="stylesheet">

<!-- GSAP 3.12.5 -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>

<!-- Lenis 1.0.42 -->
<script src="https://cdn.jsdelivr.net/npm/@studio-freight/lenis@1.0.42/dist/lenis.min.js"></script>
```

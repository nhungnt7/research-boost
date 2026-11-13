# Worked example: Multi-Agent Coordination for Robotics

[PowerPoint](demo.pptx) · [PDF](demo.pdf) · [English speaker text](speaker-text.md) · [Source hyperlinks](sources.json)

**Watch the ResearchBoost field walkthrough**

https://github.com/user-attachments/assets/49012eab-6328-414f-a09a-8fde1d4a1dfa

The promotional walkthrough starts with an illustrated LLM-agent background → seed papers → Codex + ResearchBoost → robotics deck workflow. It then uses source slides 1–40, explaining each slide's role and why it helps a newcomer understand the field. The five selection criteria appear immediately before the frontier; the paper-reading list is retained and technical appendix slides 41–46 are omitted. The annual chart on source slide 5 automatically advances through 2022–2026. English narration explains the value of each slide.

This is a 46-slide retained November 2026 research talk from the Survey to Slides template, packaged as a ResearchBoost demo. It shows the expected depth and narrative structure, rather than a freshly rerun review. The project introduction is separate in `slides/research-boost-intro/`.

## Navigate the demo

| Slides | What to inspect |
| --- | --- |
| 1-3 | Cover, detailed agenda, and a concrete two-robot coordination problem. |
| 4-11 | Scoped literature statistics, direction/application comparisons, and robotics evaluation settings. |
| 12-16 | Applications, research community and decision authority. |
| 17-22 | The forces behind historical milestones and their limitations. |
| 23-36 | Five selection criteria, frontier overview, methods, training and results. |
| 37-38 | Evidence-derived questions and concrete proposed experiments. |
| 39-46 | Conclusion and problem-based reading/technical appendix. |

The inherited Presenter Perspective box and embedded bilingual notes have been removed from this distribution. Separate English narration and the original source links are provided. The original installed skill and source deck were not changed. The PDF agenda page is a rendered visual copy after removal of the inherited statement. Slides otherwise retain the source material, figures, theme and animations. Google Slides import and animation behavior have not been revalidated for this distribution.

## Evidence snapshot and limits

The original deck uses several populations. Do not combine them as if they shared a denominator:

- `data/evaluation-corpus.csv`: 205 selected evaluation studies; multi-label downstream tasks and settings can overlap. The deck's robotics/embodiment slice contains 36 studies.
- `data/conference-direction-coding.csv`: 308 coded conference title matches, distinct from the broader retrieved candidate pool.
- `data/annual-counts.csv`: five annual aggregate rows with the source conference denominators and title-match rates.
- `data/robot-runtime-authority.csv`: 36 robotics/embodiment authority codings.
- `data/displayed-statistics.json` and `robotics-venue-comparison.json`: retained display aggregates and official program URLs. The latter records retrieval on 11 November 2026; the deck's evaluation sample caption uses a 10 November 2026 cutoff.

These files permit checks of the retained categories and displayed aggregates. The complete raw proceedings/program harvest and every retrieval operation are not bundled, so the package does not claim to reproduce the full search or validate recall. A new run must rebuild venue/year coverage, queries, screening and counts for its own field and cutoff. This packaging pass did not re-audit every scientific claim or live source URL.

## Recreate the workflow on a new topic

Use `brief.json` as a concrete input example, replace its topic and seeds, then invoke `$research-boost`. For a full rerun, ask the agent to refresh primary sources and build its own evidence ledger and corpus. Do not copy this demo's values into a new field.

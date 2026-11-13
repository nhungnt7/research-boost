# Validation record

Checked on 13 November 2026.

- Skill Creator quick validation passed for the new `research-boost` skill.
- Package validation passed: relative links, self-contained template paths, provenance hash, deck slide counts and expected corpus row count.
- Installer integration test passed, including a second install that refuses to overwrite the first. Brief creation passed for all five modes (the four seed types and mixed input).
- The 12-slide introduction passed PPTX package integrity, geometry, font-policy and first-party reimport checks. All slides were rendered and visually reviewed; the revised history and workflow slides were rechecked.
- The 46-slide demo passed PPTX package integrity checks. The modified agenda was inspected; its remaining research content is retained from the original.
- Both PDFs have the expected page counts. The introduction PDF uses reviewed slide images with searchable English text; the PowerPoint retains editable text and diagrams.
- File hashes confirmed every file in the original installed Survey to Slides skill was unchanged.

These checks do not constitute a new scientific audit of the demo, a full retrieval rerun, a live-URL availability test, or a native PowerPoint/Google Slides animation test. See the demo README for the evidence snapshot and coverage limits.

## Update checked on 14 November 2026

Added materials-first guidance to the skill, README, customization guide and prompt examples, together with launch copy. Updated introduction slides 1, 3, 8 and 9 and aligned English narration. Rechecked the changed slides, regenerated the PDF and refreshed the ZIP. The retained template, robotics demo and keynote acknowledgments were preserved.

## ResearchBoost rename and video

Renamed the public project, skill identifier, package paths, instructions and introduction deck to ResearchBoost (`research-boost`). Added a 12-slide, 6 minute 39 second English overview with local synthetic narration, an audio-only file, exact utterance captions and chapters. The full 46-slide demo and retained reference content remain unchanged.

The overview MP4 and M4A decoded successfully. Audio levels were checked for non-silence and headroom. Video samples from the beginning, middle and end were visually checked; chapter continuity, caption timing, 1080p dimensions and square pixels were checked. The renamed introduction was rendered and visually reviewed.

## Complete promotional walkthrough (superseded version)

Created a 7 minute 42 second promotional video with English synthetic narration, captions, audio-only export and chapters. The opening states the skill output and five frontier-selection criteria. Coverage checks require all 46 demo slides, in order; all 46 rendered demo frames exactly matched the retained source renders. Every scene is held for at least five seconds. The three editable promotional cards passed package, geometry, font and import checks and were visually reviewed. The video and audio decoded successfully; captions, chapter continuity, square pixels, full-HD dimensions and audio headroom were checked. A deliberately omitted demo page was correctly rejected by the builder.

## Revised field walkthrough and illustrated setup (superseded version)

The earlier 7:32 version includes 39 selected demo slides (1–22 and 24–40), plus an opening, an illustrated background/input/Codex/output context and a closing. The standalone criteria card, source slide 23 and technical appendix slides 41–46 are excluded. The paper list on source slide 40 remains. Each selected scene has an explicit role and reason it matters, expressed in narration and labeled in the transcript. The context illustration uses native editable diagram objects and an actual output-slide thumbnail. Selected source frames, coverage/order, media decoding, dimensions and captions were checked; the complete source deck and skill template are unchanged.

## Local neural voice, restored criteria, and annual chart playback

Checked on 14 November 2026. The final promotional video is 7:59 (478.625 seconds of narration), with 43 scenes and demo slides 1–40 in order. Source slide 23 is restored immediately before 24; paper-list slide 40 remains and technical appendix slides 41–46 are excluded. The separate early criteria title card remains removed.

Narration is synthesized locally with Kokoro-82M and the generic `af_heart` voice at speed 1.25, using continuous scene phrasing. All 43 scenes have phoneme-derived sentence alignment; the 93 English caption cues are monotonic and within the media duration. The MP4 and M4A fully decoded. The MP4 is 1920 × 1080, square pixels, H.264/AAC, with embedded English captions. Decoded audio is non-silent with a measured maximum of -1.2 dBFS.

Source slide 5 plays the original annual chart images in order, 2022–2026. The first four hold for 1.25 seconds each; the final 2026 view fills the rest of the 11.775-second scene. Frame durations sum to the scene duration, and each frame hash is recorded. All five encoded views were checked against their corresponding exported slide states. An 11.8-second preview is included.

The package validator and two existing helper tests passed. Hashes confirm the source demo PPTX/PDF and retained skill template are unchanged. The ZIP excludes model weights, caches and local environment directories. The promotional media retains its production metadata for provenance. These checks do not constitute a fresh audit of the retained research claims.

## README visual showcase

Checked on 14 November 2026. The README now explicitly offers an editable `.pptx` deck and links directly to the included file. Added a project-authored SVG banner, a 17.5-second animated preview linked to the full narrated video, and six actual slide previews with explanations of their value to a newcomer. The materials-first guidance, installation instructions and keynote acknowledgments remain.

A local browser render verified all eight README images loaded, with no horizontal page overflow at desktop and 430-pixel mobile widths. The desktop opening, gallery and mobile opening were visually reviewed. All eleven intended visual states occur in order in the GIF; its file size is under 1 MB. Relative Markdown and HTML links, image paths and the unchanged demo/template hashes were checked. GitHub’s live renderer and an uploaded native video attachment were not exercised; the README uses a portable animated image and linked MP4.

## Promotional-only video scope

Updated on 14 November 2026. The README presents the video as a promotional example of the skill’s output. Removed the video-generation guide, optional speech-package requirements, video-building helpers, and video-embedding instructions from the public package. Installation and customization guidance remain focused on the research skill and editable slide deliverables. The promotional MP4, embedded captions, animated README preview and slide highlights remain unchanged. Standalone audio exports, video transcripts and narration plans have been removed from the public package; the video section now offers the video alone. The separate English speaker text for the research deck remains a core skill deliverable. Package links and unchanged media/source hashes were checked before refreshing the ZIP.

## Playable video on GitHub

Updated on 14 November 2026. Replaced links to the repository MP4 with a GitHub-hosted video attachment in the main and robotics-example READMEs. The full 7:59 walkthrough is available through an inline player. A 1600 × 900 H.264/AAC playback copy was prepared below 10 MB, retaining the narration and timings; the original 1920 × 1080 MP4 remains unchanged in the repository. The playback copy fully decoded, and GitHub’s editor preview loaded the full-duration video with readyState 4 and no media error. Playback provenance is recorded beside the original MP4. No video-production guide or standalone audio/script downloads were added.

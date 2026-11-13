# Survey to Slides workflow

Use the retained robotics v44 as the layout and sequence reference. Replace its domain examples and figures with material for the requested topic. Use [evidence and narrative conventions](evidence-and-narrative.md) for the evidence and writing conventions; no personal skill installation is required.

## Keep this sequence

1. Cover and a detailed agenda on slide 02. Include a presenter perspective near the start only when the user supplies or confirms it for this talk.
2. One real example that makes the research problem visible. For coordination talks, explain what depends on another participant and what fails without coordination.
3. Broad literature landscape. Show a time-normalized retrieval chart, annual chart views with click transitions if appropriate, direction totals, and the application-domain comparison. Build annual views from editable slide elements when the deck will be opened in Google Slides.
4. Domain focus. Compare what changes across domains, cross-tabulate directions and downstream tasks, and show the focal domain’s task mix, evaluation settings and yearly representation.
5. Applications and evidence, then the community map and who has authority to decide. Follow the [community map workflow](#build-the-community-map) for layout, sources and verification.
6. History. Explain the forces behind the milestones, show a timeline with years and groups, then give selected milestones individual evidence slides. End each with the limitation that motivates the next one.
7. Current frontier. Use the five criteria below, then an overview mapping major problems to selected works, groups, years, mechanisms, baselines and tested scale. Include decision authority when relevant. Highlight the active work before its deep dive. Explain the task, mechanism, training where applicable, experiment, baselines, results and limitations. Choose the number of works to cover the field's main developments. Move secondary comparisons to the appendix.
8. Two future slides. First connect observed signals to questions. Then specify proposed datasets, methods, baselines and metrics with audience and adoption implications. End with a conclusion that answers the opening example.
9. Appendix reading guide by problem, with years, original-source links, and one reason to read each item.

## Build a detailed agenda

Inspect [the robotics agenda](../assets/agenda-reference.png). Use its numbered rows, section title on the left and a one- or two-line description on the right. Adapt the wording to the new topic and the slides actually included. The descriptions should tell the audience what they will understand in each section.

| Agenda section | Detail to adapt to the focal field |
| --- | --- |
| Research landscape | Core problem, concepts, publication trends and application domains. |
| Why focus on this domain? | Practical applications, domain publication context, research groups and distinctive constraints. |
| Milestones and their limitations | Earlier methods, the constraints they addressed, and the changes that motivated later approaches. |
| Current frontier | Main problem families, representative mechanisms, training or construction, comparisons and tested scale. |
| What to test next | Open questions derived from evidence, with concrete methods, datasets, baselines and metrics. |

Adjust row count when the scope calls for it. A short section name alone does not meet the agenda requirement. When Presenter Perspective is omitted, use the freed area for legibility and spacing. Do not leave its label or an empty box.

## Count and label evidence consistently

Follow [the research statistics workflow](research-statistics.md) before making quantitative slides. It covers field-specific conferences and journals, query expansion, relevance checks, dated denominators, direction and downstream-task coding, and trend highlighting. Keep every displayed count traceable to deduplicated source records. Use identical categories across charts, animations and tables that describe the same set. State coverage limits where they affect interpretation.

## Select and explain the Current Frontier

Inspect [the robotics selection slide](../assets/frontier-selection-reference.png). Preserve the five criteria below and give each criterion a concrete explanation in the new field. Keep the reference's four readable cards and wider scaling card when that layout fits.

| Criterion shown on the slide | What the description and selected evidence must establish |
| --- | --- |
| CHALLENGING PROBLEM | Identify the practical failure or bottleneck, its consequences, and why strong existing approaches struggle. Use a domain-specific example. |
| ELEGANT, USABLE IDEA | Explain the mechanism, the interface or intervention it changes, and why a reader could implement or use it. Include key assumptions and dependencies. |
| OUTPERFORM STRONG BASELINES | Name the credible baselines and show the measured improvement under comparable tasks and budgets. Include ablations when available. Identify trade-offs and negative results when they determine the conclusion. |
| WORKS FROM LEADING GROUPS | Name the industrial teams, university labs or established open projects responsible for the work. Verify affiliations and show a dated contribution. Use deployment, adoption or influence evidence when available. Treat the group's name as context for interpreting the actual result. |
| DEMONSTRATED SCALING | State what grows, the tested range, and how quality and cost change. Examples include agents, task length, environment diversity, users, repositories, data size or throughput. Distinguish a measured scale sweep from a demonstration at one size, and simulation from deployment. |

Use these criteria to build the candidate set and write the slide. For each selected work, record the evidence or the untested part of each criterion. A benchmark or deployment may be included for a major evaluation or adoption contribution with its evidence type identified. Avoid claiming it outperforms methods or demonstrates team scaling without a corresponding experiment.

Choose the shortlist from the field's development, rather than from a fixed number of tracks or papers. Cover the major problem families, distinct mechanisms, evaluation settings and important recent shifts supported by the sources. Keep a compact mapping from these developments to the chosen works. Add a work when it contributes a missing mechanism, setting or strong result. Consolidate redundant examples and put useful alternatives in the appendix.

The robotics example's four main works and two overview slides are layout examples. Expand the overview to additional slides when the field needs more coverage. If the requested duration cannot support every technical deep dive, retain the overview coverage and move secondary details to the appendix. Explain any remaining major gap.

Every main technical work needs enough content for the audience to understand the problem, method, how it was trained or constructed, test tasks, named baselines and result. Prefer the original architecture or algorithm figure with a concise explanation. Add a separate mathematical or training slide when needed to understand a learned method. A result slide includes a finding sentence and the conditions that make the comparison meaningful. Explain the transition from one work to the next using the unresolved limitation or dependency.

## Build the community map

Use [the rendered Robotics v44 Community slide](../assets/community-reference.png) (slide 15) as the visual input for the layout brief. Inspect the image at presentation size before drafting.

> Use the Robotics Community slide for its full-width field of marks, organization names and short project labels. Organize the new slide into two visually distinct areas, **Closed** and **Open research**. Give each side enough room for the contributions that matter in this field. Preserve the reference’s navy labels, teal links and restrained footer.

- Start with the most influential industry teams, universities, research labs and open-source or standards groups active in the field. Look for one representative paper, product, demo, repository, standard or dataset per group. Select for relevance and evidence, then fill the available slide width and height. Let row count, group count and column widths follow the material.
- Put proprietary products and private implementations under **Closed**. Put public papers, open code, datasets and specifications under **Open research**. Classify the linked contribution. A company can appear on either side according to what the entry links to.
- Prefer the group's official mark or a mark supplied by the project. Keep each entry compact and legible, with the mark above the editable organization and project labels. Link the entry to its primary source and use short labels where helpful.
- Render the slide and compare it with the reference. Check that the two areas read clearly, the field fills the slide, and the marks, labels and links work at presentation size.

## Rebuild embedded charts for Google Slides

1. Identify the chart panels in the working deck. When the request names two charts, replace both in place. If a chart has annual states or a thumbnail strip, rebuild the chart content in those states and thumbnails too. Keep the slide order, layout, and surrounding content.
2. Use the source data or embedded workbook when available. Otherwise, transcribe the values printed in the original. Preserve category and series order, displayed values and precision, units, axis limits and baseline, ticks, legends, annotations, colors, and the chart bounds. Derive bar lengths from the verified values on the original scale. Flag any value that cannot be verified.
3. Draw bars with native rectangles and draw axes, gridlines, and markers with basic slide shapes or lines. Use editable text boxes for titles, category names, tick labels, data labels, and legend text. Use original positions, spacing, alignment, and visual hierarchy. Remove the chart image from the rebuilt panel after verifying the replacement. The rebuilt chart should contain no raster picture, SVG or EMF picture, or outlined text. For a click-through annual view, group each year’s editable shapes as a panel and bind the fade to that group. Verify each animation target and the final static view. Keep photos and figures outside these chart panels as source images.
4. Render the exported PowerPoint and compare both charts against the originals. Verify the numbers, bar lengths, order, colors, alignment, and label fit. Inspect the slide objects or file structure to confirm the bars and text remain separately editable. When Google Slides import is available, open the converted deck and check both charts at presentation size. Select a bar and edit a label in a test copy or confirm the native shape and text objects through the Slides API. Check that annual states do not obscure each other and that the intended static view remains legible if animations differ after import. If Google Slides import cannot be checked, state which local checks passed and that import was unverified.

## Deliver and check

Retain the personal 16:9 template, black Arial Narrow titles, navy/teal structure, light-green highlights and original figure colors. Use editable charts and native tables for survey statistics, with the shape and text workflow above for Google Slides chart panels. Link source images or demos. Give each slide one takeaway and put explanation in the separate speaker text. By default provide editable PPTX, PDF and separate English speaker text. Embed speaker notes only when requested. Verify rendered slides, links and the appendix reading map.

## Acceptance checks

Before delivery, inspect the exported artifact and the supporting evidence.

- Slide 02 has concrete descriptions beside its agenda section titles and matches the actual sequence.
- Presenter Perspective appears only with user-supplied or user-confirmed wording for this talk. Otherwise its box and label are absent.
- Quantitative slides are based on a corpus and a venue-by-year coverage record built for this domain. Relevant leading conferences and journals were considered, missing sources and incomplete years are identified, and the captions use the actual denominators.
- The direction-by-downstream-task table has verified cell counts, a stated ranking direction, bold positive maxima including ties, and a visible trend conclusion. Any secondary emphasis follows the stated legend.
- The frontier selection slide explains all five criteria with domain-specific examples. The overview covers the field's principal developments and each selected work has readable method and result evidence.
- Charts, animations, matrices and narration agree on counts, labels and scope. Original figures remain readable, sources open correctly, and embedded speaker notes match the user's preference.

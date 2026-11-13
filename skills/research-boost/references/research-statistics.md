# Research statistics for a new field

Use this workflow whenever the talk makes claims about publication volume, attention, growth, research directions or downstream applications. Construct the corpus for the current task. The retained deck supplies presentation examples.

## Define the question and source coverage

Record the research question, domain boundary, date range, cutoff date, counting unit, languages covered and inclusion rules before generating the charts. Distinguish the wider research landscape from the focal domain if both are shown.

Select sources from the field's influential papers, domain surveys and official venue scope. Consider the major general AI venues together with the domain's leading specialist conferences and journals. Explain the role of each selected venue and any important exclusion. Read proceedings or journal issue metadata to establish yearly coverage. A search-engine result list alone cannot establish a publication denominator.

These are starting candidates to check for relevance, coverage and current naming. Adapt the list to the actual research question.

| Field | Conference families to consider | Journal families to consider |
| --- | --- | --- |
| Language models and language agents | ACL, EMNLP, NAACL, ICLR, ICML, NeurIPS, AAAI, IJCAI, AAMAS when multi-agent interaction is in scope | TACL, Computational Linguistics, JMLR, TMLR, JAIR |
| Robotics and embodied coordination | ICRA, IROS, RSS, CoRL, with relevant ML, AI and vision venues when they cover the question | IEEE T-RO, IEEE RA-L, IJRR, Science Robotics, Autonomous Robots |
| Software and coding agents | ICSE, FSE, ASE, ISSTA, MSR, with relevant language-model and learning venues | IEEE TSE, ACM TOSEM, Empirical Software Engineering, Automated Software Engineering |
| Agent economies and markets | ACM EC, AAMAS, AAAI, IJCAI, with relevant ML, NLP and systems venues | ACM TEAC, JAAMAS, JAIR, and economics or market-design journals represented in the seed bibliography |
| Other research domains | Identify the main general and specialist conferences from official scope and the seed bibliography | Identify the principal research journals and their relevant article types from the same evidence |

Build a venue-by-year coverage record containing the source URL, retrieval date, included series or article types, total records, abstract availability and known gaps. For proceedings, distinguish main papers, Findings, workshops and auxiliary programs. For journals, define which research article types enter the counts, and how publication year is assigned. Record a journal extension and its earlier conference version as one research work when the unit is unique works, with both venue appearances retained for audit.

Include the current year through the recorded cutoff when requested. Mark partially released proceedings, online-first articles and incomplete years. For a yearly trend, use a consistent venue panel or show the effect of changing coverage. A rise caused by adding venues or improving abstract availability requires a coverage explanation.

## Retrieve across the field's vocabulary

Start from representative papers and their references to collect terms for the problem, mechanisms, application settings and historical names. For multi-agent coordination, this may include coordination, cooperation, collaboration, team planning, task allocation, communication, negotiation, orchestration, workflows, delegation, distributed control and relevant system names. Verify these terms against the field being studied.

Use complementary retrieval passes.

1. Search titles and available abstracts with the expanded term families, spelling variants and abbreviations. Record which query retrieved each candidate.
2. Add papers from the references and citing literature of strong seeds, and search the relevant official proceedings or journal collections for missed terminology.
3. Inspect representative matches for false positives, review influential seeds that were missed, and examine a sample of unmatched records for relevant alternatives. Revise the query and rerun before counting.

Record the result of this coverage check. If it uses a sample, state its size and sampling method. Describe an unmeasured recall as unknown. Search effort or the number of returned records does not establish completeness.

Keep title-only and title-plus-abstract results separate when their available years or records differ. If only part of a venue has abstracts, record the searchable fraction. Use the same searchable fields across years for a directly comparable trend, or identify the limitation in the chart.

Deduplicate by DOI, arXiv identifier, official paper ID and normalized title, resolving revisions and venue versions. Screen relevance using the problem actually studied. A mention of the focal term in related work is insufficient. Retain exclusion reasons and separate uncertain records for review.

## Keep the counting units traceable

Retain stable record identifiers and the fields needed to reproduce each chart.

- Source fields include title, authors, affiliations where verified, DOI or paper ID, source URL, version, venue, article type, publication year and earliest public year.
- Retrieval fields include query family, title or abstract availability, inclusion decision, exclusion reason, duplicate group and confidence.
- Coding fields include research direction, downstream tasks, evaluation setting, evidence type, and the source passage supporting each label.

Use one defined year rule per chart. For publication-rate charts, publication year is usually appropriate. If historical first appearance matters, show earliest public year separately. Use article-level IDs to reconcile the two.

Distinguish these populations in captions and data.

| Population | What it counts |
| --- | --- |
| Venue records | All eligible records in the selected venues and years |
| Retrieved candidates | Unique records matching the search before relevance screening |
| Included research works | Relevant deduplicated studies after screening |
| Coded studies | Included studies with the labels needed for a specific analysis |
| Evaluation-domain slice | Coded studies evaluated on a particular downstream application |
| Qualitative frontier | Representative papers, demos, products and protocols selected for the technical story |

A company blog, demo, standard or production deployment can support the frontier or community story. Include it in a quantitative series only when that series explicitly counts such items, with its own unit and denominator. Keep bibliometric counts distinct from deployment or adoption signals.

Compute rates from matching numerator and denominator populations. For example, matches per 1,000 venue records equals 1,000 times the matched records divided by all eligible records from the same venues, year, fields and inclusion rules. A share within the coded corpus answers a different question. Identify the population in the title or caption.

Generate charts, tables, annual frames and narration from the same recorded data. Reconcile yearly totals, label totals and the study IDs contributing to each cell. Account for overlap, excluded records and uncoded cases. Report a coverage gap when it affects the result.

When reusing authoring or retrieval scripts, inspect their venue lists, year windows, topic labels, counts, captions, axis limits and emphasis rules. Replace inherited constants with the current task's verified data and scope. A copied builder must not silently carry the robotics example's corpus or a previous field's trends into the new talk.

## Derive directions and downstream tasks separately

Build the research-direction labels from the corpus and the literature. They describe the technical challenge or intervention. Downstream tasks describe where the approach was evaluated. An official conference program topic can assist discovery but does not define the whole field's research directions.

Write a short codebook with definitions, inclusion examples, borderline cases and whether each axis is exclusive or multi-label. Use one primary direction only when it represents the study faithfully. Otherwise use multiple labels and show how overlap affects counts.

Cross-tabulate directions and downstream domains using study IDs. Label the unit as studies or evaluations as appropriate. For a multi-domain study, count it once in each supported domain, and explain that domain totals can overlap. Use unknown for an unverified label. Distinguish unknown from zero.

Check sensitive labels against the full paper, especially ambiguous terms such as planning, adaptation, reasoning or multi-agent. Record whether coding was automated, manually checked or independently double-coded. Report agreement statistics only when actual independent coding data exist.

## Highlight trends in matrices and tables

Choose the comparison axis to match the claim. For a table explaining the challenge most studied in each application domain, rank values within each downstream-task column. For a table explaining where a direction is applied, rank within each direction row. State the ranking direction in a compact legend.

- Bold every positive maximum within the stated comparison unit, including ties. Use light-green cell highlighting when it helps locate the leaders.
- When the runner-up matters to the story, emphasize the second-highest distinct positive value with a lighter fill or another clearly stated treatment. The maximum must remain distinguishable.
- Render zero and missing values neutrally. An all-zero column has no highlighted leader. Exclude totals, headers and missing entries from the rank calculation.
- Compute emphasis from the displayed values. If the table presents proportions, rank the proportions. Use the unrounded values only when the legend identifies a precision issue, and resolve displayed ties consistently.
- Use within-column proportions or a companion normalized view when raw column totals differ enough to affect interpretation. Explain both prevalence and within-domain concentration when the evidence supports them.

Verify emphasis after PPTX export by checking the cell text and styling. Selecting or tinting the focal domain is a separate visual cue from bolding its largest values. Make the legend clear when both are used.

Every matrix needs a takeaway title or one short finding sentence naming the actual pattern. Explain which directions dominate which downstream tasks, how the balance changes, or where evidence is sparse. A large cell shows attention in this corpus. Reasons for that attention need separate evidence from the papers.

For attention over time, show counts and an appropriate share or rate, together with yearly coverage. Use several years to support a trend. Avoid describing a recent partial year as a decline without explaining the incomplete coverage. Preserve flat or decreasing findings when those are what the records show.

## Review before delivery

Verify the source coverage, retrieval sample, deduplication and coding enough to support the claims made in the talk. Make the corpus, coverage record and codebook available with the statistics deliverable or in a compact reproducibility appendix.

Confirm that each chart has its actual units, years, source coverage and denominator. Check that every highlighted matrix maximum and runner-up matches the data, that the reading guide covers important missed mechanisms, and that the stated findings follow from the displayed population. If retrieval or coding remains partial, name the sample and the limitation instead of presenting it as the whole field.

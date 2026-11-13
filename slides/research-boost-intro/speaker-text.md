# ResearchBoost introduction: English speaker text

## Slide 01 - ResearchBoost

However you use AI to accelerate your research, someone is moving faster. This is the project’s invitation to improve how you learn a field. Bring the best papers, literature reviews, notes and research-group knowledge you already have. ResearchBoost helps organize them into a field map, reading path and next research question.

## Slide 02 - Agenda

We will look at the four input modes, the research process, the robotics example, the installation flow and the evidence standards. The final slide acknowledges the keynote talks that inspired the history and research-impact parts of the workflow.

## Slide 03 - Start with quality materials you already have

For a stronger starting point, bring quality papers, literature reviews, curated reading lists, relevant notes, course or talk materials, and research-group links you already find useful. These provide context about your intended problems, vocabulary and community. Explain why the materials matter and what you want to understand. Use keywords to expand discovery, or start from keywords when no materials are available. Verify supplied claims and include relevant alternatives beyond the starting set.

## Slide 04 - Move from a seed to a testable next step

Begin with a scope record. Retrieve and screen sources, verify claims in primary material, map the problems and groups, and then explain why the field changed. The output should help a newcomer decide what to read and what experiment to attempt. Quantitative trends require an auditable corpus and coverage record.

## Slide 05 - Explain why a field changed

A useful history connects each milestone to a changed constraint and to the limitation that remains. The robotics example moves from job allocation and routing to uncertain field settings, language plans and local execution. These are selected milestones from the retained demo, not a new exhaustive historical review. Pascale Fung’s keynote inspired the creator’s emphasis on this style of historical understanding.

Sources for the selected history examples: [MRTA](https://robotics.usc.edu/publications/media/uploads/pubs/347.pdf) · [Kiva](https://onlinelibrary.wiley.com/doi/abs/10.1609/aimag.v29i1.2082) · [CERBERUS](https://arxiv.org/abs/2207.04914) · [RoCo](https://ieeexplore.ieee.org/document/10610855) · [CHORUS](https://chorus-model.github.io/). See the full demo for intermediate milestones and experimental conditions.

## Slide 06 - Choose frontier work using five criteria

The creator adapted these five criteria after being inspired by Graham Neubig’s keynote. For each candidate, record actual evidence and what is untested. A well-known group gives context but cannot substitute for a strong result. Scaling requires identifying what grows and how quality and cost change; a one-size demonstration is not a scale sweep.

## Slide 07 - Worked example: multi-robot coordination

The included demo contains 46 slides. A two-robot basket lift makes timing dependencies visible before statistics and technical terminology appear. The talk then maps research activity, explains historical constraints, compares current methods and proposes experiments. Its data are a retained November 2026 snapshot. The full raw search is not bundled, so a new run must rebuild coverage and counts.

## Slide 08 - Install once, then bring your own question

Download or clone the repository and run the installer from its root. The installer copies the complete skill and refuses to overwrite an existing installation. Open the destination project in Codex and invoke ResearchBoost. Share quality papers, literature reviews, research materials and group links, then state your research question, audience and desired outputs. Installation and brief preparation use Python’s standard library; research and slide creation require host tools.

## Slide 09 - Adapt the brief before starting research

Start the brief from quality materials you already have. Attach or link the actual papers, reviews, notes and official research-group pages, and explain their relevance to your question. Ask ResearchBoost to read them first, verify claims against primary sources, and use keywords to find gaps and competing approaches. Specify the audience, talk length and source cutoff. The example’s bracketed fields are intentionally editable.

## Slide 10 - Keep the skill reusable and each run traceable

The repository separates the installable skill from its worked example, project introduction and blank tables. Keep run-specific sources and outputs outside the installed skill so future work does not silently alter the template or mix corpora. The installer and brief builder are optional local conveniences.

## Slide 11 - Make evidence easy to inspect

Review the evidence and the artifact separately. A valid file is not proof of a correct scientific claim. Check the date and coverage, follow numeric claims to source records, and distinguish simulation from hardware. Render every slide and verify the reading path. The helper scripts check packaging and safe installation; they do not validate research quality.

## Slide 12 - Inspiration and thanks

Thank you to Pascale Fung: her EMNLP 2026 keynote inspired the creator to understand a field through its history. Thank you to Graham Neubig: his EMNLP 2026 keynote helped the creator select criteria for research impact. The official conference program verifies the talk identities and titles. The operational criteria in this project are the creator’s adaptation, not a verbatim keynote checklist. Neither speaker is affiliated with or endorses ResearchBoost.

Sources: [EMNLP 2026 keynote program](https://2026.emnlp.org/program/keynotes/) · [Official Codex skill documentation](https://learn.chatgpt.com/docs/build-skills)

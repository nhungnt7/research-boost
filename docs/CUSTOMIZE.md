# Adapt ResearchBoost to your field

Keep the skill and retained template as reusable resources. Put each research run in a separate folder, with its own brief, sources, corpus and outputs.

## Start with quality materials you already have

For the most useful starting point, share strong papers, a literature review or survey, a curated reading list, relevant notes, course/talk materials, and links to research groups you already follow. This gives ResearchBoost more context than a keyword-only brief about the problems, vocabulary, methods and communities you care about.

Tell the skill which materials are especially useful, why you trust them, which questions they cover, and what is missing or unclear. It should read accessible inputs first, trace secondary claims back to primary sources, and then search beyond your materials for gaps and alternative approaches. The supplied collection guides the search; it does not establish complete coverage.

Use keywords to extend this starting set. When you have no materials yet, keywords remain a practical way to begin. [Copy a materials-first prompt](../examples/prompts/materials.md).

## Make a brief

```sh
python3 scripts/new_brief.py --mode papers --topic "Your research question"   --seed "DOI, arXiv URL, or local PDF path" --out runs/first-brief
```

Supported `--mode` values: `papers`, `keywords`, `person`, `group`, `mixed`. Use `papers` for papers and related reading materials; use `mixed` to combine them with group/profile links or keywords. Repeat `--seed` for multiple seeds. Set `--audience`, `--minutes`, `--years`, and `--cutoff` when useful. The script records your choices; your agent does the research.

## Start from papers

Provide the actual PDFs, links or bibliography, together with any quality literature reviews, reading lists or notes you already have. Say which paper is the starting point, what you want to understand, and which assumptions matter. Ask the agent to follow references and citing work, include alternatives, and explain how each selected paper changes the problem.

## Start from keywords

Supply the topic, synonyms, exclusions and desired years. Ask for a query log and venue/journal coverage before requesting counts. A search result total is not a publication denominator.

## Start from a person

Supply a name plus an official profile. Specify whether you want their research trajectory or a whole-field map seeded by their work. Ask for competing approaches and verified affiliations at publication time.

## Start from a lab or team

Supply the official lab URL and focal projects. Distinguish the lab's public papers, open artifacts, products and deployments. Ask which adjacent groups address the same problem and what evidence separates their approaches.

## Change output and style

Set audience, talk length, language, technical depth and desired deliverables. Supply your own PPTX to override the retained visual template. Keep the detailed agenda, evidence ledger, problem-driven history and frontier, and two future slides unless your purpose calls for another structure. Presenter Perspective is optional and requires your wording or confirmation.

## Reuse the blank tables

`templates/` includes a source ledger, venue coverage, frontier criteria, paper corpus and experiment plan. The agent should fill these from verified evidence, not treat empty cells as zero evidence or generate chart values to complete a layout.

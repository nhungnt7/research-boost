#!/usr/bin/env python3
"""Prepare a research brief and agent prompt; no research or API calls are made."""
import argparse
from datetime import date
import json
from pathlib import Path

MODES = ('papers', 'keywords', 'person', 'group', 'mixed')

def create_brief(out, mode, topic, seeds, audience, minutes, years, cutoff):
    if mode not in MODES or minutes <= 0 or not topic.strip() or not seeds:
        raise ValueError('Supply a valid mode, topic, seed and positive duration')
    date.fromisoformat(cutoff)
    out = Path(out)
    if out.exists():
        raise FileExistsError('Output directory already exists: ' + str(out))
    brief = dict(topic=topic, research_question='', mode=mode, seeds=seeds,
                 audience=audience, duration_minutes=minutes, language='English',
                 years=years, cutoff=cutoff, exclude=[], presenter_perspective=None,
                 deliverables=['editable presentation', 'PDF', 'English speaker text',
                               'source ledger', 'reading path', 'corpus and coverage for statistics'])
    prompt = (f'Use $research-boost to help me get up to speed on {topic}.\n'
              f'Start from {mode}: {json.dumps(seeds, ensure_ascii=False)}.\n'
              f'Audience: {audience}. Duration: {minutes} minutes. Language: English.\n'
              f'Years: {years or "choose a justified scope"}. Source cutoff: {cutoff}.\n'
              'Explain the core problems, community, history and current frontier.\n'
              'Use the five frontier criteria and two future slides with concrete experiments.\n'
              'Verify primary sources and keep statistics traceable to a dated corpus.\n'
              'Provide separate English speaker text, a source ledger and a reading path.\n'
              'Omit Presenter Perspective. Record inaccessible sources and untested claims.\n')
    out.mkdir(parents=True)
    (out / 'brief.json').write_text(json.dumps(brief, indent=2, ensure_ascii=False) + '\n')
    (out / 'prompt.txt').write_text(prompt)
    return out

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--mode', required=True, choices=MODES)
    parser.add_argument('--topic', required=True)
    parser.add_argument('--seed', action='append', required=True, help='Repeat for several seeds')
    parser.add_argument('--audience', default='Researchers entering this field')
    parser.add_argument('--minutes', type=int, default=30)
    parser.add_argument('--years', default='')
    parser.add_argument('--cutoff', default=date.today().isoformat())
    parser.add_argument('--out', required=True, type=Path)
    args = parser.parse_args()
    try:
        out = create_brief(args.out, args.mode, args.topic, args.seed,
                           args.audience, args.minutes, args.years, args.cutoff)
    except (ValueError, OSError) as error:
        parser.error(str(error))
    print('Prepared ' + str(out) + '. Give brief.json and prompt.txt to your agent.')

if __name__ == '__main__':
    main()

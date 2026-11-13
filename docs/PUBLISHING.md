# Publish your copy to GitHub

The project is prepared locally. No remote repository is created by these instructions or by the package tools.

1. Review `README.md`, acknowledgments and third-party notices. Add your public author/contact details if you want them. The proposed repository name is `research-boost`; availability has not been checked.
2. Create an empty GitHub repository named `research-boost` in your account.
3. From this project folder, run:

   ```sh
   python3 scripts/validate.py
   python3 -m unittest discover -s tests
   git init -b main
   git add .
   git commit -m "Add ResearchBoost research onboarding skill and robotics demo"
   ```

4. Copy the repository remote URL shown by GitHub, then run `git remote add origin` followed by that URL, and `git push -u origin main`.
5. The README's relative links work after upload. Add a short description: **Build research expertise faster from papers, keywords, researchers, or labs.** Suggested topics: `agent-skills`, `research`, `literature-review`, `research-onboarding`, `presentations`.
6. For a release, attach the prepared ZIP so people can download it without Git. Users can install with the included script, or copy the entire `skills/research-boost` folder to their supported skills directory.

GitHub Actions checks the package and helper scripts with Python's standard library. It does not execute the agent research workflow or verify scientific claims.

## Copy for a launch post

**However you use AI to accelerate your research, someone is moving faster.**

ResearchBoost helps you turn quality papers, literature reviews, existing research materials and research-group knowledge into a source-linked field map, a reading path and a research talk. Understand how the field developed, compare its frontier, and choose what to investigate next.

Bring the best materials you already have. Use keywords to explore beyond them.

Watch the [promotional field walkthrough](../examples/robotics-coordination/promo/researchboost-promo.mp4) to follow the illustrated workflow from LLM-agent coordination and seed papers to a robotics field presentation. It explains why the problem, statistics, history, frontier evidence, experiments and paper list help you understand the new field.

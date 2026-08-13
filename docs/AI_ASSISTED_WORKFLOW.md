# Responsible AI-assisted thesis workflow

AI tools can search a large source tree, propose narrowly scoped edits, run builds and
help interpret compiler errors. They cannot assume authorship responsibility, verify
evidence automatically, decide what an examiner meant, or safely receive confidential
material by default.

## Install one provider only if you want it

- **Codex:** follow the official [Codex IDE extension guide](https://developers.openai.com/codex/ide)
  and its official marketplace installation link. The repository's `AGENTS.md` supplies
  project instructions.
- **Claude Code:** follow Anthropic's official [VS Code integration guide](https://code.claude.com/docs/en/ide-integrations).
  The repository's `CLAUDE.md` supplies equivalent project instructions.

These extensions are optional and are deliberately not forced through
`.vscode/extensions.json`. Accounts, availability, pricing, data controls and supported
platforms can change; consult the provider's current official documentation.

## Safe working sequence

1. Classify the material before sharing it. Exclude identifiable participants,
   confidential examiner reports, unpublished third-party manuscripts, credentials and
   restricted research data unless an explicitly approved system and workflow permits it.
2. Ask for a read-only explanation or plan first when the requested change is broad.
3. Name the exact files and the intended outcome.
4. Require preservation of citations, labels, equations, examiner IDs and LaTeX syntax.
5. Review the diff; reject claims, citations or numbers that cannot be verified.
6. Build the relevant PDF and inspect the rendered pages.
7. Record and disclose AI use exactly as required by current university, ethics,
   publisher and discipline instructions.

Example prompt:

```text
Read chapters/03-methodology/chapter.tex and the figure it inputs. Do not edit yet.
Identify where the prose fails to explain Figure 3.1 and propose a two-sentence revision.
Preserve the figure label and do not invent methods, results, citations or approval IDs.
After I approve, make only that edit and run make clean-thesis.
```

Examiner prompt:

```text
Work only on comment E2-01. Preserve the examiner comment verbatim in the response file.
Compare the comment with the relevant thesis passage, propose the substantive correction,
and identify the evidence needed. Do not implement until I approve the wording. When
approved, use CorrectionAdd or CorrectionReplace with ID E2-01-a, build make response,
and report the rendered page number.
```

## UTS requirement

As checked on 13 August 2026, version 1.19 of the official
[Graduate Research Candidature Management, Thesis Preparation and Submission Procedures](https://www.uts.edu.au/globalassets/shared-media/documents/grs/graduate-research-candidature-management-thesis-preparation-submission-procedures.pdf)
requires every UTS graduate research student to indicate how generative AI was used in
the research or preparation of the thesis. It distinguishes four categories:

- **No substantive use:** no deliberate use beyond AI unavoidably embedded in common
  software or search tools.
- **Assistive use:** support for the researcher's expression or workflow without AI
  supplying original ideas, interpretations or data.
- **Generative use:** AI production of material that may enter the research output,
  including text, code, images or summaries, even when later rewritten.
- **Analytical use:** AI interpretation, evaluation, classification, critique, pattern
  identification or suggested conclusions.

The selected current statement belongs in the Certificate of Original Authorship. When
assistive, generative or analytical use is declared, the current procedure also requires
a table identifying the affected chapter/location, tool and version, platform, purpose,
and how outputs were incorporated. The worked structure is in
`frontmatter/generative-ai-use.tex`.

Do not assume that using Codex, Claude or ChatGPT for writing, editing, coding,
summarising or analysis qualifies as “no substantive use.” Classify the actual use and
confirm it with the supervisory panel where necessary.

UTS researchers must also consult the current
[Use of AI in Research Guidelines](https://www.uts.edu.au/about/leadership-governance/policies/a-z/use-of-ai-in-research-guidelines).
They require documentation throughout the project, human responsibility, verification
of claims and citations, attention to bias, and compliance with research integrity,
privacy, confidentiality, ethics, intellectual-property, licensing, data-classification
and cybersecurity obligations.

The UTS guidelines' documentation checklist includes the tool and version, date,
prompts or queries, generated responses, follow-up interactions, the person who queried,
and durable records of relevant chats. Keep this research record in an approved secure
location; do not publish sensitive prompts or data in GitHub issues.

This repository includes a practical ongoing log at
[`records/ai-use-log.example.csv`](../records/ai-use-log.example.csv). Copy it to
`records/ai-use-log.csv` before beginning real work. The private filename is ignored by
Git by default. Record one materially distinct activity per row, including:

1. stable record ID and date;
2. exact chapter, section or source file affected;
3. no substantive, assistive, generative or analytical category;
4. provider, tool, model/version and platform;
5. purpose and a secure reference to prompts and responses;
6. exactly what was incorporated or rejected;
7. human verification performed;
8. data classification and relevant approval/policy check; and
9. notes needed to prepare the final declaration.

The declaration is a concise submission statement; the log is the evidence used to
prepare it. Neither should contain false, guessed or reconstructed information.

These requirements can change. Re-download the official procedure immediately before
submission and follow any newer outcome-letter, faculty, school, ethics, funder,
publisher and supervisory instructions. Never treat an AI provider's convenience as
permission to upload university or research data.

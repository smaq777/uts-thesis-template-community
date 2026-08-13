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

UTS researchers must consult the current
[Use of AI in Research Guidelines](https://www.uts.edu.au/about/leadership-governance/policies/a-z/use-of-ai-in-research-guidelines).
The guidance requires careful attention to research integrity, privacy, security,
verification and disclosure. UTS thesis-preparation procedures and school instructions
may impose additional or updated requirements. Never treat an AI provider's convenience
as permission to upload university or research data.


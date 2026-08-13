# Community LaTeX Thesis Template

An unofficial, logo-free and fully worked thesis template for UTS HDR students and
students at other universities. It includes example prose, figures, tables,
references, chapter organisation, VS Code configuration, an Overleaf route, and a
traceable post-examination revision workflow.

> **UTS students:** this repository is practical writing and typesetting guidance,
> not an official UTS template or source of policy. Requirements change. Always follow
> your current examination outcome letter, supervisory panel, school/faculty research
> office, Graduate Research School instructions, and the current
> [UTS thesis submission and examination page](https://www.uts.edu.au/research/graduate/current-research-students/thesis-submission-and-examination).

No UTS logo is distributed. The title page contains a neutral placeholder. Only add an
institutional logo if you are authorised to use it.

## Choose your route

| Route | Best for | What you need |
|---|---|---|
| Local VS Code | Large theses, fast builds, Git history, local AI tools | A TeX distribution, VS Code and LaTeX Workshop |
| Overleaf | Students wanting a browser-only setup | An Overleaf account and the repository ZIP |

Local writing keeps large image collections and build files on your device, provides
fast search and version control, and lets tools such as Codex or Claude work with the
specific source files you approve. AI is optional: it does not replace authorship,
source verification, research judgement or institutional disclosure requirements.

## First local build

1. Download this repository with **Code → Download ZIP**, or clone it:

   ```bash
   git clone https://github.com/smaq777/uts-thesis-template-community.git
   cd uts-thesis-template-community
   ```

2. Install a TeX distribution:

   - macOS: [MacTeX](https://www.tug.org/mactex/)
   - Windows: [MiKTeX](https://miktex.org/download) or [TeX Live](https://tug.org/texlive/)
   - Linux: install TeX Live through your distribution, including XeLaTeX, BibTeX and
     `latexmk` (for Ubuntu/Debian, see [the exact command](docs/LOCAL_SETUP.md#linux-ubuntudebian)).

3. Install [Visual Studio Code](https://code.visualstudio.com/Download), open this
   folder, and accept its extension recommendations. The required extension is
   [LaTeX Workshop (`James-Yu.latex-workshop`)](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop).
   It supplies the build integration, log view, SyncTeX and an in-editor PDF tab.

4. In the VS Code terminal, verify and build:

   ```bash
   make doctor
   make all
   ```

5. Open these generated files:

   - `build/Thesis_CLEAN.pdf` — final prose, without revision marks
   - `build/Thesis_REVIEW.pdf` — examiner IDs, colours, deletions and margin markers
   - `build/Revision_Response.pdf` — separate response table with linked page numbers

Read [Local setup](docs/LOCAL_SETUP.md) if a command is missing or the build fails.

## Start replacing examples

Work in this order:

1. Replace all values in `config/thesis-details.tex`.
2. Review every file under `frontmatter/`; use the exact current declarations required
   by your university.
3. Rename chapter folders if your approved structure differs, then update `thesis.tex`.
4. Replace example text one section at a time. Search globally for `Replace this
   example`, `placeholder`, `synthetic`, `20XX` and `00000000` before submission.
5. Replace `bibliography/references.bib` with verified records from your reference
   manager. Never accept an AI-generated citation without checking the original source.
6. Run `make all`, read the PDFs as a reader, and resolve warnings that affect content.

## Folder architecture

```text
.
├── thesis.tex                       # Shared thesis body
├── thesis-clean.tex                 # Clean output entry point
├── thesis-review.tex                # Review output entry point
├── revision-response.tex            # Examiner response entry point
├── config/                          # Student, institution, package and revision settings
├── frontmatter/                     # Title, declaration, abstract and required statements
├── chapters/
│   ├── 01-introduction/chapter.tex
│   └── ...
├── figures/
│   ├── 03-methodology/              # Images or TikZ belonging to that chapter
│   └── shared/                      # Reused figures only
├── tables/
│   ├── 04-results/                  # Table source belonging to that chapter
│   └── shared/                      # Reused tables only
├── appendices/                      # One named folder per appendix
├── bibliography/references.bib
├── docs/                            # Student guides
└── build/                           # Generated files; never edit these
```

The matching number and descriptive name make a figure or table findable even when the
thesis contains hundreds of assets. Use descriptive filenames such as
`participant-flow.pdf`, not `figure-new-final2.png`. See
[File organisation](docs/FILE_ORGANISATION.md) for naming and scaling guidance.

## Examination corrections

Examiner IDs drive both the review thesis and the response table:

```tex
\CorrectionAdd{E1-01}{a}{This paragraph was added in response to Examiner 1, comment 1.}
\CorrectionReplace{E2-03}{a}{old wording}{revised wording}
\CorrectionDelete{E3-02}{a}{text removed after review}
```

The first two fields create the stable label `E1-01-a`; use `b`, `c` and so on when one
comment requires several changes. Never use colour alone: the ID is printed in the text
and response table. Read the complete [Examination and revision workflow](docs/EXAMINATION_WORKFLOW.md)
before modifying these examples.

## Overleaf

Download the repository ZIP, create a blank Overleaf project, upload the ZIP contents,
set the compiler to **XeLaTeX**, and set the main document to `thesis-clean.tex`.
Overleaf is convenient for browser-only collaboration; a very large thesis may build
more slowly or encounter project limits. Full steps are in [Overleaf setup](docs/OVERLEAF.md).

## AI-assisted workflow (optional)

The repository provides `AGENTS.md` for Codex and `CLAUDE.md` for Claude. They instruct
an assistant to make small, reviewable edits, preserve citations and examiner IDs, build
the requested output, and never invent evidence. Install only the provider you choose:

- [OpenAI Codex IDE extension](https://developers.openai.com/codex/ide) — official
  setup and marketplace link.
- [Claude Code for VS Code](https://code.claude.com/docs/en/ide-integrations) — official
  requirements, installation and sign-in instructions.

Before sending any content to any provider, check ethics approval, consent, contracts,
data classification, privacy, confidentiality and university policy. UTS researchers
must consult the current [Use of AI in Research Guidelines](https://www.uts.edu.au/about/leadership-governance/policies/a-z/use-of-ai-in-research-guidelines),
verify outputs and make required disclosures. See [Responsible AI workflow](docs/AI_ASSISTED_WORKFLOW.md).

## UTS-specific checkpoints

UTS students should check, at minimum:

- [Thesis submission and examination](https://www.uts.edu.au/research/graduate/current-research-students/thesis-submission-and-examination)
- [Graduate research policies, guides and forms](https://www.uts.edu.au/research/graduate/current-research-students/policies-guides-and-forms)
- [HDR online forms](https://www.uts.edu.au/research/graduate/current-research-students/policies-guides-and-forms/hdr-online-forms)
- [Student Rules, Section 11](https://www.uts.edu.au/about/leadership-governance/governance/rules/student-rules/section-11)
- the instructions issued by your school/faculty and your individual outcome letter.

The links above were checked on 13 August 2026. Web content, forms, required wording and
procedures can change after that date.

Before changing GitHub visibility, complete the [public release checklist](docs/PUBLIC_RELEASE_CHECKLIST.md).

## Attribution, licence and status

This community edition is maintained by **Saleh Alqahtani (`@smaq777`)** and is
substantially reorganised and extended from the publicly available UTS thesis template
by **Dr Chandranath Adak**. It does not claim that the original author endorsed these
changes or granted a private permission beyond the published licence.

The LaTeX template derivative is distributed under LPPL 1.3c; original documentation in
`docs/` is CC BY 4.0; repository automation is MIT. Read [LICENSE.md](LICENSE.md) and
[CREDITS.md](CREDITS.md). This repository is unofficial, carries no warranty and is not
endorsed by UTS.

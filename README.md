# Community LaTeX Thesis Template

An unofficial, logo-free and fully worked LaTeX thesis template maintained by
**Saleh Alqahtani (`@smaq777`)**. It is designed first for UTS Higher Degree by
Research students, while remaining reusable by students at other universities.

The repository is deliberately more than a collection of `.tex` files. It provides a
local VS Code workspace, realistic placeholder chapters, organised chapter assets,
three examination outputs, Git revision governance, Overleaf instructions, and safe
handoff files for Codex or Claude.

> **UTS students:** this is community guidance, not an official UTS template or source
> of policy. Requirements, forms and required declarations can change. Always follow
> your current examination outcome letter, supervisory panel, school/faculty research
> office, Graduate Research School instructions, and the current
> [UTS thesis submission and examination page](https://www.uts.edu.au/research/graduate/current-research-students/thesis-submission-and-examination).

No UTS logo is distributed. The title page uses a neutral placeholder. Add an
institutional logo only if you are authorised to use it.

## Preview before installing

GitHub can open these example PDFs directly in the browser:

- [Clean thesis preview](examples/pdfs/Thesis_CLEAN.pdf) — the submission-style copy.
- [Review thesis preview](examples/pdfs/Thesis_REVIEW.pdf) — changes, examiner IDs and
  margin markers visible to a supervisor.
- [Revision response preview](examples/pdfs/Revision_Response.pdf) — the separate
  examiner-response table.

All names, prose, data, figures and references in the examples are synthetic
placeholders. They demonstrate structure; they are not a thesis and must not be
submitted.

## Contents

- [Why work locally?](#why-work-locally)
- [Choose a route](#choose-a-route)
- [Required software and extensions](#required-software-and-extensions)
- [Local installation: first successful build](#local-installation-first-successful-build)
- [What every build command does](#what-every-build-command-does)
- [Your first writing session](#your-first-writing-session)
- [Folder architecture](#folder-architecture)
- [Adding chapters, figures, tables, equations and references](#adding-chapters-figures-tables-equations-and-references)
- [Revision history with GitHub issues and branches](#revision-history-with-github-issues-and-branches)
- [Examination corrections and three final outputs](#examination-corrections-and-three-final-outputs)
- [Using Codex or Claude responsibly](#using-codex-or-claude-responsibly)
- [Overleaf route](#overleaf-route)
- [Troubleshooting](#troubleshooting)
- [UTS checkpoints](#uts-checkpoints)
- [Attribution, licence and status](#attribution-licence-and-status)

## Why work locally?

A thesis grows into hundreds of source files, images, tables, citations and build
artefacts. A local project keeps that collection on your own Mac, Windows PC or Linux
machine and gives you:

- fast file search, rename and navigation in VS Code;
- chapter-specific figure and table folders instead of one enormous asset directory;
- Git history, branches and milestone tags, so old accepted versions remain
  recoverable;
- repeatable one-command builds without repeatedly uploading a large project;
- an integrated PDF tab with source-to-PDF and PDF-to-source navigation;
- local automation for building clean, review and response documents together;
- optional access for an AI coding/writing assistant to only the files you approve;
- offline writing and control over when the project is synchronised.

Local work is not automatically faster in every situation: speed depends on your
machine, image sizes, bibliography and LaTeX packages. It also requires a one-time TeX
installation. The advantage is control and repeatability. Overleaf remains an excellent
browser-only route for beginners and real-time collaboration, but very large projects
can take longer to upload or compile and may encounter account or project limits.

## Choose a route

| Route | Best for | Main trade-off |
|---|---|---|
| **Local VS Code (recommended)** | Large theses, Git history, repeatable builds, local AI tools | Requires VS Code and a TeX distribution |
| **Overleaf** | No-install browser setup and live co-authoring | Large projects may upload/build more slowly; Git and local automation are reduced |
| **Hybrid** | Local master copy plus occasional Overleaf collaboration | Requires discipline about which copy is authoritative |

If you use a hybrid workflow, declare one authoritative copy. Do not independently edit
local and Overleaf copies and later try to combine them manually.

## Required software and extensions

Install a TeX distribution **and** an editor. LaTeX Workshop does not contain the TeX
compiler by itself.

| Item | Required? | Purpose | Official download or instructions |
|---|---:|---|---|
| MacTeX | macOS | XeLaTeX, BibTeX, `latexmk` and standard packages | [tug.org/mactex](https://www.tug.org/mactex/) |
| MiKTeX or TeX Live | Windows | LaTeX compiler and packages | [MiKTeX](https://miktex.org/download) / [TeX Live](https://tug.org/texlive/) |
| TeX Live | Linux | LaTeX compiler and packages | [TeX Live](https://tug.org/texlive/) |
| Visual Studio Code | Local route | Source editor, terminal and extension host | [code.visualstudio.com/Download](https://code.visualstudio.com/Download) |
| LaTeX Workshop | Yes in VS Code | Builds LaTeX, shows logs, PDF preview and SyncTeX | [`James-Yu.latex-workshop`](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop) |
| Code Spell Checker | Recommended | Catches spelling mistakes in prose | [`streetsidesoftware.code-spell-checker`](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker) |
| LTeX+ | Optional | Language and grammar checking for LaTeX | [`ltex-plus.vscode-ltex-plus`](https://marketplace.visualstudio.com/items?itemName=ltex-plus.vscode-ltex-plus) |
| Git | Recommended | Version history, branches, tags and GitHub use | [git-scm.com/downloads](https://git-scm.com/downloads) |
| GitHub Desktop | Optional | Visual Git interface if terminal Git is unfamiliar | [desktop.github.com](https://desktop.github.com/download/) |
| Codex IDE extension | Optional | OpenAI agent inside VS Code | [Official Codex IDE setup](https://developers.openai.com/codex/ide) |
| Claude Code | Optional | Anthropic agent integration | [Official VS Code integration](https://code.claude.com/docs/en/ide-integrations) |

The included [`.vscode/extensions.json`](.vscode/extensions.json) recommends the editor
extensions. The included [`.vscode/settings.json`](.vscode/settings.json) configures the
repository build recipes and in-editor PDF viewer. Restart VS Code after installing a
TeX distribution so its terminal can find the new commands.

## Local installation: first successful build

### 1. Obtain the files

**Beginner:** select **Code → Download ZIP** on GitHub, extract the ZIP, and open the
extracted folder in VS Code.

**Git user:** clone the repository:

```bash
git clone https://github.com/smaq777/uts-thesis-template-community.git
cd uts-thesis-template-community
code .
```

If `code` is not recognised, open VS Code manually and choose **File → Open Folder**.

### 2. Install the compiler

- **macOS:** install MacTeX. The full distribution is large but avoids repeated package
  installation later. Close and reopen VS Code.
- **Windows:** install MiKTeX or TeX Live. Allow MiKTeX to install missing packages if
  prompted. Close and reopen VS Code.
- **Ubuntu/Debian Linux:** run the package command documented in
  [Local setup](docs/LOCAL_SETUP.md#linux-ubuntudebian).

### 3. Install the VS Code recommendations

Open the Extensions view with `Cmd+Shift+X` on macOS or `Ctrl+Shift+X` on Windows/Linux.
Search for the exact identifiers in the table above. At minimum install LaTeX Workshop.
When VS Code offers **Install Workspace Recommended Extensions**, accept it.

### 4. Diagnose before building

Open **Terminal → New Terminal** inside VS Code and run:

```bash
make doctor
```

It must find `xelatex`, `bibtex` and `latexmk`. If one is missing, do not edit recipes
randomly; finish the TeX installation and restart VS Code. Windows users without
`make` can use the LaTeX Workshop build button or the direct `latexmk` commands in
[Local setup](docs/LOCAL_SETUP.md).

### 5. Build all outputs

```bash
make all
```

Open:

- `build/Thesis_CLEAN.pdf`
- `build/Thesis_REVIEW.pdf`
- `build/Revision_Response.pdf`

In VS Code, open `thesis-clean.tex`, select **LaTeX Workshop: Build LaTeX project** from
the Command Palette, then select **LaTeX Workshop: View LaTeX PDF file**. The PDF opens
inside VS Code. `Cmd+Option+J` on macOS or `Ctrl+Alt+J` on Windows/Linux performs
forward SyncTeX from source to PDF; inverse SyncTeX behaviour depends on platform and
mouse settings.

## What every build command does

| Command | Result |
|---|---|
| `make doctor` | Confirms the required local tools are visible |
| `make clean-thesis` | Builds `build/Thesis_CLEAN.pdf` |
| `make review` | Builds `build/Thesis_REVIEW.pdf` with correction marks |
| `make response` | Builds `build/Revision_Response.pdf` after the review thesis |
| `make all` | Builds all three deliverables |
| `make watch` | Watches source files and rebuilds the clean thesis while you write |
| `make previews` | Builds and refreshes the three public examples under `examples/pdfs/` |
| `make clean` | Removes generated build files; it does not delete thesis source |

Generated files belong in `build/`. Never correct a PDF directly and never edit `.aux`,
`.bbl`, `.log`, `.toc` or `.synctex.gz` files. Correct the source and rebuild.

## Your first writing session

Keep the example content until one complete build works. Then replace it gradually:

1. Create a private backup or Git repository before entering personal information.
2. Replace every value in [`config/thesis-details.tex`](config/thesis-details.tex).
3. Review every file in [`frontmatter/`](frontmatter/). Use the exact current wording
   required by your institution, school and degree.
4. Replace the abstract and Chapter 1 examples first. Build after each small group of
   changes so errors stay easy to locate.
5. Rename chapter folders only when necessary, then update the corresponding `\input`
   lines in [`thesis.tex`](thesis.tex).
6. Replace synthetic bibliography entries with records verified against the original
   publications or exported from your reference manager.
7. Search globally for `Replace this example`, `placeholder`, `synthetic`, `20XX` and
   `00000000` before any real submission.
8. Run `make all`, read each PDF as a reader, and ask another person to inspect it.

A productive rhythm is small and boring: edit one section, save, build, inspect, commit.
That rhythm makes thesis writing calmer because each problem has a small search area.

## Folder architecture

```text
.
├── thesis.tex                         # Shared thesis body and chapter order
├── thesis-clean.tex                   # Clean output entry point
├── thesis-review.tex                  # Tracked/review output entry point
├── revision-response.tex              # Examiner-response entry point
├── config/                            # Metadata, packages, macros and revision settings
├── frontmatter/                       # Title, declaration, abstract and required statements
├── chapters/
│   ├── 01-introduction/
│   │   ├── chapter.tex                # Chapter assembly file
│   │   └── sections/                  # Optional large section files
│   ├── 02-literature-review/
│   ├── 03-methodology/
│   ├── 04-results/
│   ├── 05-discussion/
│   └── 06-conclusion/
├── figures/
│   ├── 01-introduction/               # Figures used by Chapter 1
│   ├── 03-methodology/                # Figures used by Chapter 3
│   └── shared/                        # Genuinely reused figures only
├── tables/
│   ├── 03-methodology/                # Table source used by Chapter 3
│   ├── 04-results/                    # Table source used by Chapter 4
│   └── shared/                        # Genuinely reused tables only
├── appendices/                        # One descriptive folder per appendix
├── bibliography/references.bib
├── examples/pdfs/                     # Clickable public previews
├── docs/                              # Detailed guides
└── build/                             # Generated locally; never edit
```

Matching numeric prefixes make chapters and their assets easy to find when hundreds of
files exist. Use descriptive lowercase filenames such as `participant-flow.pdf` and
`model-performance.tex`, not `figure-new-final2.png` or `table1.tex`. Read
[File organisation](docs/FILE_ORGANISATION.md) for naming, image formats and scaling.

## Adding chapters, figures, tables, equations and references

### Chapter or section

Copy the closest example chapter. Keep `chapter.tex` as its assembly file. When a
section becomes difficult to navigate, create `sections/descriptive-name.tex` and input
it from the chapter:

```tex
\input{chapters/03-methodology/sections/sampling-strategy}
```

### Figure

Put a Chapter 3 image in `figures/03-methodology/`, then use a stable label:

```tex
\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.85\textwidth]{figures/03-methodology/participant-flow.pdf}
  \caption{Participant recruitment and analysis flow.}
  \label{fig:method-participant-flow}
\end{figure}
```

Refer to it in prose as `Figure~\ref{fig:method-participant-flow}`. Prefer vector PDF
for diagrams and plots; use appropriately sized PNG/JPEG for raster images. Compress
very large images before committing them.

### Table

Keep a substantial table in its own `.tex` file under the matching chapter folder:

```tex
\input{tables/04-results/model-performance}
```

Give it a caption and a stable label such as `tab:results-model-performance`, and cite
it explicitly in the surrounding prose.

### Equation

Label every displayed equation that carries an argument:

```tex
\begin{equation}
  y = \beta_0 + \beta_1 x + \varepsilon
  \label{eq:method-regression-model}
\end{equation}
```

Introduce and interpret it as `Equation~\eqref{eq:method-regression-model}` rather than
leaving a formula detached from the argument.

### Citation

Add a verified BibTeX record to `bibliography/references.bib`, cite it with the template's
configured command, and rebuild enough times for BibTeX and cross-references to settle.
Never use a citation invented by an AI assistant. Open the source and verify authors,
title, venue, year, DOI and the claim it is being used to support.

## Revision history with GitHub issues and branches

Use an issue for **why**, a branch for **isolated work**, commits for **reviewable
steps**, a pull request for **acceptance evidence**, and tags/releases for **important
thesis milestones**.

1. Open a [new thesis revision issue](https://github.com/smaq777/uts-thesis-template-community/issues/new?template=thesis-revision.yml).
2. Record the baseline, requested revision, affected files, acceptance criteria,
   validation, privacy risk and recovery plan.
3. Create a branch such as `revision/42-methodology-rationale`. An AI agent following
   this repository uses `codex/issue-42-methodology-rationale`.
4. Make the bounded change, run `make all`, inspect the PDFs and commit it.
5. Push the branch and open a pull request containing `Closes #42`.
6. Merge only after the build and required human review pass.
7. Tag accepted milestones such as `thesis-v1.0-examination` and
   `thesis-v2.0-final`.

This preserves old states without duplicating the entire thesis into folders named
“final”, “final-new” and “final-real”. Read the exact commands, recovery examples and
privacy cautions in [Revision and version control](docs/REVISION_AND_VERSION_CONTROL.md).

Do not place confidential examiner reports, signatures, participant information,
embargoed research or restricted data in a public GitHub issue, commit, PDF or release.

## Examination corrections and three final outputs

First convert the outcome letter into a controlled comment matrix. Give every comment
a stable ID such as `E1-01`, preserve the examiner's wording in your approved private
record, decide the response, identify the source locations, and obtain supervisor
agreement. Then implement changes with stable sub-identifiers:

```tex
\CorrectionAdd{E1-01}{a}{This paragraph was added in response to Examiner 1, comment 1.}
\CorrectionReplace{E2-03}{a}{old wording}{revised wording}
\CorrectionDelete{E3-02}{a}{text removed after review}
```

`E1-01-a` connects the marked thesis location to the corresponding response-table row.
If a single comment requires three locations, use `E1-01-a`, `E1-01-b` and `E1-01-c`.
Never rely on colour alone: IDs remain readable when printed in greyscale and help a
reviewer find the evidence.

Run `make all` to produce:

1. **`Thesis_CLEAN.pdf`** — final corrected wording with no coloured revision markup;
2. **`Thesis_REVIEW.pdf`** — additions, replacements, deletions and IDs visible for
   supervisor review;
3. **`Revision_Response.pdf`** — a separate response explaining how and where every
   examiner comment was addressed.

The template demonstrates examiner colours, stable IDs and linked page references. The
official submission set and permitted markup are determined by your outcome letter and
current university/school instructions. Read the complete
[Examination workflow](docs/EXAMINATION_WORKFLOW.md) before using the macros.

## Using Codex or Claude responsibly

AI assistance is optional. A capable agent can navigate many files, apply a consistent
rename, draft placeholder prose, update cross-references, run builds, read logs and show
exactly which files changed. It cannot take responsibility for your authorship,
research claims, citations, ethics obligations, examiner interpretation or submission.

This repository includes [`AGENTS.md`](AGENTS.md) for Codex and
[`CLAUDE.md`](CLAUDE.md) for Claude. After installing only the provider you choose,
open the repository root so the agent can read those instructions.

### Copyable first prompt for an AI agent

```text
Read README.md, AGENTS.md (or CLAUDE.md), config/thesis-details.tex, thesis.tex,
and the chapter files relevant to my request. Do not edit yet. First report:
1. the exact files you propose to change;
2. the GitHub revision issue and branch you will use;
3. risks to citations, labels, examiner IDs, privacy, and formatting;
4. the build and visual checks you will run.
Wait for my approval, then make a small change, run make all, inspect the affected
pages in the clean/review/response PDFs, and report changed paths and evidence.
Never invent a source, result, examiner instruction, or institutional requirement.
```

Give the agent only the smallest relevant source set. Keep raw participant data,
confidential interviews, unpublished examiner reports, credentials and restricted
material outside the agent workspace unless your approvals and provider terms clearly
permit their use. Review the diff before accepting any edit.

UTS researchers must consult the current
[Use of AI in Research Guidelines](https://www.uts.edu.au/about/leadership-governance/policies/a-z/use-of-ai-in-research-guidelines),
verify outputs and make required disclosures. See the fuller
[Responsible AI workflow](docs/AI_ASSISTED_WORKFLOW.md).

## Overleaf route

For a browser-only setup:

1. Select **Code → Download ZIP** on GitHub.
2. Create a new blank Overleaf project and upload the ZIP contents.
3. Open **Menu → Settings**, choose **XeLaTeX**, and select `thesis-clean.tex` as the
   main document.
4. Compile the unchanged example first.
5. Replace metadata and example content gradually, recompiling after small changes.
6. Change the main document to `thesis-review.tex` or `revision-response.tex` when
   producing those outputs.

Do not upload the `.git/` folder, local `build/` directory, secrets or confidential
source material. Download a full project backup regularly. See
[Overleaf setup](docs/OVERLEAF.md) for the complete route.

## Troubleshooting

### `xelatex`, `bibtex` or `latexmk` is not found

Run `make doctor`. Install the full TeX distribution, then completely restart VS Code.
On macOS, confirm `/Library/TeX/texbin` is available to the VS Code terminal. On
Windows, restart after MiKTeX/TeX Live installation.

### The PDF does not update

Save the source, check the LaTeX Workshop log, run `make clean`, then `make all`. Make
sure you are opening `build/Thesis_CLEAN.pdf`, not an older exported PDF elsewhere.

### Citations show as question marks

Check the BibTeX key and `.bib` syntax. Use `make all`, which invokes the required
passes. Read the first relevant error in the log; later errors are often consequences.

### A figure is missing or enormous

Check exact filename capitalisation, relative path and extension. Keep the image under
the matching `figures/<chapter>/` folder and set an explicit width such as
`width=0.85\textwidth`.

### The GitHub PDF preview is old

Maintainers run `make previews` and commit all three refreshed files. Ordinary thesis
writers should read their fresh local PDFs under `build/`; tracked previews exist only
to demonstrate the public template.

More platform-specific commands and direct `latexmk` alternatives are in
[Local setup](docs/LOCAL_SETUP.md).

## UTS checkpoints

UTS students should check, at minimum:

- [Thesis submission and examination](https://www.uts.edu.au/research/graduate/current-research-students/thesis-submission-and-examination)
- [Graduate research policies, guides and forms](https://www.uts.edu.au/research/graduate/current-research-students/policies-guides-and-forms)
- [HDR online forms](https://www.uts.edu.au/research/graduate/current-research-students/policies-guides-and-forms/hdr-online-forms)
- [Student Rules, Section 11](https://www.uts.edu.au/about/leadership-governance/governance/rules/student-rules/section-11)
- the exact instructions issued by their school/faculty and their individual outcome
  letter.

These links were checked on **13 August 2026**. Website content, forms, required wording
and procedures can change. If this repository conflicts with current official guidance,
the official guidance and your individual instructions take priority.

Before changing GitHub visibility, complete the
[public release checklist](docs/PUBLIC_RELEASE_CHECKLIST.md). Remove personal metadata,
signatures, examiner material, unpublished research, credentials and accidental build
artefacts.

## Attribution, licence and status

This community edition is substantially reorganised and extended from the publicly
available UTS thesis template by **Dr Chandranath Adak**. It does not claim that the
original author endorsed these changes or granted a private permission beyond the
published licence. See [`CREDITS.md`](CREDITS.md) for provenance and change history.

The LaTeX template derivative is distributed under LPPL 1.3c; original documentation
under `docs/` is CC BY 4.0; repository automation is MIT. Read
[`LICENSE.md`](LICENSE.md). This repository is unofficial, carries no warranty and is
not endorsed by UTS.

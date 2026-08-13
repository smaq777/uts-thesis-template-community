# Local setup and build guide

## What each component does

- A **TeX distribution** provides XeLaTeX, BibTeX, packages and fonts.
- **VS Code** edits and searches the source files.
- **LaTeX Workshop** connects VS Code to the compiler and displays the PDF inside VS Code.
- `latexmk` runs XeLaTeX and BibTeX the required number of times.
- `make` gives memorable commands for the three supported outputs.

LaTeX Workshop is not a TeX distribution. Installing only the extension cannot compile
a thesis.

## macOS

1. Install [MacTeX](https://www.tug.org/mactex/). The full distribution is the least
   surprising option for a thesis.
2. Close and reopen VS Code so it receives the updated `PATH`.
3. Run `make doctor`. If `xelatex` is still missing on Apple Silicon or Intel macOS,
   confirm `/Library/TeX/texbin` is on your shell path.

## Windows

Install either [MiKTeX](https://miktex.org/download) or
[TeX Live](https://tug.org/texlive/), including XeLaTeX, BibTeX and `latexmk`. Restart VS
Code after installation. The repository's VS Code tasks call `make`; if GNU Make is not
available, use LaTeX Workshop's standard `latexmk (xelatex)` recipe or run:

```powershell
latexmk -xelatex -interaction=nonstopmode -halt-on-error -file-line-error -outdir=build -jobname=Thesis_CLEAN thesis-clean.tex
latexmk -xelatex -interaction=nonstopmode -halt-on-error -file-line-error -outdir=build -jobname=Thesis_REVIEW thesis-review.tex
latexmk -xelatex -interaction=nonstopmode -halt-on-error -file-line-error -outdir=build -jobname=Revision_Response revision-response.tex
```

## Linux (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install latexmk texlive-xetex texlive-latex-extra texlive-fonts-recommended
```

Package names differ on Fedora, Arch and other distributions. Install the equivalent
XeLaTeX, BibTeX, `latexmk`, recommended fonts and extra LaTeX packages.

## VS Code and extensions

Install [VS Code](https://code.visualstudio.com/Download), then install:

| Extension | ID | Need | Purpose |
|---|---|---|---|
| [LaTeX Workshop](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop) | `James-Yu.latex-workshop` | Required | Build, logs, PDF tab, SyncTeX, citations and labels |
| [LTeX+](https://marketplace.visualstudio.com/items?itemName=ltex-plus.vscode-ltex-plus) | `ltex-plus.vscode-ltex-plus` | Optional | Grammar and language checking in LaTeX |
| [Code Spell Checker](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker) | `streetsidesoftware.code-spell-checker` | Optional | Lightweight spelling checks |

VS Code will offer these when the folder opens because `.vscode/extensions.json` is
included. The PDF viewer is already part of LaTeX Workshop; no separate PDF extension
is required.

## Commands

```bash
make doctor         # report missing build programs
make clean-thesis   # build build/Thesis_CLEAN.pdf
make review         # build build/Thesis_REVIEW.pdf
make response       # build review thesis, then response with current page links
make all            # build all three PDFs
make watch          # rebuild clean thesis when files change
make clean          # remove generated build products
```

Inside VS Code, use **Terminal → Run Task → Thesis: build all three PDFs**. Open a PDF
from the Explorer, or run **LaTeX Workshop: View LaTeX PDF** from the Command Palette.
Ctrl/Cmd-click in the PDF or source enables SyncTeX navigation when supported.

## Troubleshooting

- `xelatex: command not found`: install a TeX distribution, restart VS Code and rerun
  `make doctor`.
- `bibtex: command not found`: add BibTeX through your TeX distribution/package manager.
- Missing `.sty`: use your TeX package manager to install the named package; do not
  download random `.sty` files into the thesis.
- Citations show as question marks: run `make clean-thesis`; `latexmk` will invoke BibTeX
  and rerun XeLaTeX.
- Response page shows `??`: run `make response`, not XeLaTeX on the response alone.
- A build loops or behaves strangely: run `make clean`, then `make all`.
- Paths fail: keep the repository in a normal local folder; avoid cloud-sync conflicts,
  exotic characters and deeply nested directory names while diagnosing.

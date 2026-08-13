# File organisation for a large thesis

Good structure prevents the final months from becoming a search through files named
`final`, `new`, `use-this-one` and `final2`. The organising principle here is simple:
every chapter, figure folder and table folder uses the same numeric prefix and the same
descriptive name.

## Adding a chapter

For a new chapter called “Case Study”, create:

```text
chapters/07-case-study/chapter.tex
figures/07-case-study/
tables/07-case-study/
```

Then add this line at the correct location in `thesis.tex`:

```tex
\input{chapters/07-case-study/chapter}
```

If one chapter grows beyond comfortable navigation, split only its sections:

```text
chapters/07-case-study/
├── chapter.tex
└── sections/
    ├── 01-context.tex
    ├── 02-analysis.tex
    └── 03-summary.tex
```

The `chapter.tex` file remains the entry point and uses `\input{...}` for those sections.

## Figures

- Use vector PDF for diagrams and plots when possible; use PNG/JPEG for suitable raster
  images.
- Use descriptive lowercase filenames such as `participant-recruitment-flow.pdf`.
- Keep the editable source of a figure when licensing, confidentiality and size permit.
- Put a shared item in `figures/shared/` only when it genuinely appears in multiple chapters.
- Add informative alternative text if your institution or publication workflow supports
  it, and never encode meaning through colour alone.
- Check copyright and permissions before distributing third-party figures.

Example:

```tex
\begin{figure}[htbp]
  \centering
  \includegraphics[width=.82\textwidth]{figures/04-results/outcome-comparison.pdf}
  \caption{A precise, self-contained caption.}
  \label{fig:outcome-comparison}
\end{figure}
```

Refer to it as `\Cref{fig:outcome-comparison}` rather than typing a number manually.

## Tables

Place substantial table source in a separate `.tex` file and input it from the chapter:

```tex
\input{tables/04-results/primary-outcomes}
```

The table file should contain its environment, caption and stable label. Do not paste
tables as screenshots when accessible text can express the information.

## Labels and references

Use consistent prefixes: `chap:`, `sec:`, `fig:`, `tab:`, `eq:` and `app:`. Every
displayed equation should have a label and be introduced or interpreted in prose using
`Equation~\eqref{...}`. Stable semantic labels survive chapter reordering.

## Generated and private material

- Only generated products belong in `build/`; never edit them.
- Do not commit participant data, identifiable material, ethics-confidential documents,
  API keys, private examiner reports or copyrighted PDFs to a public repository.
- Keep dated submission snapshots outside the source tree or attach them to a private,
  controlled release. Git is history, not an approved research-data repository.

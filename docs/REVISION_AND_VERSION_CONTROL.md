# Thesis revision and version-control workflow

> **Use this workflow in your own repository created from this template.** The upstream
> `smaq777/uts-thesis-template-community` repository does not accept external pull
> requests, feature requests, contribution proposals or personal thesis-revision
> issues.

Git makes every committed state recoverable. GitHub adds an issue for the reason, a
branch for isolated work, a pull request for review, and a tag or release for important
milestones. Together, these records are much safer than filenames such as
`thesis-final-final-2.tex`.

## The recommended lifecycle

1. **Create one revision issue.** Describe the requested change, affected files,
   acceptance criteria, validation, privacy risk and recovery plan. Use the repository's
   **Thesis revision** issue form.
2. **Start from the accepted baseline.** Usually this is `main`; after examination it
   may be a tagged submission such as `thesis-v1.0-examination`.
3. **Create a short-lived branch.** Students can use `revision/42-methodology-rationale`.
   An AI coding agent working under this repository's rules should use
   `codex/issue-42-methodology-rationale`.
4. **Make small commits.** Each commit should explain one coherent change and reference
   the issue where helpful.
5. **Build and inspect.** Run `make all`; inspect the affected pages in the clean,
   review and response PDFs. A successful compiler exit is not a visual review.
6. **Open a pull request.** Link the issue with `Closes #42`, show what changed and
   record the evidence. Ask a supervisor or trusted reviewer to check meaning as well
   as typesetting.
7. **Merge only accepted work.** Keep `main` as the current accepted thesis state.
8. **Tag milestones.** Tag examination submission, supervisor review, corrected
   submission and final award states. A tag is a stable pointer; a GitHub release can
   also hold the three PDFs.
9. **Delete the merged branch.** The commits, issue, pull request and tag remain.

## Exact command example

Replace `42` and the description with your real GitHub issue number and revision.

```bash
git switch main
git pull --ff-only
git switch -c revision/42-methodology-rationale

# Edit only the files required by Issue #42, then build and inspect.
make all
git status --short
git add chapters/03-methodology/sections/sampling.tex
git commit -m "Revise methodology sampling rationale (#42)"
git push -u origin revision/42-methodology-rationale
```

Open a pull request on GitHub, link Issue #42, wait for the PDF build check, and obtain
the required human review. After the pull request is accepted and merged:

```bash
git switch main
git pull --ff-only
git branch -d revision/42-methodology-rationale
```

Do not force-push shared branches, rewrite accepted history, or use `git reset --hard`
as a routine undo method.

## Milestone tags and releases

Use meaningful, ordered tag names:

```bash
git tag -a thesis-v1.0-examination -m "Thesis submitted for examination"
git push origin thesis-v1.0-examination

git tag -a thesis-v1.1-supervisor-review -m "Corrections sent for supervisor review"
git push origin thesis-v1.1-supervisor-review

git tag -a thesis-v2.0-final -m "Final corrected thesis submitted"
git push origin thesis-v2.0-final
```

Before tagging, record the exact date, build all outputs and visually inspect them.
When permitted by your institution, attach `Thesis_CLEAN.pdf`, `Thesis_REVIEW.pdf` and
`Revision_Response.pdf` to a GitHub release. Never publish a confidential thesis,
embargoed research, examiner report, signature, participant data or private metadata.

## Safely returning to an older state

Inspect an old milestone without changing your working branch:

```bash
git show thesis-v1.0-examination:chapters/03-methodology/chapter.tex
git switch --detach thesis-v1.0-examination
```

Return to current work with `git switch main`. To recover old content into a new,
reviewable branch:

```bash
git switch -c recovery/42-from-examination thesis-v1.0-examination
```

To undo an already shared commit while preserving history, use a new issue and a
revert commit:

```bash
git switch -c revision/57-revert-methodology main
git revert <commit-id>
make all
```

## Suggested revision labels

- `thesis-revision`: every bounded thesis change.
- `examiner-correction`: changes tied to stable examiner IDs.
- `supervisor-review`: work awaiting supervisory review.
- `submission-snapshot`: a proposed tag or release.
- `build`: LaTeX compilation, warnings or output problems.
- `documentation`: guidance rather than thesis content.

Labels show category; the issue and pull request hold the evidence. A GitHub issue is
not a safe location for confidential feedback. Use a stable private identifier such as
`E1-04` and store the source report only in an institution-approved location.

# Examination and revision workflow

This is a worked method for organising corrections, not an official examination form.
UTS students must use the current Thesis Revision Response template and follow the
individual outcome letter, deadline, supervisory panel and faculty/GRS instructions.

## 1. Freeze the examined version

Keep an immutable copy of the exact thesis sent for examination. Record its date and a
checksum if your process permits. Do not silently replace it; it is the baseline against
which corrections are explained.

## 2. Build a complete comment matrix before editing

Copy every examiner comment verbatim and in report order. Assign stable IDs:

- `E1-01`, `E1-02`, ... for Examiner 1
- `E2-01`, `E2-02`, ... for Examiner 2
- use `RAO-01` or another clearly defined prefix only when your official instructions
  require responses to an additional source.

For each row record: verbatim comment, interpretation, proposed action, thesis location,
evidence needed, supervisor decision, status and final page. If no text changes, explain
substantively why and provide evidence; never mark a comment “done” without a response.

## 3. Agree on the correction

Discuss ambiguous, contradictory or scope-changing comments with your supervisory panel.
The student should not guess how conflicting examiner requests are to be reconciled.
Follow the decision-making and approval route in the outcome documentation.

## 4. Mark source changes with stable IDs

For an addition:

```tex
\CorrectionAdd{E1-01}{a}{New final text.}
```

For a replacement:

```tex
\CorrectionReplace{E2-03}{a}{Old text.}{Revised final text.}
```

For a deletion:

```tex
\CorrectionDelete{E3-02}{a}{Text removed from the clean version.}
```

Use suffixes `a`, `b`, `c` for multiple locations responding to one comment. Examiner 1
is blue, Examiner 2 is vermillion and Examiner 3 is purple, but every marking also shows
the ID so it remains interpretable without colour.

## 5. Write the response row

Preserve the examiner's words verbatim. In the response, state the substantive correction
directly, identify where it was made, and explain the intellectual effect. Avoid internal
process narration such as “we discussed this” unless the official form specifically asks
for it.

Page references are drawn from labels in the review thesis:

```tex
\CorrectionPage{E1-01}{a}
```

Always build the final source before confirming page numbers.

## 6. Generate and inspect three outputs

```bash
make all
```

1. `Thesis_CLEAN.pdf`: the revised thesis as continuous final prose.
2. `Thesis_REVIEW.pdf`: the same thesis with examiner IDs, colours and visible deletions
   for supervisor checking.
3. `Revision_Response.pdf`: the separate comment-response table for the university.

Compare the clean and review outputs. Confirm that every ID in the response exists in the
review thesis, every review ID has a response row, deleted text vanishes from the clean
copy, citations resolve, and final page references are correct.

## 7. Obtain approvals and follow current submission instructions

The template does not submit anything. UTS students should check the current
[thesis submission and examination page](https://www.uts.edu.au/research/graduate/current-research-students/thesis-submission-and-examination),
[policies, guides and forms](https://www.uts.edu.au/research/graduate/current-research-students/policies-guides-and-forms),
Student Rules and all school/faculty instructions. Requirements and forms can change.


# Example PDF previews

These three synthetic PDFs let visitors inspect the template before installing LaTeX:

- `Thesis_CLEAN.pdf`: the clean submission-style thesis.
- `Thesis_REVIEW.pdf`: the supervisor/examiner review copy with stable change IDs.
- `Revision_Response.pdf`: the separate examiner-response document.

They contain placeholder names, data, prose, figures and references. They are not a
real thesis and must not be submitted. Regenerate all previews after changing template
output:

```bash
make previews
```

Commit the source change and the three refreshed PDFs together. GitHub Actions builds
the source again and checks that the tracked previews are present and readable.

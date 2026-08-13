# Overleaf setup

1. On GitHub, select **Code → Download ZIP**.
2. In Overleaf, create **New Project → Upload Project** and select the ZIP.
3. Open **Menu → Settings** and choose **XeLaTeX** as the compiler.
4. Set the main document to `thesis-clean.tex`.
5. Compile and check the log for missing packages, images or fonts.

To see examiner markings, change the main document to `thesis-review.tex`. To build the
response, first compile the review thesis. Overleaf's handling of separately named
auxiliary files can differ from the local `make response` workflow, so page references
may require an Overleaf-specific project arrangement. The supported and automatically
tested three-output route is local `make all`.

Avoid uploading generated `build/` content, old PDFs, datasets or private examination
reports. A ZIP containing only source files is smaller, easier to audit and faster to
transfer. Confirm current Overleaf project limits on Overleaf's own documentation,
because plan limits and compile behaviour can change.


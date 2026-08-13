# Public repository release checklist

Keep a thesis repository private until every item below has been checked. A successful
build is not a privacy, copyright or institutional approval.

## Content and privacy

- [ ] No participant names, identifiers, contact details, raw data or re-identification keys.
- [ ] No confidential examiner reports, outcome letters, ethics correspondence or contracts.
- [ ] No unpublished co-author material without permission.
- [ ] No API keys, tokens, `.env` files, passwords, private URLs or cloud credentials.
- [ ] No personal signatures, student cards, addresses, private email or phone numbers.
- [ ] Git history has also been checked; deleting a current file does not remove it from history.

## Rights and attribution

- [ ] Every third-party figure, table, photograph, font and text extract is permitted for
  public redistribution, not merely for thesis examination.
- [ ] No UTS or other institution logo is included unless written authority permits it.
- [ ] `CREDITS.md`, `LICENSE.md` and change history remain present.
- [ ] The repository is described as unofficial and does not imply author or university endorsement.

## Template quality

- [ ] `make clean && make all` succeeds.
- [ ] All three PDFs were opened and visually inspected.
- [ ] No unresolved citations, references, examiner IDs or page numbers remain.
- [ ] Example student identity, `20XX`, synthetic values and placeholder text are intentional.
- [ ] Links to current university requirements were rechecked and the checked date updated.

## GitHub controls

- [ ] Branch protection, issue templates and review requirements are configured as desired.
- [ ] GitHub Actions passes on a clean clone.
- [ ] A private review was completed before changing visibility to public.
- [ ] The maintainer understands that making a repository public can create copies that
  cannot be recalled even if the original is later made private.


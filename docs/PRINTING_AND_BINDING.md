# Printing and binding a thesis

This guide helps students prepare a print copy from the template and find printing
services in Sydney. It is community guidance, not an official university instruction
or a recommendation of any commercial provider.

> **Verify before every order and submission.** University, faculty and examiner
> requirements can change. Check the current official website, your individual
> examination or outcome letter, and instructions from your supervisor and research
> office immediately before you pay for printing, approve binding or submit a copy.

The university may require only a digital thesis. Do not pay for examination or final
binding until the responsible university office confirms that a physical copy is
required. A personal keepsake copy is optional and may use different specifications.

Many universities now use digital submission and examination, so a printed thesis is
often optional rather than a submission requirement. However, completing a thesis
represents years of sustained work. Students may still decide that one carefully made
personal copy is worth keeping as a permanent record of that achievement.

## Build a print copy

The normal `make all` command still produces the clean, review and revision-response
files. It does not produce the optional print variants.

```bash
make print-single
make print-duplex
```

The outputs are:

- `build/Thesis_PRINT_SINGLE.pdf`: one-sided pages with a left binding margin.
- `build/Thesis_PRINT_DUPLEX.pdf`: mirrored inner and outer margins, right-hand
  chapter starts and intentional blank pages where needed.

Build both with:

```bash
make print
```

The default print settings are in [`config/print-settings.tex`](../config/print-settings.tex).
They use the current UTS minimum margins, with a small bottom safety allowance for
LaTeX line-grid rounding. Students at another university must replace the values with
their own current requirements before building.

## Current UTS print requirements

The current UTS Graduate Research Candidature Management, Thesis Preparation and
Submission Procedures, version 1.19, were checked on **15 August 2026**. They state
that when one or more examiners request printed copies:

- the paper size is A4, 297 mm by 210 mm, except approved illustrative material;
- paper has a minimum weight of 80 gsm;
- copies may be printed single-sided or double-sided;
- text uses a legible font with 1.5 or double spacing, with single spacing permitted
  for appendices and footnotes;
- minimum margins are 40 mm left, 20 mm right, 30 mm top and 20 mm bottom.

UTS normally requires a digital thesis for examination. If an examiner requests a hard
copy, the student must supply it and the Graduate Research School forwards it. A final
bound copy is required only when the faculty requires one.

If a final bound copy is required, the current UTS procedure specifies:

- boards with dark red buckram for a Doctoral degree;
- boards with University blue, described as dark blue, for a Master's degree;
- gold lettering on the spine.

Do not copy spine wording from an old thesis. Ask the faculty research office to confirm
the exact degree abbreviation, year, name format, lettering direction, cover wording and
number of copies before ordering.

Official UTS sources:

- [Graduate Research Thesis Submission](https://www.uts.edu.au/research/graduate/current-research-students/thesis-submission-and-examination)
- [Graduate Research Candidature Management, Thesis Preparation and Submission Procedures](https://www.uts.edu.au/globalassets/shared-media/documents/grs/graduate-research-candidature-management-thesis-preparation-submission-procedures.pdf)
- [Student printing and Digital Imaging Service](https://www.uts.edu.au/for-students/current-students/managing-your-course/using-uts-systems/student-printing)
- [UTS Student Rules, Section 11](https://www.uts.edu.au/about/leadership-governance/governance/rules/student-rules/section-11)

UTS scholarship holders may be eligible for reimbursement of thesis editing or
printing costs if their current Conditions of Award include a Thesis Allowance. The UTS
submission page currently says a claim must be made within 12 months of thesis
submission and supported by original tax invoices. Verify eligibility before spending.

## Students at other NSW universities

There is no single printing or binding standard shared by all NSW universities. Many
universities now use electronic submission and request a hard copy only in specific
circumstances. A UTS print build is not proof that a thesis meets another university's
requirements.

Check the current official source for your institution:

| University | Current starting point |
|---|---|
| University of Sydney | [Preparing your thesis](https://www.sydney.edu.au/research/graduate-research/current-students/thesis-and-examination/preparing-your-thesis.html) and [Submit your thesis](https://www.sydney.edu.au/research/graduate-research/current-students/thesis-and-examination/notice-of-intent-to-submit.html) |
| UNSW Sydney | [Thesis Format Guide](https://www.unsw.edu.au/content/dam/pdfs/research/higher-degree-research/thesis-format-guide.pdf) and [HDR Examination Procedure](https://www.unsw.edu.au/content/dam/pdfs/governance/policy/2022-01-policies/hdrexamprocedure.pdf) |
| Macquarie University | [Graduate Research Thesis Preparation, Submission and Examination Procedure](https://policies.mq.edu.au/document/view.php?id=172&version=2) |
| Western Sydney University | [Thesis submission and examination FAQ](https://www.westernsydney.edu.au/schools/grs/higher-degree-research-students/frequently-asked-questions) and [current forms and handbook](https://www.westernsydney.edu.au/schools/grs/higher-degree-research-students/forms-policies-and-guidelines) |
| University of Wollongong | [Thesis preparation and submission](https://www.uow.edu.au/research/graduate-research/current-students/thesis-preparation-and-submission/) |

For any NSW university:

1. Confirm whether a physical copy is required at all.
2. Confirm whether the copy is for examination, final deposit or personal use.
3. Confirm paper size, weight, sides, margins, colour and large-page handling.
4. Confirm temporary or permanent binding, cover material and colour.
5. Confirm exact spine and front-cover wording.
6. Confirm the number of copies, destination and deadline.
7. Obtain a printer proof when lettering or colour is important.

Record the confirmed order in the placeholder-only
[`PRINT_ORDER_CHECKLIST.md`](PRINT_ORDER_CHECKLIST.md).

## Printing and binding services in Sydney

Service details, prices and opening hours can change. Contact the provider, send the
current university specification, request a written quote and confirm turnaround before
placing an order. Listing does not mean endorsement.

### UTS self-service printing

UTS provides self-service printing, copying and scanning across its campuses. The
[student printing page](https://www.uts.edu.au/for-students/current-students/managing-your-course/using-uts-systems/student-printing)
contains current prices, account recharge instructions and access requirements. This
option is suitable for ordinary A4 or A3 pages but does not itself confirm faculty
binding requirements.

Prices shown by UTS when this guide was checked on 15 August 2026 were:

| Size and sides | Black and white | Colour |
|---|---:|---:|
| A4 single-sided | $0.11 | $0.34 |
| A4 double-sided | $0.19 | $0.60 |
| A3 single-sided | $0.21 | $0.68 |
| A3 double-sided | $0.36 | $1.30 |

Scanning was listed as free, with at least $0.01 required in the printing account. UTS
also listed a cash and card recharge station at `CB10.02.471`. Check the live page
before adding credit because unused credit is not refundable.

### UTS Digital Imaging Service

The UTS Digital Imaging Service lists A4, A3 and large-format printing, scanning, comb,
wire, tape, photobook and thesis binding.

- Location: CB06, Design, Architecture and Building, 702 Harris Street, Ultimo,
  Level 3 Computer Lab, Room 03.11a
- Phone: (02) 9514 8030
- Email: digital.image@uts.edu.au
- Listed session hours when checked: Monday to Friday, 9:00 am to 5:00 pm
- Details: [UTS student printing page](https://www.uts.edu.au/for-students/current-students/managing-your-course/using-uts-systems/student-printing)

The service accepts UTS Student ID card, EFTPOS or credit card and states that it does
not accept cash. Confirm current access, file-transfer and thesis-binding arrangements.

### Thesis Online and World of Print

[Thesis Online](https://thesisonline.com.au/) is partnered with World of Print near UTS.
It lists thesis printing, hard book binding, buckram, spine or cover lettering, acid-free
80 gsm, 90 gsm and 100 gsm stocks, pickup and delivery.

- Location: Shop 3, 702 Harris Street, Ultimo NSW 2007
- Phone: (02) 9280 4244
- Email: broadway@worldofprint.com.au

UTS also lists [World of Print on its campus map](https://maps.uts.edu.au/life.cfm/map.cfm?point=1158)
as providing thesis printing and binding. Ask the provider to confirm the university
specification before approving the order.

### Les Baddock Bookbinders

[Les Baddock Bookbinders](https://www.baddocks.com.au/thesis-binding) lists specialist
thesis binding using buckram and foil lettering to a university or faculty specification.
It binds supplied printed pages, so confirm whether printing must be arranged separately.

- Location: 33 Clapham Road, Regents Park NSW 2143
- Phone: (02) 9560 9222

### Officeworks

[Officeworks Print and Copy](https://www.officeworks.com.au/print-copy/home) and the
[Sydney store locator](https://www.officeworks.com.au/shop/officeworks/storelocator/2000)
provide general document printing and binding. Confirm whether the selected store can
produce the exact temporary or permanent binding required. Standard retail binding may
not satisfy a formal buckram, board and gold-lettering specification.

## Final checks before paying

- Use the correct print PDF, not an old clean or review copy.
- Open the PDF and inspect every page at 100 percent zoom.
- Confirm A4 page size and print at actual size without fit-to-page scaling.
- Confirm that colour figures remain understandable in the chosen colour mode.
- Check blank pages, chapter starts, page numbers, fold-outs and landscape pages.
- Remove revision marks from any final clean copy.
- Keep confidential examiner reports and private records out of the print package.
- Ask for a proof of cover and spine lettering before permanent binding.
- Keep the quote and final tax invoice.
- Verify the university website and personal instructions again on submission day.

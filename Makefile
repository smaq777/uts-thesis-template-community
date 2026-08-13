LATEXMK ?= latexmk
OUT := build

.PHONY: all clean-thesis review response examples watch clean doctor

all: clean-thesis review response

examples: all

$(OUT):
	mkdir -p $(OUT)

clean-thesis: | $(OUT)
	$(LATEXMK) -xelatex -interaction=nonstopmode -halt-on-error -file-line-error -outdir=$(OUT) -jobname=Thesis_CLEAN thesis-clean.tex

review: | $(OUT)
	$(LATEXMK) -xelatex -interaction=nonstopmode -halt-on-error -file-line-error -outdir=$(OUT) -jobname=Thesis_REVIEW thesis-review.tex

response: review | $(OUT)
	$(LATEXMK) -xelatex -interaction=nonstopmode -halt-on-error -file-line-error -outdir=$(OUT) -jobname=Revision_Response revision-response.tex

watch: | $(OUT)
	$(LATEXMK) -xelatex -pvc -interaction=nonstopmode -file-line-error -outdir=$(OUT) -jobname=Thesis_CLEAN thesis-clean.tex

doctor:
	@command -v xelatex
	@command -v bibtex
	@command -v latexmk
	@xelatex --version | head -n 1
	@bibtex --version | head -n 1
	@latexmk -v | head -n 2

clean:
	$(LATEXMK) -C -outdir=$(OUT) thesis-clean.tex thesis-review.tex revision-response.tex
	rm -f $(OUT)/Thesis_CLEAN.* $(OUT)/Thesis_REVIEW.* $(OUT)/Revision_Response.*

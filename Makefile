LATEXMK ?= latexmk
OUT := build

.PHONY: all clean-thesis review response examples previews watch clean doctor

all: clean-thesis review response

examples: all

previews: all
	mkdir -p examples/pdfs
	cp $(OUT)/Thesis_CLEAN.pdf examples/pdfs/Thesis_CLEAN.pdf
	cp $(OUT)/Thesis_REVIEW.pdf examples/pdfs/Thesis_REVIEW.pdf
	cp $(OUT)/Revision_Response.pdf examples/pdfs/Revision_Response.pdf

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
	@command -v $(LATEXMK)
	@xelatex --version | sed -n '1p'
	@bibtex --version | sed -n '1p'
	@$(LATEXMK) -v | sed -n '1,2p'

clean:
	$(LATEXMK) -C -outdir=$(OUT) thesis-clean.tex thesis-review.tex revision-response.tex
	rm -f $(OUT)/Thesis_CLEAN.* $(OUT)/Thesis_REVIEW.* $(OUT)/Revision_Response.*

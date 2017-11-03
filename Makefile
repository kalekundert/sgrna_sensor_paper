BUILD := build
SLUG := main
LATEX := xelatex --halt-on-error --output-directory build
BIBER := biber --output-directory build

PREAMBLE := \
	preamble.tex

FIGURES := \
	figure_1/figure_1.pdf \
	figure_2/figure_2.pdf \
	figure_3/figure_3.pdf \
	table_1/summary_tabular.tex \
	supp_mat/rational_design_sequences.tex \
	supp_mat/library_sequences/library_tabular.tex \

BIBLIOGRAPHIES := \
	curated_refs.bib \

$(BUILD)/$(SLUG).pdf: $(SLUG).tex $(PREAMBLE) $(FIGURES) $(BUILD)/$(SLUG).bbl Makefile
	$(LATEX) $< 

$(BUILD)/$(SLUG).bbl : $(BIBLIOGRAPHIES) Makefile
	$(LATEX) $(SLUG)
	$(BIBER) $(SLUG)
	$(LATEX) $(SLUG)

again : 
	$(LATEX) $(SLUG).tex 

bib :
	$(LATEX) $(SLUG)
	$(BIBER) $(SLUG)
	$(LATEX) $(SLUG)

clean :
	rm $(BUILD)/*

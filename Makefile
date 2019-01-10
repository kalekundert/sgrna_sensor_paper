BUILD := build
SLUG := sgrna_figures
LATEX := xelatex --halt-on-error --output-directory $(BUILD)
BIBER := biber --output-directory $(BUILD)

PREAMBLE := \
	preamble.tex

FIGURES := \
	figure_1/figure_1.pdf \
	figure_2/figure_2.pdf \
	figure_3/figure_3.pdf \
	table_1/summary_tabular.tex \
	$(wildcard supp_mat/*.pdf) \
	$(wildcard supp_mat/*.tex) \

BIBLIOGRAPHIES := \
	curated_refs.bib \
	uncurated_refs.bib \

figures :
	$(LATEX) sgrna_figures

$(BUILD)/$(SLUG).pdf: $(SLUG).tex $(PREAMBLE) $(FIGURES) $(BUILD)/$(SLUG).bbl Makefile
	$(LATEX) $< 

$(BUILD)/$(SLUG).bbl : $(BIBLIOGRAPHIES) Makefile
	$(LATEX) $(SLUG)
	$(BIBER) $(SLUG)
	$(LATEX) $(SLUG)

again : 
	$(LATEX) $(SLUG)

twice : 
	$(LATEX) $(SLUG)
	$(LATEX) $(SLUG)

bib :
	$(LATEX) $(SLUG)
	$(BIBER) $(SLUG)
	$(LATEX) $(SLUG)

clean :
	rm $(BUILD)/*

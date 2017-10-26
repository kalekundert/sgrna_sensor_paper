SLUG := sgrna_paper
LATEX := xelatex --halt-on-error
BIBER := biber

FIGURES := \
	figure_1/figure_1.pdf \
	figure_2/figure_2.pdf \
	figure_3/figure_3.pdf \
	table_1/summary_tabular.tex \

BIBLIOGRAPHIES := \
	curated_refs.bib \

sgrna_paper.pdf: $(SLUG).tex $(SLUG).bbl $(FIGURES) Makefile
	$(LATEX) $< 

$(SLUG).bbl : $(BIBLIOGRAPHIES) Makefile
	$(LATEX) $(SLUG)
	$(BIBER) $(SLUG)
	$(LATEX) $(SLUG)


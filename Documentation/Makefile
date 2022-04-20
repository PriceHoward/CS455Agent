# CS 455 docs
TEX=/usr/local/bin/xelatex
XPDF=/usr/local/bin/xpdf

.PHONY: all clean

all: sdmp srs

sdmp: sdmp.tex
	$(TEX) sdmp.tex
	$(TEX) sdmp.tex
	$(XPDF) sdmp.pdf

srs: srs.tex
	$(TEX) srs.tex
	$(TEX) srs.tex
	$(XPDF) srs.pdf

clean:
	@/bin/rm -f *dvi *aux *log *toc *lof *lot *bbl *blg *xcp *out *xml *cut *.pdf


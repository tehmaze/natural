PYTHON := python
DOMAIN := natural
LOCALE := natural/locales/en_US/LC_MESSAGES
ALL_PO := $(shell ls -1 locales/*.po | while read po; do basename "$$po"; done)
ALL_MO := $(shell ls -1 locales/*.po | while read po; do basename "$$po" | sed -e 's/po$$/mo/'; done)

test: test-nosetests test-pep8

test-nosetests:
	@nosetests -w natural/ -v --with-doctest

test-pep8:
	@pep8 --ignore=E128,E221,E241 natural/

translate: en_US.mo en_GB.mo nl_NL.mo af_ZA.mo de_DE.mo fr_FR.mo

translate-all: $(ALL_PO) $(ALL_MO)

translate-extract:
	@mkdir -p locales
	@echo "Extracting gettext to locales/natural.pot"
	@xgettext \
        --language=Python \
        --keyword=_ --keyword=__  \
        --package-name natural \
        --copyright-holder "Wijnand Modderman-Lenstra" \
        -d $(DOMAIN) -o locales/natural.pot natural/*.py
	@sed -e 's/charset=CHARSET/charset=UTF-8/' -i locales/natural.pot

%.po:
	@if [ -e locales/$@ ]; then \
        echo -n "Merging locales/$@: "; \
        msgmerge -U locales/$@ locales/natural.pot; \
    else \
	    msginit \
        --input=locales/natural.pot \
        --locale=$(@:.po=) \
        --no-translator \
        --output-file=locales/$@; \
	fi

%.mo:
	@mkdir -p natural/locales/$(@:.mo=)/LC_MESSAGES
	@echo "Compiling natural/locales/$(@:.mo=)/LC_MESSAGES/natural.mo"
	@msgfmt \
        --output-file=natural/locales/$(@:.mo=)/LC_MESSAGES/natural.mo \
        locales/$(@:.mo=.po)

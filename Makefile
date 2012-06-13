PYTHON := python
DOMAIN := natural
LOCALE := natural/locale/en_US/LC_MESSAGES
ALL_PO := $(shell ls -1 locale/*.po | while read po; do basename "$$po"; done)
ALL_MO := $(shell ls -1 locale/*.po | while read po; do basename "$$po" | sed -e 's/po$$/mo/'; done)

test: test-nosetests test-pep8

test-nosetests:
	PYTHONPATH=$(shell pwd) nosetests -w tests/ -v

test-pep8:
	@pep8 --ignore=E221,E241 natural/

translate: en_US.mo en_GB.mo nl_NL.mo

translate-all: $(ALL_PO) $(ALL_MO)

translate-extract:
	@mkdir -p locale
	@echo "Extracting gettext to locale/natural.pot"
	@xgettext \
        --language=Python \
        --keyword=_ --keyword=__  \
        --package-name natural \
        --copyright-holder "Wijnand Modderman-Lenstra" \
        -d $(DOMAIN) -o locale/natural.pot natural/*.py
	@sed -e 's/charset=CHARSET/charset=UTF-8/' -i locale/natural.pot

%.po:
	@if [ -e locale/$@ ]; then \
        echo -n "Merging locale/$@: "; \
        msgmerge -U locale/$@ locale/natural.pot; \
    else \
	    msginit \
        --input=locale/natural.pot \
        --locale=$(@:.po=) \
        --no-translator \
        --output-file=locale/$@; \
	fi

%.mo:
	@mkdir -p natural/locale/$(@:.mo=)/LC_MESSAGES
	@echo "Compiling natural/locale/$(@:.mo=)/LC_MESSAGES/natural.mo"
	@msgfmt \
        --output-file=natural/locale/$(@:.mo=)/LC_MESSAGES/natural.mo \
        locale/$(@:.mo=.po)

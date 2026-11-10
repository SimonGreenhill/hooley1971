all: output/hooley1971.nex \
    output/hooley1971.asc.nex \
    output/hooley1971.ascwords.nex

output/hooley1971.nex: cldf/forms.csv
	cldfbench hooley1971.nexus --output $@

output/hooley1971.asc.nex: cldf/forms.csv
	cldfbench hooley1971.nexus --output $@ --ascertainment overall

output/hooley1971.ascwords.nex: cldf/forms.csv
	cldfbench hooley1971.nexus --output $@ --ascertainment word

clean:
	rm -f output/*.nex

.PHONY: all clean

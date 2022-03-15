PROJECT = mooringSimulator
MAIN = $(PROJECT).py
PYTHON = python

.PHONY: test run

test:
	$(PYTHON) -m unittest  discover -v 

run:
	$(PYTHON) $(MAIN)
	
debug:
	$(PYTHON) $(MAIN) -d -l
	
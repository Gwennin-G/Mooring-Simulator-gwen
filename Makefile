PROJECT = mooringSimulator
MAIN = $(PROJECT).py
PYTHON = python
TESTUNMODIFIABLE = testUnmodifiableElementFactory.py 
TESTROPE = testRopeElementFactory.py 
TESTMASS = testMassDependantElementFactory.py

.PHONY: test run

test-all: test-unmodifiable test-rope test-mass
	
test-unmodifiable: 
	$(PYTHON) $(TESTUNMODIFIABLE)

test-rope: 
	$(PYTHON) $(TESTROPE)

test-mass: 
	$(PYTHON) $(TESTMASS)

run:
	$(PYTHON) $(MAIN)
	
debug:
	$(PYTHON) $(MAIN) -d -l
	
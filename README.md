# Homework 1: Decision Trees

Just type
	make
or, equivalently
	make test-all
while in the src directory to run the code on all of the configurations of L and K
listed in the report. 

You can also run all tests for one of the datasets by typing
	make test-<dataset number>
Example:
	make test-1

or a specific test by typing
	make test-<dataset number>-<config number>
Example:
	make test-1-0
(runs the first test for the first dataset)

Printing is enabled by default, but just set PRINT=no to avoid printing.
Example:
	make PRINT=no

Alternatively, just execute the code directly by passing typing
	python3 main.py <L> <K> <training-set> <validation-set> <test-set> <to-print>

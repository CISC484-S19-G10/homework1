DATASET_1 = ../data_sets1
DATASET_2 = ../data_sets2

FILES = @training_set.csv @validation_set.csv @test_set.csv
DATA_FILES_1 = $(subst @,$(DATASET_1)/,$(FILES))
DATA_FILES_2 = $(subst @,$(DATASET_2)/,$(FILES))

#Config    L  K
#---------------
CONFIG_0 = 20 5
CONFIG_1 = 20 10
CONFIG_2 = 20 15
CONFIG_3 = 20 20
CONFIG_4 = 20 25
CONFIG_5 = 5  20
CONFIG_6 = 10 20
CONFIG_7 = 15 20
CONFIG_8 = 25 20
CONFIG_9 = 30 20
CONFIG_NUMS = _0 _1 _2 _3 _4 _5 _6 _7 _8 _9

TESTS_SET_1 = $(subst _,test-1-,$(CONFIG_NUMS))
TESTS_SET_2 = $(subst _,test-2-,$(CONFIG_NUMS))

.DUMMY:test-all
test-all:test-1 test-2

#tests for dataset 1:
.DUMMY:test-1 $(TESTS_SET_1)
test-1:$(TESTS_SET_1) 

test-1-0:$(SRC)
	python3 main.py $(CONFIG_0) $(DATA_FILES_1) yes

test-1-1:$(SRC)
	python3 main.py $(CONFIG_1) $(DATA_FILES_1) yes

test-1-2:$(SRC)
	python3 main.py $(CONFIG_2) $(DATA_FILES_1) yes

test-1-3:$(SRC)
	python3 main.py $(CONFIG_3) $(DATA_FILES_1) yes

test-1-4:$(SRC)
	python3 main.py $(CONFIG_4) $(DATA_FILES_1) yes

test-1-5:$(SRC)
	python3 main.py $(CONFIG_5) $(DATA_FILES_1) yes

test-1-6:$(SRC)
	python3 main.py $(CONFIG_6) $(DATA_FILES_1) yes

test-1-7:$(SRC)
	python3 main.py $(CONFIG_7) $(DATA_FILES_1) yes

test-1-8:$(SRC)
	python3 main.py $(CONFIG_8) $(DATA_FILES_1) yes

test-1-9:$(SRC)
	python3 main.py $(CONFIG_9) $(DATA_FILES_1) yes

test-2-0:$(SRC)
	python3 main.py $(CONFIG_0) $(DATA_FILES_2) yes

#tests for dataset 2:
.DUMMY:test-2 $(TESTS_SET_2)
test-2:$(TESTS_SET_2) 

test-2-1:$(SRC)
	python3 main.py $(CONFIG_1) $(DATA_FILES_2) yes

test-2-2:$(SRC)
	python3 main.py $(CONFIG_2) $(DATA_FILES_2) yes

test-2-3:$(SRC)
	python3 main.py $(CONFIG_3) $(DATA_FILES_2) yes

test-2-4:$(SRC)
	python3 main.py $(CONFIG_4) $(DATA_FILES_2) yes

test-2-5:$(SRC)
	python3 main.py $(CONFIG_5) $(DATA_FILES_2) yes

test-2-6:$(SRC)
	python3 main.py $(CONFIG_6) $(DATA_FILES_2) yes

test-2-7:$(SRC)
	python3 main.py $(CONFIG_7) $(DATA_FILES_2) yes

test-2-8:$(SRC)
	python3 main.py $(CONFIG_8) $(DATA_FILES_2) yes

test-2-9:$(SRC)
	python3 main.py $(CONFIG_9) $(DATA_FILES_2) yes

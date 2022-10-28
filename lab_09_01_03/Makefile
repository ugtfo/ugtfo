CC := gcc

CFILES_DIR := ./src
CFILES := $(wildcard $(CFILES_DIR)/*.c)
INC_DIR := ./inc
INCLUDES := $(wildcard $(INC_DIR)/*.h)
UNIT_DIR := ./unit_tests
UNITS := $(wildcard $(UNIT_DIR)/*.c)

OBJ_DIR := ./out
OBJECTS := $(CFILES:$(CFILES_DIR)/%.c=$(OBJ_DIR)/%.o)
OBJECTS_UNIT := $(UNITS:$(UNIT_DIR)/%.c=$(OBJ_DIR)/%.o)
OBJECTS_UNIT += $(filter-out $(OBJ_DIR)/main.o, $(OBJECTS))
FLAGS := -Wall -Werror -pedantic -std=c99
U_FLAGS := -lcheck -lpthread -lrt

APP = app.exe
UNIT_TEST = unit_tests.exe


.PHONY : clean run unit


$(APP): $(OBJECTS)
	$(CC) $(OBJECTS) -o $@


$(UNIT_TEST): $(OBJECTS_UNIT)
	$(CC) $(OBJECTS_UNIT) -o $@ $(U_FLAGS)


$(OBJ_DIR):
	@mkdir -p $@


$(OBJ_DIR)/%.o: $(CFILES_DIR)/%.c $(INCLUDES) $(OBJ_DIR)
	$(CC) $(FLAGS) $(U_FLAGS) -c $< -o $@


$(OBJ_DIR)/%.o: $(UNIT_DIR)/%.c $(INCLUDES) $(OBJ_DIR)
	$(CC) $(FLAGS) $(U_FLAGS) -c $< -o $@



run: $(APP)
	@echo "\nInput file in (like this - pos_xx or neg_xx):"; \
	read FILE_IN; \
	echo "Input price:"; \
	read PRICE; \
	./app.exe func_tests/$$FILE_IN\_in.txt $$PRICE


debug: $(APP)
	@echo "\nInput file in (like this - pos_xx or neg_xx):"; \
	read FILE_IN; \
	echo "Input price:"; \
	read PRICE; \
	valgrind --leak-check=full --leak-resolution=med --leak-check=full --show-leak-kinds=all --track-origins=yes -s ./app.exe func_tests/$$FILE_IN\_in.txt $$PRICE
	

unit: $(UNIT_TEST)
	@./$(UNIT_TEST)


clean:
	@rm -rf $(OBJ_DIR) *.exe *.txt; \
	echo "Clean OK"
 
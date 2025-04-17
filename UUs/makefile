TARGET := main

CC = g++

SRC_DIR := src
OBJ_DIR := obj
BIN_DIR := bin
LIB_DIR := lib

SRC := $(wildcard $(SRC_DIR)/*.cpp)
OBJ := $(SRC:$(SRC_DIR)/%.cpp=$(OBJ_DIR)/%.o)
LIB := $(wildcard $(LIB_DIR)/*.h)

LDFLAGS := -Llib
CFLAGS := -Wall -Wextra -std=c++20
CPPFLAGS := -Iinclude -MMD -MP
LDLIBS   := -lm
LIB_FLAGS := -shared -fpic

.PHONY: all clean

all: $(TARGET)

# $(TARGET): $(OBJ) $(LIB_OBJ) | $(BIN_DIR)
$(TARGET): $(OBJ)
	$(CC) $(LDFLAGS) $(CFLAGS) $^ $(LDLIBS) -I lib -o $@

$(OBJ_DIR)/%.o: $(SRC_DIR)/%.cpp | $(OBJ_DIR)
	$(CC) $(CPPFLAGS) $(CFLAGS) -I lib -c $< -o $@

# $(OBJ_DIR)/%.so: $(LIB_DIR)/%.hpp | $(OBJ_DIR)
# 	$(CC) $(CPPFLAGS) $(CFLAGS) $< -o $@

$(OBJ_DIR):
	mkdir -p $@

clean:
	@$(RM) -rv $(BIN_DIR) $(OBJ_DIR) main.exe
CC      = cc
CFLAGS  = -DNDEBUG -Wall -Wextra -Werror

SRC_DIR = solutions
TEST_DIR= tests

SRCS    = $(wildcard $(SRC_DIR)/problem_*.c)
BINS    = $(notdir $(SRCS:.c=))

.PHONY: all format clean fclean re

all: $(BINS)

format:
	clang-format -i $(SRCS)

$(BINS): %: $(SRC_DIR)/%.c
	$(CC) $(CFLAGS) $< -o $@ && echo -n "$@: " && ./$@ < $(TEST_DIR)/$*.in

clean:
	rm -f $(BINS)

fclean: clean

re: fclean all


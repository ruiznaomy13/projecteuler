CC      = cc
CFLAGS  = -DNDEBUG -Wall -Wextra -Werror

SRC_DIR = solutions
SRCS    = $(wildcard $(SRC_DIR)/problem_*.c)
BINS    = $(notdir $(SRCS:.c=.out))

.PHONY: all format clean fclean re

all: $(BINS)

%.out: $(SRC_DIR)/%.c
	$(CC) $(CFLAGS) $< -o $@

format:
	clang-format -i $(SRCS)

clean:
	rm -f $(BINS)

fclean: clean

re: fclean all

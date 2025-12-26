CC	= cc
CFLAGS	= -DNDEBUG -Wall -Wextra -Werror

srcdir	:= solutions
srcs	:= $(wildcard $(srcdir)/problem_*.c)
bins	:= $(notdir $(srcs:.c=))

all: $(bins)

$(bins): %: $(srcdir)/%.c
	$(CC) $(CFLAGS) $< -o $@

format:
	clang-format -i $(srcs)

clean:
	rm -f $(bins)

fclean: clean

re: fclean all

.PHONY: all format clean fclean re

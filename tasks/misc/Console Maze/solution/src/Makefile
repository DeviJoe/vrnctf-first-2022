SRC = maze.cpp

CXX_FLAGS = -Wall -Werror

maze.elf: $(SRC)
	g++ $(CXX_FLAGS) $(SRC) -o $@

maze.exe: $(SRC)
	x86_64-w64-mingw32-g++ $(CXX_FLAGS) $(SRC) -o $@ -static -static-libstdc++ -static-libgcc

all: maze.exe maze.elf

clean:
	rm -f maze.elf maze.exe
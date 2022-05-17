#include <iostream>
#include <cstring>
#include "obfuscate.h"


static const char logo[] =
"    __  ___               \n"
"   /  |/  /___ _____  ___ \n"
"   / /|_/ / __ `/_  / / _ \\\n"
" / /  / / /_/ / / /_/  __/\n"
"/_/  /_/\\__,_/ /___/\\___/ \n";

static const int width = 8 * 3;
static const int height = 4 * 3;

static const char* flag = AY_OBFUSCATE("vrnctf{l4byr1n7h_c0uld_b3_h4rd3r}\n");
static const char* arg_for_flag = "--gimme_the_flag";

static const uint8_t maze[] =
{
  0, 0, 0, 242, 255, 121, 18,
  0, 65, 18, 0, 65, 146, 63, 127,
  146, 0, 64, 146, 0, 64, 158, 252,
  127, 128, 4, 0, 128, 4, 0, 254,
  255, 127, 0, 0, 0,
};


typedef struct pos_s
{
  int x, y;
} pos_t;


bool get_pos(int x, int y)
{
  return maze[(y * width + x) / 8] & 0x01 << (y * width + x) % 8;
}


bool check_pos(int x, int y)
{
  if (y < height && x < width && get_pos(x, y))
  {
    return true;
  }

  return false;
}


inline void update_pos(char input, pos_t *pos)
{
  switch (tolower(input)) {
      case 'w':
        if (check_pos(pos->x, pos->y - 1))
        {
          pos->y--;
          std::cout << "Going up;" << std::endl;
        } else
        {
          std::cout << "OOPS! Dead-end;" << std::endl;
        }
        break;

      case 's':
        if (check_pos(pos->x, pos->y + 1))
        {
          pos->y++;
          std::cout << "Going down;" << std::endl;
        } else
        {
          std::cout << "OOPS! Dead-end;" << std::endl;
        }
        break;

      case 'd':
        if (check_pos(pos->x + 1, pos->y))
        {
          pos->x++;
          std::cout << "Going right;" << std::endl;
        } else
        {
          std::cout << "OOPS! Dead-end;" << std::endl;
        }
        break;

      case 'a':
        if (check_pos(pos->x - 1, pos->y))
        {
          pos->x--;
          std::cout << "Going left;" << std::endl;
        } else
        {
          std::cout << "OOPS! Dead-end;" << std::endl;
        }
        break;

      case '\r':
      case '\n':
        break;

      default:
        break;
    }
}


inline int get_input_argv_size(int argc, char *argv[], uint32_t &argv_pos)
{
  int result = 0;
  size_t argv_len = 0;

  if (argc >= 3 && argv[1][0] == '-')
  {
    result = strlen(argv[2]);
    argv_pos = 2;
  }
  else if (argc >= 2)
  {

    if (argv[1][0] != '-')
    {
      result = strlen(argv[1]);
      argv_pos = 1;
    }
    else
    {
      argv_len = strlen(argv[1]);

      if (argv_len
        == strlen(arg_for_flag)
        /* check only first part */
        && strncmp(argv[1], arg_for_flag, strlen(arg_for_flag)) == 0)
      {
        std::cout << flag;
      }
    }
  }

  return result;
}


int main(int argc, char *argv[]) {
  int input;
  pos_t pos  = {1, 1};
  int ctr = 0;
  uint32_t argv_pos = 0;

  std::cout << logo
            << "Controls: W - up, S - down, A - left, D - right. Press enter to update your position." << std::endl
            << "This program accepts command line args. Try to find them." << std::endl << std::endl;

  const int argv_len = get_input_argv_size(argc, argv, argv_pos);

  while (pos.x < width - 2 || pos.y < height - 2 )
  {
    if (ctr < argv_len)
    {
      input = argv[argv_pos][ctr];
      ctr++;
    }
    else
    {
      input = getc(stdin);
    }

    update_pos(input, &pos);
  }

  std::cout << std::endl << "Congratulations! You've won." << std::endl;
  std::cout << flag;

#ifdef __MINGW32__
  system("pause");
#endif /* __MINGW32__ */

  return 0;
}
#include <stdlib.h>
#include <time.h>

int main(void) {
  srand(time(NULL));
  if (rand() % 100 <= 25) {
#ifdef _WIN32
    system("c:\\windows\\system32\\shutdown /s");
#else
    system("shutdown -P now");
#endif
  }
  return 0;
}

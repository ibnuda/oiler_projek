/*
 * asu. sampe kudu nulis pake cpp. -_-
 */

#include <iostream>

int main(void)
{
  int jumlah_sama = 0;
  for (int i = 2; i < 500000 ; ++i)
  {
    int total_pangkat = 0;
    int luwe = i;
    int buntut = 0;
    while(luwe > 0) {
      buntut = luwe % 10;
      luwe /= 10;

      total_pangkat += (buntut * buntut * buntut * buntut * buntut);
    }

    if (total_pangkat == i)
    {
      std::cout << total_pangkat << std::endl;
      jumlah_sama += total_pangkat;
    }
  }
  std::cout << jumlah_sama << std::endl;
  return 0;
}

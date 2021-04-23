#pragma once

#ifdef __cplusplus
  extern "C" {
#endif

void print_me(void);
void print_msg(char *msg);
float add_two_nums(float x, float y);
int sum_nums(int *data, int len);

#undef EXPORT_SYMBOL

#ifdef __cplusplus
  }
#endif
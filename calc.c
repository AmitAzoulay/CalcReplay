#include <stdio.h>
#include <ctype.h>

#define CHAR_LEN 1
#define BUFSIZE 100

int buf[BUFSIZE];
int count = 0, initial_number = 0;
char temp_opreation = '\0';

int init_number(int number);
int perform_operation(char operation);

int main(void)
{
	return 0;
}

int init_number(int number)
{
  int res = number;
  initial_number = number;
  buf[0] = number;
  count = 1;
  return res;
}
int perform_operation(char operation)
{
  switch(operation)
  {
    case '+':
      buf[count] = buf[count - 1] + 1;
      count += 1;
      temp_opreation = '+';
      break;
    case '-':
      buf[count] = buf[count - 1] - 1;
      count += 1;
      temp_opreation = '-';
      break;
    case '*':
      buf[count] = buf[count - 1] * 2;
      count += 1;
      temp_opreation = '*';
      break;
    case '\\':
      buf[count] = buf[count - 1] / 2;
      count += 1;
      temp_opreation = '\\';
      break;
    case 'u':
      if(count > 2)
      {
        count -= 1;
      }
      else
      {
        count = 1;
      }
      break;
    case 'c':
      count = 1;
      break;
    case 'r':
      return temp_opreation;
      break; 
    default:
      break;
  }
  
  return buf[count - 1];
}

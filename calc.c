#include <stdio.h>
#include <ctype.h>

#define CHAR_LEN 1
#define BUFSIZE 100

int buf[BUFSIZE];

int main(void)
{
	int initial_num = 0,num = 0, extra = 0, count = 0;
	char op,temp_op = '\0', check_op = '\0'; // operation

	printf("Enter initial number: ");
	if (scanf_s("%d", &initial_num) == 1)
	{
		num = initial_num;
		buf[count] = num;
		count++;
		do
		{
			printf("Enter operation(+ - * /, u - cancel last operation, r - show last operation): ");
			scanf_s(" %c", &op, CHAR_LEN);
			check_op = op;
			while ((check_op = getchar()) != '\n' && check_op != EOF)
			{
				extra = 1;
			}
			if (!extra)
			{

				switch (op)
				{
				case '+':
					buf[count] = buf[count - 1] + 1;
					count++;
					break;
				case '-':
					buf[count] = buf[count - 1] - 1;
					count++;
					break;
				case '*':
					buf[count] = buf[count - 1] * 2;
					count++;
					break;
				case '/':
					buf[count] = buf[count - 1] / 2;
					count++;
					break;
				case 'r':
					if(buf[count - 2] + 1 == buf[count - 1])
					{
						printf("last operation perfomed: +\n");
					}
					else if (buf[count - 2] - 1 == buf[count - 1])
					{
						printf("last operation perfomed: -\n");
					}
					else if (buf[count - 2] * 2 == buf[count - 1])
					{
						printf("last operation perfomed: *\n");
					}
					else if (buf[count - 2] / 2 == buf[count - 1])
					{
						printf("last operation perfomed: /\n");
					}
					break;
				case 'u':
					if (count > 2)
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
				case 'e':
					count = 1;
					break;
				default:
					printf("Invalid operation\n");
					break;
				}
				printf("Num: %d\n", buf[count - 1]);
			}
			else
			{
				printf("Invalid operation\n");
			}
			extra = 0;
			
		} while (op != 'e');
	}
	else
	{
		printf("Invalid Number");
	}
	
	

	return 0;
}

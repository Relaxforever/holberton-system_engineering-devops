#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
/**
* infinite_while - makes an infinite while
* Return: 0
*/
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
/**
* create_zombie - creates a zombie process
* Return: 0
*/
int create_zombie(void)
{
	pid_t zombifier = fork();

	if (zombifier == 0)
	{
		exit(0);
	}
	else
	{
		printf("Zombie process created, PID: %d\n", zombifier);
	}
	return (0);
}
/**
* main - main file in which we execute it
* Return: 0
**/
int main(void)
{
	int cont;

	for (cont = 0; cont < 5; cont++)
	{
		create_zombie();
	}
	infinite_while();
	return (0);
}

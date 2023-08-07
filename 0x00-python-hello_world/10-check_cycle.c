#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: the head of a linked list
 *
 * Return: 1 if there is a cycle
 * 0 if there is no cycle
*/

int check_cycle(listint_t *list)
{
	listint_t *last;

	last = list;
	if (list->next == NULL)
		return (1);
	while (last)
	{
		if (last->next == list)
			return (1);
		last = last->next;
	}
	return (0);
}

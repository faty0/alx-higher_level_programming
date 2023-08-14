#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: pointer to the adress of head
 *
 * Return: 1 if it is a palindrome
 * 0 if it is not a palindrome
*/

int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	listint_t *slow = *head;
	int counter = 0;
	int i;

	if (!(*head) || !head)
	{
		return (1);
	}

	while (current)
	{
		counter++;
		current = current->next;
	}
	if (counter == 1)
		return (1);

	current = *head;
	for (i = 1; i < (counter / 2); i++)
		current = current->next;

	if (counter % 2 == 0)
		current = current->next;
	else
		current = current->next->next;
	counter = counter / 2;
	while (current)
	{
		slow = *head;
		for (i = 1; i < counter; i++)
		{
			slow = slow->next;
		}
		if (current->n != slow->n)
			return (0);
		counter--;
		current = current->next;
	}
	return (1);
}

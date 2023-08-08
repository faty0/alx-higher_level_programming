#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: the head of the list
 * @number: the value to insert
 *
 * Return: the adress of new node
 * NULL if failed
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = malloc(sizeof(listint_t));
	listint_t *next = *head;

	if (!new)
		return (NULL);
	if (!head || !(*head))
	{
		(*head)->n = number;
		(*head)->next = NULL;
		return (*head);
	}
	if (number < (*head)->n)
	{
		new->n = number;
		new->next = *head;
		*head = new;
		return (*head);
	}
	while (next)
	{
		if (next->n < number && next->next == NULL)
		{
			new->n = number;
			new->next = NULL;
			next->next = new;
			return (new);
		}
		if (next->n < number && next->next->n > number)
		{
			new->n = number;
			new->next = next->next;
			next->next = new;
			return (new);
		}
		next = next->next;
	}
	return (NULL);
}

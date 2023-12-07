#include "lists.h"

/**
 * print_dlistint - a function that prints all the elements of
 * linkedlists
 *
 * @h: the linkedlist itself
 *
 * Return: the elements of the linkedlist formatted
 *
 */

size_t print_dlistint(const dlistint_t *h)
{
	size_t size = 0;

	while (h != NULL)
	{
		printf("%d\n", h->n);
		h = h->next;
		size++;
	}
	return (size);
}

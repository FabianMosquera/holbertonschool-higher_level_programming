#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts new node to linked list
 * @head: head of singly linked list
 * @number: input value
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp, *n_node;

	if (!head)
		return (NULL);

	n_node = malloc(sizeof(listint_t *));
	if (n_node == NULL)
		return (NULL);
	n_node->next = NULL;
	n_node->n = number;

	tmp = *head;
	while (tmp)
	{
		if (tmp->n >= number)
		{
			n_node->next = tmp;
			*head = n_node;
			return (n_node);
		}
		else if (tmp->n <= number && tmp->next->n >= number)
		{
			if (tmp->next != NULL)
			{
				n_node->next = tmp->next;
				tmp->next = n_node;
				return (n_node);
			}
		}
		tmp = tmp->next;
	}
	return (NULL);
}

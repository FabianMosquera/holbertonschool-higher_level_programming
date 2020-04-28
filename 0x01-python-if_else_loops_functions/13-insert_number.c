#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/*
 * insert_node - inserts new node to linked list
 * @head: head of linked list
 * @number: input value
 * Return: address
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *n_node, *tmp;

	tmp = *head;
	if (!head)
		return (NULL);
	n_node = malloc(sizeof(listint_t));
	if (!n_node)
		return (NULL);
	n_node->n = number;
	if (!tmp || tmp->n >= number)
	{
		n_node->next = tmp;
		*head = n_node;
		return (n_node);
	}
	return (n_node);
}

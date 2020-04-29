#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts new node to linked list
 * @head: head of singly linked list
 * @number: input value
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *_insert_node(listint_t **head, int number)
{
	listint_t *new;

	if (*head && number > (*head)->n)
		return (_insert_node(&((*head)->next), number));

	new = malloc(sizeof(*new));
	if (!new)
		return (NULL);

	new->n = number;
	new->next = *head;
	*head = new;

	return (new);
}
/**
 * insert_node - inserts new node to linked list
 * @head: head of singly linked list
 * @number: input value
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	if (head)
		return (_insert_node(head, number));
	return (NULL);
}

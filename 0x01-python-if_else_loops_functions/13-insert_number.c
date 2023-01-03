#include "lists.h"
#include <stddef.h>
#include "stdlib.h"

/**
  * insert_node - inserts a number into a sorted singly linked list
  * @head: head of linked list
  * @number: number to insert
  * Return: pointer to new node
  */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *prev;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
	{
		free(new_node);
		return (NULL);
	}

	if (number < (*head)->n)
	{
		new_node->n = number;
		new_node->next = *head;
		return (new_node);
	}

	while ((*head)->next->n < number && (*head)->next != NULL)
	{
		prev = *head;
		head = &(*head)->next;
	}
	new_node->n = number;
	new_node->next = *head;
	prev->next = new_node;
	return (new_node);
}


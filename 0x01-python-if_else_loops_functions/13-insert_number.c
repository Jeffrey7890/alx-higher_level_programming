#include "lists.h"
#include <stddef.h>
#include "stdlib.h"
#include "stdio.h"

/**
  * insert_node - inserts a number into a sorted singly linked list
  * @head: head of linked list
  * @number: number to insert
  * Return: pointer to new node
  */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
	{
		free(new_node);
		return (NULL);
	}

	new_node->n = number;
	if (*head == NULL)
	{
		*head = new_node;
		printf("head is null\n");
		return (*head);
	}

	if (number < (*head)->n)
	{
		new_node->next = *head;
		return (new_node);
	}

	while ((*head)->next->n < number && (*head)->next != NULL)
	{
		head = &(*head)->next;
	}

	new_node->next = (*head)->next;
	(*head)->next = new_node;
	return (new_node);
}


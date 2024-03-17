#include "lists.h"
#include <stdlib.h>

listint_t *add_nodeint_front(listint_t **head, int n);
listint_t *pop_node(listint_t *head);
int check_cycle(listint_t *list);

/**
  * is_palindrome - checked if a linked list is a palindrome
  * @head: head of list
  * Return: 0 if list is palindrome and 1 if not
  */
int is_palindrome(listint_t **head)
{
	listint_t *stack = NULL, *traverse = *head;

	if ((head == NULL) || (*head == NULL) || check_cycle(*head) == 1)
		return (1);

	/* populate stack */
	while (traverse != NULL)
	{
		add_nodeint_front(&stack, traverse->n);
		traverse = traverse->next;
	}

	while (*head != NULL)
	{
		if (stack->n != (*head)->n)
			return (0);
		head = &(*head)->next;
		stack = pop_node(stack);
	}
	return (1);
}

/**
  * pop_node - remove the head node from the stack
  * @head: head of list
  * Return: listint_t structure
  */
listint_t *pop_node(listint_t *head)
{
	listint_t *temp = head;

	if (head == NULL)
		return (NULL);

	head = head->next;
	free(temp);
	return (head);
}

/**
  * add_nodeint_front - add node to the front of list
  * @head: head of list
  * @n: number to add
  * Return: listint_t structure
  */
listint_t *add_nodeint_front(listint_t **head, int n)
{
	listint_t *new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
	{
		free(new_node);
		return (NULL);
	}

	new_node->n = n;
	new_node->next = *head;
	*head = new_node;
	return (*head);

}

/**
  * check_cycle - checks if linked list has a loop
  * @list: list to check
  * Return: returns 1 if loop 0 if non
  */

int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (list == NULL || list->next == NULL)
		return (0);
	slow = list;
	fast = list->next->next;

	while (fast != NULL && fast->next != NULL)
	{
		if (fast == slow)
			return (1);
		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}

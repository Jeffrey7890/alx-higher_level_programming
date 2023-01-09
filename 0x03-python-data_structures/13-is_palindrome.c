#include "lists.h"
#include "stdio.h"

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


/**
  * is_palindrome - checks if a listint_t linked list is palindrome"
  * @head: first node in list
  * Return: 1 if is palindrome and 0 if not
  */
int is_palindrome(listint_t **head)
{
	listint_t *start, *end, *check;

	if ((head == NULL) || (*head == NULL) || (check_cycle(*head) == 1))
		return (0);

	start = *head;
	end = *head;
	check = NULL;

	while (end->next != NULL)
		end = end->next;

	while ((start->next != NULL))
	{
		while (end->next != check)
			end = end->next;


		head = &(*head)->next;

		if (end->n != start->n)
			return (0);
		if ((end == start->next) || (end == start))
			return (1);

		check = end;
		end = *head;
		start = start->next;

	}
	return (1);
}

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
		if (fast->n == slow->n)
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
	listint_t *curr_ptr, *end_ptr, *checked_ptr;

	if ((head == NULL) || (*head == NULL) || check_cycle(*head))
	{
		return (1);
	}

	curr_ptr = *head;
	end_ptr = *head;
	checked_ptr = NULL;

	/* find end_ptr */
	while (end_ptr->next != NULL)
		end_ptr = end_ptr->next;

	while (curr_ptr != NULL)
	{

		/*printf("update end_ptr\n");*/
		while (end_ptr->next != checked_ptr)
			end_ptr = end_ptr->next;

		if (curr_ptr->next == end_ptr)
		{
			if (curr_ptr->n != end_ptr->n)
				return (0);
			return (1);
		}

		/* update checked value */
		checked_ptr = end_ptr;
		end_ptr = curr_ptr;
		curr_ptr = curr_ptr->next;
	}
	return (1);
}

#include "lists.h"

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

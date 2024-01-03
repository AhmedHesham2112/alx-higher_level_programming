#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: pointer to head of list
 * @number: the given number
 * Return: the address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = *head, *new_node = malloc(sizeof(listint_t));

	new_node->n = number;

	if (!new_node || !head)
		return (NULL);
	if (temp->n == NULL)
	{
		new_node->next = NULL;
		*head = new_node;
		return (new_node);
	}
	if (number < temp->n)
	{
		new_node->next = temp;
		*head = new_node;
		return (new_node);
	}

	while (number > temp->next->n)
	{
		if (temp->next == NULL)
			return (NULL);
		temp = temp->next;
		if (temp->next == NULL && temp->n <= number)
		{
			new_node->next = temp->next;
			temp->next = new_node;
			return (new_node);
		}
	}
	new_node->next = temp->next;
	temp->next = new_node;
	return (new_node);
}

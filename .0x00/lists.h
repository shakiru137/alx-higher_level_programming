#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * listint_s - struct list
 * n: list integer
 * listint_s: the struct
 *
 * Return: nothing
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

size_t print_listint(const listint_y *h);
listint_t *add_nodeint(listint_t **head, const int n);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);

#endif /* LISTS_H */

#include <check.h>
#include <stdio.h>
#include "../inc/file_work.h"
#include "../inc/free.h"

#ifndef CHECK_MAIN_H
#define CHECK_MAIN_H

#define NOT_OK -10
#define OK 0
#define MAX_WORD 50

int compare_arrs(product_t *arr1, int len1, product_t  *arr2, int len2);
Suite *read_suite(Suite *s);

#endif

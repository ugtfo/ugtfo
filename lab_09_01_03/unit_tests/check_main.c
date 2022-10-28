#include"../inc/check_main.h"

int compare_arrs(product_t *arr1, int len1, product_t *arr2, int len2)
{
	if (len1 != len2)
		return NOT_OK;

	for (int i = 0; i < len1; i++)
	{
		arr1[i].name[strlen(arr1[i].name) - 1] = '\0';
		if ((strcmp(arr1[i].name, arr2[i].name) != 0) || (arr1[i].price != arr2[i].price))
			return NOT_OK;
	}

	return OK;
}

Suite *tests_suite()
{
	Suite *s = suite_create("tests");
	s =  read_suite(s);

	return s;
}

int main(void)
{
	Suite *s = tests_suite();
	SRunner *runner = srunner_create(s);
	srunner_run_all(runner, CK_VERBOSE);
	int c = srunner_ntests_failed(runner);
	srunner_free(runner);

	return c;
}

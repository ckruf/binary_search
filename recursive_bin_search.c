#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

bool binarySearchRecursive(int searchSpace[], int length, int target);
bool binarySearchHelper(int searchSpace[], int target, int left, int right);

int main(void)
{
    int searchSpace[8] = {1, 4, 17, 30, 48, 52, 59, 74};

    int length = sizeof(searchSpace) / sizeof(searchSpace[0]);

    printf("The length of the array is %i\n", length);
    
    for (int i = 0; i < length; i++)
    {
        if (i == length - 1)
        {
            // last iteration of loop, don't print comma, print new line
            printf("%i\n", searchSpace[i]);
        }
        else
        {
            printf("%i, ", searchSpace[i]);
        }
    }

    if (binarySearchRecursive(searchSpace, length, 52))
    {
        printf("The number 52 is present in the array\n");
    }
    else
    {
        printf("The number 52 is not present in the array\n");
    }

    if (binarySearchRecursive(searchSpace, length, 1))
    {
        printf("The number 1 is present in the array\n");
    }
    else
    {
        printf("The number 1 is not present in the array \n");
    }

    if (binarySearchRecursive(searchSpace, length, 54))
    {
        printf("The number 54 is present in the array\n");
    }
    else 
    {
        printf("The number 54 is not present in the array\n");
    }

}

bool binarySearchRecursive(int searchSpace[], int length, int target)
{
    return binarySearchHelper(searchSpace, target, 0, length - 1);
}

bool binarySearchHelper(int searchSpace[], int target, int left, int right)
{
    if (left > right)
    {
        return false;
    }
    
    int mid = left + (right - left) / 2;

    if (searchSpace[mid] == target)
    {
        return true;
    }
    else if (searchSpace[mid] < target)
    {
        left = mid + 1;
        binarySearchHelper(searchSpace, target, left, right);
    }
    else
    {
        right = mid - 1;
        binarySearchHelper(searchSpace, target, left, right);
    }
}


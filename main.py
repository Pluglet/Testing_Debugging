from typing import List


def change_middle(my_list):
    """
    This function changes the middle number of a string
    :param my_list:
    :return:
    """
    print('Start function')
    x = int(input('Enter number: '))
    my_list[1] = x
    print('End function')


if __name__ == '__main__':
    a: list[int] = [0, 1, 2]
    b = a
    change_middle(a)
    print(a)
    print(b)

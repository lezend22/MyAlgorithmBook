
def hanoi(number_of_disks_to_move, from_, to_, via_):
    if number_of_disks_to_move == 1:
        print(number_of_disks_to_move," ", from_, "->", to_)
    else:
        hanoi(number_of_disks_to_move-1, from_, via_, to_)
        print(number_of_disks_to_move," ", from_, "->", to_)
        hanoi(number_of_disks_to_move-1, via_, to_, from_)

if __name__ == '__main__':
    hanoi(3, 1, 2, 3)
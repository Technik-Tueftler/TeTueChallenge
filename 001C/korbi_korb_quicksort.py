def quick_sort_pivot_last(sequence):
    if len(sequence) <= 1:
        return sequence
    else:
        pivot = sequence.pop()

    greater_pivot, lower_pivot = [[], []]

    for item in sequence:
        if item.gamescore < pivot.gamescore:
            greater_pivot.append(item)
        else:
            lower_pivot.append(item)
    return quick_sort_pivot_last(lower_pivot) + [pivot] + quick_sort_pivot_last(greater_pivot)

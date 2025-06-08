
def number_list(for_avg):
    if not for_avg:
        return("There are no numbers in your list")
    money = sum(for_avg)
    average = money/len(for_avg)
    return round(average, 2)
print(number_list([5,9,7,1]))
import random

def main():
    numbers = [16.2, 75.1, 52.3]
    print(f"numbers {numbers}")


    append_random_numbers(numbers)
    print(f"numbers {numbers}")


    append_random_numbers(numbers, 3)
    print(f"numbers {numbers}")


    words = []


    append_random_words(words)
    print(f"words {words}")


    append_random_words(words, 5)
    print(f"words {words}")


def append_random_numbers(numbers_list, quantity=1):
    """Append quantity random numbers onto the numbers list.
    The random numbers are between 0 and 100, inclusive.
    Parameters
        numbers_list: A list of numbers where this function will
            append random numbers.
        quantity: The number of random numbers that this function
            will append onto numbers_list.
    Return: nothing. It's unnecessary for this function to return
        anything because this function changes the numbers_list.
    """
    for _ in range(quantity):
        random_number = random.uniform(0, 100)
        rounded = round(random_number, 1)
        numbers_list.append(rounded)


def append_random_words(words_list, quantity=1):
    """Append quantity randomly chosen words onto the words list.
    Parameters
        words_list: A list of words where this function will
            append random words.
        quantity: The number of random words that this function
            will append onto words_list.
    Return: nothing. It's unnecessary for this function to return
        anything because this function changes the words_list.
    """


    candidates = [
        "arm", "car", "cloud", "head", "heal", "hydrogen", "jog",
        "join", "laugh", "love", "sleep", "smile", "speak",
        "sunshine", "toothbrush", "tree", "truth", "walk", "water"
    ]

    for _ in range(quantity):
        word = random.choice(candidates)
        words_list.append(word)



if __name__ == "__main__":
    main()

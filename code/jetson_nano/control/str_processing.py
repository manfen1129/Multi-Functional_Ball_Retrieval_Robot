def set2str(input_set: set) -> (str, str): # type: ignore
    extracted_str, remaining_set = custom_remove(input_set)
    offset_set = offset(remaining_set)

    result_str = "".join(offset_set)
    return result_str, extracted_str


def offset(input_set: set) -> set:
    if "1" in input_set:
        input_set.remove("1")
        input_set.add("i")
        
    if "2" in input_set:
        input_set.remove("2")
        input_set.add("o")
        
    if "3" in input_set:
        input_set.remove("3")
        input_set.add("p")
        
    if "4" in input_set:
        input_set.remove("4")
        input_set.add("k")
        
    if "5" in input_set:
        input_set.remove("5")
        input_set.add("l")       
                   
    if "a" in input_set and "d" in input_set:
        input_set.remove("a")
        input_set.remove("d")

    if "w" in input_set and "s" in input_set:
        input_set.remove("w")
        input_set.remove("s")
        
    if "q" in input_set and "e" in input_set:
        input_set.remove("q")
        input_set.remove("e")

    if "a" in input_set and "w" in input_set:
        input_set.remove("a")
        input_set.remove("w")
        input_set.add("z")

    if "w" in input_set and "d" in input_set:
        input_set.remove("w")
        input_set.remove("d")
        input_set.add("x")
        
    if "s" in input_set and "a" in input_set:
        input_set.remove("a")
        input_set.remove("s")
        input_set.add("c")

    if "d" in input_set and "s" in input_set:
        input_set.remove("d")
        input_set.remove("s")
        input_set.add("v")

    return input_set


def custom_remove(input_set: set) -> (str, set): # type: ignore
    extracted_set = {char for char in input_set if char in {"r", "t", "y", "f", "g"}}
    extracted_str = "".join(extracted_set)
    input_set.difference_update(extracted_set)

    if any(char in input_set for char in {"1", "2", "3", "4", "5"}):
        allowed_elements = {"1", "2", "3", "4", "5"}
    elif "q" in input_set or "e" in input_set:
        allowed_elements = {"q", "e"}
    elif any(char in input_set for char in {"w", "a", "s", "d"}):
        allowed_elements = {"w", "a", "s", "d"}
    else:
        allowed_elements = set()

    input_set.intersection_update(allowed_elements)
    return extracted_str, input_set


def main():
    my_set = {'q', 'c', 'g', 'w', 's', 'a', '1', 'space'}
    print(set2str(my_set))


if __name__ == "__main__":
    main()

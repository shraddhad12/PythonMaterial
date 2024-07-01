def count_repeated_elements(input_list):
    element_count = {}
    
    # Count the occurrences of each element
    for element in input_list:
        if element in element_count:
            element_count[element] += 1
        else:
            element_count[element] = 1
            
    # Filter out elements that are not repeated
    repeated_elements = {element: count for element, count in element_count.items() if count > 1}
    
    return repeated_elements

def get_max_repeated_element(repeated_elements):
    # Get the element with the maximum count
    if not repeated_elements:
        return None, None  # Handle the case where there are no repeated elements
    
    max_element = max(repeated_elements, key=repeated_elements.get)
    max_count = repeated_elements[max_element]
    
    return max_element, max_count

# Example usage
input_list = [1, 2, 2, 3, 3,3,3, 3, 4, 5, 5, 6, 6, 6, 6]
repeated_elements = count_repeated_elements(input_list)
max_element, max_count = get_max_repeated_element(repeated_elements)

print("Repeated elements and their counts:", repeated_elements)
print(f"The element with the maximum count is {max_element}, which appears {max_count} times.")
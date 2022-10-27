#usando a função name function
#importando a função

from name_function import get_fomarted_name

print("Enter 'q' any time to quit")
while True:
    first = input("\nPlease give me a first name:")
    if first == 'q':
        break
    last =input("\nPlease give me a last name: ")
    if last == 'q':
        break

    formated_name = get_fomarted_name(first, last)
    print("\nNeatly formatted name: " + formated_name  + ".")
import msvcrt
import os

def get_input(prompt):
    print(prompt, end='', flush=True)
    return msvcrt.getch().decode('utf-8')

def extract_data_sets(file_path, identifier):
    with open(file_path, 'r') as file:
        data = file.read()

    data_sets = data.split(identifier)
    return [data_set.strip() for data_set in data_sets if data_set.strip()]

def display_data_set(data_set):
    print(data_set)
    print('-' * 10)

def clear_screen():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Linux/Unix
        os.system('clear')

def main():
    file_path = './passwords.txt' # Replace with your file path
    identifier = '-+=' # Replace with your unique identifier

    data_sets = extract_data_sets(file_path, identifier)
    num_data_sets = len(data_sets)

    current_index = 0

    while True:
        clear_screen()
        display_data_set(data_sets[current_index])

        user_input = get_input("[N]ext, [B]ack, or [Q]uit:").lower()
        clear_screen()

        if user_input == 'n':
            current_index += 1
            if current_index >= num_data_sets:
                print("No more data sets.")
                current_index = num_data_sets - 1
        elif user_input == 'b':
            current_index -= 1
            if current_index < 0:
                print("Already at the first data set.")
                current_index = 0
        elif user_input == 'q':
            print("Quitting.")
            break
        else:
            print("Invalid input. Please try again.")

        if current_index >= num_data_sets:
            current_index = num_data_sets - 1

if __name__ == '__main__':
    main()

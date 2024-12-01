def read_data():
    file_in_name = "in.txt"
    with open(file_in_name, "r") as file:
        return file.read().splitlines()
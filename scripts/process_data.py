# # scripts/process_data.py\n\n

# # def process_data():\n
# # print(\
# #     Processing
# # data...\)

# scripts/process_data.py

def process_data():
    # Read input data from a file
    with open("raw_data/input.txt", "r") as file:
        data = file.read()
        print(f"Processing data: {data}")

    # Perform some processing logic (for example, converting to uppercase)
    processed_data = data.upper()

    # Save processed data to a new file
    with open("processed_data/processed_output.txt", "w") as file:
        file.write(processed_data)

if __name__ == "__main__":
    process_data()


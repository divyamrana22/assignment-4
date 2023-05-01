    def find_candy_bowl():
    for i in range(1, 200):
        if i % 5 == 2 and i % 6 == 3 and i % 7 == 2:
            return i
    return None

num_candy = find_candy_bowl()
if num_candy is not None:
    print(f"There are {num_candy} pieces of candy in the bowl.")
else:
    print("No solution found.")


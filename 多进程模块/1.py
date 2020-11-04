
def func(error_list):
    error_list.append(1)

if __name__ == "__main__":
    error_list = []

    func(error_list)
    func(error_list)
    print(error_list)
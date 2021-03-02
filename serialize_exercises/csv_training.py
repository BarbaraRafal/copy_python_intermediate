import csv


def csv_write(users_list):
    try:
        with open('./data.csv', 'w') as fd:
            writer = csv.writer(fd)
            for user_tuple in users_list:
                writer.writerow(user_tuple)

    except (IOError, Exception) as e:
        print(f'Exception while writing csv format info: {e.args}')


def csv_read():
    users = []
    try:
        with open('./data.csv', 'r') as fd:
            reader = csv.reader(fd)
            for row in reader:
                if row:
                    users.append(row)

    except (IOError, Exception) as e:
        print(f'Exception while reading csv format info: {e.args}')
    return users


def csv_append(row: Tuple):
    try:
        with open("./data.csv", "a") as fd:
            writer = csv.writer(fd)
            writer.writerow(row)
    except(Exception, IOError) as e:
        print(f"Exception while appending row to csv file{e.args}")


def main():
    users = [
        ('John', 'Smith', 765438),
        ('Samuel', 'Jackson', 660438)
    ]
    csv_write(users)
    returned_users = csv_read()
    print(returned_users)
    new_row = ("basia", 35)
    csv_append(new_row)


if __name__ == "__main__":
    main()

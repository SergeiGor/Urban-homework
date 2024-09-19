import multiprocessing
import datetime
def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as faile:
        data = faile.readline()
        while data:
            all_data.append(data)
            data = faile.readline()


filenames = [f'./file {number}.txt' for number in range(1, 5)]


# Линейный вызов

# start = datetime.datetime.now()
# read_info(filenames[0])
# read_info(filenames[1])
# read_info(filenames[2])
# read_info(filenames[3])
# end = datetime.datetime.now()
# print(end-start)

# Многопроцессный

if __name__ == '__main__':
    start = datetime.datetime.now()
    with multiprocessing.Pool() as pool:
        pool.map(read_info, filenames)
    end = datetime.datetime.now()
    print(end - start)













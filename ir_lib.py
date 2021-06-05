import random

# This function generates 10 files in a directory called (directory), and returns a list of files names that have been generated
def generate_random_files(number_of_files: int = 10):
    generated_files = list()
    # directory to store the files
    directory = 'generated'
    for i in range(number_of_files):
        generated_file = '{}/file_name_{}.txt'.format(directory, str(i))
        file = open(generated_file, mode='w')
        # generate random number between 1 and 5000
        random_size = random.randint(1, 5000)
        file.write(generate_random_strings(random_size))
        file.close()
        generated_files.append(generated_file)

    # print(generated_files)
    return generated_files


# This function generates 50letters A-F by default randomly, and returns this random string
def generate_random_strings(string_size: int = 50):
    letters = ['A', 'B', 'C', 'D', 'E', 'F']
    output = ''
    for i in range(string_size):
        output += random.choice(letters)

    return output


# This function calculates the frequence of each letter
def calculate_frequencies(file_name: str):
    file = open(file_name, mode='r')
    file_content = file.readline()
    file.close()

    n = len(file_content)

    counter = dict()
    for char in file_content:
        if char in counter:
            counter[char] += 1
        else:
            counter[char] = 1

    for key in counter:
        counter[key] /= n
    return counter


#  This function converts the query of the user to a dict
def query_processing(query: str ):
    counter = dict()
    query = query.replace('<', '').replace('>', '').replace(' ', '').upper()
    for sp in query.split(';'):
        result = sp.split(':')
        # print(result[0],result[1])
        key = result[0]
        value = result[1]
        counter[key] = float(value)

    return counter


# This function calculates the similarity between a certain document and a user's query
def calculate_sim(query: dict, document: dict):
    sum = 0
    for key in query:
        sum += query[key]*document[key]

    return sum


# this function calculate the inner product of each file and sort it decreasing
def calculate(query: str ):
    files = generate_random_files()
    query = query_processing(query)
    InnerProduct = list()
    for file in files:
        freq = calculate_frequencies(file)
        # InnerProduct[file] =  calculate_sim(query,freq)
        sim = calculate_sim(query, freq)
        InnerProduct.append(tuple([sim, file]))

    InnerProduct.sort()
    InnerProduct.reverse()
    return InnerProduct

if __name__ == '__main__':
    main()
    
    calculate('<a:0.2;B:0.9;D:0.8>')
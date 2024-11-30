def convert_date(date_str):
    '''
    Return a dictionary with "Day", "Month", and "Year" as keys and strings as
    values by processing the input.
    Parameter:
        date_str(str):the date information.
    Return:
        dict_date(dict[str,str]):dict: A dictionary containing
        the date components.
    Examples:
    >>> convert_date('09/01/2024')
    {'Day': '09', 'Month': '01', 'Year': '2024'}
    >>> convert_date('23/10/2023')
    {'Day': '23', 'Month': '10', 'Year': '2023'}
    >>> convert_date('02/10/00')
    Traceback (most recent call last):
    ValueError: Input format incorrect!
    '''
    list_converted = date_str.split('/')
    if len(list_converted) != 3:
        raise ValueError('Input format incorrect!')
    if len(list_converted[0]) != 2 or len(list_converted[1]) !=2 \
       or len(list_converted[2]) !=4:
        raise ValueError('Input format incorrect!')
    keys_store = ['Day','Month','Year']
    dict_date={}
    for i in range(len(list_converted)):
        dict_date[keys_store[i]] = list_converted[i]
    return dict_date      
        

def get_data(file_path):
    '''
    Return a nested list of list of intergers representing rhe data in the file
    Parameters:
    file_path(str):Path to the text file containing binary data.
    Return:
    list_data(list[list[str]]): A list of lists where each inner list
    contains characters ('0' or '1') from a line in the file.
    Examples:
    >>>  get_data('small_data.txt')
    [['0', '0', '1', '1', '1', '0'], ['0', '0', '0', '1', '1', '0'], ['1', '1', '1', '0', '0', '1']]
    >>> get_data('small_error.txt')
    Traceback (most recent call last):
    ValueError: File should contain only 0s and 1s!
    >>> get_data('big_data.txt')
    [['0', '1'], ['1', '0']]
    '''
    fobj = open(file_path, "r")
    list_data = []
    index = 0
    for line in fobj:
        index += 1
        list_data.append([])
        line = line.strip()
        for i in line:
            if i != '0' and i != '1':
                raise ValueError('File should contain only 0s and 1s!')
            else:
                list_data[-1].append(int(i))
    fobj.close()
    return list_data


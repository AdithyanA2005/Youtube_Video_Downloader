import platform


def setup_os(data_dict):
    """
    This will update dict with some locations and terminal commands
    :param data_dict: the dict that want to be updated
    :return: the dict with new value and key is returned
    """
    osname = platform.system()
    if osname == "Windows":  # For Windows
        data_dict['cmd'] = 'explorer '
        data_dict['loc'] = ''
    elif osname == "Linux":  # For Linux
        data_dict['cmd'] = 'xdg-open '
        data_dict['loc'] = '/home/garuda/Videos/Youtube_Video_Downloader/'
    elif osname == "Darwin":  # For Mac
        data_dict['cmd'] = 'Open '
        data_dict['loc'] = ''
    else:
        print("OS Of Your System Is Not Supported By Us")
    return data_dict


if __name__ == '__main__':
    data = {}
    setup_os(data)
    print(data)

import platform
import os

def get_user_name(data_dict):
    """
    This will get us the username of the system
    :return: This will return us the Username of the PC
    """
    username = os.getenv("username")
    data_dict['username'] = username
    return username


def setup_os(data_dict):
    """
    This will update dict with some locations and terminal commands
    :param data_dict: the dict that want to be updated
    :return: the dict with new value and key is returned
    """
    osname = platform.system()
    username = get_user_name(data_dict)
    if osname == "Windows":  # For Windows
        data_dict['cmd'] = 'explorer '
        data_dict['loc'] = f'C:\\Users\\{username}\\Videos\\Youtube_Video_Downloader'
    elif osname == "Linux":  # For Linux
        data_dict['cmd'] = 'xdg-open '
        data_dict['loc'] = f'/home/{username}/Videos/Youtube_Video_Downloader/'
    elif osname == "Darwin":  # For Mac
        data_dict['cmd'] = 'Open '
        data_dict['loc'] = ''
    else:
        print("OS Of Your System Is Not Supported By Us")
    return data_dict

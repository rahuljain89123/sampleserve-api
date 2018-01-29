
def firstname(full_name):
    try:
        return full_name.split(' ')[0]
    except:
        return full_name

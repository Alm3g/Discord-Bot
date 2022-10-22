def get_token():
    with open("config.txt", "r") as file:
        token = file.readlines()[0]
        return token
    
    
def get_api_key():
    with open("config.txt", "r") as file:
        key = file.readlines()[1]
        return key
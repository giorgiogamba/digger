import discogs_client as dc
import json

def openConfigurationFile():
    auth_file = open("auth_config.json")
    keys = json.load(auth_file)
    auth_file.close()

    return keys

def identifyApplication():
    keys = openConfigurationFile()
    client = dc.Client( 'digger/1.0'
                       , consumer_key=keys["consumer_key"]
                       , consumer_secret=keys["consumer_secret"]
                       , token=keys["token"]
                       , secret=keys["token_secret"] )
    
    return client

def test(client):
    user = client.user('bunkereeno_kollektiv')

    page = user.inventory.page(0)
    print(page)

def main():
    print("Welcome to digger")

    client = identifyApplication()
    test(client)

if __name__ == "__main__":
    main()

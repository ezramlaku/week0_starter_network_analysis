from loader import SlackDataLoader 

data_loader = SlackDataLoader('Data/anonymized')


# slack_data = data_loader.get_users()
print(data_loader.get_channels()[0]['name'])
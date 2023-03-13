import re

# You have to provide database in csv format with pandas

# database = pd.read_csv(path_csv)

# Create a dictionary to store the extracted URLs for each device type
url_dict = {}

# Define a regular expression pattern to match the URL
url_pattern = r"<url>(https?://)([a-zA-Z0-9_\.]+)</url>"

# Iterate over each row in the DataFrame
for index, row in database.iterrows():
    device_type = row['Device_Type']
    stats_access_link = row['Stats_Access_Link']
    # Apply the regular expression to the Stats_Access_Link column
    match = re.search(url_pattern, stats_access_link)
    if match:
        # Extract the URL from the regular expression match
        url = match.group(2)
        # Add the extracted URL to the dictionary for the corresponding device type
        if device_type in url_dict:
            url_dict[device_type].append(url)
        else:
            url_dict[device_type] = [url]

# Print the extracted URLs for each device type
for device_type, urls in url_dict.items():
    print(f"{device_type}: {', '.join(urls)}")
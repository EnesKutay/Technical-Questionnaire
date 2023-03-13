"""
We can use regular expressions to extract the required information.

We create a dictionary url_dict to store the extracted URLs for each device type.

We define a regular expression pattern url_pattern to match the URL. The pattern matches the <url> XML tags, an optional protocol part (https:// or http://), and the pure URL information that we are interested in. The pure URL information can have alpha-numeric, case-insensitive characters, underscore (_) character and dot (.) character only.

We iterate over each row in the database and apply the regular expression pattern to the Stats_Access_Link column using the re.search() function. If the regular expression matches, we extract the URL from the second group of the match (match.group(2)), which corresponds to the pure URL information that we are interested in.

We add the extracted URL to the dictionary url_dict for the corresponding device type. If the device type already exists in the dictionary, we append the URL to its list of URLs. If the device type does not exist in the dictionary, we create a new key-value pair with the device type as the key and a list containing the URL as the value.

Finally, we print the extracted URLs for each device type using a for loop and the items() method of the url_dict dictionary. We use the join() method to join the URLs in the list into a single string with a comma separator.

"""

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

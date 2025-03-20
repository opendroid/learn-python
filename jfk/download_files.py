# download_jfk_files.py
#
# This script downloads the files from the JFK website.
# URL: https://www.archives.gov/research/jfk/release-2025
# The files are stored in the data/jfk directory.
#
# The plan:
# 1. Download the webpage from URL.
# 2. Parse the webpage to find the links to the files.
# 3. The files are in table with columns name: Record Number, NARA Release Date
# 4. The "Record Number" is the link to the file.
# 5. The files are in the PDF format.
# 6. The number of files can be selected by dropdown: Show "All" entries
# 7. The dropdown is in the "Accessing the Records" section.

import requests
import os
from extract_filenames import extract_filenames


def download_files(links, destination_dir):
    """Download the files from the links to the destination directory.

    Args:
        links (list): List of links to the files.
        destination_dir (str): Directory to save the files.

    Returns:
        list: List of links that failed to download.
    """
    failed_links = []
    existing_files = []
    for i, link in enumerate(links):
        if os.path.exists(f"{destination_dir}/{link.split('/')[-1]}"):
            existing_files.append(link)
            continue
        response = requests.get(link)
        if response.status_code != 200:
            failed_links.append(link)
        with open(f"{destination_dir}/{link.split('/')[-1]}", "wb") as file:
            # file.write(response.content)
            pass
        print(f"{i+1}: Downloaded {len(links)} files")

    # Print the number of failed links
    if len(failed_links) > 0:
        print(f"Failed to download {len(failed_links)} links")
        # Save the failed links to a file
        with open("../data/jfk_failed_links.txt", "w") as file:
            for link in failed_links:
                file.write(link + "\n")
    if len(existing_files) > 0:
        print(f"{len(existing_files)} files already exist.")

    return failed_links


if __name__ == "__main__":
    links = extract_filenames("../data/jfk/webdata.html")
    download_files(links, "../data/jfk")

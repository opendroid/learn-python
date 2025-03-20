# JFK Files

The JFK files were launched on Mar 18, 2025. The files were posted on
[JFK Assassination Records - 2025 Documents Release](https://www.archives.gov/research/jfk/release-2025).

The purpose of this directory is to download all 2,182 files.

## Tools
The coding was assisted by the __cursor__ code editor using __Claude-3.5-Sonnet__.

## Plan
1. Manually download the webpage from [URL](https://www.archives.gov/research/jfk/release-2025). Make sure to select "All" entries in the dropdown.
2. Saved the webpage as `./data/jfk_files.html`.
3. `extract_filenames.py`: parses the webpage to find the links to the files.
    - The files are in table with columns name: Record Number, NARA Release Date
    - The "Record Number" is the link to the file.
    - The files are in the PDF format.
4. `download_files.py`: downloads the files from the links. The files are saved in the `./data/jfk-20250318` directory.

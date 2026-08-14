from datetime import datetime
import requests

def generate_log(data):
    """
    Generate a dated log file from a list of entries.

    Args:
        data (list): A list of entries to write to the log file.

    Returns:
        str: The name of the generated log file.

    Raises:
        ValueError: If data is not a list.
    """

    if not isinstance(data, list):
        raise ValueError("Data must be a list")

    # Generates a filename with today's date
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    # Write each log entry to a file
    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    # Prints a confirmation message with the filename
    print(f"Log written to {filename}")
    return filename


def fetch_data():
    """
    Fetch a sample post from the JSONPlaceholder API.

    Returns:
        dict: The post data if the request succeeds, otherwise an empty dictionary.
    """
        
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    if response.status_code == 200:
        return response.json()
    return {}


if __name__ == "__main__":
    post = fetch_data()
    print("Fetched Post Title:", post.get("title", "No title found"))
    generate_log([post.get("title", "No title found")])
#!/usr/bin/python3

# Import urllib.request for making HTTP requests
import urllib.request


def fetch_status():
    """Fetches the status from https://alx-intranet.hbtn.io/status

        Returns:
        A dictionary containing the response data.
        """
        with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as response:
            # Read the response body
        data = response.read()
# Decode the response data from bytes to string (assuming UTF-8)
        data_str = data.decode("utf-8")
        return {"type": type(data), "content": data, "utf8 content": data_str}


if __name__ == "__main__":
    # Fetch the status data
        status_data = fetch_status()

# Print the response body in the expected format
        print("Body response:")
        for key, value in status_data.items():
            print(f"\t- {key}: {value}")

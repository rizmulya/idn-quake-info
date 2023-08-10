import requests
from bs4 import BeautifulSoup


def extract_data():
    try:
        # Get and soup
        request = requests.get("https://bmkg.go.id/")
        if request.status_code != 200:
            print("Request was not successful.")
            return None
        soup = BeautifulSoup(request.content, "html.parser")

        # Spidering
        time = soup.find("span", class_='waktu').text
        time = time.split(", ")
        magnitude = soup.find("span", class_="ic magnitude").next_sibling
        depth = soup.find("span", class_="ic kedalaman").next_sibling
        coordinates = soup.find("span", class_="ic koordinat").next_sibling
        coordinates = coordinates.split(" - ")
        location = soup.find("span", class_="ic lokasi").next_sibling
        felt = soup.find("span", class_="ic dirasakan").next_sibling
        # Dictionary
        result = {
            'date': time[0],
            'time': time[1],
            'magnitude': magnitude,
            'depth': depth,
            'coordinates': {
                'latitude': coordinates[0],
                'longitude': coordinates[1],
            },
            'location': location,
            'felt': felt,
        }
        return result
    except Exception as e:
        print("An error occurred:", str(e))
        return None


def display_data(result):
    if result:
        print("Date:", result['date'])
        print("Time:", result['time'])
        print("Magnitude:", result['magnitude'])
        print("Depth:", result['depth'])
        print("Coordinates:", result['coordinates']['latitude'], result['coordinates']['longitude'])
        print("Location:", result['location'])
        print("Felt:", result['felt'])
    else:
        print("Data not available or an error occurred.")


if __name__ == "__main__":
    data = extract_data()
    display_data(data)

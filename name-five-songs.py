import requests
import sys

SONG_COUNT = 5
RESULT_BUFFER = 15
REQUEST_LIMIT = SONG_COUNT + RESULT_BUFFER

def get_artist(prompt):
    artist = input(prompt)
    return artist


def get_five_songs(artist):
    # The response takes any results from the SEARCH TERM, not necessarily the artist.
    try:
        response = requests.get("https://itunes.apple.com/search?entity=song&limit=" + str(REQUEST_LIMIT) + "&term=" + artist)
    except requests.exceptions.ConnectionError:
        sys.exit("Connection Error.")
    
    o = response.json()

    tracks = []

    count = 1
    for result in o["results"]:
        if count > SONG_COUNT: 
            break
        # Filter tracks from the artist and collabs (e.g. artist = "artist, another_artist")
        if not artist in result["artistName"].title():
            continue
        tracks.append(result["trackName"])
        count += 1

    # Fallback
    if count < SONG_COUNT:
        return []
    
    return tracks


def print_dialogue(artist, has_results):
    is_vowel = artist[0].lower() in "aeiou"

    # Basic article checking; doesn't account for vowel sounding words
    article = "an" if is_vowel else "a"

    print(f"Gatekeeper: So you wear {article} {artist} shirt? Name five songs.")

    print("You:", end=" ")
    if has_results:
        print("OK.")
    else:
        print("You know what, I can't. You win.")


def main():
    artist = get_artist("Choose a band/artist: ").title()

    tracks = get_five_songs(artist)

    has_results = len(tracks) != 0

    print_dialogue(artist, has_results)

    # Displays every track
    for i, track in enumerate(tracks):
        print(f"{i+1}. {track}")



if __name__ == "__main__":
    main()
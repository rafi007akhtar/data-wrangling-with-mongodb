"""
To experiment with this code freely you will have to run this code locally.
Take a look at the main() function for an example of how to use the code. We
have provided example json output in the other code editor tabs for you to look
at, but you will not be able to run any queries through our UI.
"""
import json
import requests

BASE_URL = "http://musicbrainz.org/ws/2/"
ARTIST_URL = BASE_URL + "artist/"


# query parameters are given to the requests.get function as a dictionary; this
# variable contains some starter parameters.
query_type = {  "simple": {},
                "atr": {"inc": "aliases+tags+ratings"},
                "aliases": {"inc": "aliases"},
                "releases": {"inc": "releases"}}


def query_site(url, params, uid="", fmt="json"):
    """
    This is the main function for making queries to the musicbrainz API. The
    query should return a json document.
    """
    params["fmt"] = fmt
    r = requests.get(url + uid, params=params)
    print ("requesting", r.url)

    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        r.raise_for_status()


def query_by_name(url, params, name):
    """
    This adds an artist name to the query parameters before making an API call
    to the function above.
    """
    params["query"] = "artist:" + name
    return query_site(url, params)


def pretty_print(data, indent=4):
    """
    After we get our output, we can use this function to format it to be more
    readable.
    """
    if type(data) == dict:
        print (json.dumps(data, indent=indent, sort_keys=True))
    else:
        print (data)


def main():
    """
    Below is an example investigation to help you get started in your
    exploration. Modify the function calls and indexing below to answer the
    questions on the next quiz.

    HINT: Note how the output we get from the site is a multi-level JSON
    document, so try making print statements to step through the structure one
    level at a time or copy the output to a separate output file. Experimenting
    and iteration will be key to understand the structure of the data!
    """

    # Query for information in the database about bands named Nirvana
    results = query_by_name(ARTIST_URL, query_type["simple"], "Nirvana")
    pretty_print(results)

    # Isolate information from the 4th band returned (index 3)
    print("\nARTIST:")
    pretty_print(results["artists"][3])

    # Query for releases from that band using the artist_id
    artist_id = results["artists"][3]["id"]
    artist_data = query_site(ARTIST_URL, query_type["releases"], artist_id)
    releases = artist_data["releases"]

    # Print information about releases from the selected band
    print ("\nONE RELEASE:")
    pretty_print(releases[0], indent=2)

    release_titles = [r["title"] for r in releases]
    print ("\nALL TITLES:")
    for t in release_titles:
        print (t)

    print()

    # Getting Nirvana's aliases
    artist_aliases = query_by_name(ARTIST_URL, query_type["aliases"], "Nirvana")
    # went through the full list of aliases
    # coundn't find the Spanish alias, so skipping that

    # Getting Nirvana's disambiguation
    print('DISAMBIGUATIONS BY NIRVANA:')
    artists_nirvana = artist_aliases['artists']
    disambiguations_nirvama = [info['disambiguation'] for info in artists_nirvana if 'disambiguation' in info]
    print(disambiguations_nirvama)

    print()    

    # Getting Queen's begin-area name
    print('QUEEN BEGIN AREAS:')
    queen_search = query_by_name(ARTIST_URL, query_type["simple"], 'Queen')['artists']
    begin_areas_queen = [qs['begin-area']['name'] for qs in queen_search if 'begin-area' in qs]
    print(begin_areas_queen)

    print()

    # Getting One Directions's launch year
    print('ONE DIRECTION LIFE SPANS:')
    one_d = query_by_name(ARTIST_URL, query_type, "One Direction")['artists']
    life_spans_one_d = [od['life-span'] for od in one_d if 'life-span' in od]
    print(life_spans_one_d)

    print()

    # Getting First Aid Kit's band names (I think)
    print("FIRST AID KIT NAMES:")
    first_aid_kit: dict = query_by_name(ARTIST_URL, query_type["simple"], "First Aid Kit")
    names_fkit = [item['name'].lower() for item in first_aid_kit['artists'] if 'name' in item]
    print(set(names_fkit))

    print()

if __name__ == '__main__':
    main()
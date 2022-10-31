favorite_places = {
    'Polly': ['Brasil', 'Mexico'],
    'Sabrina': ['Japao', 'Suiça'],
    'Ju': ['França', 'brasil']
}

for name, places in favorite_places.items():
    print("\n" + name.title() + "'s favorite place are: ")
    for place in places:
        print("\t" + place.title())


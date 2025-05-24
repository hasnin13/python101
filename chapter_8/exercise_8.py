#exercise 8.1:
def display_message():
    print("In this chapter, I am learning about functions in Python.")

display_message()

#exercise 8.2:
def fav_book(bookname):
    print(f"one of my fav book is {bookname.title()}")

fav_book("alice in wonderland")

#exercise 8.3:
def make_shirt(size,mssg):
    print(f'making the shirt in size : {size} with the mssg: {mssg}')
make_shirt("small","blehhh")
make_shirt(size="large",mssg="blehh blehh")

#exercise 8.4:
def make_shirt(size='large',mssg='I love Python'):
    print(f"size:{size}, message:{mssg}")
make_shirt()
make_shirt(size='medium')
make_shirt(size="small",mssg="hehhh")

#exercise 8.5:
def describe_city(city='Reykjavik',country='Iceland'):
    print(f"{city} is in {country}")
describe_city()
describe_city(city="idk_any_name")
describe_city(city='Seoul',country='S.Korea')


#exercise 8.6:
def city_country(city, country):
    return f"{city}, {country}"

location1 = city_country("Dhaka", "Bangladesh")
location2 = city_country("Oslo", "Norway")
location3 = city_country("Tokyo", "Japan")

print(location1)
print(location2)
print(location3)

#exercise 8.7:
def make_album(artist, title, num_songs=None):
    album = {
        "artist": artist,
        "title": title
    }
    if num_songs is not None:
        album["num_songs"] = num_songs
    return album

album1 = make_album("BTS", "Love Yourself")
album2 = make_album("Adele", "25")
album3 = make_album("Suga", "D-Day", num_songs=4)

print(album1)
print(album2)
print(album3)

#exercise 8.8:
def make_album(artist, title, num_songs=None):
    album = {
        "artist": artist,
        "title": title
    }
    if num_songs is not None:
        album["num_songs"] = num_songs
    return album

print("Enter album information. Type 'quit' at any time to stop.")

while True:
    artist = input("Enter the artist's name: ")
    if artist.lower() == 'quit':
        break

    title = input("Enter the album title: ")
    if title.lower() == 'quit':
        break

    num_songs_input = input("Enter number of songs (or press Enter to skip): ")
    if num_songs_input.lower() == 'quit':
        break

    if num_songs_input:
        album = make_album(artist, title, int(num_songs_input))
    else:
        album = make_album(artist, title)

    print(f"Album created: {album}\n")


#exercise 8.9:
def show_messages(messgs):
    for message in messgs:
        print(message)

text_messages = [
    "Hey,Hannah",
    "hahahehe",
    "unga bunga",
]
show_messages(text_messages)


#exercise 8.10:
def show_messages(messages):
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop(0)
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)
text_messages = [
    "Hey,Hannah",
    "hahahehe",
    "unga bunga",
]
sent_messages = []
send_messages(text_messages, sent_messages)
print("\nOriginal messages list (should be empty):", text_messages)
print("Sent messages list:", sent_messages)

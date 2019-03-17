import urllib.request
import urllib.parse


def read_text():
    quotes = open(
        "/Users/yerlanshaikh/Desktop/udacity_python/prog_fund/profanity_editor/movie_quotes.txt")
    contents_of_file = quotes.read()
    # print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)


def check_profanity(text_to_check):
    encoded_text = urllib.parse.quote(text_to_check, 'utf-8')
    address = "http://www.wdylike.appspot.com/?q="+encoded_text
    # print(address)
    connection = urllib.request.urlopen(address)
    output = connection.read()
    print(output)
    connection.close()
    if b"true" in output:
        print("Profanity Alert!")
    elif b"false" in output:
        print("No curse words")
    else:
        print("Could not scan the document properly")


read_text()

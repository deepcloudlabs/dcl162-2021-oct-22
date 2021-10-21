import xml.sax

from world.domain import Country


class MovieHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.genre_histogram = {}
        self.opening_tag = ""

    def startElement(self, tag, attributes):
        self.opening_tag = tag

    def characters(self, content):
        if self.opening_tag == "genre":
            genre = content.lower()
            self.genre_histogram[genre] = 1 if genre not in self.genre_histogram else self.genre_histogram[genre] + 1

    def endElement(self, tag):
        self.opening_tag = ""


if __name__ == '__main__':
    parser = xml.sax.make_parser()
    handler = MovieHandler()
    parser.setContentHandler(handler)
    # parsing+processing
    parser.parse("resources/movies.xml")
    print(handler.genre_histogram)

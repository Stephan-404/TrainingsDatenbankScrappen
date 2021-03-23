import scrapy


class QuotesSpider(scrapy.Spider):
    name = "test"
    start_urls = [
        'https://www.meinefitness.net/pull-over/',
        'https://www.meinefitness.net/negativ-bankdruecken/',
        'https://www.meinefitness.net/bankdruecken/'
    ]

    def parse(self, response):
        titel=str(response.css('h1.entry-title::text').get()).replace("ö","oe").replace("Ö","Oe").replace("ä","ae").replace("Ä","Ae").replace("ü","ue").replace("Ü","ue")
        details=response.css('div.uebungsbox p::text').getall()
        muskelgruppen=""
        for muskel in response.css('div.uebungsbox li::text').getall():
            muskelgruppen=muskelgruppen+muskel+","

        muskelBild=response.css('div.muskelgruppe img::attr(src)').get()

        ablauf=""
        counter=1
        for strong in response.css('table.evergreen-uebung li::text').getall():
            ablauf="Schritt"+str(counter)+": "+ablauf+str(strong)+";\n"
            counter=counter+1

        yield{
            'Titel':titel,
            'Equipment':details[0].replace("ö","oe").replace("Ö","Oe").replace("ä","ae").replace("Ä","Ae").replace("ü","ue").replace("Ü","ue").replace("ß","ss"),
            'Schwierigkeit':details[1].replace("ö","oe").replace("Ö","Oe").replace("ä","ae").replace("Ä","Ae").replace("ü","ue").replace("Ü","ue").replace("ß","ss"),
            'AndereNamen':details[2].replace("ö","oe").replace("Ö","Oe").replace("ä","ae").replace("Ä","Ae").replace("ü","ue").replace("Ü","ue").replace("ß","ss"),
            'Muskeln':muskelgruppen.replace("ö","oe").replace("Ö","Oe").replace("ä","ae").replace("Ä","Ae").replace("ü","ue").replace("Ü","ue").replace("ß","ss"),
            'Bild':muskelBild,
            'Ablauf=': ablauf.replace("ö","oe").replace("Ö","Oe").replace("ä","ae").replace("Ä","Ae").replace("ü","ue").replace("Ü","ue").replace("ß","ss").replace("</li>","").replace("<li>","")
        }








import scrapy


class QuotesSpider(scrapy.Spider):
    name = "workout"
    start_urls = [
        'https://www.meinefitness.net/rueckentraining/oberer-ruecken/',
        'https://www.meinefitness.net/rueckentraining/unterer-ruecken/',
        'https://www.meinefitness.net/schultertraining/vordere-schulter/',
        'https://www.meinefitness.net/schultertraining/seitliche-schulter/',
        'https://www.meinefitness.net/schultertraining/hintere-schulter/',
        'https://www.meinefitness.net/brustmuskeltraining/obere-brust/',
        'https://www.meinefitness.net/brustmuskeltraining/mittlere-brust/',
        'https://www.meinefitness.net/brustmuskeltraining/untere-brust/',
        'https://www.meinefitness.net/armtraining/bizeps/',
        'https://www.meinefitness.net/armtraining/trizeps/',
        'https://www.meinefitness.net/armtraining/unterarme/',
        'https://www.meinefitness.net/bauchmuskeltraining/obere-bauchmuskeln/',
        'https://www.meinefitness.net/bauchmuskeltraining/untere-bauchmuskeln/',
        'https://www.meinefitness.net/bauchmuskeltraining/seitliche-bauchmuskeln/',
        'https://www.meinefitness.net/po-training/',
        'https://www.meinefitness.net/po-training/abduktoren/',
        'https://www.meinefitness.net/beintraining/oberschenkel/beinbizeps/',
        'https://www.meinefitness.net/beintraining/oberschenkel/beinstrecker/',
        'https://www.meinefitness.net/beintraining/oberschenkel/adduktoren/',
        'https://www.meinefitness.net/beintraining/Waden/'
    ]

    def parse(self, response):
        for quote in response.css('article.herald-lay-b'):
            yield {
                'Titel': str(quote.css('h2.entry-title a::text').get()).replace("ö","oe").replace("Ö","Oe").replace("ä","ae").replace("Ä","Ae").replace("ü","ue").replace("Ü","ue"),
                'Bild': str(quote.css('div.herald-post-thumbnail a::attr(href)').get()),
                'Equipment': str(quote.css('div.entry-content p::text').get()).replace("Benötigtes Equipment: ","").replace("ö","oe").replace("Ö","Oe").replace("ä","ae").replace("Ä","Ae").replace("ü","ue").replace("Ü","ue"),
                'Schwierigkeit': str(quote.css('div.entry-content p::text').getall()[1]).replace(" Schwierigkeitsgrad: ","").replace("ö","oe").replace("Ö","Oe").replace("ä","ae").replace("Ä","Ae").replace("ü","ue").replace("Ü","ue"),
                'WeiterführendeLink': str(quote.css('a.herald-read-more::attr(href)').get()),
            }
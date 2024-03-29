import scrapy
import os


urls = [
    "https://katalog.trojmiasto.pl/gastronomia_i_jedzenie/fast_food/",
    "https://katalog.trojmiasto.pl/gastronomia_i_jedzenie/bary/",
    "https://katalog.trojmiasto.pl/gastronomia_i_jedzenie/bary_mleczne/",
    "https://katalog.trojmiasto.pl/gastronomia_i_jedzenie/bary_przekaskowe/",
    "https://katalog.trojmiasto.pl/gastronomia_i_jedzenie/bistro/",
    "https://katalog.trojmiasto.pl/gastronomia_i_jedzenie/browary/",
    "https://katalog.trojmiasto.pl/gastronomia_i_jedzenie/burgery/",
    "https://katalog.trojmiasto.pl/gastronomia_i_jedzenie/drink_bary/",
    "https://katalog.trojmiasto.pl/gastronomia_i_jedzenie/food_hall/",
    "https://katalog.trojmiasto.pl/gastronomia_i_jedzenie/food_truck/",
    "https://katalog.trojmiasto.pl/gastronomia_i_jedzenie/jedzenie_na_wynos/",
    "https://katalog.trojmiasto.pl/gastronomia_i_jedzenie/lodziarnie/",
    "https://katalog.trojmiasto.pl/gastronomia_i_jedzenie/kawiarnie_i_herbaciarnie/",
    "https://katalog.trojmiasto.pl/gastronomia_i_jedzenie/kebaby/",
    "https://katalog.trojmiasto.pl/gastronomia_i_jedzenie/nalesnikarnie/",
    "https://katalog.trojmiasto.pl/gastronomia_i_jedzenie/pierogarnie/",
    "https://katalog.trojmiasto.pl/gastronomia_i_jedzenie/palarnie_kawy/",
    "https://katalog.trojmiasto.pl/gastronomia_i_jedzenie/pierogarnie/",
    "https://katalog.trojmiasto.pl/gastronomia_i_jedzenie/pizzerie/",
    "https://katalog.trojmiasto.pl/gastronomia_i_jedzenie/puby/",
    "https://katalog.trojmiasto.pl/gastronomia_i_jedzenie/restauracje/",
    "https://katalog.trojmiasto.pl/gastronomia_i_jedzenie/smazalnia_ryb/",
    "https://katalog.trojmiasto.pl/gastronomia_i_jedzenie/sushi/",
    "https://katalog.trojmiasto.pl/gastronomia_i_jedzenie/winiarnie/",
    "https://katalog.trojmiasto.pl/gastronomia_i_jedzenie/restauracje_za_miastem/",
    "https://katalog.trojmiasto.pl/rozrywka/kina/",
    "https://katalog.trojmiasto.pl/rozrywka/kluby_dyskoteki/",
    "https://katalog.trojmiasto.pl/rozrywka/kluby_nocne/",
    "https://katalog.trojmiasto.pl/rozrywka/kluby_studenckie/",
    "https://katalog.trojmiasto.pl/rozrywka/obiekty_koncertowe/",
    "https://katalog.trojmiasto.pl/rozrywka/place_zabaw_i_malpie_gaje/",
    "https://katalog.trojmiasto.pl/handel/centra_handlowe/",
    "https://katalog.trojmiasto.pl/handel/cukiernie_i_piekarnie/",
    "https://katalog.trojmiasto.pl/handel/dewocjonalia/",
    "https://katalog.trojmiasto.pl/handel/hipermarkety/",
    "https://katalog.trojmiasto.pl/handel/ksiegarnie/",
    "https://katalog.trojmiasto.pl/handel/punkty_odbioru_przesylek/",
    "https://katalog.trojmiasto.pl/handel/sklepy_zoologiczne/",
    "https://katalog.trojmiasto.pl/handel/sklepy_miesne/",
    "https://katalog.trojmiasto.pl/handel/sklepy_rybne/",
    "https://katalog.trojmiasto.pl/handel/sklepy_z_winami/",
    "https://katalog.trojmiasto.pl/handel/supermarkety/",
    "https://katalog.trojmiasto.pl/handel/targowiska/",
    "https://katalog.trojmiasto.pl/handel/zdrowa_zywnosc/",
    "https://katalog.trojmiasto.pl/uslugi/bookcrossing/",
    "https://katalog.trojmiasto.pl/hobby_i_czas_wolny/kursy_tanca/",
    "https://katalog.trojmiasto.pl/hobby_i_czas_wolny/pole_dance/",
    "https://katalog.trojmiasto.pl/hobby_i_czas_wolny/modelarstwo/",
    "https://katalog.trojmiasto.pl/zdrowie_i_medycyna/medytacje/",
    "https://katalog.trojmiasto.pl/zdrowie_i_medycyna/pediatrzy/",
    "https://katalog.trojmiasto.pl/zdrowie_i_medycyna/prywatne_kliniki_i_spoldzielnie/",
    "https://katalog.trojmiasto.pl/urzedy_i_instytucje/narodowy_fundusz_zdrowia/",
    "https://katalog.trojmiasto.pl/nauka_i_szkolnictwo/zlobki/",
    "https://katalog.trojmiasto.pl/sport_i_rekreacja/aquafitness/",
    "https://katalog.trojmiasto.pl/sport_i_rekreacja/aquapark/",
    "https://katalog.trojmiasto.pl/sport_i_rekreacja/baseny/",
    "https://katalog.trojmiasto.pl/sport_i_rekreacja/kluby_bilardowe/",
    "https://katalog.trojmiasto.pl/sport_i_rekreacja/golf/",
    "https://katalog.trojmiasto.pl/sport_i_rekreacja/jazda_konna/",
    "https://katalog.trojmiasto.pl/sport_i_rekreacja/joga/",
    "https://katalog.trojmiasto.pl/sport_i_rekreacja/kajaki/",
    "https://katalog.trojmiasto.pl/sport_i_rekreacja/kluby_sportowe/",
    "https://katalog.trojmiasto.pl/sport_i_rekreacja/korty_badminton/",
    "https://katalog.trojmiasto.pl/sport_i_rekreacja/korty_tenisowe/",
    "https://katalog.trojmiasto.pl/sport_i_rekreacja/kregielnie/",
    "https://katalog.trojmiasto.pl/sport_i_rekreacja/kulig/",
    "https://katalog.trojmiasto.pl/sport_i_rekreacja/lodowiska/",
    "https://katalog.trojmiasto.pl/sport_i_rekreacja/nauka_plywania/",
    "https://katalog.trojmiasto.pl/sport_i_rekreacja/nauka_tenisa/",
    "https://katalog.trojmiasto.pl/sport_i_rekreacja/nordic_walking/",
    "https://katalog.trojmiasto.pl/sport_i_rekreacja/nurkowanie/",
    "https://katalog.trojmiasto.pl/sport_i_rekreacja/orliki/",
    "https://katalog.trojmiasto.pl/sport_i_rekreacja/paintball/",
    "https://katalog.trojmiasto.pl/sport_i_rekreacja/sztuki_walki_i_samoobrona/",
    "https://katalog.trojmiasto.pl/sport_i_rekreacja/sauny/",
    "https://katalog.trojmiasto.pl/sport_i_rekreacja/silownie_i_fitness_kluby/",
    "https://katalog.trojmiasto.pl/sport_i_rekreacja/silownie_pod_chmurka/",
    "https://katalog.trojmiasto.pl/sport_i_rekreacja/skateparki/",
    "https://katalog.trojmiasto.pl/sport_i_rekreacja/sklepy_i_serwisy_rowerowe/",
    "https://katalog.trojmiasto.pl/sport_i_rekreacja/sklepy_turystyczne_i_sportowe/",
    "https://katalog.trojmiasto.pl/sport_i_rekreacja/squash/",
    "https://katalog.trojmiasto.pl/sport_i_rekreacja/stowarzyszenia_i_organizacje_sportowe/",
    "https://katalog.trojmiasto.pl/sport_i_rekreacja/strzelnice/",
    "https://katalog.trojmiasto.pl/sport_i_rekreacja/studio_pilates/",
    "https://katalog.trojmiasto.pl/sport_i_rekreacja/szkolki_pilkarskie/",
    "https://katalog.trojmiasto.pl/sport_i_rekreacja/trener_personalny/",
    "https://katalog.trojmiasto.pl/sport_i_rekreacja/wspinaczka/",
    "https://katalog.trojmiasto.pl/nauka_i_szkolnictwo/biblioteki/",
    "https://katalog.trojmiasto.pl/nauka_i_szkolnictwo/centra_edukacyjne_dla_dzieci/",
    "https://katalog.trojmiasto.pl/nauka_i_szkolnictwo/stowarzyszenia_i_kola_naukowe/",
    "https://katalog.trojmiasto.pl/nauka_i_szkolnictwo/kursy_edukacyjne_dla_rodzicow_i_wychowawcow/",
    "https://katalog.trojmiasto.pl/nauka_i_szkolnictwo/przedszkola/",
    "https://katalog.trojmiasto.pl/nauka_i_szkolnictwo/szkoly_podstawowe/",
    "https://katalog.trojmiasto.pl/nauka_i_szkolnictwo/szkolnictwo_policealne_i_pomaturalne/",
    "https://katalog.trojmiasto.pl/nauka_i_szkolnictwo/szkolnictwo_prywatne_i_spoleczne/",
    "https://katalog.trojmiasto.pl/nauka_i_szkolnictwo/szkoly_wizazu_i_stylizacji/",
    "https://katalog.trojmiasto.pl/nauka_i_szkolnictwo/szkoly_srednie/",
    "https://katalog.trojmiasto.pl/nauka_i_szkolnictwo/szkoly_wyzsze/",
    "https://katalog.trojmiasto.pl/nauka_i_szkolnictwo/technika/",
    "https://katalog.trojmiasto.pl/nauka_i_szkolnictwo/uniwersytety_trzeciego_wieku/",
    "https://katalog.trojmiasto.pl/nauka_i_szkolnictwo/zlobki/",
    "https://katalog.trojmiasto.pl/hobby_i_czas_wolny/kursy_tanca/",
    "https://katalog.trojmiasto.pl/moda_i_uroda/barber_shop/",
    "https://katalog.trojmiasto.pl/moda_i_uroda/depilacja_laserowa/",
    "https://katalog.trojmiasto.pl/moda_i_uroda/depilacja_pasta_cukrowa/",
    "https://katalog.trojmiasto.pl/moda_i_uroda/depilacja_woskiem/",
    "https://katalog.trojmiasto.pl/moda_i_uroda/drogerie/",
    "https://katalog.trojmiasto.pl/moda_i_uroda/fryzjerzy/",
    "https://katalog.trojmiasto.pl/moda_i_uroda/masazysci/",
    "https://katalog.trojmiasto.pl/moda_i_uroda/solaria/",
    "https://katalog.trojmiasto.pl/moda_i_uroda/spa/",
    "https://katalog.trojmiasto.pl/sport_i_rekreacja/silownie_i_fitness_kluby/",
    "https://katalog.trojmiasto.pl/zdrowie_i_medycyna/apteki/",
    "https://katalog.trojmiasto.pl/zdrowie_i_medycyna/apteki_calodobowe/",
    "https://katalog.trojmiasto.pl/finanse_i_ubezpieczenia/banki/",
    "https://katalog.trojmiasto.pl/finanse_i_ubezpieczenia/bankomaty/",
    "https://katalog.trojmiasto.pl/uslugi/wybiegi_dla_psow/",
    "https://katalog.trojmiasto.pl/uslugi/zwierzeta/hotele_dla_zwierzat/",
    "https://katalog.trojmiasto.pl/uslugi/zwierzeta/pielegnacja_zwierzat/",
    "https://katalog.trojmiasto.pl/uslugi/zwierzeta/weterynarze/",
    "https://katalog.trojmiasto.pl/uslugi/szewc/",
    "https://katalog.trojmiasto.pl/uslugi/pralnie/",
    "https://katalog.trojmiasto.pl/uslugi/drukarnie_poligrafia_dtp/",
    "https://katalog.trojmiasto.pl/uslugi/drukarnie_3d/",
    "https://katalog.trojmiasto.pl/uslugi/kaletnik/",
    "https://katalog.trojmiasto.pl/uslugi/pracownie_krawieckie/",
    "https://katalog.trojmiasto.pl/uslugi/punkty_ksero/",
    "https://katalog.trojmiasto.pl/uslugi/magiel_farbiarnie/",
    "https://katalog.trojmiasto.pl/uslugi/opieka_nad_dziecmi/",
]


class TrojmiastoSpider(scrapy.Spider):
    name = "trojmiasto",
    start_urls = urls

    custom_settings = {
        'LOG_LEVEL': 'ERROR'
    }

    def parse(self, response):
        for poi in response.css("div.basicInfo__item.basicInfo__item--presentationNotPaid"):
            address_info = poi.css("a.objectAddress__link span::text").getall()
            address = {}
            try:
                address["postcode"] = poi.css('.objectAddress__postCode::text').get().strip()
            except AttributeError:
                address["postcode"] = ''
            try:
                address["city"] = poi.css('.objectAddress__city::text').get().strip()
                address["street"] = poi.css('.objectAddress__street::text').get().strip()
            except AttributeError as e:
                address = {}
                self.logger.error(f"Exception: {e}, Address Info: {address_info}, Reason: {str(e)}")

            res = {
                "name": poi.css("h2 a.objectName__link span::text").get(),
                "categories": poi.css("a.objectTags__item::text").getall(),
                "address": address,
                'url': response.url
            }
            yield res
        next_page = response.css('a[title="następna"]::attr("href")').get()

        if next_page:
            yield response.follow(next_page, self.parse)

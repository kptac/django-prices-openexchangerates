# coding: utf-8
from django.utils.translation import gettext_lazy as _

# List of currencies supported by OpenExchange
# http://openexchangerates.org/currencies.json


CURRENCIES = [
    ('AED', _('United Arab Emirates Dirham')),
    ('AFN', _('Afghan Afghani')),
    ('ALL', _('Albanian Lek')),
    ('AMD', _('Armenian Dram')),
    ('ANG', _('Netherlands Antillean Guilder')),
    ('AOA', _('Angolan Kwanza')),
    ('ARS', _('Argentine Peso')),
    ('AUD', _('Australian Dollar')),
    ('AWG', _('Aruban Florin')),
    ('AZN', _('Azerbaijani Manat')),
    ('BAM', _('Bosnia-Herzegovina Convertible Mark')),
    ('BBD', _('Barbadian Dollar')),
    ('BDT', _('Bangladeshi Taka')),
    ('BGN', _('Bulgarian Lev')),
    ('BHD', _('Bahraini Dinar')),
    ('BIF', _('Burundian Franc')),
    ('BMD', _('Bermudan Dollar')),
    ('BND', _('Brunei Dollar')),
    ('BOB', _('Bolivian Boliviano')),
    ('BRL', _('Brazilian Real')),
    ('BSD', _('Bahamian Dollar')),
    ('BTC', _('Bitcoin')),
    ('BTN', _('Bhutanese Ngultrum')),
    ('BWP', _('Botswanan Pula')),
    ('BYN', _('Belarusian Ruble')),
    ('BZD', _('Belize Dollar')),
    ('CAD', _('Canadian Dollar')),
    ('CDF', _('Congolese Franc')),
    ('CHF', _('Swiss Franc')),
    ('CLF', _('Chilean Unit of Account (UF)')),
    ('CLP', _('Chilean Peso')),
    ('CNH', _('Chinese Yuan (Offshore)')),
    ('CNY', _('Chinese Yuan')),
    ('COP', _('Colombian Peso')),
    ('CRC', _('Costa Rican Colón')),
    ('CUC', _('Cuban Convertible Peso')),
    ('CUP', _('Cuban Peso')),
    ('CVE', _('Cape Verdean Escudo')),
    ('CZK', _('Czech Republic Koruna')),
    ('DJF', _('Djiboutian Franc')),
    ('DKK', _('Danish Krone')),
    ('DOP', _('Dominican Peso')),
    ('DZD', _('Algerian Dinar')),
    ('EGP', _('Egyptian Pound')),
    ('ERN', _('Eritrean Nakfa')),
    ('ETB', _('Ethiopian Birr')),
    ('EUR', _('Euro')),
    ('FJD', _('Fijian Dollar')),
    ('FKP', _('Falkland Islands Pound')),
    ('GBP', _('British Pound Sterling')),
    ('GEL', _('Georgian Lari')),
    ('GGP', _('Guernsey Pound')),
    ('GHS', _('Ghanaian Cedi')),
    ('GIP', _('Gibraltar Pound')),
    ('GMD', _('Gambian Dalasi')),
    ('GNF', _('Guinean Franc')),
    ('GTQ', _('Guatemalan Quetzal')),
    ('GYD', _('Guyanaese Dollar')),
    ('HKD', _('Hong Kong Dollar')),
    ('HNL', _('Honduran Lempira')),
    ('HRK', _('Croatian Kuna')),
    ('HTG', _('Haitian Gourde')),
    ('HUF', _('Hungarian Forint')),
    ('IDR', _('Indonesian Rupiah')),
    ('ILS', _('Israeli New Sheqel')),
    ('IMP', _('Manx pound')),
    ('INR', _('Indian Rupee')),
    ('IQD', _('Iraqi Dinar')),
    ('IRR', _('Iranian Rial')),
    ('ISK', _('Icelandic Króna')),
    ('JEP', _('Jersey Pound')),
    ('JMD', _('Jamaican Dollar')),
    ('JOD', _('Jordanian Dinar')),
    ('JPY', _('Japanese Yen')),
    ('KES', _('Kenyan Shilling')),
    ('KGS', _('Kyrgystani Som')),
    ('KHR', _('Cambodian Riel')),
    ('KMF', _('Comorian Franc')),
    ('KPW', _('North Korean Won')),
    ('KRW', _('South Korean Won')),
    ('KWD', _('Kuwaiti Dinar')),
    ('KYD', _('Cayman Islands Dollar')),
    ('KZT', _('Kazakhstani Tenge')),
    ('LAK', _('Laotian Kip')),
    ('LBP', _('Lebanese Pound')),
    ('LKR', _('Sri Lankan Rupee')),
    ('LRD', _('Liberian Dollar')),
    ('LSL', _('Lesotho Loti')),
    ('LYD', _('Libyan Dinar')),
    ('MAD', _('Moroccan Dirham')),
    ('MDL', _('Moldovan Leu')),
    ('MGA', _('Malagasy Ariary')),
    ('MKD', _('Macedonian Denar')),
    ('MMK', _('Myanma Kyat')),
    ('MNT', _('Mongolian Tugrik')),
    ('MOP', _('Macanese Pataca')),
    ('MRO', _('Mauritanian Ouguiya (pre-2018)')),
    ('MRU', _('Mauritanian Ouguiya')),
    ('MUR', _('Mauritian Rupee')),
    ('MVR', _('Maldivian Rufiyaa')),
    ('MWK', _('Malawian Kwacha')),
    ('MXN', _('Mexican Peso')),
    ('MYR', _('Malaysian Ringgit')),
    ('MZN', _('Mozambican Metical')),
    ('NAD', _('Namibian Dollar')),
    ('NGN', _('Nigerian Naira')),
    ('NIO', _('Nicaraguan Córdoba')),
    ('NOK', _('Norwegian Krone')),
    ('NPR', _('Nepalese Rupee')),
    ('NZD', _('New Zealand Dollar')),
    ('OMR', _('Omani Rial')),
    ('PAB', _('Panamanian Balboa')),
    ('PEN', _('Peruvian Nuevo Sol')),
    ('PGK', _('Papua New Guinean Kina')),
    ('PHP', _('Philippine Peso')),
    ('PKR', _('Pakistani Rupee')),
    ('PLN', _('Polish Zloty')),
    ('PYG', _('Paraguayan Guarani')),
    ('QAR', _('Qatari Rial')),
    ('RON', _('Romanian Leu')),
    ('RSD', _('Serbian Dinar')),
    ('RUB', _('Russian Ruble')),
    ('RWF', _('Rwandan Franc')),
    ('SAR', _('Saudi Riyal')),
    ('SBD', _('Solomon Islands Dollar')),
    ('SCR', _('Seychellois Rupee')),
    ('SDG', _('Sudanese Pound')),
    ('SEK', _('Swedish Krona')),
    ('SGD', _('Singapore Dollar')),
    ('SHP', _('Saint Helena Pound')),
    ('SLL', _('Sierra Leonean Leone')),
    ('SOS', _('Somali Shilling')),
    ('SRD', _('Surinamese Dollar')),
    ('SSP', _('South Sudanese Pound')),
    ('STD', _('São Tomé and Príncipe Dobra (pre-2018)')),
    ('STN', _('São Tomé and Príncipe Dobra')),
    ('SVC', _('Salvadoran Colón')),
    ('SYP', _('Syrian Pound')),
    ('SZL', _('Swazi Lilangeni')),
    ('THB', _('Thai Baht')),
    ('TJS', _('Tajikistani Somoni')),
    ('TMT', _('Turkmenistani Manat')),
    ('TND', _('Tunisian Dinar')),
    ('TOP', _('Tongan Pa\'anga')),
    ('TRY', _('Turkish Lira')),
    ('TTD', _('Trinidad and Tobago Dollar')),
    ('TWD', _('New Taiwan Dollar')),
    ('TZS', _('Tanzanian Shilling')),
    ('UAH', _('Ukrainian Hryvnia')),
    ('UGX', _('Ugandan Shilling')),
    ('USD', _('United States Dollar')),
    ('UYU', _('Uruguayan Peso')),
    ('UZS', _('Uzbekistan Som')),
    ('VEF', _('Venezuelan Bolívar Fuerte (Old)')),
    ('VES', _('Venezuelan Bolívar Soberano')),
    ('VND', _('Vietnamese Dong')),
    ('VUV', _('Vanuatu Vatu')),
    ('WST', _('Samoan Tala')),
    ('XAF', _('CFA Franc BEAC')),
    ('XAG', _('Silver Ounce')),
    ('XAU', _('Gold Ounce')),
    ('XCD', _('East Caribbean Dollar')),
    ('XDR', _('Special Drawing Rights')),
    ('XOF', _('CFA Franc BCEAO')),
    ('XPD', _('Palladium Ounce')),
    ('XPF', _('CFP Franc')),
    ('XPT', _('Platinum Ounce')),
    ('YER', _('Yemeni Rial')),
    ('ZAR', _('South African Rand')),
    ('ZMW', _('Zambian Kwacha')),
    ('ZWL', _('Zimbabwean Dollar'))
]

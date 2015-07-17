#!/usr/bin/python
# -*- coding: utf-8 -*-



terder_email = ['minoborony.com',
		'bvostok.com',
		'syriaunion.com',
		'kiev-news.com',
		'grant-jt.com',
		'veshdoki.com',
		'syriainform.com',
		'i-am-ass.com',
		'material-evidence.com',
		'goodbyeusa.com',
		'putininfo.com',
		'euhistory.net',
		'euhisory.net',
		'historywar.org',
		'new-travel.info']

checked = [
'UA-65088212',
'UA-65108871',
'UA-53159797',
'UA-61760291',
'UA-53176102',
'UA-65085532',
'UA-65083743',
'UA-65082064',
'UA-65083063',
'UA-65083161',
'UA-65085044',
'UA-45821488',
'UA-65083654',
'UA-53175219',
'UA-65082468',
'UA-47768234',
'UA-53585314',
'UA-44865638',
'UA-41128422',
'UA-55552418', # !!!!!!!! Более 10000 сайтов, преимущественно .ru
]


#**bireconomy.ru >>
#2015.06.30	104.28.18.29 >>	Analytics: UA-53585314

#**trasi.com >>
#2015.07.16	104.28.0.73 >>	Analytics: UA-45089542 53585314

sameid_links = {'news-region.ru': {'ga': ['UA-47768234', 'UA-53159797', 'UA-53176102', 'UA-53585314']},
			 'kiev-news.com': {'ga': ['UA-53159797']},
			 'kievsmi.net': {'ga': ['UA-53159797'], 'ads': ['pub-1034041724441909']},
			 'apmahachkala.ru': {'ga': ['UA-53159797']},
			 '1bitrix.ru': {'ga': ['UA-53159797']},
			 'worldsochi.com': {'ga': ['UA-47768234', 'UA-53159797']},
			 'grant-jt.com': {'ga': ['UA-53159797']},
			 'kavkazprom.ru': {'ga': ['UA-53159797']},
			 'nahnews.com.ua': {'ga': ['UA-53159797']},
			 'fapnews.ru': {'ga': ['UA-53159797']},
			 'jpgazeta.ru': {'ga': ['UA-53159797', 'UA-41128422']},
			 'putininfo.com': {'ga': ['UA-53159797']},
			 'politictop.com': {'ga': ['UA-53159797']},
			 'riafan.ru': {'ga': ['UA-53159797']},
			 'nahnews.org': {'ga': ['UA-53159797', 'UA-61760291']},
			 'nevnov.ru': {'ga': ['UA-53159797', 'UA-44865638']},
			 'slova-dela.ru': {'ga': ['UA-53159797']},
			 'worldukraine.com.ua': {'ga': ['UA-53176102']},
			 'material-evidence.com': {'ga': ['UA-53176102', 'UA-53175219']},
			 'yapatriot.ru': {'ga': ['UA-53176102 ']},
			 'zanogu.com': {'ga': ['UA-53176102 ']},
			 'whoswho.com.ua': {'ga': ['UA-53176102 ']},
			 'adamants.ru': {'ga': ['UA-53176102 ']},
			 'emaidan.com.ua': {'ga': ['UA-65083743', 'UA-53159797']},
			 'bvostok.com': {'ga': ['UA-65083161']},
			 'otpusk.travel': {'ga': ['UA-45821488']},
			 'ultramir.net': {'ga': ['UA-53175219'], 'ads': ['pub-4362632766044795']},
			 'infosurfing.ru': {'ga': ['UA-53159797']},
			 'nation-news.ru': {'ga': ['UA-47768234', 'UA-53585314']},
			 'rueconomy.ru': {'ga': ['UA-53585314'], 'ads': ['pub-7402614738147167']},
			 'rueconomics.ru': {'ga': ['UA-53585314']},
			 'aviapress.net': {'ga': ['UA-55552418', 'UA-53585314']},
			 #'': {'ga': ['']},
			 #'': {'ga': ['']},
			 #'': {'ga': ['']},
			 #'': {'ga': ['']},
			 #'': {'ga': ['']},
			 #'': {'ga': ['']},
			 #'': {'ga': ['']},
			 }


def add_manual_data(data):
	for url, info in data.items():
		if url in terder_email:
			info['email'] = 'terder.n@gmail.com'
		if url in sameid_links:
			if 'ga' in info and 'ga' in sameid_links[url]:
				info['ga'] += sameid_links[url]['ga']

	for url, info in sameid_links.items():
		if url not in data:
			data[url] = info

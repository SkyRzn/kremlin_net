#!/usr/bin/python
# -*- coding: utf-8 -*-


import requests, re, json
from subprocess import Popen, PIPE
import manual_data


loaded_urls = ['minoborony.com',
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
		'new-travel.info',
		'вштабе.рф',
		'yapatriot.ru',
		'whoswho.com.ua',
		'adamants.ru',
		'zanogu.com',
		'worldukraine.com.ua',
		'syriainform.com',
		'news-region.ru',
		'worldsochi.com',
		'nation-news.ru',
		'rueconomics.ru',
		'rueconomy.ru',
		'nahnews.com.ua',
		'politictop.com',
		'kavkazprom.ru',
		'riafan.ru',
		'nahnews.org',
		'1bitrix.ru',
		'nevnov.ru',
		'slova-dela.ru',
		'apmahachkala.ru',
		'emaidan.com.ua',
		'kievsmi.net',
		'fapnews.ru',
		'jpgazeta.ru']


def whois(domain):
	res = {}

	lines = Popen('whois %s' % domain, shell=True, stdin=PIPE, stdout=PIPE).stdout.read()

	if lines:
		res['whois_txt'] = lines
		lines = lines.split('\n')
		whdata = []
		for line in lines:
			try:
				i = line.index(':')
			except:
				whdata.append([line, ''])
				continue
			k = line[:i].strip()
			v = line[i+1:].strip()
			whdata.append([k, v])
		res['whois'] = whdata

	return res

def get_info(urls):
	f = open('data.json', 'r')
	j = f.read()
	f.close()

	if j:
		res = json.loads(j)
	else:
		res = {}

	for url in urls:
		print url
		res[url] = whois(url)
		try:
			r = requests.get('http://%s' % url)
		except:
			res[url]['err'] = 1
			print '\t', 'error 1'
			continue
		if r:
			uas = re.findall('(UA-[0-9\-]+)', r.text)
			res[url]['ga'] = uas
			print '\t', uas

			uas = re.findall('(yaCounter[0-9]+)', r.text)
			uas = [v[9:] for v in uas]
			res[url]['ym'] = uas
			print '\t', uas
		else:
			res[url]['err'] = 2
			print '\t', 'error 2'

	j = json.dumps(res)

	f = open('data.json', 'w')
	f.write(j)
	f.close()

urls = ['sochiworld.com']
#for url in manual_data.sameid_links.keys():
	#if url not in loaded_urls:
		#urls.append(url)

get_info(urls)


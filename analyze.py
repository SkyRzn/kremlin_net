#!/usr/bin/python
# -*- coding: utf-8 -*-


import json
import manual_data


def analyze():
	f = open('data.json', 'r')
	j = f.read()
	f.close()

	if not j:
		print 'read file error'
		return

	data = json.loads(j)
	manual_data.add_manual_data(data)

	for k, v in data.items():
		if 'ga' in v:
			ga = v['ga']
			for ua in ga:
				ua = ua[:11]
				if ua not in manual_data.checked:
					print ua


	ga = {}
	ym = {}
	res = {}
	for k, v in data.items():
		if 'whois' in v:
			for kk, vv in v['whois']:
				if ('privacyprotect.org' not in vv) and \
					('abuse@reg.ru' not in vv) and \
					('abuse@godaddy.com' not in vv) and \
					('abuse@regtime.net' not in vv) and \
					('publicdomainregistry.com' not in vv) and \
					('@' in vv):
					print '!!!!!!!', k, kk, vv
			#if v['whois'].get('e-mail'):
				#print '!!!!!!!', v['whois'].get('e-mail')

		if type(v) != dict:
			continue

		ga_ids = v.get('ga', [])
		ym_ids = v.get('ym', [])
		for ua in ga_ids:
			#print '\t', ua
			ua = ua[:11]
			if not res.get(ua):
				res[ua] = set()
			res[ua].add(k)

		#for ua in ym_ids:
			##print '\t', ua
			#if not res.get(ua):
				#res[ua] = set()
			#res[ua].add(k)

	for k, v in res.items():
		if len(v) > 1:
			print k
			for url in v:
				print '\t', url

analyze()


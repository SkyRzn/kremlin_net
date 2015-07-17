#!/usr/bin/python
# -*- coding: utf-8 -*-


import json, sys
import networkx as nx
from manual_data import add_manual_data

from PyQt4.QtCore import *
from PyQt4.QtGui import *

def id_count(id_, data):
	n = 0
	for url, info in data.items():
		if id_ in info.get('ga', []):
			n += 1
		if id_ in info.get('ym', []):
			n += 1
	return n

def cut_ga(data):
	for url, info in data.items():
		if info.get('ga'):
			info['ga'] = [v[:11] for v in info['ga']]


def draw():
	f = open('data.json', 'r')
	j = f.read()
	f.close()

	if not j:
		print 'read file error'
		return

	data = json.loads(j)

	add_manual_data(data)

	cut_ga(data)

	graph = nx.Graph()

	nodes = {}
	edges = []

	ga_pix = QPixmap('google.png')
	ym_pix = QPixmap('yandex.png')
	email_pix = QPixmap('email.png')
	site_pix = QPixmap('site.png')

	for url, info in data.items():
		if info.get('err'):
			continue
		for id_ in info.get('ga', []):
			id_ = id_[:11]
			if id_count(id_, data) > 1:
				graph.add_edge(url, id_)
				edges.append([url, id_])
				nodes[id_] = QGraphicsPixmapItem(ga_pix)
				nodes[id_].name = id_
				nodes[id_].setFlag(QGraphicsItem.ItemIsMovable, True)
		for id_ in info.get('ym', []):
			id_ = id_[:11]
			if id_count(id_, data) > 1:
				graph.add_edge(url, id_)
				edges.append([url, id_])
				nodes[id_] = QGraphicsPixmapItem(ym_pix)
				nodes[id_].name = id_
				nodes[id_].setFlag(QGraphicsItem.ItemIsMovable, True)

		if info.get('email'):
			email = info.get('email')
			nodes[email] = QGraphicsPixmapItem(email_pix)
			nodes[email].name = email
			nodes[email].setFlag(QGraphicsItem.ItemIsMovable, True)
			graph.add_edge(url, email)
			edges.append([url, email])

		nodes[url] = QGraphicsPixmapItem(site_pix)
		nodes[url].name = url
		nodes[url].setFlag(QGraphicsItem.ItemIsMovable, True)
		graph.add_node(url)

	for key, data in nx.graphviz_layout(graph).items():
		x, y = map(lambda x: x*1.5, data)

		if key in nodes:
			nodes[key].setPos(QPointF(x, y))
			nodes[key].lol = key

	return nodes, edges


app = QApplication(sys.argv)
win = QGraphicsView()

scene = QGraphicsScene()
win.setScene(scene)

nodes, edges = draw()



def redraw(self):
	for item in scene.items():
		if type(item) == QGraphicsLineItem or type(item) == QGraphicsTextItem or type(item) == QGraphicsPixmapItem:
			scene.removeItem(item)

	for n1, n2 in edges:
		p1 = nodes[n1].pos()
		p2 = nodes[n2].pos()
		p1.setX(p1.x() + 16)
		p1.setY(p1.y() + 16)
		p2.setX(p2.x() + 16)
		p2.setY(p2.y() + 16)
		scene.addLine(QLineF(p1, p2))

	for node in nodes.values():
		scene.addItem(node)

	for node in nodes.values():
		it = scene.addText(node.name)
		it.name = node.name
		pos = QPointF(node.pos())
		pos.setX(pos.x() - it.boundingRect().width()/2 + 16)
		pos.setY(pos.y() + 24)
		it.setPos(pos)



win.mouseDoubleClickEvent = redraw
#redraw()

win.setGeometry(QRect(100, 100, 400, 400))
win.show()
app.exec_()



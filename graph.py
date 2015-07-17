#!/usr/bin/python
# -*- coding: utf-8 -*-


import json, sys
import networkx as nx
from manual_data import add_manual_data

from PyQt4.QtCore import *
from PyQt4.QtGui import *


def draw():
	f = open('data.json', 'r')
	j = f.read()
	f.close()

	if not j:
		print 'read file error'
		return

	data = json.loads(j)

	add_manual_data(data)

	graph = nx.Graph()

	nodes = {}
	edges = []

	acc_pix = QPixmap('acc.png')
	site_pix = QPixmap('site.png')

	for url, info in data.items():
		if info.get('err'):
			continue
		for id_ in info.get('ga', []):
			id_ = id_[:11]
			graph.add_edge(url, id_)
			edges.append([url, id_])
			nodes[id_] = QGraphicsPixmapItem(acc_pix)
			nodes[id_].name = id_
		for id_ in info.get('ym', []):
			id_ = id_[:11]
			graph.add_edge(url, id_)
			edges.append([url, id_])
			nodes[id_] = QGraphicsPixmapItem(acc_pix)
			nodes[id_].name = id_
		nodes[url] = QGraphicsPixmapItem(site_pix)
		nodes[url].name = url
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
	it = scene.addText(node.name)
	it.setPos(node.pos())

win.setGeometry(QRect(100, 100, 400, 400))
win.show()
app.exec_()



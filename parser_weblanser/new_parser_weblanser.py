#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Парсер рабочий 05.09.2016
"""
import csv
import urllib.request
from bs4 import BeautifulSoup

BASE_URL = 'https://www.weblancer.net/jobs/'

def get_html(url):
	response = urllib.request.urlopen(url)
	return response.read()

def get_page_count(html):
	soup = BeautifulSoup(html)
	pagination = soup.find('ul', class_ = 'pagination')
	old_str = str(pagination.find_all('a')[-1:])
	ind1, ind2 = old_str.find('page='), old_str.find('>Последняя')
	old_page = int(old_str[ind1 + 5: ind2 - 1])
	return old_page

def parse(html):
	soup = BeautifulSoup(html)
	table = soup.find('div', class_= 'container-fluid cols_table show_visited')
	
	projects = []
	for rows in table.find_all('div', class_='row'):
		cols = rows.find_all('div')

		def categor(str_caterories):
			if str_caterories != None:
				return str_caterories.string
			else:
				return str(None)

		projects.append({
			'title' : str(cols[0].find('a').string),
			'categories' : categor(cols[1].find('a')),
			'money' : str(cols[2].string).strip(),
			'application' : str(cols[3].string).strip()
		})
	return projects

def save(projects, path):
	with open(path, 'w') as csvfile:
		writer = csv.writer(csvfile)
		writer.writerow(('Проект', 'Категории', 'Цена', 'Заявки'))

		for project in projects:
			writer.writerow((project['title'], project['categories'], project['money'], project['application']))

def main():
	page_count = get_page_count(get_html(BASE_URL))

	print('Всего страниц %d' % page_count)
	projects = []

	for page in range(1, page_count):
		print('Парсинг %d%%' % (page / page_count * 100))
		projects.extend(parse(get_html(BASE_URL + '?page=%d' % page)))
	save(projects, 'projects.csv')
	# print(get_page_count(get_html(BASE_URL)))


if __name__ == '__main__':
	main()

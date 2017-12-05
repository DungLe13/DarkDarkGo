#! /usr/bin/env python3
"""
    seed_queue.py - a simple queue that has endpoints to request a list of seeds and
        to add new seeds to the queue.
    Author: mgmt
    Date: 11/28/2017
"""

from flask import Flask, request, jsonify
from queue import Queue

dm_queue = Flask(__name__)
q = Queue()     # queue stores seed urls
n = 10          # num of links in a chunk
c_id = 0        # chunk id starts at 0 and increases incrementally

# a temp starting set of links
links = ["https://vinaora.com/at/vulputate/vitae/nisl/aenean/lectus/pellentesque.js",
        "https://google.fr/massa.js",
        "http://bing.com/nec/sem.js"]

# insert these temp links to the queue
def insert_from_array(q, linksArray):
    for link in linksArray:
        q.put(link)
insert_from_array(q, links)

# call this endpoint to add seed urls to the queue
@dm_queue.route("/add_links", methods=['POST'])
def add_links_to_queue():
    """
        Adds links from an array that is sent to the endpoint to the queue.
    """
    links_from_crawler = request.get_json()
    for link in links_from_crawler['links']:
        if link not in q:
            q.put(link)

# call this endpoint to get n seed urls from the queue
# returns json with a chunk id and set of n links
@dm_queue.route("/get_links", methods=['GET'])
def get_links_from_queue():
    """
        Creates an array of seed urls from the queue and retuns them along with the
        chunk id of the chunk to be created.
        :return: json containing the chunk id and the collection of seeds
    """
    temp_links = {}
    if q.qsize() <= n:
        # throws exception code 01 when queue doesn't have enough seed urls
        temp_links = {'exception': 01}
        return jsonify(temp_links)
    else:
        temp_links['c_id'] = generate_chunk_id()
        temp_links['links'] = []
        for i in range(0,n):
            temp_links['links'].append(q.get())
        print(temp_links)
        return jsonify(temp_links)

# temp chunk id function
def generate_chunk_id():
    """
        Generates chunk id. Right now it is an integer that starts at 0 and increases
        by one.
        :return: chunk id as integer
    """
    return c_id + 1


if __name__ == '__main__':
    dm_queue.run(host='0.0.0.0')
#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const URL = process.argv[2];
const FILE = process.argv[3];

function requestStore (err, resp, body) {
	if (err == null) {
		fs.writeFileSync(FILE, body);
	}
}
request(URL, requestStore);

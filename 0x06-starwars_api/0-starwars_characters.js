#!/usr/bin/node
// prints character of star war movies

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2]

request.get(url, function(error, response, body) {
    if (!error) {
	const characters = JSON.parse(body).characters;
	const len = characters.length;
	Names(0, characters[0], characters, len);
    }
});
function Names (i, url, chars, len) {
    if (i === len) {
	return;
    }
    request.get(url, function (error, response, body) {
	if(!error) {
	    console.log(JSON.parse(body).name);
	    i++;
	    Names(i, chars[i], chars, len);
	}
    });
}

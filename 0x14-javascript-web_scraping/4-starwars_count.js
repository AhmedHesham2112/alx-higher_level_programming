#!/usr/bin/node
const request = require('request');
const url = `${process.argv[2]}`;
request.get(url, (err, res, body) => {
  if (!err) {
    const films = JSON.parse(body).results;
    let count = 0;
    films.forEach(film => {
      if (film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
        count++;
      }
    });
    console.log(count);
  }
});

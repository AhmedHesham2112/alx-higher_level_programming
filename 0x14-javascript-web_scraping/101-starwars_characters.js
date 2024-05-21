#!/usr/bin/node
const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
request.get(url, (err, res, body) => {
  if (err) {
    return console.log(err);
  } else {
    const characters = JSON.parse(body).characters;
    for (const character of characters) {
      request.get(character, (err, res, bodyy) => {
        if (err) {
          console.log(err);
        }
        const char = JSON.parse(bodyy);
        console.log(char.name);
      });
    }
  }
});

#!/usr/bin/node
const fs = require('fs');
const request = require('request');
request.get(process.argv[2], (err, res) => {
  if (err) {
    return console.log(err);
  }
  console.log(`code: ${res.statusCode}`);
});

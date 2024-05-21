#!/usr/bin/node
const request = require('request');
const url = `${process.argv[2]}`;
request.get(url, (err, res, body) => {
  if (err) {
    return console.log(err);
  } else {
    const users = JSON.parse(body);
    const completedTasks = {};
    users.forEach(user => {
      if (user.completed) {
        if (!completedTasks[user.userId]) {
          completedTasks[user.userId] = 0;
        }
        completedTasks[user.userId]++;
      }
    });
    console.log(completedTasks);
  }
});

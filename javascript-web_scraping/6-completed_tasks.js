#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Unexpected response: ${response.statusCode}`);
    return;
  }

  const todos = JSON.parse(body);
  const completedByUser = {};

  todos.forEach(todo => {
    if (todo.completed) {
      const userId = todo.userId;
      completedByUser[userId] = (completedByUser[userId] || 0) + 1;
    }
  });

  Object.entries(completedByUser).forEach(([userId, count]) => {
    console.log(`'${userId}': ${count},`);
  });
});

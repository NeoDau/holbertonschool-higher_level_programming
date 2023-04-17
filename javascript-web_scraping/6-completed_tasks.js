#!/usr/bin/node

const request = require('request');
const apiUrl = 'https://jsonplaceholder.typicode.com/todos';

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  
  const todos = JSON.parse(body);
  const completedUser = {};
  
  todos.forEach((todo) => {
    if (todo.completed) {
      if (completedUser[todo.userId]) {
        completedUser[todo.userId]++;
      } else {
        completedUser[todo.userId] = 1;
      }
    }
  });
  console.log(completedUser);
});

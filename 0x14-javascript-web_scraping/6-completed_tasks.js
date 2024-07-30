#!/usr/bin/node

const request = require('request');

const URL = process.argv[2];

if (!URL) {
  process.exit(1);
}
request(URL, (error, response, body) => {
  if (error) {
    process.exit(1);
  }
  const tasks = JSON.parse(body);
  const completedTasksCount = tasks.reduce((acc, task) => {
    if (task.completed) {
      if (!acc[task.userId]) {
        acc[task.userId] = 0;
      }
      acc[task.userId]++;
    }
    return acc;
  }, {});
  console.log(completedTasksCount);
});

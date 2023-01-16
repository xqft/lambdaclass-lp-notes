const express = require("express");
const redis   = require("redis");

const web   = express();
const port  = 3000;

const client = redis.createClient();
client.on('error', console.log);

web.get("/", async (_req, res) => {
  await client.connect();
  const count = await client.incr('count') // sets to 0 if key doesn't exist.

  res.status(200).send("Hello! you have visited this page " + Number(count + 1) + " times!");

  await client.disconnect();
});

web.listen(port);

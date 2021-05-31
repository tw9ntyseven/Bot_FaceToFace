const express = require('express');
const bodyParser = require('body-parser');
const VkBot = require('node-vk-bot-api');

const app = express();
const bot = new VkBot("1dbcda3e92d5fc461cf43916382318e64202ac8e3fa85317139c4f01a9497a3bc0fff2d2621c673c3baa3");

bot.on((ctx) => {
    console.log(ctx)
    ctx.reply('Hello!');
});

app.use(bodyParser.json());

app.post('/', bot.webhookCallback);

app.listen(80);
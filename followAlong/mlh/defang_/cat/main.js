const express = require('express');
const axios = require('axios');
const app = express();

const CAT_API_KEY = process.env.CAT_API_KEY;
const CAT_API_URL = 'https://api.thecatapi.com/v1/images/search';

app.get('/', async (req, res) => {
  try {
    const response = await axios.get(CAT_API_URL, {
      headers: { 'x-api-key': CAT_API_KEY }
    });
    const catImageUrl = response.data[0].url;
    res.redirect(catImageUrl);
  } catch (error) {
    res.status(500).send('Error fetching cat image');
  }
});

app.listen(3000, () => {
  console.log('Server started on port 3000');
});

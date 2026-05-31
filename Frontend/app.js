const express = require('express');
const axios = require('axios');
const bodyParser = require('body-parser');

const app = express();

app.set('view engine', 'ejs');
app.use(bodyParser.urlencoded({ extended: true }));

// Flask backend URL (important for Docker)
const BACKEND_URL = "http://13.201.99.67:5000";

// Form page
app.get('/', (req, res) => {
    res.render('form');
});

// Submit form → send to Flask
app.post('/submit', async (req, res) => {
    console.log("REQ BODY:", req.body);

    try {
        const response = await axios.post(
            `${BACKEND_URL}/submit`,
            req.body
        );

        console.log("BACKEND RESPONSE:", response.data);

        res.redirect('/success');
    } catch (error) {
        console.log(error);
        res.render('form', { error: "Error submitting form" });
    }
});
// Todo page
app.get('/todo', (req, res) => {
    res.render('todo');
});

// Submit todo → Flask
app.post('/submittodoitem', async (req, res) => {
    try {
        await axios.post(`${BACKEND_URL}/submittodoitem`, req.body);
        res.redirect('/success');
    } catch (error) {
        res.render('todo', { error: "Error submitting todo" });
    }
});

app.get('/success', (req, res) => {
    res.render('success');
});

app.listen(3000, () => console.log("Frontend running on port 3000"));
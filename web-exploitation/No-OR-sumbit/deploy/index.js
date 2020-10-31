const express = require('express')
const app = express()
const port = 14045

const db = require('./db/sql.js')

app.use(express.json());

app.use(express.urlencoded({
    extended: false
}));

app.use(express.text({
    type: 'text/html'
}))

app.get('/', (req, res) => {
    res.sendFile('frontend/index.html', {
        root: __dirname
    })
})

app.post('/search', (req, res) => {
    const id = req.body.src
    db.query(`SELECT * FROM explo WHERE id = ${id}`, (err, result, fields) => {
        if (err != null) {
            console.log(err)
            res.send(err)
        } else {
            res.send(result)
            console.log(result)
        }
    });

})

app.listen(port, () => {
    console.log(`Example app listening at http://localhost:${port}`)
})
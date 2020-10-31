const mysql = require('mysql2');

const db = mysql.createPool({
    host: "localhost",
    user: "root",
    database: "basicsqli"
});

db.query(
    'SELECT 1=1 AS RESULT',
    (err, results, fields) => {
        if (err != null) {
            console.log(err);
        } else {
            console.log("Connected")
        }
    }
);

module.exports = db
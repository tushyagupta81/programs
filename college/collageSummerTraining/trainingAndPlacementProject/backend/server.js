const http = require("http");
const mysql = require("mysql2");

var con = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "Ra1nm3t3r",
  database: "test",
});

const server = http.createServer((req, res) => {
  let body = "";
  req.on("data", (chunk) => {
    body += chunk.toString();
  });
  req.on("end", () => {
    const { name,id,date,fname,mname,country,address,terms} = JSON.parse(body);
    // console.log(`username = ${username}, password = ${password}`); 
    // Connect to mySql server
    con.connect(function (err) {
      if (err) throw err;
      console.log("Connected to MySQL server!");

      // Insert values into table
      sql = `INSERT INTO USERS (name,id,dob,fname,mname,country,address) VALUES ('${name}','${id}','${date}','${fname}','${mname}','${country}','${address}');`;
      con.query(sql, function (err, result) {
        if (err) throw err;
        console.log("Values inserted");
      });
    });
  });
  res.statusCode = 200;
  res.setHeader("Content-Type", "text/plain");
  res.write("Done!");
  res.end();
});

const port = 3000;

server.listen(port, () => {
  console.log(`Server running on port ${port}`);
});

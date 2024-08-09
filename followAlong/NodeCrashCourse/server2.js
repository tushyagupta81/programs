import { createServer } from 'http';
const PORT = process.env.PORT;

const users = [
    { id: 1, name: "John doe" },
    { id: 2, name: "John 2" },
    { id: 3, name: "John 3" },
];
// looger middleware
const logger = (req, res, next) => {
    console.log(`${req.method} ${req.url}`);
    next();
}

// json middleware
const jsonMiddleware = (req, res, next) => {
    res.setHeader("Content-Type", "application/json");
    next();
}

// route handler for /api/users
const getUsersHandler = (req, res) => {
    res.write(JSON.stringify(users));
    res.end();
}

// Route handler for get /api/users/:id
const getUserByIdHandler = (req, res) => {
    const id = req.url.split('/')[3];
    const user = users.find((user) => user.id === parseInt(id));
    if (user) {
        res.write(JSON.stringify(user));
    } else {
        res.write(JSON.stringify({ message: "user not found" }));
    }
    res.end();
}

// Not found handler
const notFoundHandler = (req, res) => {
    res.statusCode = 404;
    res.write(JSON.stringify({ message: "route not found" }));
    res.end();
}

// Route handler for post request to /api/users
const createUserHandler = (req,res) => {
    let body = '';
    req.on('data',(chunk)=>{
        body += chunk.toString();
    })
    req.on('end',()=>{
        const newUser = JSON.parse(body);
        res.statusCode = 201;
        res.write(JSON.stringify(newUser));
        users.push(newUser);
        res.end();
    })
}

const server = createServer((req, res) => {
    logger(req, res, () => {
        jsonMiddleware(req,res, () => {
            if(req.url === '/api/users' && req.method === 'GET'){
                getUsersHandler(req,res);
            }else if(req.url.match(/\/api\/users\/([0-9]+)/) && req.method ==='GET'){
                getUserByIdHandler(req,res);
            }else if(req.url === '/api/users' && req.method === 'POST'){
                createUserHandler(req,res);
            }else{
                notFoundHandler(req,res);
            }
        })
    });
});

server.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
})

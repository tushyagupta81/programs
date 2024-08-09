// import fs from 'fs';
import fs from 'fs/promises';

// fs.readFile('./test.txt','utf8',(err,data) =>{
//     if(err){
//         throw err;
//     }
//     console.log(data);
// })
//
// const data = fs.readFileSync('./test.txt','utf8');
// console.log(data);
//


fs.readFile('./test.txt','utf8')
    .then((data) => console.log(data))
    .catch((err) => console.log(err));



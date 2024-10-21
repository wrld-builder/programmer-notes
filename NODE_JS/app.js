const http = require('http');

http.createServer(function(request, response) {
    response.end('Hello world!');
}).listen(3000, '127.0.0.1', function() {
    console.log('Server start listening on port 3000...');
});
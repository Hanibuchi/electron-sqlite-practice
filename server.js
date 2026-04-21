const http = require('http');

const server = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain; charset=utf-8' });
  res.end('Node.jsサーバーが立ち上がりました！\n');
});

// ポート5000で待ち受け
server.listen(5000, () => {
  console.log('Server running at http://localhost:5000/');
});
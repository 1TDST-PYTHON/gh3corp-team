const app = require('./app');

app.listen(process.env.PORT || 3333, () => {
    console.log('🚀 Start Server : http://localhost:3333/');
});
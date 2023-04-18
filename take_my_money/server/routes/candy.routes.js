
const CandyController = require('../controllers/candy.controller');

module.exports = (app) => {
    // app.get('/api', CandyController.index);
    app.get('/api/candy', CandyController.getAll);
    app.get('/api/candy/:id', CandyController.getOne);
    app.post('/api/candy', CandyController.create);
    app.put('/api/candy/:id', CandyController.update);
    app.delete('/api/candy/:id', CandyController.delete);
}
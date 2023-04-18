const Candy = require('../models/candy.model')


module.exports = {

    create : (req, res) => {
        Candy.create(req.body)
            .then(result => {
                console.log(result);
                res.json(result);
            })
            .catch(err => res.status(400).json(err));
    },

    getAll : (req,res) => {
        Candy.find({})
            .then(result => {
                console.log(result);
                res.json(result);
            })
            .catch(err => {
                console.log(err)
                .catch((err) => res.status(400).json(err))
            })
    },

    getOne : (req,res) => {
        Candy.findOne({_id: req.params.id})
            .then(result => {
                console.log(result);
                res.json(result);
            })
            .catch(err => {
                console.log(err)
                .catch((err) => res.status(400).json(err))
            })
    },

    update : (req,res) => {
        Candy.findOneAndUpdate({_id: req.params.id}, req.body, {new:true})
            .then(result => {
                console.log(result);
                res.json(result);
            })
            .catch(err => {
                console.log(err)
                .catch((err) => res.status(400).json(err))
            })
    },

    delete : (req,res) => {
        Candy.deleteOne({ _id: req.params.id})
            .then(deleteConfirmation => res.json(deleteConfirmation))
            .catch((err) => res.status(400).json(err))
    }
}







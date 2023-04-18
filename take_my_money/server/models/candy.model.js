const mongoose = require('mongoose');
const CandySchema = new mongoose.Schema({
    name: { 
        type: String,
        required: [true, "Candy Name Required"],
        minlenth: [2, "Name must be at least 2 characters long"]
    },
    
    
}, { timestamps: true }); 
module.exports = mongoose.model('Candy',CandySchema);

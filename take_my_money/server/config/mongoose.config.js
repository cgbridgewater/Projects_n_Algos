
const mongoose = require('mongoose');

mongoose.connect("mongodb://127.0.0.1:27017/candyshop", {
    useNewUrlParser: true,
    useUnifiedTopology: true,
})
    .then(() => console.log("Established a connection, I'll take you to the candy shop..."))
    .catch(err => console.log("Something went wrong when connecting to the database",err))
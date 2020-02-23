const express = require('express');
const router = express.Router();
const mongoose = require('mongoose');
const passport = require('passport');
let {PythonShell} = require('python-shell')

let pyshell = new PythonShell('Main/query_to_model.py');


// Load problem model
const problem = require('../../models/problem');

// @route   POST api/problem/submitProblem
// @desc    Submit problem statement -> send problem to python -> recive schema from python.
// @access  Public
router.post('/submitProblem', (req, res) => {
    const newProblem = new problem({
        title: req.body.title,
        defination: req.body.defination,
      });

    // sends a message to the Python script via stdin
       // pyshell.send(newProblem.title);
       let pyshell = new PythonShell('Main/query_to_model.py');

         pyshell.send(newProblem.defination);


    pyshell.on('message', function (message) {
    // received a message sent from the Python script (a simple "print" statement)
    console.log(message);
    });
    newProblem
    .save()
    .then(problem => res.json(problem))
    .catch(err => console.log(err));
});

module.exports = router;
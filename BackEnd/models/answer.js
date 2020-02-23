const mongoose = require('mongoose');
const Schema = mongoose.Schema;

// Create Schema
const AnswerSchema = new Schema({
  text: {
    type: String,
    required: true
  },
  priority: {
    type: Number,
    required: true
  },
  date: {
    type: Date,
    default: Date.now
  }
});

module.exports = Answer = mongoose.model('answers', UserSchema);

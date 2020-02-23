const mongoose = require('mongoose');
const Schema = mongoose.Schema;

// Create Schema
const ProjectSchema = new Schema({
  title: {
    type: String,
    required: true
  },
  description: {
    type: String,
  },
  avatar: {
    type: String
  },
  date: {
    type: Date,
    default: Date.now
  }
});

module.exports = Project = mongoose.model('projects', UserSchema);

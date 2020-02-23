const mongoose = require('mongoose');
const Schema = mongoose.Schema;

// Create Schema
const problemResultSchema = new Schema({
  result: {
    type: String,
  },
  steps: [{

    toolName:{
    type: String,
  },

  toolLink:{
  type: String,
  }
}],
  date: {
    type: Date,
    default: Date.now
  }
});

module.exports = problemResult = mongoose.model('problemResult', UserSchema);

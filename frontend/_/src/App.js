import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './styles.css';

function App() {
  const [thoughts, setThoughts] = useState([]);
  const [input, setInput] = useState('');

  useEffect(() => {
    axios.get('https://your-backend-url.com/thoughts')
      .then(response => setThoughts(response.data))
      .catch(error => console.error('Error fetching thoughts:', error));
  }, []);

  const handleSubmit = () => {
    if (input.trim()) {
      axios.post('https://your-backend-url.com/thoughts', { text: input })
        .then(response => {
          setThoughts([...thoughts, response.data]);
          setInput('');
        })
        .catch(error => console.error('Error adding thought:', error));
    }
  };

  return (
    <div className="app-container">
      <h1>Share Your Thoughts</h1>
      <textarea
        value={input}
        onChange={e => setInput(e.target.value)}
        maxLength={999}
        placeholder="Write your thought..."
      />
      <button onClick={handleSubmit}>Submit</button>
      <div className="thoughts-container">
        {thoughts.map((thought, index) => (
          <div key={index} className="thought">
            <p>{thought.text}</p>
            <span>{new Date(thought.timestamp).toLocaleString()}</span>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;

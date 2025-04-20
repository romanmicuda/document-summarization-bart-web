// src/components/Summarizer.jsx
import React, { useState } from 'react';
import axios from 'axios';
import './Summarizer.css';

const Summarizer = () => {
  const [text, setText] = useState('');
  const [summary, setSummary] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsLoading(true);
    setError('');
    
    try {
      const response = await axios.post('http://localhost:5001/summarize', {
        text: text
      });
      setSummary(response.data.summary);
    } catch (err) {
      setError(err.response?.data?.error || 'Failed to generate summary');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="summarizer-container">
      <h1>AI Text Summarizer</h1>
      
      <form onSubmit={handleSubmit}>
        <textarea
          value={text}
          onChange={(e) => setText(e.target.value)}
          placeholder="Enter text to summarize..."
          rows={10}
          required
        />
        
        <button type="submit" disabled={isLoading}>
          {isLoading ? 'Generating...' : 'Summarize'}
        </button>
      </form>

      {error && <div className="error">{error}</div>}
      
      {summary && (
        <div className="summary-result">
          <h2>Summary:</h2>
          <p>{summary}</p>
        </div>
      )}
    </div>
  );
};

export default Summarizer;
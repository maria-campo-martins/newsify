import React, { useState } from 'react';
import Table from "./Table.js";

function App() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [maxArticles, setMaxArticles] = useState('');

  const handleInput = (e) => {
    setMaxArticles(e.target.value);
  };

  const handleScrape = async () => {
    setLoading(true);
    setData(null);
    const response = await fetch('http://localhost:8000/api/scrape/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ maxArticles: maxArticles }),
    });

    const result = await response.json();
    setLoading(false);
    setData(result);
  };

  return (
    <div className="App">
      <h1>Newsify</h1>
      
      <div> 
      <input
        type="number"
        name="number"
        value={maxArticles}
        onChange={handleInput}
        placeholder="Max number of articles to be displayed"
      />
      <button onClick={handleScrape} disabled={loading}>
        {loading ? "Scraping..." : "Scrape Data"}
      </button>
      </div>

      {/* Display the scraped data in a table */}
      {data && <Table data={data} />}
    </div>
  );
}

export default App;

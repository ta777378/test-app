import { useEffect, useState } from 'react';

function App() {
  const [message, setMessage] = useState('Loading...');

  useEffect(() => {
    fetch('/api/hello')
      .then((res) => res.json())
      .then((data) => setMessage(data.message))
      .catch((err) => {
        console.error('API error:', err);
        setMessage('Error connecting to API');
      });
  }, []);

  return (
    <div>
      <h1>MyTask</h1>
      <p>{message}</p>
    </div>
  );
}

export default App;

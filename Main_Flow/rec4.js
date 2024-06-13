import React, { useState } from 'react';
import { Button, Card } from './components';
import { trackEvent } from './analytics';

function App() {
  const [count, setCount] = useState(0);

  const handleClick = () => {
    setCount(count + 1);
    trackEvent('button_click', { label: 'Increment' });
  };

  return (
    <div>
      <Card>
        <Button onClick={handleClick}>Click me!</Button>
        <p>Count: {count}</p>
      </Card>
    </div>
  );
}

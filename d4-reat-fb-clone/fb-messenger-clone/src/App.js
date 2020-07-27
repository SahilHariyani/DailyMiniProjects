import React, { useState } from 'react';

import './App.css';

function App() {
  const [input, setInput] = useState('');
  const [messages, setMessages] = useState(['a','b']);

  console.log(input);
  console.log(messages);

  const sendMessage = (event) =>{
    setMessages([...messages,input])
    //
  }
  return (
    <div className="App">
      <h1>Hello World! 🙂 </h1>
      <form>
      <input value={input} onChange={event => setInput(event.target.input)}/>
      <button type="submit" onClick={sendMessage}>Send message</button>
      </form>
    </div>
  );
}

export default App;

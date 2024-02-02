
import React, { useState } from 'react';
import './UserAuthPage.css';

const UserAuthPage = () => {
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [isLogin, setIsLogin] = useState(true);

  const handleToggleAuthMode = () => {
    setIsLogin(!isLogin);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // Here, you can implement form submission logic, such as sending data to the backend for authentication.
    if (isLogin) {
      console.log('Logging in...');
      console.log('Email:', email);
      console.log('Password:', password);
    } else {
      console.log('Registering...');
      console.log('Username:', username);
      console.log('Email:', email);
      console.log('Password:', password);
    }
  };

  return (
    <div className="form-container">
      <h2>{isLogin ? 'Login' : 'Register'}</h2>
      <form onSubmit={handleSubmit}>
        {!isLogin && (
          <div className="form-group">
            <label className="form-label">Username:</label>
            <input
              type="text"
              className="form-input"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
            />
          </div>
        )}
        <div className="form-group">
          <label className="form-label">Email:</label>
          <input
            type="email"
            className="form-input"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
        </div>
        <div className="form-group">
          <label className="form-label">Password:</label>
          <input
            type="password"
            className="form-input"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
        </div>
        <button type="submit" className="form-button">
          {isLogin ? 'Login' : 'Register'}
        </button>
      </form>
      <p>
        {isLogin ? "Don't have an account?" : 'Already have an account?'}
        <button className="toggle-button" onClick={handleToggleAuthMode}>
          {isLogin ? 'Register here' : 'Login here'}
        </button>
      </p>
    </div>
  );
};

export default UserAuthPage;

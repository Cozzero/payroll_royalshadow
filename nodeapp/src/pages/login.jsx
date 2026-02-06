import React, { useState } from 'react';
import axios from 'axios';

export default function Login() {
    const [formData, setFormData] = useState({
        email: '',
        password: '',
    });
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState('');

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData(prev => ({
            ...prev,
            [name]: value,
        }));
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        setError('');
        setLoading(true);

        try {
            const response = await axios.post('/api/auth/login', {
                email: formData.email,
                password: formData.password,
            });

            // Store token for future requests
            localStorage.setItem('authToken', response.data.token);
            localStorage.setItem('userId', response.data.userId);

            // Redirect to dashboard or home
            window.location.href = '/dashboard';
        } catch (err) {
            setError(err.response?.data?.message || 'Login failed. Please try again.');
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="login-container">
            <div className="login-card">
                <h1>Client Login</h1>
                {error && <div className="error-message">{error}</div>}
                
                <form onSubmit={handleSubmit}>
                    <div className="form-group">
                        <label htmlFor="email">Email</label>
                        <input
                            type="email"
                            id="email"
                            name="email"
                            value={formData.email}
                            onChange={handleChange}
                            required
                            placeholder="Enter your email"
                        />
                    </div>

                    <div className="form-group">
                        <label htmlFor="password">Password</label>
                        <input
                            type="password"
                            id="password"
                            name="password"
                            value={formData.password}
                            onChange={handleChange}
                            required
                            placeholder="Enter your password"
                        />
                    </div>

                    <button type="submit" disabled={loading}>
                        {loading ? 'Logging in...' : 'Login'}
                    </button>
                </form>

                <div className="login-footer">
                    <p>Don't have an account? <a href="/register">Register here</a></p>
                </div>
            </div>
        </div>
    );
}

<div className="register-prompt">
    <p>If you don't have an account, please register:</p>
    <button onClick={async () => {
        try {
            const response = await axios.post('/api/auth/register', {
                email: formData.email,
                password: formData.password,
            });

            // Store token for future requests
            localStorage.setItem('authToken', response.data.token);
            localStorage.setItem('userId', response.data.userId);

            // Redirect to dashboard or home
            window.location.href = '/dashboard';
        } catch (err) {
            setError(err.response?.data?.message || 'Registration failed. Please try again.');
        }
    }}>
        Register
    </button>
</div>

import { useState } from "react";
import api from "../api/axios";
import { useNavigate } from "react-router-dom";

function Login() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  const login = async () => {
    const res = await api.post("login/", {
      username,
      password,
    });

    localStorage.setItem("token", res.data.access);
    navigate("/");
  };

  return (
    <div>
      <h2>Login</h2>

      <input onChange={(e) => setUsername(e.target.value)} placeholder="Username" />
      <input type="password" onChange={(e) => setPassword(e.target.value)} placeholder="Password" />

      <button onClick={login}>Login</button>
    </div>
  );
}

// export default Login;

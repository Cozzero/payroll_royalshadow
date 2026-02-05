import React from 'react';
import './AppHeader.css';

const AppHeader = () => {
    return (
        <header className="app-header">
            <div className="header-container">
                <div className="logo">
                    <h1>Payroll System</h1>
                </div>
                <nav className="header-nav">
                    <ul>
                        <li><a href="/">Dashboard</a></li>
                        <li><a href="/employees">Employees</a></li>
                        <li><a href="/payroll">Payroll</a></li>
                        <li><a href="/reports">Reports</a></li>
                    </ul>
                </nav>
                <div className="user-menu">
                    <button className="user-btn">Profile</button>
                    <button className="logout-btn">Logout</button>
                </div>
            </div>
        </header>
    );
};

export default AppHeader;
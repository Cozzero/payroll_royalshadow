import React, { useState, useEffect } from 'react';
import './dashboard.css';

const Dashboard = () => {
    const [dashboardData, setDashboardData] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        fetchDashboardData();
    }, []);

    const fetchDashboardData = async () => {
        try {
            setLoading(true);
            // Replace with your actual API endpoint
            const response = await fetch('/api/dashboard');
            if (!response.ok) throw new Error('Failed to fetch dashboard data');
            const data = await response.json();
            setDashboardData(data);
        } catch (err) {
            setError(err.message);
        } finally {
            setLoading(false);
        }
    };

    if (loading) return <div className="dashboard">Loading...</div>;
    if (error) return <div className="dashboard error">Error: {error}</div>;

    return (
        <div className="dashboard">
            <header className="dashboard-header">
                <h1>Payroll Dashboard</h1>
                <p>Welcome, {dashboardData?.userName}</p>
            </header>

            <div className="dashboard-grid">
                <div className="card">
                    <h2>Current Pay Period</h2>
                    <p className="amount">${dashboardData?.currentPaycheck}</p>
                    <p className="date">{dashboardData?.payPeriod}</p>
                </div>

                <div className="card">
                    <h2>Year-to-Date Earnings</h2>
                    <p className="amount">${dashboardData?.ytdEarnings}</p>
                </div>

                <div className="card">
                    <h2>Next Payday</h2>
                    <p className="date">{dashboardData?.nextPayday}</p>
                </div>
            </div>

            <div className="dashboard-section">
                <h2>Recent Paychecks</h2>
                <table className="paycheck-table">
                    <thead>
                        <tr>
                            <th>Date</th>
                            <th>Gross Pay</th>
                            <th>Deductions</th>
                            <th>Net Pay</th>
                        </tr>
                    </thead>
                    <tbody>
                        {dashboardData?.recentPaychecks?.map((check) => (
                            <tr key={check.id}>
                                <td>{check.date}</td>
                                <td>${check.grossPay}</td>
                                <td>${check.deductions}</td>
                                <td>${check.netPay}</td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        </div>
    );
};

export default Dashboard;
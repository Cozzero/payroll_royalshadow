import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Employee = () => {
    const [employee, setEmployee] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        fetchEmployeeDetails();
    }, []);

    const fetchEmployeeDetails = async () => {
        try {
            const response = await axios.get('/api/employees'); // Adjust endpoint as needed
            setEmployee(response.data);
            setLoading(false);
        } catch (err) {
            setError(err.message);
            setLoading(false);
        }
    };

    if (loading) return <div>Loading...</div>;
    if (error) return <div>Error: {error}</div>;

    return (
        <div className="employee-container">
            <h1>Employee Details</h1>
            {employee && (
                <div className="employee-details">
                    <p><strong>Name:</strong> {employee.name}</p>
                    <p><strong>Email:</strong> {employee.email}</p>
                    <p><strong>Position:</strong> {employee.position}</p>
                    <p><strong>Department:</strong> {employee.department}</p>
                    <p><strong>Salary:</strong> ${employee.salary}</p>
                    <p><strong>Start Date:</strong> {employee.startDate}</p>
                </div>
            )}
        </div>
    );
};

export default Employee;
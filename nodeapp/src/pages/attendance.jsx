import React, { useState, useEffect } from 'react';
import axios from 'axios';

const AttendancePage = () => {
    const [attendanceData, setAttendanceData] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        fetchAttendance();
    }, []);

    const fetchAttendance = async () => {
        try {
            setLoading(true);
            const response = await axios.get('/api/attendance');
            setAttendanceData(response.data);
            setError(null);
        } catch (err) {
            setError(err.message || 'Failed to fetch attendance');
            console.error('Error fetching attendance:', err);
        } finally {
            setLoading(false);
        }
    };

    if (loading) return <div className="loading">Loading attendance data...</div>;
    if (error) return <div className="error">Error: {error}</div>;

    return (
        <div className="attendance-container">
            <h1>Attendance Management</h1>
            <table className="attendance-table">
                <thead>
                    <tr>
                        <th>Employee ID</th>
                        <th>Name</th>
                        <th>Date</th>
                        <th>Status</th>
                    </tr>
                </thead>
                <tbody>
                    {attendanceData.map((record) => (
                        <tr key={record.id}>
                            <td>{record.employeeId}</td>
                            <td>{record.name}</td>
                            <td>{record.date}</td>
                            <td>{record.status}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default AttendancePage;
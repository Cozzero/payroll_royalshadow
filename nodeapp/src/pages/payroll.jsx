import React, { useState } from 'react';

export default function PayrollPage() {
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);
    const [success, setSuccess] = useState(null);
    const [filters, setFilters] = useState({
        month: new Date().getMonth() + 1,
        year: new Date().getFullYear(),
        department: '',
    });

    const handleGeneratePayroll = async () => {
        setLoading(true);
        setError(null);
        setSuccess(null);

        try {
            const response = await fetch('/api/payroll/generate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(filters),
            });

            if (!response.ok) {
                throw new Error('Failed to generate payroll');
            }

            const data = await response.json();
            setSuccess(`Payroll generated successfully for ${filters.month}/${filters.year}`);
        } catch (err) {
            setError(err.message);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="payroll-container">
            <h1>Generate Payroll</h1>
            
            <div className="filters">
                <input
                    type="number"
                    min="1"
                    max="12"
                    value={filters.month}
                    onChange={(e) => setFilters({ ...filters, month: e.target.value })}
                    placeholder="Month"
                />
                <input
                    type="number"
                    value={filters.year}
                    onChange={(e) => setFilters({ ...filters, year: e.target.value })}
                    placeholder="Year"
                />
                <input
                    type="text"
                    value={filters.department}
                    onChange={(e) => setFilters({ ...filters, department: e.target.value })}
                    placeholder="Department"
                />
            </div>

            <button onClick={handleGeneratePayroll} disabled={loading}>
                {loading ? 'Generating...' : 'Generate Payroll'}
            </button>

            {error && <p className="error">{error}</p>}
            {success && <p className="success">{success}</p>}
        </div>
    );
}
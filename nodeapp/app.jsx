import React from 'react';
import ReactDOM from 'react-dom';
import './styles.css'; // Import your CSS styles here
import AppHeader from './components/AppHeader';
import AppFooter from './components/AppFooter';
import MainContent from './components/MainContent';

const App = () => {
    return (
        <div className="app">
            <AppHeader />
            <MainContent />
            <AppFooter />
        </div>
    );
};

ReactDOM.render(<App />, document.getElementById('root'));
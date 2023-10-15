import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import './index.css';
import LeftPanel from './components/LeftPanel';
import MiddlePanel from './components/MiddlePanel';
import RightPanel from './components/RightPanel';
import ProgressBar from './components/ProgressBar';

function App() {
    const [progress, setProgress] = React.useState(0);

    React.useEffect(() => {
        setProgress(50);
    }, []);

    return (
        <div className="container mx-auto my-10 p-4 md:p-8 bg-gray-50 rounded-xl shadow-md">
            <h1 className="text-3xl md:text-4xl mb-6 font-bold text-gray-700">Semantic Search</h1>
            <ProgressBar progress={progress} />
            <div className="flex flex-col md:flex-row space-y-6 md:space-x-6 mt-6">
                <LeftPanel />
                <MiddlePanel />
                <RightPanel />
            </div>
        </div>
    );
}

export default App;

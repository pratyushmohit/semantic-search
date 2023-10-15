import React from 'react';
import LoadingBar from 'react-top-loading-bar';

const ProgressBar: React.FC<{ progress: number }> = ({ progress }) => {
    return (
        <LoadingBar
            color='#3498db'
            progress={progress}
            height={3}
        />
    );
}

export default ProgressBar;

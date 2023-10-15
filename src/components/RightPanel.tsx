import React, { useState, useEffect } from 'react';

interface RightPanelProps {
    results: string[];
}

const RightPanel: React.FC<RightPanelProps> = ({ results }) => {
    const [highlight, setHighlight] = useState(false);
    const [highlightStyle, setHighlightStyle] = useState({});

    useEffect(() => {
        if (highlight) {
            setHighlightStyle({
                backgroundColor: 'transparent',
                transition: 'background-color 2s',
            });
        } else {
            setHighlightStyle({});
        }
    }, [highlight]);

    return (
        <div className="flex flex-col space-y-6 w-full md:w-1/3 p-8 bg-gradient-to-tr from-teal-50 to-blue-200 rounded-r-lg shadow-xl">
            <label className="text-xl font-semibold text-gray-800">Highlighted Sentence</label>
            
            {results.map((result, index) => (
                <p key={index} className="p-4 bg-white border rounded-lg shadow-inner text-center text-gray-600">
                    {result.split(" ").map((word, wordIndex) => (
                        <span key={wordIndex} className="cursor-pointer hover:bg-yellow-200 transition-colors duration-300" style={highlightStyle}>
                            {word} 
                        </span>
                    ))}
                </p>
            ))}

            <button onClick={() => setHighlight(!highlight)} className="mt-auto btn btn-secondary text-white bg-gradient-to-r from-blue-500 to-teal-600 hover:from-teal-600 hover:to-blue-500 transition py-2 px-4 rounded-lg shadow-md">
                {highlight ? "Stop Highlighting" : "Start Highlighting"}
            </button>
        </div>
    );
}

export default RightPanel;

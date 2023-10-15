import React from 'react';
import { FiSearch } from 'react-icons/fi';

interface MiddlePanelProps {
    sentence: string;
}

const MiddlePanel: React.FC<MiddlePanelProps> = ({ sentence }) => {
    const findSimilar = async () => {
        try {
            const response = await fetch(`http://localhost:8000/find-similar?sentence=${encodeURIComponent(sentence)}&limit=2`);
            const data = await response.json();
            console.log(data);
        } catch (error) {
            console.error('Error finding similar sentences:', error);
        }
    };


    return (
        <div className="flex flex-col justify-center items-center mx-auto p-6 md:p-12 space-y-4">
            <div className="relative">
                <button
                    onClick={findSimilar}
                    className="flex items-center space-x-2 bg-transparent border border-green-500 py-2 px-6 rounded-full hover:bg-green-500 hover:text-white transition-transform transform hover:scale-105 shadow-lg"
                    onMouseEnter={(e) => e.currentTarget.classList.add('animate-pulse')}
                    onMouseLeave={(e) => e.currentTarget.classList.remove('animate-pulse')}
                >
                    <FiSearch className="text-green-500 text-xl" />
                    <span className="text-green-500 font-semibold">Find Similar</span>
                </button>
                <div className="absolute top-0 right-0 -mt-2 -mr-2 w-4 h-4 bg-green-500 rounded-full animate-ping"></div>
            </div>
        </div>
    );
}

export default MiddlePanel;
